import os
from azure.storage.blob import BlobServiceClient

storage_connection_string = 'DefaultEndpointsProtocol=https;AccountName=imagensinterclasse;AccountKey=BM/mVQXYFVf6gWn2k0Xd9Fj+jCbEv7C4nh/slDBcdMxgITFFHnpUuCYSSr+jdQkqxfcmziPllMy4+ASt95owUQ==;EndpointSuffix=core.windows.net'
blob_service_client = BlobServiceClient.from_connection_string(storage_connection_string)
container_name = 'isimagefolder'

# Upload my files 
file_folder = './img'

for file_name in os.listdir(file_folder):
    blob_obj = blob_service_client.get_blob_client(container=container_name, blob=file_name)
    print("Upando o arquivo {}".format(file_name))
    
    with open(os.path.join(file_folder, file_name), mode='rb') as file_data:
        blob_obj.upload_blob(file_data)