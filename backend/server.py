from flask import Flask, jsonify, request
from flask_cors import CORS
from .controller import Controller

app = Flask(__name__)
CORS(app)
controller = Controller()


def respond_game_state():
    response = jsonify(controller.game.to_json())
    #response = add_cors_headers(response)
    return response

def add_cors_headers(p_response):
    p_response.headers.add('Access-Control-Allow-Origin', '*')
    p_response.headers.add('Access-Control-Allow-Methods', '*')
    p_response.headers.add('Access-Control-Allow-Headers', '*')
    return p_response


@app.route('/game', methods=['GET'])
def get_game_state():
    return respond_game_state()


@app.route('/game', methods=['POST'])
def update_game_state():
    controller.update()
    return respond_game_state()



@app.route('/game/pause', methods=['POST'])
def pause_game():
    controller.pause()
    return respond_game_state()


@app.route('/game/resume', methods=['POST'])
def resume_game():
    controller.resume()
    return respond_game_state()


@app.route('/game/newgame', methods=['POST'])
def new_game():
    controller.newgame()
    return respond_game_state()


@app.route('/game/direction', methods=['POST'])
def change_direction():
    direction = request.json.get('direction')
    controller.change_direction(direction)
    return respond_game_state()
