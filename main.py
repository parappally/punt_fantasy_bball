import pandas as pd

df = pd.read_excel(r'/Users/josiahparappally/dev/punt_fantasy_bball/stats.xlsx') # change this to where you store the excel file

# if you don't use a category in your league or you're punting it, set it's value to 0
# I'm punting rpg, apg, spg, and bpg
# data is from: https://www.nbastuffer.com/2019-2020-nba-player-stats/

cats = {
    "FTA": 1, # FREE THROWS ATTEMPTED
    "FTP": 1, # FREE THROW PERCENTAGE
    "2PA": 1, # TWO POINTERS ATTEMPTED
    "2PP": 1, # TWO POINT PERCENTAGE
    "3PA": 1, # THREE POINTERS ATTEMPTED
    "3PP": 1, # THREE POINT PERCENTAGE
    "PPG": 1, # POINTS PER GAME
    "RPG": 0, # REBOUNDS PER GAME
    "APG": 0, # ASSISTS PER GAME
    "SPG": 0, # STEALS PER GAME
    "BPG": 0, # BLOCKS PER GAME
    "TOPG": 1 # TURNOVERS PER GAME
}

player_lst = []

for index, row in df.iterrows():
    aggregate_score = 0
    player_name = row[0]
    player_team = row[1]
    player_position = row[2]
    player_free_throw_attempted = row[3]
    player_free_throw_percentage = row[4]
    player_two_point_attempted = row[5]
    player_two_point_percentage= row[6]
    player_three_point_attempted = row[7]
    player_three_point_percentage = row[8]
    player_points = row[9]
    player_rebounds = row[10]
    player_assists = row[11]
    player_steals = row[12]
    player_blocks = row[13]
    player_turnovers = row[14]
    
    if 1 == cats["FTA"]:
        aggregate_score += player_free_throw_attempted

    if 1 == cats["FTP"]:
        aggregate_score += player_free_throw_percentage

    if 1 == cats["2PA"]:
        aggregate_score += player_two_point_attempted

    if 1 == cats["2PP"]:
        aggregate_score += player_two_point_percentage

    if 1 == cats["3PA"]:
        aggregate_score += player_three_point_attempted

    if 1 == cats["3PP"]:
        aggregate_score += player_three_point_percentage

    if 1 == cats["PPG"]:
        aggregate_score += player_points

    if 1 == cats["RPG"]:
        aggregate_score += player_rebounds

    if 1 == cats["APG"]:
        aggregate_score += player_assists

    if 1 == cats["SPG"]:
        aggregate_score += player_steals

    if 1 == cats["BPG"]:
        aggregate_score += player_blocks

    if 1 == cats["TOPG"]:
        aggregate_score -= player_turnovers
    
    player_lst.append([player_name, player_position, aggregate_score])

player_lst.sort(key=lambda player: player[2], reverse=True) # sorts by their aggregate score, the 2nd index

f = open("output.txt", "w")
for counter, player in enumerate(player_lst):
    f.write(str(counter))
    f.write(str(player))
    f.write("\n")
f.close()
