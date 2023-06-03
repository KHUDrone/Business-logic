from imutils.video import VideoStream
from pyzbar import pyzbar
import argparse
import datetime
import imutils
import time
import cv2
import torch


def decoding_QR(frame):

    #frame = imutils.resize(frame, width=400)
    # find the barcodes in the frame and decode each of the barcodes
    # 프레임에서 바코드를 찾고, 각 바코드들 마다 디코드
    barcodes = pyzbar.decode(frame)

    barcodeDates = []

    ### Let’s proceed to loop over the detected barcodes
    # loop over the detected barcodes
    for barcode in barcodes:
        # extract the bounding box location of the barcode and draw
        # the bounding box surrounding the barcode on the image
        # 이미지에서 바코드의 경계 상자부분을 그리고, 바코드의 경계 상자부분(?)을 추출한다. 
        (x, y, w, h) = barcode.rect

        # the barcode data is a bytes object so if we want to draw it
        # on our output image we need to convert it to a string first
        # 바코드 데이터는 바이트 객체이므로, 어떤 출력 이미지에 그리려면 가장 먼저 문자열로 변환해야 한다.
        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type

        barcodeDates.append(barcodeData)
        # draw the barcode data and barcode type on the image
        # 이미지에서 바코드 데이터와 테입(유형)을 그린다
        # text = "{} ({})".format(barcodeData, barcodeType)
        # cv2.putText(frame, text, (x, y - 10),
        #     cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        # if the barcode text is currently not in our CSV file, write
        # the timestamp + barcode to disk and update the set
        # 현재 바코드 텍스트가 CSV 파일안에 없을경우, timestamp, barcode를 작성하고 업데이트
        
    return barcodeDates

if __name__ == "__main__":
    im = "qr2.png"
    img = cv2.imread(im)

    datas = decoding_QR(img)
    print(datas)