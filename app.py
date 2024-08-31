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



app.run(debug=True)
