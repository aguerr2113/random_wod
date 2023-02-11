import random

off = ['Off Day']
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

up_wod_m1 ={
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
upwodm1 = str(up_wod_m1).replace(",","\n").replace("'","\n").replace("{","").replace("}", "")
dupwodm1 =str(dup_wod_ml).replace(",","\n").replace("'","\n").replace("{","").replace("}", "")
tripwodm = str(triplet_wod_m).replace(",","\n").replace("'","\n").replace("{","").replace("}", "")
dupwodmg = str(dup_wod_mg).replace(",","\n").replace("'","\n").replace("{","").replace("}", "")
upwodm2 = str(up_wod_m2).replace(",","\n").replace("'","\n").replace("{","").replace("}", "")
office = str(off).replace(",","\n").replace("'","\n").replace("{","").replace("}", "")

upwodg1 = str(up_wod_g1).replace(",","\n").replace("'","\n").replace("{","").replace("}", "")
dupwodgl = str(dup_wod_gl).replace(",","\n").replace("'","\n").replace("{","").replace("}", "")
tripletwodg = str(triplet_wod_g).replace(",","\n").replace("'","\n").replace("{","").replace("}", "")
dupwodgm = str(dup_wod_gm).replace(",","\n").replace("'","\n").replace("{","").replace("}", "")
upwodg2 = str(up_wod_g2).replace(",","\n").replace("'","\n").replace("{","").replace("}", "")

upwodl1 = str(up_wod_l1).replace(",","\n").replace("'","\n").replace("{","").replace("}","")
dupwodlm = str(dup_wod_lm).replace(",","\n").replace("'","\n").replace("{","").replace("}","")
tripletwodl = str(triplet_wod_l).replace(",","\n").replace("'","\n").replace("{","").replace("}","")
dupwodlg = str(dup_wod_lg).replace(",","\n").replace("'","\n").replace("{","").replace("}","")
upwodl2 = str(up_wod_l2).replace(",","\n").replace("'","\n").replace("{","").replace("}","")





meta_week_1 = {
    "day1":upwodm1,
    "day2":dupwodm1,
    "day3":tripwodm,
    "day4":dupwodmg,
    "day5":upwodm2,
    "day6":office,
    "day7":office
}
gym_week_1 = {
    "day1":upwodg1,
    "day2":dupwodgl,
    "day3":tripletwodg,
    "day4":dupwodgm,
    "day5":upwodg2,
    "day6":office,
    "day7":office
}



lift_week_1 = {
    'day1':upwodl1,
    'day2':dupwodlm,
    'day3':tripletwodl,
    'day4':dupwodlg,
    'day5':upwodl2,
    'day6':office,
    'day7':office
}






lift_week_one = str(lift_week_1).replace("{","").replace("}", "")
gym_week_one = str(gym_week_1).replace("{","").replace("}", "")
meta_week_one = str(meta_week_1).replace("{","").replace("}", "")
