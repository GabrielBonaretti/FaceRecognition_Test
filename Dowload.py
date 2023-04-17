import os
from azure.storage.blob import BlobServiceClient, BlobClient    
MY_CONNECTION_STRING = 'DefaultEndpointsProtocol=https;AccountName=imagensinterclasse;AccountKey=BM/mVQXYFVf6gWn2k0Xd9Fj+jCbEv7C4nh/slDBcdMxgITFFHnpUuCYSSr+jdQkqxfcmziPllMy4+ASt95owUQ==;EndpointSuffix=core.windows.net'
MY_BLOB_CONTAINER = 'isimagefolder'
LOCAL_BLOB_PATH = './dload'


class AzureBlobFileDownloader:
    def __init__(self):
        print("Intializing AzureBlobFileDownloader")      
        self.blob_service_client = BlobServiceClient.from_connection_string(MY_CONNECTION_STRING)
        self.my_container = self.blob_service_client.get_container_client(MY_BLOB_CONTAINER)
        
    def save_blob(self, file_name, file_content):
            # Get full path to the file 
        download_file_path = os.path.join(LOCAL_BLOB_PATH, file_name)
        os.makedirs(os.path.dirname(download_file_path), exist_ok=True)
        with open(download_file_path, "wb") as file:
            file.write(file_content)
    
    
    def download_all_blobs_in_container(self):
        my_blobs = self.my_container.list_blobs()
        for blob in my_blobs:
            print(blob.name)
            bytes = self.my_container.get_blob_client(blob).download_blob().readall()
            self.save_blob(blob.name, bytes) 
   
azure_blob_file_downloader = AzureBlobFileDownloader()
azure_blob_file_downloader.download_all_blobs_in_container()