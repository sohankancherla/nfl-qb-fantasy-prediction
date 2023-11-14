import pandas as pd

for year in range(2017, 2024):
    df = pd.read_csv(f"madden/madden_{year}_ratings.csv")
    fp = pd.read_csv(f"fantasy_pros/{year}.csv").drop(columns=["Pos", "Team", "Unnamed: 0", "#", "AVG", "TTL", "Year"]).rename(columns={"Player":"Name"})
    df = pd.merge(df, fp, on="Name")
    defense = pd.read_csv(f"schedule/{year}/matchups.csv").drop(columns=["Unnamed: 0"])

    players = df[["Team", "Name", "Rating", "Experience", "Salary"]]
    weeks = 18
    if year >= 2021:
        weeks = 19
    for week in range(1, weeks):
        week_col = str(week)
        players = pd.merge(players, df[["Name", week_col]], on="Name")
        home_away_col = f"Week_{week_col}_Home_Away"
        opponent_col = f"Week_{week_col}_Opponent"
        temp_df = defense[["Team", home_away_col, opponent_col]]
        players = pd.merge(players, temp_df, on="Team")
    
    players.to_csv(f"combined/{year}.csv")
