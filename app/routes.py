from flask import render_template, Response
from app import app
from camera import Camera

#FUNCTIONS
def gen(camera):
	while True:
		frame = camera.get_frame()
		yield (b'--frame\r\n'
				b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


#ROUTES
@app.route('/')
def root():
	return render_template('root.html')

@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/cam')
def cam():
	return render_template('cam.html')

@app.route('/video_feed')
def video_feed():
	return Response(gen(Camera()),
				mimetype='multipart/x-mixed-replace; boundary=frame')
