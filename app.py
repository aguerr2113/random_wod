from flask import Flask, render_template,url_for,redirect
from backend.functions import meta_week_1,gym_week_1,lift_week_1






app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRETKEY'


@app.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html')
@app.route('/home',methods=['GET','POST'])
def home():
    return render_template('home.html')

@app.route('/wodweek1',methods=['GET','POST'])
def wod1():
    return render_template('wod_week_one.html',meta_week_1 = meta_week_1)

@app.route('/wodweek2',methods=['GET','POST'])
def wod2():
    return render_template('wod_week_two.html',gym_week_1 = gym_week_1)
@app.route('/wodweek3',methods=['GET','POST'])
def wod3():
    return render_template('wod_week_three.html',lift_week_1 = lift_week_1)


