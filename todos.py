
from fastapi import FastAPI, HTTPException, Form
from typing import Optional, List
from pydantic import BaseModel

app = FastAPI(title="TODO API", version="v1.0.0")

class Todo(BaseModel):
    name: str
    due_date: str
    description: str


store_todo = [
    
]

@app.get('/todos/', response_model=List[Todo])
async def get_all_todos():
    return store_todo

@app.post('/login/')
async def login(username: str = Form(...), password: str = Form(...)):
    return {'username': username}


@app.get('/')
async def home():
    return {'hello': 'world'}

@app.get('/todo/{id}')
async def get_to(id: int):
    try:
        return store_todo[id]
    except Exception:
        raise HTTPException(status_code=404, detail='Todo not found in Database')

@app.post('/todo')
async def create_todo(todo: Todo):
    store_todo.append(todo)
    return todo

@app.put('/todo/{id}')
async def update_todo(id: int, new_todo: Todo):
    try:
        store_todo[id] = new_todo
        return store_todo[id]
    except Exception:
        raise HTTPException(status_code=404, detail='Todo not found in Database')
    
@app.delete('/todo/{id}')
async def delete_id(id: int):
    try:
        obj = store_todo[id]
        store_todo.pop(id)
        return obj
    except Exception:
        raise HTTPException(status_code=404, detail='Todo not found in Database')