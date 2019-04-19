import boto3
#import sys
import click

session = boto3.Session(profile_name='default')
s3 = session.resource('s3')

@click.group()
def cli():
    "Webotron deploys websites to AWS"
    pass

@cli.command('list-buckets')
#@click.command('list-buckets')
def list_buckets():
    "List all s3 buckets"
    for bucket in s3.buckets.all():
        print(bucket)
@cli.command('list-bucket-objects')
@click.argument('bucket')
def list_bucket_objects(bucket):
    "List objects in an s3 bucket"
    #Bucket name is hardcodded 
    for obj in s3.Bucket(bucket).objects.all():
        print(obj)

if __name__ == '__main__':
    #print(sys.argv)
    #for bucket in s3.buckets.all():
     #   print(bucket)
     #list_buckets()
     cli()