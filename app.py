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
def team_record():
    team = request.args.get('team')

    response = analysis.teamRecord(team)

    return jsonify(response)

app.run(host='0.0.0.0', port=5000)
