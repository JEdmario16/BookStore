import argparse
import os
import configparser

parser = argparse.ArgumentParser(
    description="This is a script to manage the bookstore application.",
    prog="manager",
    usage="manager [options]",
)

parser.add_argument(
    "command",
    choices=["hello", "create_setup"],
    help="The command to run.",
)


def hello():
    print("Hello world")
    print("Your database uri is: " + os.environ["DB_URI"])


def create_setup():

    config = configparser.ConfigParser()
    config.add_section("DATABASE")
    config["DATABASE"]["db_uri"] = input("Type database connection uri: ")

    if os.path.exists("config.ini"):
        ans = input(
            "config.ini already exists. Do you want to overwrite it? (y/n)"
        )
        if ans.lower() == "n":
            return None

    # Write the config file in env directory.
    # Poetry create a virtual variable containing the path to the env directory, so we can use it.
    try:
        with open(
            os.environ["VIRTUAL_ENV"] + "/config.ini", "w"
        ) as configfile:
            config.write(configfile)
    except KeyError:
        print(
            "Cant find the virtual environment directory. Did you run poetry install/shell?"
        )

    return 1


def main():

    args = parser.parse_args()

    if args.command == "hello":
        hello()

    if args.command == "create_setup":
        create_setup()
