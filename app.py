from flask import Flask, render_template , request
import pickle
import numpy as np
from jinja2 import Template
import pandas as pd

import joblib
model = joblib.load('model/COVID_19.pkl')
    
app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    return render_template('base.html')

@app.route('/blank')
def blank():
    return render_template('blank.html')



@app.route("/DashBoard")
def DashBoard():
    return render_template("DashBoard.html")

@app.route("/News")
def News():
    return render_template("News.html")

@app.route("/calculate", methods=['POST',"GET"])
def calculate():
    return render_template("calculate.html")

@app.route('/calculate/after', methods=['GET',"POST"])
def home():
    data1 = request.form["region_p"]
    data2 = request.form["death"]
    data3 = request.form["confirm"]
    
    arr=pd.DataFrame({
'지역별인구수':data1,
"사망자":data2,
"누적확진":data3,
}, index=[0])
    pred = model.predict(arr)
    data = pred
    return render_template("cal_after.html" , data=data)



app.run('127.0.0.1', port=5000)