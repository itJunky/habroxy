import requests
from bs4 import BeautifulSoup


class Proxify:
    """Simple class for proxyfing requsts by URL"""
    def get_page(self, url):
        res = requests.get(url)
        return self.parse(res.text)

    @staticmethod
    def parse(text):
        soup = BeautifulSoup(text)
        buf_string = ''
        title = soup.findAll('span', {'class': 'post__title-text'})[0]
        new_title = soup.new_tag('span', {'class': 'post__title-text'})

        for word in title.text.split():
            # TODO очищать от завершающих знаков припенания перед проверкой длины
            print('SELECTED WORD: %s' % word)
            if len(word) > 6:
                buf_string += word + '™ '
            else:
                buf_string += word + ' '

            new_title.string = buf_string

        title.replace_with(new_title)
        return soup.prettify("utf-8")

    # def replace(self, tag):

    # TODO подменять ссылки с оригинального хабра на собственный домен прокси
