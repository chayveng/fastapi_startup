import uvicorn
from app.core.database import Database

from app.app import AppCreator

app_creator = AppCreator()
app = app_creator.app
# container = app_creator.container

if __name__ == "__main__":
    print("Startup")
    uvicorn.run("main:app", host="0.0.0.0", port=8088)
