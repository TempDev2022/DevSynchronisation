import boto3, botocore
from server_search import bucket_exists, file_exists_in_bucket
from os.path import exists
import sys, io
from hashlib import sha256

s3 = boto3.resource('s3',
    endpoint_url='http://172.17.0.2:9000',
    aws_access_key_id='minio',
    aws_secret_access_key='miniokey',
    aws_session_token=None,
    config=boto3.session.Config(signature_version='s3v4'),
    verify=False
    )

if len(sys.argv) != 3 :
    print('Illegal number of parameters. Usage : update_bucket file_path bucket_name ')
else :
    file_path = sys.argv[1]
    bucket_name = sys.argv[2]
    if not bucket_exists(bucket_name, s3) :
        print("Error : No such bucket as " + bucket_name)
    else :
        file_exists = exists(file_path);
        file_exists_in_bucket = file_exists_in_bucket(file_path, bucket_name,s3);
        if file_exists :
            local_file = open(file_path, 'rb')
            local_file.seek(0)
            if file_exists_in_bucket : #the file in bucket needs to be updated if diferent from the local file
                temp_data = io.BytesIO()
                s3.Bucket(bucket_name).download_fileobj(file_path, temp_data)
                temp_data.seek(0)
                if not (sha256(local_file.read()).hexdigest() == sha256(temp_data.read()).hexdigest()) : #compare hashs
                    local_file.seek(0)
                    s3.Bucket(bucket_name).put_object(Key=file_path, Body=local_file)
                    print(f'{file_path} is reload on bucket {bucket_name}')
                else :
                    print(f'{file_path} already loaded on bucket {bucket_name}')
            else :
                s3.Bucket(bucket_name).put_object(Key=file_path, Body=local_file)
                print(f'{file_path} was loaded on bucket {bucket_name}')
        elif file_exists_in_bucket : #the file in bucket needs to be removed
                s3.Object(bucket_name, file_path).delete
                print(f'{file_path} was removed from bucket {bucket_name}')
