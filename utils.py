import random

from entity import Our_combat_unit,Enemy_combat_unit



def get_data(our_nums,enemy_nums):
    Our_combat=[]
    Enemy_combat=[]
    for i in range(our_nums):
        Our_combat.append(Our_combat_unit(enemy_nums))
    for i in range(enemy_nums):
        Enemy_combat.append(Enemy_combat_unit(our_nums))
    return Our_combat,Enemy_combat

def  check(val):
    for i in val:
        line = random.uniform(0, 1)
        if line<=i:
            return 0
    return 1
def find_max(my,target):
    idx=0
    maxx=0
    if isinstance(my,Our_combat_unit):
        for i,(pri ,bB) in enumerate(zip(my.pR,target)):
            tmp=pri*bB.bR*bB.bK
            if tmp>maxx:
                idx=i
                maxx=tmp
    else:
        for i, (pbi, bB) in enumerate(zip(my.pB, target)):
            tmp = pbi * bB.rR * bB.rK
            if tmp > maxx:
                idx = i
                maxx = tmp
    return idx
