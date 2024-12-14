from pydantic import BaseModel, EmailStr

# Схема для регистрации
class RegisterSchema(BaseModel):
    email: EmailStr
    password: str

# Схема для авторизации
class LoginSchema(BaseModel):
    email: EmailStr
    password: str
