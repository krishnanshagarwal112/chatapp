from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('messageFromClient')
def handle_message(message):
    print('Received message from Client > ' + message)
    socketio.emit('messageFromServer', message,broadcast=True, include_self=False)

if __name__ == '__main__':
    socketio.run(app,debug=False,host='0.0.0.0')