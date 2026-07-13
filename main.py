from site_parser.category import CategoryParser
from site_parser.detail import DetailParser
from settings import safe_to_json

def main():
    category_parser = CategoryParser()
    categories = category_parser.get_category()

    safe_to_json(categories, 'categories.json')

    detail_parser = DetailParser()
    posts = detail_parser.get_posts_by_categories(categories)

    safe_to_json(posts, 'posts.json')


main()