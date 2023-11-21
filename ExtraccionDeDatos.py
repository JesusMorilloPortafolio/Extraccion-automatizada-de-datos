#Script para recopilar información de mundiales de futbol desde 1930 a 2018.
from bs4 import BeautifulSoup
import requests #Esta libreria nos ayuda a mandar solisitudes a una apgina web
import pandas as pd

years = [1930, 1934, 1938, 1950, 1954, 1958, 1962, 1966, 1970, 1974,
         1978, 1982, 1990, 1994, 1998, 2002, 2006, 2010, 2014,
         2018]

def get_matches(year):

    web = f'https://en.wikipedia.org/wiki/{year}_FIFA_World_Cup'
    response = requests.get(web)
    content = response.text
    soup = BeautifulSoup(content, 'lxml')

    matches = soup.find_all('div', class_='footballbox')


    home = []
    score = []
    away = []
    for match in matches:
        home.append(match.find('th', class_= 'fhome').get_text())
        score.append(match.find('th', class_= 'fscore').get_text())
        away.append(match.find('th', class_= 'faway').get_text())

    dict_football = {'Local':home, 'Puntos':home, 'Visitante':away}
    df_football = pd.DataFrame(dict_football)
    df_football['year'] = year
    return df_football

#Datos historicos 
fifa = [get_matches(year) for year in years]
df_fifa = pd.concat(fifa, ignore_index=True)#esto nos ayuda a concatenar los DataFrames
df_fifa.to_csv('soccerWorldCup_datos_historicos.csv', index=False)

#fixture datos 2022
df_fixture = get_matches('2022')
df_fixture.to_csv('soccerWorldCup_datos_2022.csv', index=False)