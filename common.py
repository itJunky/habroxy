import requests
from bs4 import BeautifulSoup


class Proxify:
    """Simple class for proxyfing requsts by URL"""
    def get_page(self, url):
        res = requests.get(url)
        return self.parse(res.text)

    def parse(self, text):
        soup = BeautifulSoup(text)
        title = soup.findAll('span', {'class': 'post__title-text'})[0]
        new_title = soup.new_tag('span', {'class': 'post__title-text'})
        new_title = self.replace(title, new_title)
        title.replace_with(new_title)

        content = soup.find_all('div', class_='post__text post__text-html post__text_v1')[0]
        new_content = soup.new_tag('div', class_='post__text post__text-html post__text_v1')
        # print('DEBUG: parse content: %s' % content)
        new_content = self.replace(content, new_content)
        # content.replace_width(new_content)
        return soup.prettify("utf-8")

    def replace(self, tag, new_tag):
        buf_string = ''
        # print('DEBUG: replace tag: %s' % tag)
        # inner = BeautifulSoup(tag, features="lxml")
        # print(inner)
        # print("LENGTH: " + len(inner))
        for word in tag.text.split():
            # TODO очищать от завершающих знаков припенания перед проверкой длины
            print('DEBUG: replace word: %s' % word)
            if len(word) > 6:
                print('DEBUG: big: %s' % word)
                buf_string += word + '™ '
            else:
                buf_string += word + ' '

            new_tag.string = buf_string
            print('DEBUG: replace buf: %s' % buf_string)

        print('DEBUG: replace return: %s' % new_tag)
        return new_tag

    # TODO подменять ссылки с оригинального хабра на собственный домен прокси
