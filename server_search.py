import botocore

def bucket_exists(bucket_name, s3) :
    try :
        s3.meta.client.head_bucket(Bucket=bucket_name)
        return(1)
    except botocore.exceptions.ClientError as e :
            if e.response['Error']['Code'] == '404':
                return(0)
            else :
                print(f"Impossible to access {bucket_name}")

def file_exists_in_bucket(file_path, bucket_name, s3):
    try :
        s3.Object(bucket_name, file_path).load()
        return(1)
    except botocore.exceptions.ClientError as e :
        if e.response['Error']['Code'] == '404':
                return(0)
        else :
            print(f"An error occured while fetching {file_path}/{bucket_name}")
