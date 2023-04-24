from time import sleep

from teste_dowload import AzureBlobFileDownloader as dload
from create_column import create_column_items

count = 0

while True:
    sleep(1)
    count += 1
    print(count)
    if count % 240 == 0:
        azure_blob_file_downloader = dload()
        teste = azure_blob_file_downloader.download_all_blobs_in_container()
        if teste:
            create_column_items()
        else:
            print('nem, tentou criar')
    else:
        continue
