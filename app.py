from flask import Flask, render_template,url_for,redirect
from backend.functions import meta_week_1,gym_week_1,lift_week_1
import requests

import random


app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRETKEY'




# newString1 = str(up_wod_m1).replace("{",'').replace("}", '')
# newString2 = str(dup_wod_mg).replace("{",'').replace("}", '')
# newString3 = str(triplet_wod_m).replace("{",'').replace("}", '')
# newString4 = str(dup_wod_ml).replace("{",'').replace("}", '')
# newString5 = str(up_wod_m2).replace("{",'').replace("}", '')
# newString6 = str(off).replace("{",'').replace("}", '')
# newString7 = str(off).replace("{",'').replace("}", '')
@app.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/wodweek1',methods=['GET','POST'])
def wod1():
    return render_template('wod_week_one.html',meta_week_1 = meta_week_1)

@app.route('/wodweek2',methods=['GET','POST'])
def wod2():
    return render_template('wod_week_two.html',gym_week_1 = gym_week_1)
@app.route('/wodweek3',methods=['GET','POST'])
def wod3():
    return render_template('wod_week_three.html',lift_week_1 = lift_week_1)
