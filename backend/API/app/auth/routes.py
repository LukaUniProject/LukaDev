from fastapi import APIRouter, HTTPException

from .schemas import RegisterSchema, LoginSchema
from .services import create_jwt_token

auth_router = APIRouter()

# Временное хранилище пользователей
fake_users_db = {}


@auth_router.post("/register")
async def register(user: RegisterSchema):
    # Проверка, существует ли уже пользователь с таким email
    if user.email in fake_users_db:
        raise HTTPException(status_code=400, detail="Email already in use")

    # Сохранение пользователя (в этом примере просто хешируем пароль)
    fake_users_db[user.email] = user.password  # В реальной жизни нужно хешировать пароль!

    return {"message": "Registration successful", "status": 201}


@auth_router.post("/login")
async def login(user: LoginSchema):
    # Проверка наличия пользователя и правильности пароля
    if user.email not in fake_users_db or fake_users_db[user.email] != user.password:
        raise HTTPException(status_code=400, detail="Login or password incorrect")

    # Создание JWT токена
    token = create_jwt_token({"address": user.email, "role": "user"})  # Можно заменить роль на что-то другое

    return {"token": token, "status": 200}
