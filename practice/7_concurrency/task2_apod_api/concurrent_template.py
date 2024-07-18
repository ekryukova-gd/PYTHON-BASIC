import os
import requests
import json
import shutil
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import time
import secrets # get you API_KEY from https://api.nasa.gov/


API_KEY = secrets.API_KEY
APOD_ENDPOINT = 'https://api.nasa.gov/planetary/apod'
OUTPUT_IMAGES = './output'
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                         'AppleWebKit/537.36 (KHTML, like Gecko)'
                         'Chrome/102.0.0.0 '
                         'Safari/537.36'}


def get_apod_metadata(start_date: str, end_date: str, api_key: str) -> list:
    response = requests.get(APOD_ENDPOINT,
                            params={'api_key': api_key, 'start_date': start_date, 'end_date': end_date}, headers=HEADERS)
    return json.loads(response.text)


def download_apod_images(metadata: list):
    if not os.path.exists(OUTPUT_IMAGES):
        os.mkdir(OUTPUT_IMAGES)

    def save_image_to_file(image):
        r = requests.get(image['url'], stream=True)
        if r.status_code == 200:
            with open(os.path.join(OUTPUT_IMAGES, image['url'].split('/')[-1]), 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)

    with ThreadPoolExecutor(max_workers=None) as ex:
        ex.map(save_image_to_file, metadata)


def measure_execution_time(func, *args, **kwargs):
    start_time = time.time()
    func(*args, **kwargs)
    end_time = time.time()
    return end_time - start_time

def main():
    metadata = get_apod_metadata(
        start_date='2021-08-01',
        end_date='2021-09-30',
        api_key=API_KEY,
    )
    print(f'execution time {round(measure_execution_time(download_apod_images, metadata=metadata), 2)} seconds')


if __name__ == '__main__':
    main()

