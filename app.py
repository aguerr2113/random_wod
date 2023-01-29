from flask import Flask, render_template

import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRETKEY'

off = ['Off Day']
metabolic = ['Jump Rope', 'Burpees','Jumping Jacks','Mountain Climbers']
gymnastics = ['air squat','pull up','push up', 'dip', 'sit up', 'lunge']
weightlifting = ['deadlift','shoulder press','squat','kettlbell swing','thruster','benchpress']
wod_type = ['Rounds For Time','As Many Rounds As Possible']

beg_gym_move1 = random.randint(1,5)
beg_gym_move2 = random.randint(1,5)
beg_gym_move3 = random.randint(1,5)

beg_lift_move1 = random.randint(1,5)
beg_lift_move2 = random.randint(1,5)
beg_lift_move3 = random.randint(1,5)


beg_wod1 = random.randint(5,10)
beg_wod2 = random.randint(5,10)
beg_wod3 = random.randint(5,10)

beg_met1 = random.randint(10,15)
beg_met2 = random.randint(10,15)
beg_met3 = random.randint(10,15)

meta = random.choice(metabolic)
gym = random.choice(gymnastics)
lift = random.choice(weightlifting)
workout = random.choice(wod_type)



triplet_wod_m = {
    workout:beg_wod1,
    meta:beg_met1,
    gym:beg_gym_move1,
    lift:beg_lift_move1
    }
triplet_wod_g = {
    workout:beg_wod1,
    gym:beg_gym_move1,
    meta:beg_met1,
    lift:beg_lift_move1
    }
triplet_wod_l = {
    workout:beg_wod1,
    lift:beg_lift_move1,
    meta:beg_met1,
    gym:beg_gym_move1
    }
dup_wod_mg = {
    workout:beg_wod1,
    meta:beg_met1,
    gym:beg_gym_move1
    }
dup_wod_ml = {
    workout:beg_wod1,
    meta:beg_met1,
    lift:beg_lift_move1
    }
dup_wod_gm = {
    workout:beg_wod1,
    gym:beg_gym_move1,
    meta:beg_met1
    }
dup_wod_gl = {
    workout:beg_wod1,
    gym:beg_gym_move1,
    lift:beg_lift_move1
    }
dup_wod_lg = {
    workout:beg_wod1,
    lift:beg_lift_move1,
    gym:beg_gym_move1
    }
dup_wod_lm = {
    workout:beg_wod1,
    lift:beg_lift_move1,
    meta:beg_met1
    }
up_wod_m = {
    workout:beg_wod1,
    meta:beg_met1
    }
up_wod_g = {
    workout:beg_wod1,
    gym:beg_gym_move1
    }
up_wod_l = {
    workout:beg_wod1,
    lift:beg_lift_move1
    }

@app.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html',up_wod_l = up_wod_l)