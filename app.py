from flask import Flask, render_template
import requests
import json

import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRETKEY'

off = {'day':'Off Day'}
metabolic = ['Jump Rope', 'Burpees','Jumping Jacks','Mountain Climbers']
gymnastics = ['air squat','pull up','push up', 'dip', 'sit up', 'lunge']
weightlifting = ['deadlift','shoulder press','squat','kettlbell swing','thruster','benchpress']
wod_type = ['Rounds For Time','As Many Rounds As Possible']

beg_gym_move1 = random.randint(1,5)
beg_gym_move2 = random.randint(1,5)
beg_gym_move3 = random.randint(1,5)
beg_gym_move4 = random.randint(1,5)
beg_gym_move5 = random.randint(1,5)

beg_lift_move1 = random.randint(1,5)
beg_lift_move2 = random.randint(1,5)
beg_lift_move3 = random.randint(1,5)
beg_lift_move4 = random.randint(1,5)
beg_lift_move5 = random.randint(1,5)


beg_wod1 = random.randint(5,10)
beg_wod2 = random.randint(5,10)
beg_wod3 = random.randint(5,10)
beg_wod4 = random.randint(5,10)
beg_wod5 = random.randint(5,10)

beg_met1 = random.randint(10,15)
beg_met2 = random.randint(10,15)
beg_met3 = random.randint(10,15)
beg_met4 = random.randint(10,15)
beg_met5 = random.randint(10,15)

meta1 = random.choice(metabolic)
gym1 = random.choice(gymnastics)
lift1 = random.choice(weightlifting)
workout1 = random.choice(wod_type)

meta2 = random.choice(metabolic)
gym2 = random.choice(gymnastics)
lift2 = random.choice(weightlifting)
workout2 = random.choice(wod_type)

meta3 = random.choice(metabolic)
gym3 = random.choice(gymnastics)
lift3 = random.choice(weightlifting)
workout3 = random.choice(wod_type)

meta4 = random.choice(metabolic)
gym4 = random.choice(gymnastics)
lift4 = random.choice(weightlifting)
workout4 = random.choice(wod_type)

meta5 = random.choice(metabolic)
gym5 = random.choice(gymnastics)
lift5 = random.choice(weightlifting)
workout5 = random.choice(wod_type)



triplet_wod_m = {
    workout3:beg_wod3,
    meta3:beg_met3,
    gym3:beg_gym_move3,
    lift3:beg_lift_move3
    }
triplet_wod_g = {
    workout3:beg_wod3,
    gym3:beg_gym_move3,
    meta3:beg_met3,
    lift3:beg_lift_move3
    }
triplet_wod_l = {
    workout3:beg_wod3,
    lift3:beg_lift_move3,
    meta3:beg_met3,
    gym3:beg_gym_move3
    }
dup_wod_mg = {
    workout2:beg_wod2,
    meta2:beg_met2,
    gym2:beg_gym_move2
    }
dup_wod_ml = {
    workout1:beg_wod1,
    meta1:beg_met1,
    lift1:beg_lift_move1
    }
dup_wod_gm = {
    workout2:beg_wod2,
    gym2:beg_gym_move2,
    meta2:beg_met2
    }
dup_wod_gl = {
    workout1:beg_wod1,
    gym1:beg_gym_move1,
    lift1:beg_lift_move1
    }
dup_wod_lg = {
    workout2:beg_wod2,
    lift2:beg_lift_move2,
    gym2:beg_gym_move2

    }
dup_wod_lm = {
    workout4:beg_wod4,
    lift4:beg_lift_move4,
    meta4:beg_met4
    }
up_wod_m1 = {
    workout4:beg_wod4,
    meta4:beg_met4
    }
up_wod_g1 = {
    workout4:beg_wod4,
    gym4:beg_gym_move4
    }
up_wod_l1 = {
    workout4:beg_wod4,
    lift4:beg_lift_move4
    }
up_wod_m2 = {
    workout5:beg_wod5,
    meta5:beg_met5
    }
up_wod_g2 = {
    workout5:beg_wod5,
    gym5:beg_gym_move5
    }
up_wod_l2 = {
    workout5:beg_wod5,
    lift5:beg_lift_move5
    }

newString1 = str(up_wod_m1).replace("{",'').replace("}", '')
newString2 = str(dup_wod_mg).replace("{",'').replace("}", '')
newString3 = str(triplet_wod_m).replace("{",'').replace("}", '')
newString4 = str(dup_wod_ml).replace("{",'').replace("}", '')
newString5 = str(up_wod_m2).replace("{",'').replace("}", '')
newString6 = str(off).replace("{",'').replace("}", '')
newString7 = str(off).replace("{",'').replace("}", '')



meta_weekbhb = {
        "day1":newString1,
        "day2":newString2,
        "day3":newString3,
        "day4":newString4,
        "day5":newString5,
        "day6":newString6,
        "day7":newString7
        }
@app.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html',meta_weekbhb = meta_weekbhb)

