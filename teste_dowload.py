import os
from time import sleep

from azure.storage.blob import BlobServiceClient, BlobClient
import mysql.connector

count = 0
MY_CONNECTION_STRING = 'DefaultEndpointsProtocol=https;AccountName=imagensinterclasse;AccountKey=BM/mVQXYFVf6gWn2k0Xd9Fj+jCbEv7C4nh/slDBcdMxgITFFHnpUuCYSSr+jdQkqxfcmziPllMy4+ASt95owUQ==;EndpointSuffix=core.windows.net'
MY_BLOB_CONTAINER = 'isimagefolder'
LOCAL_BLOB_PATH = './dload'
cadastrados = []


class AzureBlobFileDownloader:
    def __init__(self):
        print("Intializing AzureBlobFileDownloader")
        self.blob_service_client = BlobServiceClient.from_connection_string(MY_CONNECTION_STRING)
        self.my_container = self.blob_service_client.get_container_client(MY_BLOB_CONTAINER)

    def save_blob(self, file_name, file_content):
        download_file_path = os.path.join(LOCAL_BLOB_PATH, file_name)
        os.makedirs(os.path.dirname(download_file_path), exist_ok=True)
        with open(download_file_path, "wb") as file:
            file.write(file_content)

    def download_all_blobs_in_container(self):
        x = False

        conexao = mysql.connector.connect(
            host="interclasse-2023.mariadb.database.azure.com",
            user="diegos@interclasse-2023",
            password="senaimange2023",
            database="interclasse"
        )

        cursor = conexao.cursor()

        comando = 'SELECT nome FROM faces'
        cursor.execute(comando)
        cadastrados = cursor.fetchall()

        nomes = []
        for i in range(len(cadastrados)):
            nomes.append(cadastrados[i][0])

        my_blobs = self.my_container.list_blobs()
        for blob in my_blobs:
            name_jpeg = blob.values()[0]
            if name_jpeg not in nomes:
                print(f"{blob.name} cadastrado")
                x = True
                bytes = self.my_container.get_blob_client(blob).download_blob().readall()
                self.save_blob(blob.name, bytes)
            else:
                print(f"{blob.name} já existe")
                x = False
        cadastrados.clear()
        nomes.clear()

        return x


azure_blob_file_downloader = AzureBlobFileDownloader()
azure_blob_file_downloader.download_all_blobs_in_container()
