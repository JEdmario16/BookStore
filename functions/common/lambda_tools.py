import os
import configparser
import pymongo


def get_config():
    """
    Get the config from the config file.
    Note that if the application is running locally, the config file is in ``venv`` directory.
    Else, the config file must be in the root directory.
    Every time that the application is running locally, the config file will be copy to the root directory, overwriting if necessary.
    The config file can be updated by running ``manager create_setup``.

    The config file content:
    [DATABASE]
    db_uri = <database uri>
    [SECRET]
    # not in use yet
    """

    config = configparser.ConfigParser()
    config_dir = os.environ.get("VIRTUAL_ENV", ".")

    if os.path.exists(config_dir + "/config.ini"):
        config.read(config_dir + "/config.ini")
    else:
        raise Exception(
            "Cant find config file. Did you run manager create_setup?"
        )
    return config


def get_database() -> pymongo.database.Database:

    """
    Get the database connection.
    """

    config = get_config()
    client = pymongo.MongoClient(config["DATABASE"]["db_uri"])
    try:
        db = client["bookstore"]
    except Exception as e:
        raise Exception(
            "Cant connect to database. Did you run manager create_setup?", e
        )
    return db
