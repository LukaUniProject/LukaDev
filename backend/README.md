# Backend

## Установка

1. Открыть backend
2. Создайте виртуальную среду

```bash
python -m venv venv
venv\Scripts\activate
```

3. Установите зависимости

```bash
pip install -r requirements.txt
```

4. Запустите сервер

```bash
uvicorn app.main:app --reload
```
