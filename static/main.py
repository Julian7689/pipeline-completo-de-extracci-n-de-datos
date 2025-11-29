import requests
from login import logeado_credenciales
from scrapper import scrape_data
from processor import save_to_excel, save_to_csv, save_to_json

def pipeline(username, password):
    with requests.Session() as session:
        
        if not logeado_credenciales(session, username, password):
            return
        
        data = scrape_data(session)
        
        if data:
            save_to_excel(data)
            save_to_csv(data)
            save_to_json(data)
        else:
            print("No se encontró información para scrapear.")


if __name__ == "__main__":
    pipeline("mi_usuario", "mi_password")