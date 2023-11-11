import requests
from bs4 import BeautifulSoup
import csv
import os

def fetch_nfl_data(year, week):
    url = f"https://www.nflweather.com/week/{year}/week-{week}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    games = []
    for game_box in soup.find_all('div', class_='game-box'):
        teams = game_box.find_all('span', class_='fw-bold')
        if len(teams) >= 2:
            away_team = teams[0].text.strip()
            home_team = teams[2].text.strip()
            games.append((home_team, away_team))
        else:
            print(f"Debug: No teams found in game div for year {year}, week {week}")
    return games

def main():
    base_path = ''

    for year in range(2017, 2024):
        year_path = os.path.join(base_path, str(year))
        os.makedirs(year_path, exist_ok=True)

        num_weeks = 18 if year >= 2021 else 17

        for week in range(1, num_weeks + 1):
            week_path = os.path.join(year_path, f'week_{week}.csv')
            games = fetch_nfl_data(year, week)

            if games:
                with open(week_path, 'w', newline='', encoding='utf-8') as file:
                    writer = csv.writer(file)
                    writer.writerow(['Year', 'Week', 'Home Team', 'Away Team'])

                    for home_team, away_team in games:
                        writer.writerow([year, week, home_team, away_team])

                print(f"Completed: Year {year} Week {week}")
            else:
                print(f"No games data found for year {year}, week {week}")

if __name__ == "__main__":
    main()
