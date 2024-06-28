from fastapi import APIRouter
from models.todo_model import Todo
from config.database import collection_name
from schemas.todo_schema import serialize_todos
from bson import ObjectId

router = APIRouter()
 
# Get All Todos
@router.get("/todos")
async def get_todos():
    todos = serialize_todos(collection_name.find())
    return todos

# Create a Todo
@router.post("/todo")
async def create_todo(todo:Todo):
    todo = collection_name.insert_one(dict(todo))

# Update a Todo
@router.put("/todo/{id}")
async def update_todo(id:str,todo:Todo):
     collection_name.find_one_and_update({'_id':ObjectId(id)},{"$set":dict(todo)})
    
# Delete a Todo 
@router.delete("/todo/{id}")
async def delete_todo(id:str):
     collection_name.find_one_and_delete({"_id":ObjectId(id)})

