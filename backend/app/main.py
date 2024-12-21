from fastapi import FastAPI, Depends, HTTPException, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from app import models, schemas, database, crud, auth, utils

app = FastAPI()

origins = [
    "http://localhost:5173",
    "http://localhost",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

models.Base.metadata.create_all(bind=database.engine)

# Dependency для получения текущего пользователя
def get_current_user(db: Session = Depends(database.get_db), token: str = Depends(auth.decode_access_token)):
    user_id = auth.decode_access_token(token)
    if not user_id:
        raise HTTPException(status_code=401, detail="Invalid authentication token")
    user = crud.get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=401, detail="User not found")
    return user

# Регистрация пользователя
@app.post("/register", response_model=schemas.UserResponse)
def register(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    db_user = crud.get_user_by_username(db, user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return crud.create_user(db, user)

# Авторизация пользователя
@app.post("/login", response_model=schemas.Token)
def login(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    db_user = crud.authenticate_user(db, user.username, user.password)
    if not db_user:
        raise HTTPException(status_code=400, detail="Invalid username or password")
    token = auth.create_access_token({"sub": str(db_user.id)})
    return {"access_token": token, "token_type": "bearer"}

# Создание чата
@app.post("/chats", response_model=schemas.ChatResponse)
def create_chat(
    file: UploadFile = File(...),
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(get_current_user)
):
    file_path = f"./uploads/{file.filename}"
    with open(file_path, "wb") as f:
        f.write(file.file.read())

    analysis = utils.analyze_file(file_path)

    chat = crud.create_chat(db, current_user.id, analysis)
    return chat

# Получение списка чатов
@app.get("/chats", response_model=schemas.ChatListResponse)
def get_chats(
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(get_current_user)
):
    chats = crud.get_chats(db, current_user.id)
    return {"chats": chats}

# Получение информации о конкретном чате
@app.get("/chats/{chat_id}", response_model=schemas.ChatResponse)
def get_chat(
    chat_id: int,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(get_current_user)
):
    chat = crud.get_chat(db, chat_id)
    if not chat or chat.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Chat not found")
    return chat

# Удаление чата
@app.delete("/chats/{chat_id}")
def delete_chat(
    chat_id: int,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(get_current_user)
):
    chat = crud.get_chat(db, chat_id)
    if not chat or chat.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Chat not found")
    crud.delete_chat(db, chat_id)
    return {"detail": "Chat deleted"}
