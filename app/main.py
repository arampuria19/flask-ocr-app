from flask import Flask, request, jsonify
from functions import functions
app = Flask(__name__)

'''

https://192.168.1.1:8080/pat
@app.route( '/api', methods=['GET','POST','DELETE','PATCH'] )
def index():

'''

@app.route('/',methods=['GET'])
def index():
    # return ('index.html')

@app.route('/api',method=['GET','POST'])
def api():
    if request.method == 'GET':
        pass
    if request.method == 'POST':
        img = request.files.get('img')
        #A function that takes in image
        #Returns the dict of 

if __name__ == '__main__':
    app.run()