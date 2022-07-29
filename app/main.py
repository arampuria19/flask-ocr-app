from flask import Flask, request,render_template, jsonify
from app.functions import functions
import numpy as np

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
        # img = request.files.get('img')
        #A function that takes in image
        #Returns the dict of
        img_arr = cv2.imdecode(
            np.fromstring(request.data,np.uint8),
            cv2.IMREAD_COLOR
        )


if __name__ == '__main__':
    app.run()