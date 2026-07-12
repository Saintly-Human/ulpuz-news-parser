import requests
import json
from bs4 import BeautifulSoup

BASE_URL = 'https://upl.uz'

response = requests.get(BASE_URL).text
soup = BeautifulSoup(response, 'html.parser')

# print(soup)

articles_wrapper = soup.find('div', id="upl-content")
# print(articles_wrapper)

articles_list = articles_wrapper.find_all('div', class_="sh-news")
# print(articles_list, len(articles_list))

result = []

for article in articles_list:
    title = article.find('h2', {'class': 'sh-title'})
    title_text = title.get_text(strip=True)
    detail_link = title.find('a').get('href')
    img = article.find('img').get('data-src')
    text = article.find('div', class_="sh-text").next.get_text(strip=True)
    side_date = article.find('div', class_="side-date").find_all('span')

    date = ''
    comments = 0

    if len(side_date) == 2:
        date = side_date[0].get_text(strip=True)
        comments = side_date[1].get_text(strip=True)
    elif len(side_date) == 1:
        date = side_date[0].get_text(strip=True)
        comments = 0

    result.append({
        'title': title_text,
        'detail_link': detail_link,
        'img': img,
        'text': text,
        'date': date,
        'comments': comments
    })

print(result)

with open('result.json', mode='w', encoding='utf-8') as file:
    json.dump(result, file, ensure_ascii=False, indent=4)