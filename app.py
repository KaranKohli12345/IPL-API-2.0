from flask import Flask, render_template, jsonify, request
import analysis

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# API-1
@app.route('/api/teams')
def teams():
    response = analysis.teamsAPI()

    return jsonify(response)

# API-2
@app.route('/api/teamVsTeam')
def team_Vs_Team():
    team1 = request.args.get('team1')
    team2 = request.args.get('team2')

    response = analysis.teamVsTeam(team1, team2)

    return jsonify(response)

# API-3
@app.route('/api/team-record-overall')
def team_record_overall():
    team = request.args.get('team')

    response = analysis.overallTeamRecord(team)

    return jsonify(response)

# API-4
@app.route('/api/team-record-against-each-team')
def team_record_against():
    team = request.args.get('team')

    response = analysis.against_each_team(team)

    return jsonify(response)

# API-5
@app.route('/api/batter-record')
def overall_batter_record_():
    batter = request.args.get('batter')

    response = analysis.overall_batter_record(batter)

    return jsonify(response)

app.run(host='0.0.0.0', port=5000)
# app.run(debug=True)
