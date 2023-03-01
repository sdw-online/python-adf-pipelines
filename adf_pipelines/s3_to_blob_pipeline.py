import pandas as pd
import azure
import boto3
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from dotenv import load_dotenv
import os
from azure.identity import DefaultAzureCredential
from azure.mgmt.datafactory import DataFactoryManagementClient
from azure.mgmt.datafactory.models import *
from msrestazure.azure_active_directory import ServicePrincipalCredentials


load_dotenv()










# Set up environment variables

## AWS 

ACCESS_KEY              =   os.getenv("ACCESS_KEY")
SECRET_ACCESS_KEY       =   os.getenv("SECRET_ACCESS_KEY")
REGION_NAME             =   os.getenv("REGION_NAME")
S3_BUCKET               =   os.getenv("S3_BUCKET")
S3_FOLDER               =   os.getenv("S3_FOLDER")


s3_client               =   boto3()



## AZURE


CONTAINER_NAME          =   os.getenv("CONTAINER_NAME")
ACCOUNT_URL             =   os.getenv("ACCOUNT_URL")
BLOB_NAME               =   os.getenv("BLOB_NAME")
STORAGE_ACCOUNT_NAME    =   os.getenv("STORAGE_ACCOUNT_NAME")
CONNECTION_STRING       =   os.getenv("CONNECTION_STRING")

TENANT_ID = ""
CLIENT_ID = ""
CLIENT_SECRET = ""
SUBSCRIPTION_ID = ""
RESOURCE_GROUP_NAME = ""
FACTORY_NAME = ""
BLOB_STORAGE_ACCOUNT_NAME = ""
BLOB_STORAGE_ACCOUNT_KEY = ""

blob_service_client     =   BlobServiceClient()



# Create linked services for source and sink



## 1. SOURCE 


## 2. SINK





# Create datasets for source and sink




## 1. SOURCE 


## 2. SINK







# Create pipeline with copy activity 










# Create trigger to execute pipeline 

