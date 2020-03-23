from flask import Flask, render_template, Response, request
import cv2

app = Flask(__name__)


def gen_frames(selection):
    stream = ["rtsp://EU40.cast-tv.com:1935/23595_LIVE_Kotel_Live1/23595_LIVE_Kotel_Live1",
              "rtsp://EU40.cast-tv.com:1935/23595_LIVE_Kotel_LIVE2/23595_LIVE_Kotel_LIVE2",
              "rtsp://freja.hiof.no:1935/rtplive/definst/hessdalen03.stream"
              ]
    # cap = cv2.VideoCapture(
    #     "rtsp://freja.hiof.no:1935/rtplive/definst/hessdalen03.stream")

    cap = cv2.VideoCapture(
        stream[selection])
    while True:
        # for cap in caps:
        # # Capture frame-by-frame
        success, frame = cap.read()  # read the camera frame
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result


@app.route('/video0', methods=["GET"])
def video0():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen_frames(0),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/video1', methods=["GET"])
def video1():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen_frames(1),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/video2', methods=["GET"])
def video2():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen_frames(2),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')


# @app.route('/streaming/<selection>', methods=["GET"])
# def streaming(selection):

#     return render_template('stream.html')

@app.route('/streaming/0', methods=["GET"])
def stream0():

    return render_template('stream0.html')


@app.route('/streaming/1', methods=["GET"])
def stream1():

    return render_template('stream1.html')


@app.route('/streaming/2', methods=["GET"])
def stream2():

    return render_template('stream2.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
