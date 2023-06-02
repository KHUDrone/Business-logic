import torch
import cv2

model = torch.hub.load('ultralytics/yolov5', 'custom', 'weights/bird2.pt')

im = "mock/video6.avi"
#img = cv2.imread(im)
# cv2.imshow('pre',img)
# cv2.waitKey(30)

cap = cv2.VideoCapture(im) # 동영상 캡쳐 객체 생성  ---①
count = 0
if cap.isOpened():                 # 캡쳐 객체 초기화 확인
    while True:
        ret, img = cap.read()      # 다음 프레임 읽기      --- ②
        if count < 1000:
            count+=1
            continue
        if ret: # 프레임 읽기 정상
            result = model(img)

            xy = result.pandas().xyxy
            for content in xy:
                if not content.empty:

                    cv2.rectangle(img, (int(content['xmin'][0]),int(content['ymin'][0])),(int(content['xmax'][0]),int(content['ymax'][0])),(0,0,255),3)
            cv2.imshow('im', img) # 화면에 표시  --- ③
            cv2.waitKey(25)            # 25ms 지연(40fps로 가정)   --- ④
        else:                       # 다음 프레임 읽을 수 없슴,
            break

#img = cv2.cvtColor(cv2.imread(im),cv2.BGR2RGB)

#results = model(cv2.cvtColor(img,cv2.COLOR_RGB2BGR))
