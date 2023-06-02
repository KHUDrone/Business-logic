import socketio
import cv2
import numpy as np
import base64

capture = cv2.VideoCapture(0)

fps = capture.get(cv2.CAP_PROP_FPS)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
#videoWriter = cv2.VideoWriter('video.avi', fourcc, 20, (int(capture.get(3)), int(capture.get(4))))

sio = socketio.Client()
host = "http://127.0.0.1:5001"


@sio.on('connect', namespace='/realtime')
def connect():
    print("connected")

    while True:
        ret, frame = capture.read()

        if ret:
            # cv2.imshow('video', frame)

            frame = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 80])[1]
            #print(frame.shape)
            frame = frame.tolist()
            #frame = np.array(frame)

            #print("hello")
            #print(type(frame))
            sio.emit("camera", {"frame": frame}, namespace='/realtime')
            # videoWriter.write(cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
            sio.sleep(0.1)
        if cv2.waitKey(1) == 27:
            break

    capture.release()
    cv2.destroyAllWindows()


@sio.on('disconnect', namespace='/realtime')
def disconnect():
    print('disconnected')
    #sio.connect(host, namespaces='/realtime')


@sio.on("result", namespace='/realtime')
def result(data):
    print('received:', data)


# --- main ---
if __name__ == "__main__":
    print('start')
    sio.connect(host, namespaces='/realtime')
    sio.wait()


