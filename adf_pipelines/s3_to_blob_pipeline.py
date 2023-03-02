import pandas as pd
import azure
import boto3
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from dotenv import load_dotenv
import os
from azure.identity import InteractiveBrowserCredential
from azure.mgmt.datafactory import DataFactoryManagementClient
from azure.mgmt.datafactory.models import LinkedServiceResource



load_dotenv()







# Set up environment variables

## AWS 

ACCESS_KEY                          =   os.getenv("ACCESS_KEY")
SECRET_ACCESS_KEY                   =   os.getenv("SECRET_ACCESS_KEY")
REGION_NAME                         =   os.getenv("REGION_NAME")
S3_BUCKET                           =   os.getenv("S3_BUCKET")
S3_FOLDER                           =   os.getenv("S3_FOLDER")

# s3_client                           =   boto3()



## AZURE            


CONTAINER_NAME                      =   os.getenv("CONTAINER_NAME")
ACCOUNT_URL                         =   os.getenv("ACCOUNT_URL")
BLOB_NAME                           =   os.getenv("BLOB_NAME")
STORAGE_ACCOUNT_NAME                =   os.getenv("STORAGE_ACCOUNT_NAME")
CONNECTION_STRING                   =   os.getenv("CONNECTION_STRING")

TENANT_ID                           =   os.getenv("TENANT_ID")
CLIENT_ID                           =   os.getenv("CLIENT_ID")
CLIENT_SECRET                       =   os.getenv("CLIENT_SECRET")
SUBSCRIPTION_ID                     =   os.getenv("SUBSCRIPTION_ID")
RESOURCE_GROUP_NAME                 =   os.getenv("RESOURCE_GROUP_NAME")
DATA_FACTORY_NAME                   =   os.getenv("DATA_FACTORY_NAME")
BLOB_STORAGE_ACCOUNT_NAME           =   os.getenv("BLOB_STORAGE_ACCOUNT_NAME")
BLOB_STORAGE_ACCOUNT_KEY            =   os.getenv("BLOB_STORAGE_ACCOUNT_KEY")

AUTHORITY_URL                       =   f'https://login.windows.net/{TENANT_ID}'


credentials                         =   InteractiveBrowserCredential()
blob_service_client                 =   BlobServiceClient(ACCOUNT_URL)
adf_client                          =   DataFactoryManagementClient(credentials, SUBSCRIPTION_ID)

data_factory                        =   adf_client.factories.get(RESOURCE_GROUP_NAME, DATA_FACTORY_NAME)


blob_storage_linked_service_name    =   os.getenv("LINKED_SERVICE_NAME_DEST")
blob_storage_connection_string      =   CONNECTION_STRING


# print(data_factory)



blob_storage_linked_service = LinkedServiceResource(
    type='AzureBlobStorage',
    type_properties={
        'connectionString': CONNECTION_STRING
    }
)


blob_storage_linked_service_request = adf_client.linked_services.create_or_update(resource_group_name=RESOURCE_GROUP_NAME, 
                                                                                   factory_name=DATA_FACTORY_NAME,
                                                                                   linked_service_name=blob_storage_linked_service_name,
                                                                                   linked_service=blob_storage_linked_service
                                                                                   )




# Create an Azure credentials object 





# Create linked services for source and sink



## 1. SOURCE 


## 2. SINK





# Create datasets for source and sink




## 1. SOURCE 


## 2. SINK







# Create pipeline with copy activity 










# Create trigger to execute pipeline 

