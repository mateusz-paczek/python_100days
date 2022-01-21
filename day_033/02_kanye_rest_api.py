from webbrowser import get
import requests

def get_quote():
    URL = "https://api.kanye.rest"
    content = requests.get(url=URL)
    quote = content.json()["quote"]
    print(quote)

get_quote()