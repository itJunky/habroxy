from common import Proxify
from flask import Flask
app = Flask(__name__)
url_prefix = 'https://habr.com/'
p = Proxify()


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def url_handler(path):
    return p.get_page(url_prefix + path)


