import pandas as pd
import azure
import boto3
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from dotenv import load_dotenv
import os

load_dotenv()










# Set up environment variables

## AWS 

ACCESS_KEY              =   os.getenv("ACCESS_KEY")
SECRET_ACCESS_KEY       =   os.getenv("SECRET_ACCESS_KEY")
REGION_NAME             =   os.getenv("REGION_NAME")
S3_BUCKET               =   os.getenv("S3_BUCKET")
S3_FOLDER               =   os.getenv("S3_FOLDER")




## AZURE


BLOB_CONTAINER_NAME     =   os.getenv("BLOB_CONTAINER_NAME")




# Create linked services for source and sink



## 1. SOURCE 


## 2. SINK





# Create datasets for source and sink




## 1. SOURCE 


## 2. SINK







# Create pipeline with copy activity 










# Create trigger to execute pipeline 

