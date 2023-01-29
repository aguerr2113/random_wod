from flask import Flask, render_template

import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRETKEY'

off = ['Off Day']
metabolic = ['Jump Rope', 'Burpees','Jumping Jacks','Mountain Climbers']
gymnastics = ['air squat','pull up','push up', 'dip', 'sit up', 'lunge']
weightlifting = ['deadlift','shoulder press','squat','kettlbell swing','thruster','benchpress']
wod_type = ['Rounds For Time','As Many Reps As Possible']

beg_move1 = random.randint(1,5)
beg_move2 = random.randint(1,5)
beg_move3 = random.randint(1,5)

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

print(f'{beg_met1,meta},{beg_move1,gym},{beg_move1,lift},{beg_wod1,workout}')