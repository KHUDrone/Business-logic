from flask import Flask
from flask_restful import Api
from flask_socketio import SocketIO
from resources import create_socketio
import cv2

host = "0.0.0.0"
port = 5001

SECRET_KEY = "chan"
db_name = "drone"

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+db_name
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = "chan"

api = Api(app) #API FLASK SERVER

sock = SocketIO(app,cors_allowed_origins="*",max_http_buffer_size=50000 * 1000000 * 1000000,ping_timeout=9999999)

create_socketio(sock)

if __name__ == "__main__":

    print("Now we Run...")
    #app.run(host=host,port=port,debug=False)
    sock.run(app,host=host,port=port,debug=False)