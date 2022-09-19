import json
import urllib.parse
import boto3
import pandas as pd
import pybase64
from app.load.index import load_data
from dotenv import dotenv_values



print('Loading function')

def lambda_handler():
    config = dotenv_values(".env") 
    dictionary_config = dict(config)

    aws_credential_key = dictionary_config['AWS_SERVER_PUBLIC_KEY']
    aws_credential_secret = dictionary_config['AWS_SERVER_SECRET_KEY']
    aws_decode_key = pybase64.b64decode(aws_credential_key)
    aws_decode_secret = pybase64.b64decode(aws_credential_secret)
    
    sesion_boto = boto3.Session( aws_access_key_id=aws_decode_key.decode(),aws_secret_access_key=aws_decode_secret.decode(),)
    s3 = sesion_boto.resource('s3')
    bucket = s3.Bucket('data-facturedo')

    for obj in bucket.objects.all():
        key = obj.key
        body = obj.get()['Body'].read()
    file_excel = pd.read_excel(body)
    file_csv = file_excel.to_csv("Test.csv", index=False, header=True, sep=';') 
    dataframe = pd.read_table("./Test.csv", delimiter=";")
    coun_data = load_data(dataframe)    
    return coun_data



