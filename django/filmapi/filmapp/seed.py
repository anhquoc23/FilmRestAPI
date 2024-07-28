from filmapi.filmapp.models import Category


def seed_category():
    with open('./resources/category.txt', 'r', encoding='utf-8') as f:
        lines = f.read()
    lines = lines.split('\n')
    for line in lines:
        Category.objects.create(name=line)


seed_category()