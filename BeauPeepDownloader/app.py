from BeauPeepDownloader import os, requests


class DownloadBeau:

    def __init__(self, season, page_number):

        self.raw = season
        self.raw_page = page_number
        self.beau_peep_url = {
            'head': f"https://www.omgbeaupeep.com/comics/mangas/Beau%20Peep/",
            'colored_head': 'https://www.omgbeaupeep.com/comics/mangas/Beau%20Peep/021%20-%20Beau%20Peep%20Color%20Collection/',
            'colored_edition': 'read-beau-peep-online-page-',
            'odd_fourth_season_14': '/beau-peep-book-',
            'odd_fifth_season_14': '-page-',
            'middle': '%20-%20Beau%20Peep%20Book%20',
            'fourth': '/Beau-Peep-Book-',
            'fifth': '-Page-',
            'odd_season_15': '/read-beau-peep-online-page-',
            'extension': '.jpg'
        }

        if len(str(season)) == 1:
            self.season = f'00{season}'

        elif len(str(season)) == 2:
            self.season = f'0{season}'

        if len(str(page_number)) == 1:
            self.page_number = f'00{page_number}'

        elif len(str(page_number)) == 2:
            self.page_number = f'0{page_number}'
        else:
            self.page_number = str(page_number)

        if self.raw == 10:
            if len(str(page_number)) == 1:
                self.page_number = f'0{page_number}'
            else:
                self.page_number = f'{page_number}'
        elif self.raw == 11:
            if len(str(page_number)) == 1:
                self.page_number = f'000{page_number}'
            elif len(str(page_number)) == 2:
                self.page_number = f'00{page_number}'
            elif len(str(page_number)) == 3:
                self.page_number = f'0{page_number}'
        elif self.raw == 15:
            if len(str(page_number)) == 1:
                self.page_number = f'00{page_number}'
            elif len(str(page_number)) == 2:
                self.page_number = f'0{page_number}'
            elif len(str(page_number)) == 3:
                self.page_number = f'{page_number}'

        self.not_normal13 = f"{self.beau_peep_url['head']}{self.season}{self.beau_peep_url['middle']}{self.raw}{self.beau_peep_url['odd_fourth_season_14']}{self.raw}{self.beau_peep_url['odd_fifth_season_14']}{self.page_number}{self.beau_peep_url['extension']}"
        self.normal_url15 = f"{self.beau_peep_url['head']}{self.season}{self.beau_peep_url['middle']}{self.raw}{self.beau_peep_url['odd_season_15']}{self.raw}{self.beau_peep_url['odd_fifth_season_14']}{self.page_number}{self.beau_peep_url['extension']}"
        self.normal_url = f"{self.beau_peep_url['head']}{self.season}{self.beau_peep_url['middle']}{self.raw}{self.beau_peep_url['fourth']}{self.raw}{self.beau_peep_url['fifth']}{self.page_number}{self.beau_peep_url['extension']}"

    def download_one(self, name_of_directory='my_beau_peep_comic'):
        if self.raw == 13:
            self.comic = requests.get(self.not_normal13).content
        elif self.raw == 15:
            self.comic = requests.get(self.normal_url15).content
        else:
            self.comic = requests.get(self.normal_url).content
        if os.path.isdir(name_of_directory):
            with open(f'{name_of_directory}\\season{self.raw} page{self.raw_page}.jpg', 'wb') as f:
                f.write(self.comic)
        else:
            os.mkdir(name_of_directory)
            with open(f'{name_of_directory}\\season{self.raw} page{self.raw_page}.jpg', 'wb') as f:
                f.write(self.comic)

    def download_multiple(self, end):
        season = self.raw
        start = int(self.page_number)
        duration = int(end) - int(start)
        for i in range(duration):
            while start <= end:
                counter = start
                m = DownloadBeau(season, page_number=counter)
                m.download_one()
                start += 1

    def download_one_colored_edition(self,name_of_directory='my_beau_peep_comic_colored'):
        picture = f'{self.beau_peep_url["colored_head"]}{self.beau_peep_url["colored_edition"]}{self.page_number}{self.beau_peep_url["extension"]} '

        if os.path.isdir(name_of_directory):
            with open(f'{name_of_directory}\\season{self.raw} page{self.raw_page}.jpg', 'wb') as f:
                f.write(self.comic)
        else:
            os.mkdir(name_of_directory)
            with open(f'{name_of_directory}\\season{self.raw} page{self.raw_page}.jpg', 'wb') as f:
                f.write(self.comic)

        print(picture)

    def download_multiple_colored_edition(self, end):
        season = self.raw
        start = int(self.page_number)
        duration = int(end) - int(start)
        for i in range(duration):
            while start <= end:
                counter = start
                m = DownloadBeau(season, page_number=counter)
                m.download_one_colored_edition()
                start += 1
