import csv
import json
from itertools import count

from bs4 import BeautifulSoup
import  requests
import lxml
import  datetime

def get_date():
    count = 0

    with open('films_list.csv', 'w') as file_csv:
        writer = csv.writer(file_csv)
        writer.writerow(
            ['Название фильма',
            'Рейтинг',
            'Год',
            'Режисёр'
             ]
        )

    for i in range(1, 800):

        url_api = f'https://zonafilm.ru/api/movies?page={i}'
        # url = 'https://zonafilm.ru/api/movies?page=1'

        headers = {
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
            'accept': '*/*'
        }

        response = requests.get(url=url_api, headers=headers)
        # response_2 = requests.get(url=url, headers=headers)

        films = response.json()['data']
        films_list = []

        if films != 0:

            for item in films:
                item_film = item.get('title')
                item_year = item.get('year')
                item_rating = round(item.get('rating'), 2)
                item_directors = item.get('directors')

                films_list.append(
                    [item_film, item_rating, item_year, item_directors]
                )
                count += 1
                print(count)

            with open('films_list.csv', 'a') as file_csv:
                writer = csv.writer(file_csv)
                writer.writerows(
                    films_list
                )

def main():
    get_date()

if __name__ == '__main__':
    main()