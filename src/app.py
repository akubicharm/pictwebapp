from flask import Flask, render_template, request
import os
from datetime import datetime
app = Flask(__name__)

#UPLOAD_DIR="/var/tmp"
UPLOAD_DIR=os.environ['UPLOAD_DIR']

@app.route('/')
def hello_world():
    return 'Hello!'

@app.route('/upload', methods=['POST', 'GET'])
def upload():
  if 'uploadFile' not in request.files:
    return render_template('fileupload.html')

  file = request.files['uploadFile']

  fileName = file.filename
  if '' == fileName:
      return render_template('fileupload.html')
      
  saveFileName = datetime.now().strftime("%Y%m%d_%H%M%S_") + fileName 
  file.save(os.path.join(UPLOAD_DIR, saveFileName))
  return render_template('fileupload.html')
