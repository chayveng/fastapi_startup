from fastapi import APIRouter

router = APIRouter(
    prefix="/todo",
    tags=["Todo"]
)

@router.get("/greeting")
def greeting():
    return {"message": "Todo route"}

@router.get("/")
def todos():
    return {"message": "todos", "data": [{
    "userId": 1,
    "id": 1,
    "title": "delectus aut autem",
    "completed": False
  },
  {
    "userId": 1,
    "id": 2,
    "title": "quis ut nam facilis et officia qui",
    "completed": False
  }]}