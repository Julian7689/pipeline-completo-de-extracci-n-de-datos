import requests 
from bs4 import BeautifulSoup
import pandas as pd


LOGIN_ = "https://quotes.toscrape.com/login"
DATA_URL = "https://quotes.toscrape.com/"

def logeado_credenciales(session, username, password):
    try:
        payload = {
            "username": ("TUCORREO"),
            "password": ("TUCLAVE"),
        }
        response = session.post(LOGIN_, data=payload)
        if response.status_code == 200 and "Logout" in response.text:
            print("Login exitoso")
            return True
        else:
            print("Error de login")
            return False
    except Exception as e:
        print(f"Error durante el login: {e}")
        return False