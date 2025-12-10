import csv
import json
from os import write

from bs4 import BeautifulSoup
import  requests
import lxml
import  datetime

def get_date_api():
    count = 0

    with open('films_list.csv', 'w') as file_csv:
        writer = csv.writer(file_csv)
        writer.writerow(
            ['Название фильма',
            'Рейтинг',
            'Год',
            'Режисёр',
             'Ссылка'
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
                item_slug = 'https://zonafilm.ru/movies/' + item.get('slug')

                films_list.append(
                    [item_film, item_rating, item_year, item_directors, item_slug]
                )
                count += 1
                print(count)

            with open('films_list.csv', 'a') as file_csv:
                writer = csv.writer(file_csv)
                writer.writerows(
                    films_list
                )

def get_date_html():
    count = 1

    for i in range(1, 800):
        url_api = f'https://zonafilm.ru/api/movies?page={i}'
        headers = {
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
            'accept': '*/*'
        }

        response = requests.get(url=url_api, headers=headers)
        films = response.json()['data']

        with open ('data.json', 'a') as json_file:
            json.dump(films, json_file, indent=4, ensure_ascii=False)
        #
        # with open('data.json') as json_file:
        #     films = json.load(json_file)

        if films != 0:
            for item in films:
                all_links = []
                # item_film = item.get('title')
                # item_year = item.get('year')
                # item_rating = round(item.get('rating'), 2)
                # item_directors = item.get('directors')
                item_link = 'https://zonafilm.ru/movies/' + item.get('slug')
                print(f'{count}. {item_link}')
                all_links.append(item_link)
                count += 1

                with open('all_links.csv', 'a', newline='') as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow(
                        all_links
                    )

def get_data():
    with open('all_links.csv') as file:
        data = csv.reader(file)

    for i in data:
        print(i)




def main():
    # get_date_api()
    # get_date_html()
    get_data()

if __name__ == '__main__':
    main()