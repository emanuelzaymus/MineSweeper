from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/newGameData')
def newGameData():
    jsondata = {
            "rowsCount": 2,
            "columnsCount": 2,
            "data": [
                [
                    {
                        "type": "2",
                        "clickable": True
                    },
                    {
                        "type": "mine",
                        "clickable": True
                    }
                ],
                [
                    {
                        "type": "mine",
                        "clickable": True
                    },
                    {
                        "type": "2",
                        "clickable": True
                    }
                ]
            ]
        }
    return jsonify(jsondata)

@app.route('/post', methods=['POST'])
def post():
    print request.json
    if not request.json or not 'number' in request.json:
        abort(400)
    return jsonify({
        'number': request.json['number'] + 1
    })
