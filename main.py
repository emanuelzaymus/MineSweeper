from flask import Flask, request, jsonify
import json
from minesManager import minesManager

app = Flask(__name__)

jsondata = {
        "columns": 9,
        "rows": 9,
        "mines": 10,
        "data": [
            [
                {"type":"empty", "clickable":True},
                {"type":"empty", "clickable":True},
                {"type":"empty", "clickable":True},
                {"type":"empty", "clickable":True},
                {"type":"empty", "clickable":True},
                {"type":"empty", "clickable":True},
                {"type":"empty", "clickable":True},
                {"type":"1", "clickable":True},
                {"type":"mine", "clickable":True}
            ],
            [
                {"type":"empty", "clickable":True},
                {"type":"empty", "clickable":True},
                {"type":"empty", "clickable":True},
                {"type":"empty", "clickable":True},
                {"type":"empty", "clickable":True},
                {"type":"empty", "clickable":True},
                {"type":"empty", "clickable":True},
                {"type":"1", "clickable":True},
                {"type":"1", "clickable":True}
            ],
            [
                {"type":"empty", "clickable":True},
                {"type":"empty", "clickable":True},
                {"type":"1", "clickable":True},
                {"type":"1", "clickable":True},
                {"type":"1", "clickable":True},
                {"type":"1", "clickable":True},
                {"type":"1", "clickable":True},
                {"type":"1", "clickable":True},
                {"type":"empty", "clickable":True},
            ],
            [
                {"type":"1", "clickable":True},
                {"type":"1", "clickable":True},
                {"type":"2", "clickable":True},
                {"type":"mine", "clickable":True},
                {"type":"1", "clickable":True},
                {"type":"2", "clickable":True},
                {"type":"mine", "clickable":True},
                {"type":"2", "clickable":True},
                {"type":"empty", "clickable":True},
            ],
            [
                {"type":"1", "clickable":True},
                {"type":"mine", "clickable":True},
                {"type":"3", "clickable":True},
                {"type":"2", "clickable":True},
                {"type":"2", "clickable":True},
                {"type":"2", "clickable":True},
                {"type":"mine", "clickable":True},
                {"type":"4", "clickable":True},
                {"type":"3", "clickable":True},
            ],
            [
                {"type":"1", "clickable":True},
                {"type":"1", "clickable":True},
                {"type":"2", "clickable":True},
                {"type":"mine", "clickable":True},
                {"type":"1", "clickable":True},
                {"type":"2", "clickable":True},
                {"type":"3", "clickable":True},
                {"type":"mine", "clickable":True},
                {"type":"mine", "clickable":True},
            ],
            [
                {"type":"empty", "clickable":True},
                {"type":"empty", "clickable":True},
                {"type":"1", "clickable":True},
                {"type":"2", "clickable":True},
                {"type":"2", "clickable":True},
                {"type":"2", "clickable":True},
                {"type":"mine", "clickable":True},
                {"type":"3", "clickable":True},
                {"type":"2", "clickable":True},
            ],
            [
                {"type":"empty", "clickable":True},
                {"type":"empty", "clickable":True},
                {"type":"empty", "clickable":True},
                {"type":"1", "clickable":True},
                {"type":"mine", "clickable":True},
                {"type":"2", "clickable":True},
                {"type":"1", "clickable":True},
                {"type":"1", "clickable":True},
                {"type":"empty", "clickable":True},
            ],
            [
                {"type":"empty", "clickable":True},
                {"type":"empty", "clickable":True},
                {"type":"empty", "clickable":True},
                {"type":"1", "clickable":True},
                {"type":"1", "clickable":True},
                {"type":"1", "clickable":True},
                {"type":"empty", "clickable":True},
                {"type":"empty", "clickable":True},
                {"type":"empty", "clickable":True},
            ]
        ]
}

jsondata2 = {
    "columns": 5,
    "rows": 7,
    "mines": 6,
    'data': [[{'clickable': True, 'type': 1},
           {'clickable': True, 'type': 'mine'},
           {'clickable': True, 'type': 2},
           {'clickable': True, 'type': 1},
           {'clickable': True, 'type': 1}],
          [{'clickable': True, 'type': 1},
           {'clickable': True, 'type': 2},
           {'clickable': True, 'type': 3},
           {'clickable': True, 'type': 'mine'},
           {'clickable': True, 'type': 1}],
          [{'clickable': True, 'type': 1},
           {'clickable': True, 'type': 2},
           {'clickable': True, 'type': 'mine'},
           {'clickable': True, 'type': 2},
           {'clickable': True, 'type': 1}],
          [{'clickable': True, 'type': 1},
           {'clickable': True, 'type': 'mine'},
           {'clickable': True, 'type': 2},
           {'clickable': True, 'type': 1},
           {'clickable': True, 'type': 'empty'}],
          [{'clickable': True, 'type': 1},
           {'clickable': True, 'type': 1},
           {'clickable': True, 'type': 1},
           {'clickable': True, 'type': 1},
           {'clickable': True, 'type': 1}],
          [{'clickable': True, 'type': 'empty'},
           {'clickable': True, 'type': 1},
           {'clickable': True, 'type': 1},
           {'clickable': True, 'type': 2},
           {'clickable': True, 'type': 'mine'}],
          [{'clickable': True, 'type': 'empty'},
           {'clickable': True, 'type': 1},
           {'clickable': True, 'type': 'mine'},
           {'clickable': True, 'type': 2},
           {'clickable': True, 'type': 1}]]}

manager = minesManager()
generatedJson = {}

@app.route('/')
def index():
    global manager
    manager = minesManager()
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
    return jsonify(generatedJson)