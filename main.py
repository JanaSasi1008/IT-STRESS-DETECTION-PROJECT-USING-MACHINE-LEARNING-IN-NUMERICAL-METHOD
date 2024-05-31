from flask import Flask, request, jsonify,render_template
import pickle
import pandas as pd
import joblib
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('admin.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/adminval',methods=['POST','GET'])
def adminval():
    if request.method == 'POST':
        uname = request.form.get('username')
        upass = request.form.get('password')
        if uname == 'admin' and upass == '1234':
            return render_template('index.html')
        else:
            return render_template('admin.html', msg = 'Invalid Data')

@app.route('/predict', methods=['POST','GET'])
def predict():
    input_features = []
    age = request.form.get('age')
    gender = request.form.get('gender')
    dsg = float(request.form.get('dsg'))
    ra = float(request.form.get('ra'))
    mfs = float(request.form.get('mfs'))
    wfh = request.form.get('wfh')
    com = request.form.get('com')
    input_features.append(dsg)
    input_features.append(ra)
    input_features.append(mfs)
    loaded_model = joblib.load('model.joblib')

    prediction = loaded_model.predict([input_features])
    msg1 = prediction[0] * 100
    msg = "The stress level is "  + str(msg1) + " %"
    return render_template('index.html', msg=msg,age=age,gender=gender,wfh=wfh,com=com)


if __name__ == '__main__':
    app.run(debug=True)