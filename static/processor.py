import pandas as pd

def save_to_excel(data, filename="data001.xlsx"):
    df = pd.DataFrame(data)
    df.to_excel(filename, index=False)
    print(f"Data saved to {filename}")

def save_to_csv(data, filename="data001.csv"):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")

def save_to_json(data, filename="data001.json"):
    df = pd.DataFrame(data)
    df.to_json(filename, orient='records', lines=True)
    print(f"Data saved to {filename}")