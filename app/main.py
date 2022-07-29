from flask import Flask, request,render_template, jsonify
from app.functions import functions
import numpy as np
import os
app = Flask(__name__)

'''

https://192.168.1.1:8080/pat
@app.route( '/api', methods=['GET','POST','DELETE','PATCH'] )
def index():

'''

@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/api',methods=['GET','POST'])
def api():
    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template(
                'ocr.html',
                msg='NO FILE SELECTED'
            )
        file = request.files['file']
        if file.filename == '':
            return render_template(
                'ocr.html',
                msg = 'NO FILE FOUND IN THE PATH'
            )
        try:
            return functions.process(img_str)
        except:
            return render_template(
                'ocr.html',
                msg='ERROR HANDLING THE FILE'
            )


if __name__ == '__main__':
    app.run()