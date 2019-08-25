import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import csv
import pandas as pd

url = 'https://www.espn.com/soccer/team/results/_/id/360/manchester-united'
espn_score = requests.get(url) #access to site using requests library


soup = BeautifulSoup(espn_score.text, 'html.parser')


all_scores = soup.findAll('a')
scores1 = []

for element in range(23, len(all_scores)-4,2):
    #time.sleep(1)
    scores1.append(all_scores[element].text)
    #print(all_scores[element].text + ' \n ')


home_team = scores1[0::3]
team_scores = scores1[1::3]
away_team = scores1[2::3]

with open('scores.csv', 'a') as f:
    f1 = csv.writer(f)
    n = {'Home' : y, 'Score' : x, 'Away' : z}
    df = pd.DataFrame(n)
    df.to_csv('scores.csv')

    
    
#print(df)
