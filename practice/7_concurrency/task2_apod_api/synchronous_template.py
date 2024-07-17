import os
import requests
import json
import shutil
import time


API_KEY = "3mPLgcbJu0dn1gCUTzeK0LRgwVNNcEFBumFjNpIh"
APOD_ENDPOINT = 'https://api.nasa.gov/planetary/apod'
OUTPUT_IMAGES = './output'
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                         'AppleWebKit/537.36 (KHTML, like Gecko)'
                         'Chrome/102.0.0.0 '
                         'Safari/537.36'}

"""
https://api.nasa.gov/planetary/apod?api_key=YOUR_KEY&start_date=2020-07-06&end_date=2020-08-06

[{"copyright":"\nBryan Goff\n\n","date":"2020-07-06","explanation":"long_text_description",
 "hdurl":"https://apod.nasa.gov/apod/image/2007/M43_HubbleGoff_4000.jpg",
 "media_type":"image","service_version":"v1",
 "title":"M43: Dust, Gas, and Stars in the Orion Nebula",
 "url":"https://apod.nasa.gov/apod/image/2007/M43_HubbleGoff_960.jpg"}]
"""


def get_apod_metadata(start_date: str, end_date: str, api_key: str) -> list:
    response = requests.get(APOD_ENDPOINT, params={'api_key': api_key, 'start_date': start_date, 'end_date': end_date}, headers=HEADERS)
    return json.loads(response.text)


def download_apod_images(metadata: list):
    if not os.path.exists(OUTPUT_IMAGES):
        os.mkdir(OUTPUT_IMAGES)
    for image in metadata:
        if 'image' in image['media_type']:
            r = requests.get(image['url'], stream=True)
            if r.status_code == 200:
                with open(os.path.join(OUTPUT_IMAGES, image['url'].split('/')[-1]), 'wb') as f:
                    r.raw.decode_content = True
                    shutil.copyfileobj(r.raw, f)

def measure_execution_time(func, *args, **kwargs):
    start_time = time.time()
    func(*args, **kwargs)
    end_time = time.time()
    return end_time - start_time

def main():
    metadata = get_apod_metadata(
        # start_date='2021-08-01',
        # end_date='2021-09-30',
        start_date='2021-08-01',
        end_date='2021-08-03',
        api_key=API_KEY,
    )
    print(f'execution time {round(measure_execution_time(download_apod_images, metadata=metadata), 2)} seconds')


if __name__ == '__main__':
    main()

