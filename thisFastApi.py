from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from backend import Database

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class UserData(BaseModel):
    name: str = "User"
    message: str

@app.get("/", response_class=HTMLResponse)
def read_root():

    file_path = "/home/chelovek/training/fronEnd/My.html"

    with open(file_path, "r", encoding="utf-8") as file:
        html_content = file.read()

    return HTMLResponse(content=html_content)
#дай мне
@app.get("/api")
def read_api():
    return {"message": "Hello World222"}
#отправь - Заполнить анкету и отдать ее 
@app.post("/api")
def create_user(data: UserData ):
    user_text = data.message
    print(user_text)
    obj = Database() 
    obj.importDataInTables(user_text)
    return {"id": 1, "status": "created333"}

# Новый endpoint для получения данных пользователя
@app.get("/user-data")
def get_user_data():
    return {"message": "Данные успешно получены!"}

@app.post("/user-data")
def create_user_data(user: UserData):
    return {"id": 1, "name": user.name, "status": "created"}