from login import DATA_URL
import requests
from bs4 import BeautifulSoup

def scrape_data(session):
    response = session.get(DATA_URL)
    soup = BeautifulSoup(response.text, 'html.parser')

    rows = soup.find_all('div', class_='quote')
    data = []

    for row in rows:
        text_elem = row.find('span', class_='text')
        author_elem = row.find('small', class_='author')
        tittle_elem = row.find("h2")
        
        # Validar que los elementos existen
        if text_elem and author_elem:
            text = text_elem.get_text()
            author = author_elem.get_text()
            tittle = tittle_elem.text.strip() if tittle_elem else "N/A"
            description = soup.find("meta", attrs={"name": "description"})
            description = description["content"].strip() if description else "N/A"
            
            data.append({
                "Text": text,
                "Author": author,
                "Title": tittle,
                "Description": description
            })

    return data