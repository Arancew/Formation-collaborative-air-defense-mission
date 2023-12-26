import random
from copy import deepcopy

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
def find_our_alive(Our_combat:Our_combat_unit)->list:
    alive_lst=[]
    for i in range(len(Our_combat)):
        if Our_combat[i].rK==1:
            alive_lst.append(i)
    return alive_lst

def find_enemy_alive(Enemy_combat:Enemy_combat_unit)->list:
    alive_lst=[]
    for i in range(len(Enemy_combat)):
        if Enemy_combat[i].bK==1:
            alive_lst.append(i)
    return alive_lst

def get_target_score(Our_combat:list[Our_combat_unit], Enemy_combat:list[Enemy_combat_unit] ):
    our_score=0
    enemy_score=0
    for i in Our_combat:
        our_score+=i.rR*i.rK
    for i in Enemy_combat:
        enemy_score+=i.bR*i.bK
    return our_score-enemy_score,enemy_score-our_score
def update(Our_combat:list,Enemy_combat:list,out_lst,enemy_lst,flag1=1,flag2=1):
    pre_Our_combat=deepcopy(Our_combat)
    pre_Enemy_combat=deepcopy(Enemy_combat)



    # 更新敌方作战单元
    if flag2==1:
        for i in range(len(pre_Enemy_combat)):
            tmp = []
            # 找到要攻击i的我方作战单元
            our= []
            for j,val in enumerate(out_lst):
                if pre_Our_combat[j].rK==0:
                    continue
                if val[i] == 1:
                    our.append(j)
            for j in our:
                tmp.append(pre_Our_combat[j].pR[i])
            Enemy_combat[i].bK =pre_Enemy_combat[i].bK * check(tmp)
    # 更新我方作战单元
    if flag1==1:
        for j in range(len(pre_Our_combat)):
            tmp=[]
            # 找到要攻击j的敌方作战单元
            Enemy=[]
            for i,val in enumerate(enemy_lst):
                if pre_Enemy_combat[i].bK==0:
                    continue
                if val[j]==1:
                    Enemy.append(i)
            for i in Enemy:
                tmp.append(pre_Enemy_combat[i].pB[j])

            Our_combat[j].rK=pre_Our_combat[j].rK*check(tmp)


if __name__=='__main__':
    Our_combat, Enemy_combat = get_data(10, 10)
    print(find_our_alive(Our_combat))
    print(find_enemy_alive(Enemy_combat))