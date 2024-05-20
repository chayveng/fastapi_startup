# from app.core.mongo import Base
from app.core.mongo_local import Base

class Todo(Base):
    __tablename__ = "todo"
    
    userId: int
    id: int
    title: str
    completed: False