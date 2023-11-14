import pandas as pd

for year in range(2017, 2024):
    df = pd.read_csv(f"madden/madden_{year}_ratings.csv")

    defense = df["Team"].drop_duplicates().reset_index(drop=True)
    defense = defense.to_frame()
    ratings = pd.read_csv(f"defense/{year}.csv")
    ratings.set_index("DEFENSE", inplace=True)

    weeks = 18
    if year >= 2021:
        weeks = 19
    for i in range(1, weeks):
        defense[f'Week_{i}_Home_Away'] = ''
        defense[f'Week_{i}_Opponent'] = ''
    for index, row in defense.iterrows():
        team = row["Team"]
        if team == "Redskins":
            team = "Washington"
        elif team == "Commanders":
            team = "Washington"
        elif team == "Football Team":
            team = "Washington"
        for i in range(1, weeks):
            schedule = pd.read_csv(f"schedule/{year}/week_{i}.csv")
            home_games = schedule[schedule['Home Team'] == team]
            away_games = schedule[schedule['Away Team'] == team]
            if not home_games.empty:
                opponent = home_games['Away Team'].iloc[0]
                defense.at[index, f'Week_{i}_Home_Away'] = 'Home'
                rating = ratings.loc[opponent, 'DEF RATING']
                defense.at[index, f'Week_{i}_Opponent'] = rating
            elif not away_games.empty:
                opponent = away_games['Home Team'].iloc[0]
                defense.at[index, f'Week_{i}_Home_Away'] = 'Away'
                rating = ratings.loc[opponent, 'DEF RATING']
                defense.at[index, f'Week_{i}_Opponent'] = rating
            else:
                defense.at[index, f'Week_{i}_Home_Away'] = 'Bye'
                defense.at[index, f'Week_{i}_Opponent'] = 'Bye'
    
    defense.to_csv(f"schedule/{year}/matchups.csv")