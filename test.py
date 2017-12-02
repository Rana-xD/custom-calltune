from flask import Flask, request, render_template, redirect, url_for
# from dejavu.recognize import FileRecognizer, MicrophoneRecognizer
from werkzeug import secure_filename
import json
import requests
import os
import sys
app = Flask(__name__)
@app.route('/upload',methods=['GET', 'POST'])
def upload():
    data = request.body.destinationAddress
    print >> sys.stderr, data
    return render_template('index.html',data=data)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
