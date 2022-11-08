# Exercise - Synchronisation S3 - 8/11/2022
Instead of a script for Synchronisation a server based on local file, a python file update_bucket was created.   
## Author
Jade Sagot--Gentil

## Prerequisites

### Prerequisite 1 : This project needs python and docker installed

### Prerequisite 2 : Needed libraries
* boto3 :

```
pip install boto3
```

### Prerequisite 3 : Open the Minio server on docker on a separate shell
```
sudo docker run -it -e MINIO_ACCESS_KEY=minio -e MINIO_SECRET_KEY=miniokey minio/minio server /data
```

### In another shell :
### Prerequisite 4 : Make scripts executable
```
chmod +x initialize_server.sh poc.sh
```

### Prerequisite 5 : Launch initialization of the server
```
./initialize_server.sh
```

### To use the python file update_bucket (2 inputs) :
Usage :
python update_bucket.py file_path bucket_name


### To make a proof of concept
Launch the script poc.sh
  ```
  ./poc.sh
  ```
