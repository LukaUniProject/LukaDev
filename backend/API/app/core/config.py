"""
---------- Пример содержимого файла config.py ----------
import os

class Settings:
    SECRET_KEY = os.getenv("SECRET_KEY", "super_secret_key")
    ACCESS_TOKEN_EXPIRE_MINUTES = 60

settings = Settings()
---------------------------------------------------------
"""