import requests
from bs4 import BeautifulSoup

url = 'https://www.kinopoisk.ru/top/'

def parse():
    need_vote = False
    page = requests.get(url).content
    soup = BeautifulSoup(page, 'lxml')
    films = soup.findAll('td')
    for film in films:

        if need_vote:
            try:
                votes = film.find('a', class_='continue').text
                print(votes)
                need_vote = False
                # write to DB
            except:
                pass

        try:
            # if film.find('a').attrs['href'] == '#formula': continue
            if film.find('a', class_='all').text == 'Как рассчитывается Топ-250?' or \
                    film.find('a', class_='all').text == 'предыдущий день' or \
                    film.find('a', class_='all').text == 'Навигатор по лучшим фильмам >>' or \
                    film.find('a', class_='all').text == 'Текущие кассовые сборы США >>' or \
                    film.find('a', class_='all').text == 'Самые кассовые фильмы за всю историю кино >>':
                continue
            title = film.find('a', class_='all').text
            print(title)
            need_vote = True
        except:
            pass



parse()