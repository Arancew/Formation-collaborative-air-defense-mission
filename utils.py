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
    line=random.uniform(0,1)
    for i in val:
        if line<=i:
            return 0
    return 1
