import pandas as pd

ipl = pd.read_csv(r'Analysis PART/ipl-matches.csv')

def teamsAPI():
    teamsList = list(set(list(ipl['Team1']) + list(ipl['Team2'])))

    teams = {
        'Teams': teamsList
    }

    return teams

def teamVsTeam(team1, team2):
    df1 = ipl[((ipl.Team1 == team1) & (ipl.Team2 == team2)) | ((ipl.Team1 == team2) & (ipl.Team2 == team1))]
    tmp = df1.shape[0]
    mwt1 = df1[df1.WinningTeam == team1].shape[0]
    mwt2 = df1[df1.WinningTeam == team2].shape[0]
    draws = tmp - (mwt1 + mwt2)
    
    team_vs_team_record = {
        'Total matches played': tmp,
        'Matches won by ' + team1: mwt1,
        'Matches won by ' + team2: mwt2,
        'Draws': draws
    }
    return team_vs_team_record
