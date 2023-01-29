import os

MONGO_URL = os.environ.get("MONGO_URL", "mongodb://root:example@127.0.0.1:27017/")
MONGO_DB_NAME = os.environ.get("MONGO_DB_NAME", "task-api")
