# Функция вывода общей выручки
def total_revenue(purchases):
    total = sum([purchase['price'] * purchase['quantity'] for purchase in purchases])
    print(f'Общая выручка: {total}')

# Функция вывода списка товаров по категориям
def items_by_category(purchases):
    sorted_items = {}
    for purchase in purchases:
        if purchase['category'] not in sorted_items:
            sorted_items[purchase['category']] = []
        if purchase['item'] not in sorted_items[purchase['category']]:
            sorted_items[purchase['category']].append(purchase['item'])
    print(f'Товары по категориям: {sorted_items}')

# Функция вывода списка покупок, где price >= min_price
def expensive_purchases(purchases, min_price=1.0):
    exp_purch = [purchase for purchase in purchases if purchase['price'] >= min_price]
    print(f'Покупки дороже {min_price}: {exp_purch}')

# Функция вывода средней цены товаров по категориям
def average_price_by_category(purchases):
    categories = {}
    for purchase in purchases:
        if purchase['category'] not in categories:
            categories[purchase['category']] = [purchase['price']]
        else:
            categories[purchase['category']].append(purchase['price'])
    for key in categories:
        categories[key] = sum(categories[key]) / len(categories[key])
    print(f'Средняя цена по категориям: {categories}')

# Функция вывода категории с наибольшим числом проданных товаров (quantity)
def most_frequent_category(purchases, most_freq=0):
    categories = {}
    for purchase in purchases:
        if purchase['category'] not in categories:
            categories[purchase['category']] = [purchase['quantity']]
        else:
            categories[purchase['category']].append(purchase['quantity'])
    most_freq = max([sum(i) for i in categories.values()])
    for key, val in categories.items():
        if sum(val) == most_freq:
            print(f'Категория с наибольшим количеством проданных товаров: {key}')

# Функция вывода отчета
def report():
    total_revenue(purchases)
    items_by_category(purchases)
    expensive_purchases(purchases)
    average_price_by_category(purchases)
    most_frequent_category(purchases)

# Читаем файл
with open('data.txt') as f:
    exec(f.read())

report()