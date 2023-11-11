import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = "https://www.fantasypros.com/nfl/reports/leaders/qb.php"
years = range(2017, 2024)

all_data = pd.DataFrame()

for year in years:
    url = f"{base_url}?year={year}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table', {'id': 'data'})
    df = pd.read_html(str(table))[0]
    df['Year'] = year
    df.to_csv(f"{year}.csv")