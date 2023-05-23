from flask_socketio import Namespace, emit
from AI.modules import decoding_QR
import eventlet
import numpy as np
import cv2
import argparse

class ChatNamespace(Namespace):

    def on_connect(self):
        print("Client connected",)
        #sessioned= session.get()

    def on_disconnect(self):
        print("Client disconnected")

    def on_camera(self,data):

        frame = np.array(data['frame'])
        frame = cv2.imdecode(np.fromiter(frame, np.uint8), cv2.IMREAD_COLOR)
        #frame = data['frame']
        QR_datas = decoding_QR(frame)
    
        bird = 0
        #print(QR_datas)
        emit("result", {"bird":bird,"QR": 1 if QR_datas else 0})
        eventlet.sleep(3)




