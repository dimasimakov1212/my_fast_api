from fastapi import FastAPI

app = FastAPI()

# Ваша задача - создать приложение FastAPI, которое обрабатывает запросы, связанные с продуктами (товарами).
# Приложение должно иметь две конечные точки:
# 1. Конечная точка для получения информации о продукте:
#    - Маршрут: `/product/{product_id}`
#    - Метод: GET
#    - Параметр пути:
#    - `product_id`: идентификатор продукта (целое число)
#    - Ответ: Возвращает объект JSON, содержащий информацию о продукте, основанную на предоставленном `product_id`
#
# 2. Конечная точка для поиска товаров:
#    - Маршрут: `/products/search`
#    - Метод: GET
#    - Параметры запроса:
#    - `keyword` (строка, обязательна): ключевое слово для поиска товаров.
#    - `category` (строка, необязательно): категория для фильтрации товаров.
#    - `limit` (целое число, необязательно): максимальное количество товаров для возврата
#       (по умолчанию 10, если не указано иное).
#    - Ответ: Возвращает массив JSON, содержащий информацию о продукте, соответствующую критериям поиска.
#
# Запрос GET на `/product/123` должен возвращать:
#
# {
#     "product_id": 123,
#     "name": "Smartphone",
#     "category": "Electronics",
#     "price": 599.99
# }
# В ответ на GET-запрос на `/products/search?keyword=phone&category=Electronics&limit=5` должно вернуться:
#
# [
#     {
#         "product_id": 123,
#         "name": "Smartphone",
#         "category": "Electronics",
#         "price": 599.99
#     },
#     {
#         "product_id": 789,
#         "name": "Iphone",
#         "category": "Electronics",
#         "price": 1299.99
#     },
#     ...
# ]


sample_product_1 = {
    "product_id": 123,
    "name": "Smartphone",
    "category": "Electronics",
    "price": 599.99
}

sample_product_2 = {
    "product_id": 456,
    "name": "Phone Case",
    "category": "Accessories",
    "price": 19.99
}

sample_product_3 = {
    "product_id": 789,
    "name": "Iphone",
    "category": "Electronics",
    "price": 1299.99
}

sample_product_4 = {
    "product_id": 101,
    "name": "Headphones",
    "category": "Accessories",
    "price": 99.99
}

sample_product_5 = {
    "product_id": 202,
    "name": "Smartwatch",
    "category": "Electronics",
    "price": 299.99
}

products = [sample_product_1, sample_product_2, sample_product_3, sample_product_4, sample_product_5]


# Конечная точка для получения информации о товаре по ID
@app.get("/product/{product_id}")
def get_product(product_id: int):
    for product in products:

        if product['product_id'] == product_id:
            return product
    return {"error": "Product not found"}


@app.get("/products/search")
# Конечная точка для поиска товаров по ключевому слову
async def products_searching(keyword: str, category: str | None = None, limit: int = 2):
    result = list()
    for product in products:
        if keyword.lower() in product['name'].lower():
            if category:
                if category != product['category']:
                    continue
            result.append(product)
            if len(result) == limit:
                break

    return result
