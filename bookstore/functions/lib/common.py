from pymongo import MongoClient, collection

import os

db_user = os.environ["DB_USER"]
db_password = os.environ["DB_PASSWORD"]


def get_books_collection() -> collection.Collection:

    """
    Returns a MongoDB collection object

    """

    client = MongoClient(f"mongodb+srv://{db_user}:{db_password}")
    database = client["bookstore"]
    collection = database["books"]

    return collection
