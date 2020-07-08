# habroxy
Just test work for employment

### Description
Proxy for getting habra pages by URI.

### Requirements
- Python 3.5+
- Flask
- Requests
- bs4(BeautifulSoup)

### Installation
```
git clone https://github.com/itJunky/habroxy.git
cd habroxy
pip install -r requirements.txt
```

### Run
```
export FLASK_APP=habroxy.py
python3 -m flask run
```

### Use
Open in browser http://127.0.0.1:5000/ru/company/habr/blog/506348/

And you can try set any another URI after http://127.0.0.1:5000/
