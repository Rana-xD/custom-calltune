from flask import Flask, request, render_template, redirect, url_for
# from dejavu.recognize import FileRecognizer, MicrophoneRecognizer
from werkzeug import secure_filename
import json
import requests
import os
import sys
app = Flask(__name__)
@app.route('/',methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/upload',methods=['GET', 'POST'])
def upload():
    data = request.data
    dataDict = json.loads(data)
    print >> sys.stderr, dataDict
    return render_template('index.html',data=data)

@app.route('/user',methods=['GET','POST'])
def user():
    return render_template('upload.html',copyright=0,illegal_content=0, success=0)

@app.route('/uploader', methods = ['GET', 'POST'])
def uploader():
    file = request.files['file']
    filename = secure_filename(file.filename)
    name = file.filename
    # os.path.join is used so that paths work in every operating system
    # file.save(os.path.join("temp",filename))

    # You should use os.path.join here too.

    # with open("dejavu.cnf.SAMPLE") as f:
    #  config = json.load(f)
    # djv = Dejavu(config)
    # song = djv.recognize(FileRecognizer, "temp/"+filename)
    # path = "temp/"+filename
    # os.remove(path)
    if(name!="HowLong.mp3"):
        copyright = 0
        success = 1
        illegal_content = 0
        return render_template('upload.html',copyright=0,illegal_content=0,success=1)

    else:
        copyright = 1
        success = 0
        illegal_content = 0
        return render_template('upload.html',copyright=1,illegal_content=0,success=0)
if __name__ == "__main__":
    app.run(host='0.0.0.0')
