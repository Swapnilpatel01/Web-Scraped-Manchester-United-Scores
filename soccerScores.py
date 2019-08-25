import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import csv
import pandas as pd

url = 'https://www.espn.com/soccer/team/results/_/id/360/manchester-united'
espn_score = requests.get(url) #access to site using requests library


soup = BeautifulSoup(espn_score.text, 'html.parser')


allScoreAndTeam = soup.findAll('a')
scoresAndTeams = []

for element in range(23, len(allScoreAndTeam)-4,2):
    #time.sleep(1)
    scoresAndTeams.append(allScoreAndTeam[element].text)
    #print(all_scores[element].text + ' \n ')


home_team = scoresAndTeams[0::3]
final_score = scoresAndTeams[1::3]
away_team = scoresAndTeams[2::3]

with open('scores.csv', 'a') as f:
    f1 = csv.writer(f)
    n = {'Home' : home_team, 'Score' : final_score, 'Away' : away_team}
    df = pd.DataFrame(n)
    df.to_csv('scores.csv')

    
    

