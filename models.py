from pydantic import BaseModel, EmailStr, conint
from typing import Optional


# class User(BaseModel):
#     id: int
#     name: str


class User(BaseModel):
    age: int
    name: str


class Feedback(BaseModel):
    """ Класс отзыва """
    name: str
    message: str


class UserCreate(BaseModel):
    """ Создание пользователя """
    name: str
    email: EmailStr
    age: Optional[conint(gt=0)] = None  # опциональный параметр целое положительное число
    is_subscribed: bool | None = True

