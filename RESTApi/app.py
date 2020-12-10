from flask import Flask
from flask_cors import CORS

#image upload destination
UPLOAD_FOLDER = 'C:\\Users\\patil\\OneDrive\\Documents\\ASU\\Fall2020\\EEE511\\Project\\RESTApi\\uploads'

app = Flask(__name__)
CORS(app)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024