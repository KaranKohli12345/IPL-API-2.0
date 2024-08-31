import pandas as pd

ipl = pd.read_csv(r'Analysis PART/ipl-matches.csv')

def teamsAPI():
    teamsList = list(set(list(ipl['Team1']) + list(ipl['Team2'])))

    teams = {
        'Teams': teamsList
    }

    return teams
