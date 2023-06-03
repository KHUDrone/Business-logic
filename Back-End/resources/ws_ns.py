from flask_socketio import Namespace, emit
from AI.modules import decoding_QR
from pyzbar import pyzbar
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
        # cv2.imshow("img",frame)
        # cv2.waitKey(1)

        #frame = data['frame']
        QR_datas = pyzbar.decode(frame)
        ret = model(frame)
        #ret.show()
        ret = ret.pandas().xyxy[0]

        print(ret['confidence'])

        birds = [data for data in ret['confidence'] if data >= conf_thres]

        QR_loc_x=0
        QR_loc_y=0
        QR_current =0
        QR_next =0
        #print(QR_datas)
        if QR_datas: 
            (QR_loc_x,QR_loc_y,_,_) = QR_datas[0].rect
            QR_current = barcode.data.decode("utf-8")
        

        emit("result", {"TS":datetime.datetime.now().strftime("%H%M%S"),
                        "QR_loc_x":QR_loc_x,
                        "QR_loc_y":QR_loc_y,
                        "current_home":QR_current,
                        "next_home":QR_next,
                        'bird': 1 if birds else 0
                        })
        eventlet.sleep(3)




