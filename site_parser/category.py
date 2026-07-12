from .base import BaseParser


class CategoryParser(BaseParser):
    def get_category(self):
        result = []
        soup = self.get_soup()
        categories_ul = soup.find('div', class_='nav_row').find('ul')
        for item in categories_ul.find_all('a'):
            name = item.get_text(strip=True)
            href = item.get('href')

            if name in ['Реклама', 'Контакты']:
                continue

            result.append({
                'name': name,
                'href': href
            })
        return result