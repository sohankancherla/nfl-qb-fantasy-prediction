import pandas as pd

for year in range(2017, 2024):
    df = pd.read_csv(f"combined/{year}.csv").drop("Unnamed: 0", axis=1)
    weeks = 19 if year >= 2021 else 18
    
    reshaped_data = pd.DataFrame()

    for week in range(1, weeks):
        week_cols = ['Team', 'Name', 'Rating', 'Experience', 'Salary',
                     str(week), f'Week_{week}_Home_Away', f'Week_{week}_Opponent']
        
        if all(col in df.columns for col in week_cols):
            temp_df = df[week_cols].copy()
            temp_df.rename(columns={str(week): 'Score', 
                                    f'Week_{week}_Home_Away': 'Home_Away', 
                                    f'Week_{week}_Opponent': 'Opponent'}, inplace=True)
            temp_df['Week'] = week
            reshaped_data = pd.concat([reshaped_data, temp_df])

    reshaped_data.reset_index(drop=True, inplace=True)
    reshaped_data.sort_values(by=['Name', 'Week'], inplace=True)

    reshaped_data.to_csv(f"reshaped/{year}.csv")
