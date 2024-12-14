## Структура проекта
main.py - точка входа в приложение

auth - модуль для аутентификации

routers.py - роутеры для обработки запросов

schemas.py - схемы для валидации данных

services.py - сервисы для работы с данными (создание и обработка jwt токенов)

core - модуль для хранения основных настроек и функций

## Как открыть проект
### Создайте и активируйте виртуальное окружение python:
Для linux:
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
```
Для windows:
```bash
cd backend
python -m venv venv
venv\Scripts\activate
```

### Установите зависимости:
```bash
pip install -r requirements.txt
```

### Запустите проекта:
```bash
uvicorn API.app.main:app --reload
```

## Повторный запуск проекта
Для linux:
```bash
cd backend
source venv/bin/activate
uvicorn API.app.main:app --reload
```
Для windows:
```bash
cd backend
venv\Scripts\activate
uvicorn API.app.main:app --reload
```
