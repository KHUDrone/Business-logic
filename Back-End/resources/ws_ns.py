from flask_socketio import Namespace, emit
from AI.modules import decoding_QR
import eventlet
import numpy as np
import cv2
import argparse
import torch
import datetime

model = torch.hub.load('ultralytics/yolov5', 'custom', 'AI/weights/bird2.pt')
conf_thres = 0.50

class ChatNamespace(Namespace):

    def on_connect(self):
        print("Client connected",)
        #sessioned= session.get()

    def on_disconnect(self):
        print("Client disconnected")

    def on_camera(self,data):

        frame = np.array(data['frame'])
        frame = cv2.imdecode(np.fromiter(frame, np.uint8), cv2.IMREAD_COLOR)
        cv2.imshow("img",frame)
        cv2.waitKey(1)

        #frame = data['frame']
        QR_datas = decoding_QR(frame)

        ret = model(frame)
        #ret.show()
        ret = ret.pandas().xyxy[0]

        print(ret['confidence'])

        birds = [data for data in ret['confidence'] if data >= conf_thres]

        #print(QR_datas)
        emit("result", {"TS":datetime.datetime.now().strftime("%H%M%S"),"bird": 1 if birds else 0,"QR": 1 if QR_datas else 0})
        eventlet.sleep(3)




