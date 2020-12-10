import pandas as pd
import math

df = pd.read_excel(r'/Users/josiahparappally/dev/punt_fantasy_bball/all_stats.xlsx') # change this to where you store the excel file

# this is a dictionary of categories, comment out the categories that are not relevant to you

categories = {
    "MPG": 5, # minutes per game
    "MIN%": 6, # percentage of team minutes used by a player while he was on the floor
    "USG%": 7, # Usage rate calculates what percentage of team plays a player was involved in while he was on the floor
    "TO%": 8, # the number of turnovers a player commits per 100 possessions
    "FTA": 9, # free throws attempted
    "FT%": 10, # free throw percentage
    "2PA": 11, # 2 pointers attempted
    "2P%": 12, # 2 point percentage
    "3PA": 13, # 3 pointers attempted 
    "3P%": 14, # 3 point percentage
    "eFG%": 15, # 3 pointers are weighed 50% more heavily than 2 point shots
    "TS%": 16, # intended to more accurately calculate a player's shooting than field goal percentage, free throw percentage, and three-point field goal percentage taken individually
    "PPG": 17, # points per game
    "RPG": 18, # rebounds per game
    "TRB%": 19, # available rebounds grabbed by player when they are on the court
    "APG": 20, # assists per game
    "AST%": 21, # teammate field goals the player assisted while on the court
    "SPG": 22, # steals per game
    "BPG": 23, # blocks perr game
    "TOPG": 24, # turnovers per game
    "VI": 25, # players ability to produce in points, assists, and rebounds, 
    "ORTG": 26, # number of points produced by a player per 100 possessions
    "DRTG": 27, # how many points the player allowed per 100 possessions 
}

lst = []
for index, row in df.iterrows():

    if index == 0:
        continue

    player_aggregate_score = 0

    for key in categories:
        index = categories[key]

        if "TO%" == key or "TOPG" == key:
            player_aggregate_score -= row[index]
        else:
            player_aggregate_score += row[index]
    
    if math.isnan(player_aggregate_score):
        continue

    player_name = row[0]
    player_team = row[1]
    player_position = row[2]
    player_tuple = (player_name, player_team, player_position, player_aggregate_score)
    lst.append(player_tuple)

lst.sort(key=lambda player: player[-1], reverse=True)

f = open("output.txt", "w")
rank = 1
for player in lst:
    f.write(str(rank) + " - ")
    f.write(str(player))
    f.write("\n")
    rank += 1
f.close()
