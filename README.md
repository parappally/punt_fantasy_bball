# punt_fantasy_bball
Created for /r/fantasybball <br>
ESPN and Yahoo don't have a method of ranking players based on aggregate statistics <br>
e.g. https://fantasy.espn.com/basketball/players/projections <br>
You can only sort players by a specific category which is not that helpful when you want to build a team around multiple statistics <br>
Created a Python program that lets you determine who the best fantasy players are based on multiple statistics from 2019-2020 NBA player data <br>
Let me know if I missed any important statistics, I tailored it to the league that I joined <br>

Instructions:

1. Go to: https://repl.it/@parappally/puntfantasybball#main.py
2. Modify the dictionary in main.py with the categories that your team is using. <br>
For any categories you don't care about, put a hashtag at the start of the line which indicates a Python comment and my script will ignore that category <br>
e.g. if you don't care about MPG, line 9 should look like this: <br> # "MPG": 5, # minutes per game <br>
instead of <br>
"MPG": 5, # minutes per game
3. Press RUN <br>

OR

1. git clone https://github.com/parappally/punt_fantasy_bball.git <br>
2. cd punt_fantasy_bball <br>
3. python3 -m venv env <br>
4. source env/bin/activate <br>
5. pip install -r requirements.txt <br>
6. Modify the dictionary in main.py with the categories that your team is using. <br>
For any categories you don't care about, put a hashtag at the start of the line which indicates a Python comment and my script will ignore that category <br>
e.g. if you don't care about MPG, line 9 should look like this: <br> # "MPG": 5, # minutes per game <br>
instead of <br>
"MPG": 5, # minutes per game
7. python main.py <br>
8. Read the output file, and draft accordingly <br>
