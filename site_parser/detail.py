from .base import BaseParser
from settings import BASE_URL


class DetailParser(BaseParser):
    def get_posts_by_categories(self, categories):
        result = {}

        for category in categories:
            category_name, category_url = category.values()
            print(f'[INFO] получили категорию: {category_name}')
            result[category_name] = []

            category_soup = self.get_soup(BASE_URL + category_url)

            articles_wrapper = category_soup.find('div', id="content-block")

            articles_list = articles_wrapper.find_all('div', class_="sh-news")


            for article in articles_list:
                title = article.find('h2', {'class': 'sh-title'})
                title_text = title.get_text(strip=True)
                print(f'[INFO] получили пост: {title_text}')
                detail_link = title.find('a').get('href')

                detail_soup = self.get_soup(detail_link)

                full_description = detail_soup.find('div', {'itemprop': 'articleBody'})
                import bs4
                full_description = str(full_description).replace('<br/>', '\n')
                full_description = bs4.BeautifulSoup(full_description, 'html.parser').get_text(strip=True)
                print('FULL DESCRIPTION:', full_description)

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

                result[category_name].append({
                    'title': title_text,
                    'detail_link': detail_link,
                    'img': img,
                    'text': text,
                    'date': date,
                    'comments': comments,
                    'full_description': full_description
                })
        return result