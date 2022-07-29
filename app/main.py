from flask import Flask, request,render_template, jsonify
from app.functions import functions
import numpy as np
import os
import config
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
        if file and functions.allowed_file(functions,file.filename):
            file_path = os.path.join(
                config.upload_path,
                file.filename
            )
            file.save(file_path)
            img = functions.process(functions,file_path)
            path = functions.saveImage(functions,file_path,img)
            return render_template(
                'ocr.html',
                msg = 'SUCCESS',
                img_src = file.filename
            )
        else:
            return render_template(
                'ocr.html',
                msg = 'INVALID FILE FORMAT'
            )
    else:
        if not os.path.isdir(config.upload_path):
            os.mkdir(config.upload_path)
        return render_template(
            'ocr.html',
            msg = 'ENTER YOUR FILE PLIS'
        )


if __name__ == '__main__':
    app.config['UPLOAD FOLDER'] = config.upload_path
    app.run()