from flask import Flask, request, jsonify
import logging, sys, json

from functions import _register, _insert_data, _login, _train


app = Flask(__name__)

def config_log():
    LEVELS = {'debug': logging.DEBUG,
              'info': logging.INFO,
              'warning': logging.WARNING,
              'error': logging.ERROR,
              'critical': logging.CRITICAL}
    level = logging.DEBUG
    if len(sys.argv) > 1:
        sys.argv
        level_name = sys.argv[1]
        level = LEVELS.get(level_name, logging.NOTSET)

    logging.basicConfig(filename='app.log', level=level)
    if level.__eq__(logging.DEBUG):
        logging.getLogger().addHandler(logging.StreamHandler())



@app.route('/api/register', methods=['POST'])
def register():
    return jsonify(_register(request.get_json(force=True)))


@app.route('/api/insert', methods=['POST'])
def insert_data():
    return jsonify(_insert_data(request.get_json(force=True)))


@app.route('/api/train', methods=['POST'])
def train():
    return jsonify(_train(request.get_json(force=True)))

    
@app.route('/api/login', methods=['GET'])
def login():
    return jsonify(_login(request.get_json(force=True)))


@app.route('/api', methods=['GET', 'POST'])
def hello():
    return 'Hello API OK!'



if __name__ == '__main__':
    config_log()
    app.run(debug=True)