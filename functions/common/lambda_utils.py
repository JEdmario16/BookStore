import os
import pymongo
from configparser import ConfigParser


def get_config_file() -> ConfigParser:

    # If we are running the lambda function locally, we need to copy the config file from the virtual environment directory to the lambda function directory.
    # With this, we can use the same code to run the lambda function locally and in the cloud.

    # Check if we are running the lambda function in the cloud or locally
    # Note: The lambda function is running locally if the VIRTUAL_ENV variable is set and config.ini file is in the virtual environment directory.
    # If the lambda function is running in the cloud, the VIRTUAL_ENV variable is not set and the config.ini file is in the lambda function directory.

    # Try to get the VIRTUAL_ENV variable and check if the config.ini file is in the virtual environment directory.
    try:
        config_file_path = os.environ["VIRTUAL_ENV"] + "/config.ini"
        config = ConfigParser()
        config.read(config_file_path)

        # write the config file in the lambda function directory
        with open("config.ini", "w", encoding="utf-8") as configfile:
            config.write(configfile)

    # If the VIRTUAL_ENV variable is not set or the config.ini file is not in the virtual environment directory, we are running the lambda function in the cloud.
    except KeyError:
        config_file_path = "config.ini"
        config = ConfigParser()
        config.read(config_file_path)

    return config


def get_products_collection() -> pymongo.collection.Collection:
    """
    Get the products collection from mongo database.
    """

    config = get_config_file()

    # Get the database uri
    db_uri = config["DATABASE"]["db_uri"]

    # Connect to the database
    client = pymongo.MongoClient(db_uri)

    # Get the database
    db = client["bookstore"]

    # Get the products collection
    products = db["products"]

    # Try to get a random document from the products collection to check if the connection is working
    try:
        products.find_one()
    except (
        pymongo.errors.ServerSelectionTimeoutError,
        pymongo.erros.OperationFailure,
    ) as e:
        raise (
            f"Error: Could not connect to the database. Check if config.ini file is correct. {e}"
        )

    return products
