from collections import namedtuple
import requests


InnerBlock = namedtuple('Block', 'title price currency date url')


class Block(InnerBlock):
    def __str__(self):
        return f'{self.title}\t{self.price} {self.currency}\t{self.date}\t{self.url}'


class AvitoParser:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers =  {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/80.0.3987.163 Safari/537.36',
            'accept-language': 'ru'
        }

    def get_page(self, page: int = None):
        params = {
            'radius': 0,
            'q': 'bmw+5',
            'f': 'ASgBAgICAkSkA5oSygPQGA'
        }
        if page and page > 1:
            params['p'] = page
        url = 'https://www.avito.ru/krasnodar/avtomobili/'
        r = self.session.get(url, params=params)
        return r.text

    def temp(self):
        p = self.get_page(page=3)
        print(p)
        return


def main():
    p = AvitoParser;
    p.temp()


if __name__ == '__main__':
    main()


# ASgBAgICAkSkA5oSygPQGA
# ASgBAgICAkSkA5oSygPQGA