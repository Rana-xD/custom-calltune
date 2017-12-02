from flask import Flask, request, render_template, redirect, url_for
# from dejavu.recognize import FileRecognizer, MicrophoneRecognizer
from werkzeug import secure_filename
import json
import requests
import os

# from dejavu import Dejavu
app = Flask(__name__)
@app.route('/upload',methods=['GET', 'POST'])
def upload():
    data = request.body.destinationAddress
    return render_template('index.html',data=data)

    # config = {
    # apiKey: "AIzaSyBpln_ctf_CW0rptTiuA8pjdOgkXJp3kIA",
    # authDomain: "noob-7d0ad.firebaseapp.com",
    # databaseURL: "https://noob-7d0ad.firebaseio.com",
    # projectId: "noob-7d0ad",
    # storageBucket: "noob-7d0ad.appspot.com",
    # messagingSenderId: "148481981302"
    # }
    # firebase = firebase.initializeApp(config)
    # auth = firebase.auth()
    #
    # # Log the user in
    # user = auth.sign_in_with_email_and_password("ranapann1@gmail.com", "password")
    #
    # # Get a reference to the database service
    # db = firebase.database()
    #
    # # data to save
    # data = request.body
    #
    # # Pass the user's idToken to the push method
    # results = db.child("users").push(data, user['idToken'])

    # return render_template('upload.html',copyright=0,illegal_content=0, success=0)

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
        "password": "3a75f4fccb40436acd8bdec0b3c0e63a",
        "sourceAddress": "777177",
        "deliveryStatusRequest": "1",
        "destinationAddresses": ["tel: 94765762513"],
        "applicationId": "APP_041232"
        }
        headers = {"Content-type": "application/json"}
        r = requests.post(url, data=json.dumps(body), headers=headers)
        return r.text;

    if __name__ == "__main__":
        app.run(host='0.0.0.0')
