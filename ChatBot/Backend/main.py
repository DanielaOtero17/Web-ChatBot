from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from chat import get_bot_reply

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_msg = data.get('message', '')
    reply = get_bot_reply(user_msg)
    return jsonify({'reply': reply})

if __name__ == '__main__':
    app.run(debug=True, port=3000)