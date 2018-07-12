import requests
from bs4 import BeautifulSoup

url = 'https://www.kinopoisk.ru/top/'
limit = 3  # antiban for testing time

def parse():
    parsed_films = 0
    page = requests.get(url).content
    soup = BeautifulSoup(page, 'lxml')
    films = soup.findAll('td')
    for film in films:

        try:
            if film.find('a', class_='all').text == 'Как рассчитывается Топ-250?' or \
                    film.find('a', class_='all').text == 'предыдущий день' or \
                    film.find('a', class_='all').text == 'Навигатор по лучшим фильмам >>' or \
                    film.find('a', class_='all').text == 'Текущие кассовые сборы США >>' or \
                    film.find('a', class_='all').text == 'Самые кассовые фильмы за всю историю кино >>' or \
                    parsed_films >= limit:
                continue
            title = film.find('a', class_='all').text
            votes_url = 'https://www.kinopoisk.ru' + film.find('a').attrs['href']
            print('%s - %s'%(title, votes_url))
            votes_page = requests.get(votes_url).content
            votes_soup = BeautifulSoup(votes_page, 'lxml')
            votes = votes_soup.findAll('div', class_='clear_all')

            for vote in votes:
                # print(vote)
                vote_pos = vote.find('li', class_='pos').text
                vote_neg = vote.find('li', class_='neg').text

            parsed_films = parsed_films + 1  # antiban
            print('%s - %s'%(vote_pos, vote_neg))
        except:
            pass


parse()