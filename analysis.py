import pandas as pd

ipl = pd.read_csv(r'Analysis PART/ipl-matches.csv')
players = pd.read_csv(r'Analysis PART/IPL_Ball_by_Ball_2008_2022.csv')

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
    
    if team1 == team2:
        return {'Error': 'Teams name should not be same'}
    else:
        return team_vs_team_record

def overallTeamRecord(team):
    df2 = ipl[(ipl.Team1 == team) | (ipl.Team2 == team)]
    tmp = df2.shape[0]
    mw = df2[df2.WinningTeam == team].shape[0]
    draws = df2[df2.WinningTeam.isnull()].shape[0]
    ml = tmp - (mw + draws)
    sw = (df2[df2.MatchNumber == 'Final'].WinningTeam == team).sum()
    
    overall = {
        'Total matches played': str(tmp),
        'Match won': str(mw),
        'Match lost': str(ml),
        'Draws': str(draws),
        'Season winner': str(sw)
    }

    return overall

def against(team, team2):
    df1 = ipl[((ipl.Team1 == team) & (ipl.Team2 == team2)) | ((ipl.Team1 == team2) & (ipl.Team2 == team))]
    tmp = df1.shape[0]
    mwt1 = df1[df1.WinningTeam == team].shape[0]
    mwt2 = df1[df1.WinningTeam == team2].shape[0]
    draws = tmp - (mwt1 + mwt2)
    
    team_vs_team_record = {
        'Total matches played': tmp,
        'Matches won by ' + team: mwt1,
        'Matches won by ' + team2: mwt2,
        'Draws': draws
    }
    return team_vs_team_record

def against_each_team(team):
    all_teams = teamsAPI()['Teams']
    d = {}
    for each_team in all_teams:
        if team == each_team:
            continue
        else:
            d[each_team] = against(team, each_team)
    return d    


def overall_batter_record(batter):
    inn = players[players.batter == batter]
    ti = inn.ID.nunique()

    runs = inn.batsman_run.sum()
    fours = inn[inn.batsman_run == 4].shape[0]
    sixes = inn[inn.batsman_run == 6].shape[0]
    out = inn.isWicketDelivery.sum()
    avg = runs/out
    balls_faced = inn.shape[0]
    sr = (runs/balls_faced) * 100

    inn1 = inn.groupby('ID')
    inn2 = inn1.sum('batsman_run')
    fifties = inn2[(inn2.batsman_run >= 50) & (inn2.batsman_run < 100)].shape[0]
    hundreds = inn2[inn2.batsman_run >= 100].shape[0]
    
    hs = inn2.batsman_run.max()
    no = inn2[inn2.isWicketDelivery == False].shape[0]

    mom = ipl[ipl.Player_of_Match == batter].shape[0]

    return {
        'Total innings': str(ti),
        'Runs': str(runs),
        'Fours': str(fours),
        'Sixes': str(sixes),
        'Average': str(round(avg, 2)),
        'Strike Rate': str(round(sr, 2)),
        'Fifties': str(fifties),
        'Hundreds': str(hundreds),
        'Highest Score': str(hs),
        'Not Out': str(no),
        'Man of the match': str(mom)        
    }
