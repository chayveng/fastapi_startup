from app.core.database import Database

SQLALCHEMY_DATABASE_URL = "mongodb://admin:79e0c45cbf8d31f4@localhost:27017/startup"

# Create an instance of the Database class
database = Database()

# Create a MongoDB connection
mongo_instance = database.Mongo(db_url=SQLALCHEMY_DATABASE_URL)

# Access the Base attribute from the Mongo instance
Base = mongo_instance.Base

# Get the database session
db = mongo_instance.get_db()
