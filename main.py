from fastapi import FastAPI
from fastapi.responses import FileResponse
from starlette.responses import JSONResponse
import requests

from models import Feedback, User, UserCreate
from task_3_1 import products

app = FastAPI()
users_feedbacks = []

page = 'index.html'


# user = User(id=1, name='Dima')


@app.get("/")
async def root():
    return FileResponse(page)


@app.get('/custom')
def read_custom_message():
    return {"message": "This is a custom message!"}


@app.post("/calculate")
async def calculate(num1: int, num2: int):
    return f"result = {num1 + num2}"


# запрос в postman: http://localhost:8000/calculate?num1=12&num2=2


# @app.get('/users', response_model=User)
# async def get_user():
#     return user


# @app.get('/users/2')
# async def new_user():
#     user_data = {
#         "id": 1,
#         "name": 'Fifa'
#     }
#
#     my_user: User = User(**user_data)
#     # my_user = User(**user_data)  # оба варианта рабочие
#     return my_user
# ----------------------------------------------------------------------

@app.post('/user')
async def check_user():
    user_data = {
        "age": 20,
        "name": 'Frank'
    }

    user_2: User = User(**user_data)

    user_data_new = {
        "age": user_2.age,
        "name": user_2.name,
        "is_adult": user_2.age >= 18
    }

    return user_data_new


# ---------------------------------------------------------

# Пример пользовательских данных (для демонстрационных целей)
fake_users = {
    1: {"username": "john_doe", "email": "john@example.com"},
    2: {"username": "jane_smith", "email": "jane@example.com"},
    3: {"username": "piter_parker", "email": "piter@example.com"},
}


# Конечная точка для получения информации о пользователе по ID
@app.get("/users/{user_id}")
def read_user(user_id: int):
    if user_id in fake_users:
        return fake_users[user_id]
    return {"error": "User not found"}


@app.get("/users/")
def read_users(limit: int = 1):
    return dict(list(fake_users.items())[:limit])


# -----------------------------------------------------------------------------
# запись отзыва пользователя в список

@app.post("/feedback")
async def get_feedback(feedback: Feedback):
    # post запрос в postman
    #     {
    #     "name": "Nick",
    #     "message": "Great course! I'm learning a lot."
    #     }

    users_feedbacks.append({"name": feedback.name, "message": feedback.message})
    print(users_feedbacks)

    system_answer = {"message": f"Feedback received. Thank you, {feedback.name}!"}

    return system_answer


@app.get("/feedbacks")
async def feedbacks_list():
    return users_feedbacks


# --------------------------------------------------------------------------
# FastAPI предоставляет простой способ обработки параметров запроса,
# определяя их в качестве аргументов функции в ваших функциях маршрутизации

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
# в данном примере пропускает первый элемент, выводит всего 10 элементов
async def read_item(skip: int = 1, limit: int = 10):
    return fake_items_db[skip: skip + limit]


# ---------------------------------------------------------------------------
# задача - создать конечную точку FastAPI, которая принимает POST-запрос
# с данными о пользователе/юзере в теле запроса

# {
#     "name": "Alice",
#     "email": "alice@example.com",
#     "age": 30,
#     "is_subscribed": true
# }


@app.post("/create_user")
async def creating_user(new_user: UserCreate) -> UserCreate:
    # new_user.is_subscribed = False
    return new_user


# -------------------------------------------------------------------

# ----------------------------------------------------------------------------

