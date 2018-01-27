from flask import Flask, request, jsonify
import json
from minesManager import MinesManager
from minesChecker import MinesChecker

app = Flask(__name__)

manager = MinesManager()
checker = MinesChecker()
generatedJson = {}

@app.route('/')
def index():
    global manager
    manager = MinesManager()
    return app.send_static_file('index.html')

@app.route('/newGameData')
def newGameData():
    global generatedJson
    generatedJson = manager.getMines()
    return jsonify(generatedJson)

@app.route('/postMoveData', methods=['POST'])
def postMoveData():
    if not request.json:
        abort(400)
    ret = checker.checkMines(request.json)
    return jsonify(ret)