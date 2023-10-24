from flask import Flask, render_template, request
from flask_socketio import SocketIO
# from flask_cors import CORS

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
# socketio = SocketIO(app)
# CORS(app)

socketio = SocketIO(app)
# SocketIO(app,cors_allowed_origins="*")
# cors_allowed_origins= 'https://localhost'
# f = open("log.txt", 'w')


@socketio.on('object_list')
def correct_answer(obj):
    print(str(obj))

@socketio.on('wrong')
def score_handle_from_html(data):
    print(str(data))

@socketio.on('connect event')
def test_connect(message):
	print("connected")

@socketio.on('disconnect')
def test_connect(message):
	print("disconnected")


@app.route('/')
def taking_instruction():
    return render_template('index.html')


if __name__ == '__main__':
    socketio.run(app, host='http://127.0.0.1:5000/', debug=True)
