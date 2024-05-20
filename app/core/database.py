from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


class Database:
        
    class Mongo:
        def __init__(self, db_url):
            self.engine = create_engine(db_url)
            self.Session = sessionmaker(bind=self.engine)
            self.Base = declarative_base()
            
        def connect(self):
            return self.Session()

        def get_db(self):
            db = self.connect()
            try:
                yield db
            finally:
                db.close()

    class MsSql:
        def __init__(self, db_url):
            self.engine = create_engine(db_url)
            self.Session = sessionmaker(bind=self.engine)
    
    class PostgreSQL:
        def __init__(self, db_url):
            self.engine = create_engine(db_url)
            self.Session = sessionmaker(bind=self.engine)

        