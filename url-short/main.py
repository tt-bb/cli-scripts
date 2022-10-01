import pyshorteners
from dotenv import load_dotenv
import os


# VARIABLES
load_dotenv()
API_KEY = os.getenv("API_KEY")


def short():
    url = input("Enter the URL to shorten > ")
    s = pyshorteners.Shortener(api_key=KEY)
    short_url = s.bitly.short(url)
    print(f"Your new URL : {short_url}")


def expand():
    url = input("Enter the URL to expand > ")
    s = pyshorteners.Shortener(api_key=KEY)
    extended_url = s.bitly.expand(url)
    print(f"Your new URL : {extended_url}")


if __name__ == "__main__":
    KEY = API_KEY
    to_continue = True
    while to_continue:
        print("What do you want to do ?")
        print("1. Shorten an URL")
        print("2. Expand an URL")
        print("q. Quit")
        user_input = input("> ")

        if user_input == "1":
            short()
        elif user_input == "2":
            expand()
        elif user_input.lower() == "q":
            to_continue = False
        else:
            print("Enter [1] or [2] or [q]")
