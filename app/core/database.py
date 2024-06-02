from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


class Database:
        
    # class Mongo:
        # def __init__(self, uri="mongodb://admin:79e0c45cbf8d31f4@localhost:27017/startup"):
        #     self.engine = create_engine(uri)
        #     self.Session = sessionmaker(bind=self.engine)
        #     self.Base = declarative_base()
            
        # def connect(self):
        #     return self.Session()

        # def get_db(self):
        #     db = self.connect()
        #     try:
        #         yield db
        #     finally:
        #         db.close()

    class MsSql:
        def __init__(self, uri):
            self.engine = create_engine(uri)
            self.Session = sessionmaker(bind=self.engine)
    
    class PostgreSQL:
        def __init__(self, uri):
            self.engine = create_engine(uri)
            self.Session = sessionmaker(bind=self.engine)

        