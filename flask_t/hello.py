from flask import Flask
from flask import request
from werkzeug.serving import WSGIRequestHandler

WSGIRequestHandler.protocol_version = "HTTP/1.1"
app = Flask(__name__)

@app.route('/hello', methods=["POST", "GET"])
def hello():
	resp = app.make_response("World!")
	resp.headers['Access-Control-Allow-Origin'] = '*'
	resp.headers['Connection'] = request.headers.get('Connection')  
	return resp

app.run(host='0.0.0.0')
