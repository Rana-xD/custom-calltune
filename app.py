from flask import Flask, request, render_template, redirect, url_for
# from dejavu.recognize import FileRecognizer, MicrophoneRecognizer
from werkzeug import secure_filename
import json
import requests
import os
# from dejavu import Dejavu
app = Flask(__name__)
@app.route('/upload')
def upload():
   return render_template('upload.html',copyright=0,illegal_content=0, success=0)

@app.route('/uploader', methods = ['GET', 'POST'])
def uploader():
 sendsms()
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

@app.route('/sendsms')
def sendsms():
     url = "https://api.dialog.lk/sms/send"
     body= {
        "message": "Noob",
        "password": "password123#",
        "sourceAddress": "777177",
        "deliveryStatusRequest": "1",
        "destinationAddresses": ["tel: 94765762513"],
        "applicationId": "APP_041214"
     }
     headers = {"Content-type": "application/json"}
     r = requests.post(url, data=json.dumps(body), headers=headers)
     return r.text;

if __name__ == "__main__":
    app.run(host='0.0.0.0')
