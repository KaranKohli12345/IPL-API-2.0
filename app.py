from flask import Flask, render_template, jsonify
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

app.run(host='0.0.0.0', port=5000)
