from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from Chat import get_bot_reply

app = Flask(__name__)

CORS(app)

@app.route('/')
def home():
    return "Welcome"


@app.route('/respuestas/<pregunta>')
def get_response(pregunta):

    message = get_bot_reply(pregunta)
    
    response = {'mensaje': message }

    return jsonify(response),200

@app.route('/respuestas/', methods=['POST'])
def create_response():

    data = request.get_json()
    return jsonify(data), 201, 

if __name__ == '__main__':
    app.run(debug=True, port=3000 )