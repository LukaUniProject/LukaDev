from fastapi import FastAPI
from .auth.routes import auth_router

app = FastAPI()

# Подключение маршрутов
app.include_router(auth_router, prefix="/api/auth", tags=["Auth"])

# Точка входа
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
