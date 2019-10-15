import boto3
import sys
import click

session = boto3.Session(profile_name='pythonAutomation')
s3 = session.resource('s3')

@click.group()
def cli():
    "Webtron depllys websites to AWS"
    pass

@cli.command('list-buckets')
def list_buckets():
    "List all s3 buckets"
    for bucket in s3.buckets.all():
            print(bucket)


@cli.command('list-buckets-objects')
#@click.argument('objName')
@click.argument('objectName')
def list_buckets_objects(objectName):
    "List the objects in the s3"
    for obj in s3.Bucket(objectName).objects.all():
        print(obj)

if __name__ == '__main__':
    #print(sys.argv)
    #list_buckets()
    cli()
