from jose import jwt, JWTError
from fastapi import HTTPException, status, Header
from typing import Optional
import time

# Константы для JWT
SECRET_KEY = "your_secret_key"  # Замените на более надежный ключ
ALGORITHM = "HS256"

# Исключение для ошибок авторизации
credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Invalid authentication credentials",
    headers={"WWW-Authenticate": "Bearer"},
)


# Функция для создания JWT токена
def create_jwt_token(data: dict, expires_delta: Optional[int] = 3600):
    """
    Создает JWT токен.
    :param data: Данные, которые будут закодированы в токен.
    :param expires_delta: Срок жизни токена в секундах.
    :return: Закодированный JWT токен.
    """
    to_encode = data.copy()
    to_encode.update({"exp": time.time() + expires_delta})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


# Функция для декодирования и проверки JWT токена
def decode_jwt_token(authorization: str = Header(...)) -> dict:
    """
    Проверяет и декодирует JWT токен из заголовка Authorization.
    :param authorization: Заголовок Authorization с токеном.
    :return: Декодированные данные из токена.
    """
    try:
        # Проверяем наличие префикса Bearer
        if not authorization.startswith("Bearer "):
            raise credentials_exception
        token = authorization[len("Bearer "):]  # Убираем "Bearer "

        # Декодируем токен
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        address: Optional[str] = payload.get("address")

        if address is None:
            raise credentials_exception
        return {"address": address, "role": payload.get("role")}
    except JWTError as e:
        print(f"JWT Error: {str(e)}")
        raise credentials_exception
