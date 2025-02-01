import os
import requests
from bs4 import BeautifulSoup


class DownloadBeau:
    def __init__(self, season, page_number):
        self.season = season
        self.page_number = page_number
        self.base_url = "https://www.omgbeaupeep.com/comics/mangas/Beau%20Peep/"
        self.colored_base_url = "https://www.omgbeaupeep.com/comics/mangas/Beau%20Peep/021%20-%20Beau%20Peep%20Color%20Collection/"

    def get_image_url(self, colored=False):
        url = self.colored_base_url if colored else f"{self.base_url}{self.season}/"
        try:
            response = requests.get(url)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Failed to access {url}: {e}")
            return None

        soup = BeautifulSoup(response.text, 'html.parser')
        images = soup.find_all('img')

        for img in images:
            if str(self.page_number) in img['src']:
                return img['src']

        return None

    @staticmethod
    def download_image(image_url, name_of_directory, filename):
        if not image_url:
            print("Image URL not found.")
            return

        try:
            response = requests.get(image_url)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Failed to download image: {e}")
            return

        os.makedirs(name_of_directory, exist_ok=True)
        file_path = os.path.join(name_of_directory, filename)
        with open(file_path, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded: {file_path}")

    def download_one(self, name_of_directory='my_beau_peep_comic'):
        image_url = self.get_image_url()
        filename = f'season{self.season}_page{self.page_number}.jpg'
        self.download_image(image_url, name_of_directory, filename)

    def download_multiple(self, end):
        for page in range(self.page_number, end + 1):
            downloader = DownloadBeau(self.season, page)
            downloader.download_one()

    def download_one_colored_edition(self, name_of_directory='my_beau_peep_comic_colored'):
        image_url = self.get_image_url(colored=True)
        filename = f'colored_season{self.season}_page{self.page_number}.jpg'
        self.download_image(image_url, name_of_directory, filename)

    def download_multiple_colored_edition(self, end):
        for page in range(self.page_number, end + 1):
            downloader = DownloadBeau(self.season, page)
            downloader.download_one_colored_edition()