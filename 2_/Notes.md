Getting started with pipenv and boto3
pipenv is brings as for lots of flexable to the enviromates and packageing our codes

mkdir 01-webotron
pipenv --three

cat Pipfile

Pipefile--> it's depandance file 

pipenv install boto3
cat Pipfile
#Now you can see boto3 in the depandance file 

pipenv install -d ipython
ipython

pipenv run ipython

import boto3
session = boto3.Session(profile_name='pythonAutomation')

#TRy to list s3 bucke in awscli -->aws s3 ls --profile pythonAutomation
#same function trying with python boto3 environmaents

s3 = session.resource('s3')
for bucket in s3.bucket.all():
    print(bucket)
#Creaing new bucket using boto3
new_bucket = s3.create_bucket(Bucket='Automatingdevopsdymyr-boto3')
#you will get error msg for the region
new_bucket = s3.create_bucket(Bucket='Automatingdevopsdymyr-boto3', CreateBucketConfiguration={'LocationConstraint': 'us-east-2'})
new_bucket


%save ipythonsession.py 1-10
pipenv run ipython -i ipythonsession.py


#Script Skelecton,Configure boto3 & and command line arguments

mkdir webotron

touch webotron/webotron.py
 
#webotron.py
if __name__ == '__main__':
    print("Hello, World!")

#pipenv run python webotron/webotron.py