# Импортируем модули
import requests
from bs4 import BeautifulSoup

# Имитируем подключение через браузер Mozilla на Windows
st_useragent = "Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0"
st_accept = "text/html"
# формируем хеш заголовков
headers = {
   "Accept": st_accept,
   "User-Agent": st_useragent
}

# Создаем сессию
url = 'https://selectel.ru/blog/tutorials/'

# Отправим GET()-запрос на сайт и сохраним полученное в переменную 'page':
page = requests.get(url, headers)

# Проверим статус запроса
print("Статус запроса =", page.status_code)

# Создаем объект BeautifulSoup для парсинга HTML
soup = BeautifulSoup(page.text, "html.parser")

# Теперь воспользуемся функцией поиска в BeautifulSoup4:
test = soup.find_all('div', class_='category-hero_text f-24')
for tests in test:
    print(tests.text)
  
