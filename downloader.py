from tqdm import tqdm
import requests
import os


def download_file(file_name, content_url, auth_token, download_path):
    print('Downloading ' + str(file_name) + '...')
    response = requests.get(content_url, headers={"Authorization": auth_token}, stream=True)
    total_size_in_bytes = int(response.headers.get('content-length', 0))
    block_size = 1024  # 1 Kibibyte
    progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)
    with open(os.path.join(download_path, file_name), 'wb') as file:
        for data in response.iter_content(block_size):
            progress_bar.update(len(data))
            file.write(data)
    progress_bar.close()
    if total_size_in_bytes != 0 and progress_bar.n != total_size_in_bytes:
        print("ERROR, something went wrong")
