from fastapi import APIRouter
from app.model.todo import Todo as TodoDB
from app.core.mongo_local import db as mongo_db



router = APIRouter(
    prefix="/todo",
    tags=["Todo"]
)

@router.get("/greeting")
def greeting():
    return {"message": "Todo route"}


@router.get("/")
def todos():
  result = mongo_db.query(TodoDB).all()
  return {"todos:", result}

# @router.get("/")
# def todos():
#     return {"message": "todos", "data": [{
#     "userId": 1,
#     "id": 1,
#     "title": "delectus aut autem",
#     "completed": False
#   },
#   {
#     "userId": 1,
#     "id": 2,
#     "title": "quis ut nam facilis et officia qui",
#     "completed": False
#   }]}