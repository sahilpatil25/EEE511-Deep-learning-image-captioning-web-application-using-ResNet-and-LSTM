import os
import urllib.request
import sample
from app import app
from flask import Flask, request, redirect, jsonify
from werkzeug.utils import secure_filename
from build_vocab import Vocabulary

#list of image file types allowed
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/file-upload', methods=['POST'])
def upload_file():
	# check if the post request has the file part
	if 'file' not in request.files:
		resp = jsonify({'message' : 'No file part in the request'})
		resp.status_code = 400
		return resp
	file = request.files['file']
	if file.filename == '':
		resp = jsonify({'message' : 'No file selected for uploading'})
		resp.status_code = 400
		return resp
	if file and allowed_file(file.filename):
		filename = secure_filename(file.filename)
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
		result = sample.arg_prep(image_path)
		resp = jsonify({'message' : 'File successfully uploaded', 'caption' :  result[7:-6]})
		resp.status_code = 201
		return resp
	else:
		resp = jsonify({'message' : 'Allowed file types are png, jpg, jpeg, gif'})
		resp.status_code = 400
		return resp

if __name__ == "__main__":
    app.run(debug=False)