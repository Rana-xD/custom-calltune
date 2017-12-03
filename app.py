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
    print "SMS"
    data = request.get_json()
    # print data
    #return "data"
    tel=data["sourceAddress"]
    print tel
    telephone=[tel]
    print telephone
    return "rana"

    # data = {
    # "message" : telephone+"Noob Noob",
    # "password" : "3a75f4fccb40436acd8bdec0b3c0e63a",
    # "sourceAddress" : "77177",
    # "destinationAddresses": tel,
    # "applicationId": "APP_041232"
    # }
    # headers = {
    #         'Content-type': 'application/json',
    # }
    # print data
    # r = requests.post("https://api.dialog/lk/sms/send",data=json.dumps(data),headers=headers)
    # print "DONE chef!"
    #
    # resp=r.content
    # print resp

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
