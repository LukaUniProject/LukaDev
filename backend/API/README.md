# API docs
## Структура проекта
main.py - точка входа в приложение

auth - модуль для аутентификации

routers.py - роутеры для обработки запросов

schemas.py - схемы для валидации данных

services.py - сервисы для работы с данными (создание и обработка jwt токенов)

core - модуль для хранения основных настроек и функций

## Как открыть проект
### Перейдите в папку backend:
```bash
cd backend
```
### Создайте и активируйте виртуальную среду:
Для linux:
```bash
python3 -m venv venv
source venv/bin/activate
```
Для windows:
```bash
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
### Перейдите в папку backend:
```bash
cd backend
```
### Активируйте виртуальную среду:
Для linux:
```bash
source venv/bin/activate
```
Для windows:
```bash
venv\Scripts\activate
```
Запустите api:
```bash
uvicorn API.app.main:app --reload
```