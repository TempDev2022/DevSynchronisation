import boto3, botocore

s3 = boto3.resource('s3',
    endpoint_url='http://172.17.0.2:9000',
    aws_access_key_id='minio',
    aws_secret_access_key='miniokey',
    aws_session_token=None,
    config=boto3.session.Config(signature_version='s3v4'),
    verify=False
)

s3.Bucket('bucket01').create();
file = open('iceberg_broken.jpg', 'rb')
s3.Bucket('bucket01').put_object(Key='iceberg.jpg', Body=file)
file = open('anemone.jpg', 'rb')
s3.Bucket('bucket01').put_object(Key='anemone.jpg', Body=file)
print("Files added")
file = open('the wizer folly_0.txt', 'rb')
s3.Bucket('bucket01').put_object(Key='the wizer folly.txt', Body=file)
