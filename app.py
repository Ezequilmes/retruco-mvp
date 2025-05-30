from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit, join_room
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

players = {}
deck = [
    '1 de Espada', '1 de Basto', '7 de Espada', '7 de Oro',
    '3 de Espada', '3 de Basto', '3 de Oro', '3 de Copa',
    '2 de Espada', '2 de Basto', '2 de Oro', '2 de Copa',
    '1 de Oro', '1 de Copa',
    '12 de Espada', '12 de Basto', '12 de Oro', '12 de Copa',
    '11 de Espada', '11 de Basto', '11 de Oro', '11 de Copa',
    '10 de Espada', '10 de Basto', '10 de Oro', '10 de Copa',
    '7 de Basto', '7 de Copa', '6 de Espada', '6 de Basto',
    '6 de Oro', '6 de Copa', '5 de Espada', '5 de Basto',
    '5 de Oro', '5 de Copa', '4 de Espada', '4 de Basto',
    '4 de Oro', '4 de Copa'
]

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('join_game')
def on_join(data):
    username = data['username']
    room = 'sala1'
    join_room(room)
    players[request.sid] = {'username': username}
    if len(players) == 2:
        cartas = random.sample(deck, 6)
        sockets = list(players.keys())
        socketio.emit('cartas', {'cartas': cartas[:3]}, room=sockets[0])
        socketio.emit('cartas', {'cartas': cartas[3:]}, room=sockets[1])
        socketio.emit('mensaje', {'msg': '¡Reparto de cartas realizado!'}, room=room)

@socketio.on('mensaje')
def handle_message(data):
    emit('mensaje', {'msg': data['msg']}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
