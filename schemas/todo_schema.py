from models.todo_model import Todo


def serialize_todo(todo)->dict:
    return {
        "id":str(todo['_id']),
        "name": todo['name'],
        "description":todo["description"],
        "complete":todo["complete"],
    }

def serialize_todos(todos)->list:
    return [serialize_todo(todo) for todo in todos] 