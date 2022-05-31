from urllib import response
import boto3
import os
from botocore.client import Config
from requests import session

#AWS 권한 명시 
session=boto3.Session(
    aws_access_key_id='AKIAXZWL4PM4KT75FEOG',
    aws_secret_access_key='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',
    region_name='ap-northeast-2'
    )
s3 = session.client('s3')

#업로드 할 s3 버킷
bucket='autolabeling'

def upload_dir():
    #위치 설정(입력창으로 받아올 예정)
    local_dir='./img/말티즈'
    # enumerate local files recursively
    for root, dirs, files in os.walk(local_dir):
        for filename in files:
            # construct the full local path
            local_path = os.path.join(root, filename)

            # construct the full Dropbox path
            relative_path = os.path.relpath(local_path, local_dir)
            s3_path = os.path.join("img/", relative_path)

            print ('Searching "%s" in "%s"' % (s3_path, bucket))
            try:
                s3.head_object(Bucket=bucket, Key=s3_path)
                print ("Path found on S3! Skipping %s..." % s3_path)
            except:
                print ("Uploading %s..." % s3_path)
                s3.upload_file(local_path, bucket, s3_path)

if __name__=="__main__":
    upload_dir() #dir 경로명을 받아서 upload 구현