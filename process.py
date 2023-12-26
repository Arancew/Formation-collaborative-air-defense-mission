import random
import time
from copy import deepcopy


from utils import check,get_data
from strategy import *
def get_res(    check1,check2,Our_combat,Enemy_combat,people):
    Our_combat_score=0
    Enemy_combat_score = 0
    for i in Our_combat:
        if i.rK==1:
            Our_combat_score+=1
    for i in Enemy_combat:
        if i.bK==1:
            Enemy_combat_score+=1
    a,b=Our_combat_score,Enemy_combat_score
    Our_combat_score=(Our_combat_score)/len(Our_combat)*100*people/10+max(0,(check1-3)*2)
    Enemy_combat_score=(Enemy_combat_score)/len(Enemy_combat)*100*people/10+max(0,(check2-3)*2)
    return  a,b,Our_combat_score,Enemy_combat_score

def select_strategy_our(strategy_code, Our_combat, Enemy_combat):
    if strategy_code == 1:
        return randomized_strategy_our(Our_combat, Enemy_combat)
    elif strategy_code == 2:
        return Unit_Greed_strategy_our(Our_combat, Enemy_combat)  # Assume this function exists
    elif strategy_code == 3:
        return Formation_optimization_stratery_our(Our_combat, Enemy_combat)  # Assume this function exists
    elif strategy_code == 4:
        return equilibrium_Our(Our_combat, Enemy_combat)  # Assume this function exists

def select_strategy_enemy(strategy_code, Our_combat, Enemy_combat):
    if strategy_code == 1:
        return randomized_strategy_enemy(Our_combat, Enemy_combat)
    elif strategy_code == 2:
        return Unit_Greed_strategy_enemy(Our_combat, Enemy_combat)  # Assume this function exists
    elif strategy_code == 3:
        return Formation_optimization_stratery_enemy(Our_combat, Enemy_combat)  # Assume this function exists
    elif strategy_code == 4:
        return equilibrium_Enemy(Our_combat, Enemy_combat)  # Assume this function exists


if __name__=='__main__':
    #init data
    #1随机策略         2单元贪婪策略        3编队优化策略      4编队纳什策略
    check1,check2=3,4
    people=3
    Our_combat_score_lst= []
    Enemy_combat_score_lst = []
    for i in range(30000):
        Our_combat,Enemy_combat=get_data(people,people)
        idx=0
        while True:
            idx+=1
            a,b,Our_combat_score,Enemy_combat_score=get_res(    check1,check2,Our_combat, Enemy_combat,people)
            if a*b==0:
                break

            out_lst = select_strategy_our(check1, Our_combat, Enemy_combat)
            enemy_lst = select_strategy_enemy(check2, Our_combat, Enemy_combat)

            update(Our_combat, Enemy_combat, out_lst, enemy_lst, 1, 1)
            # print(a,b)
            # print(out_lst)
            # print(enemy_lst)
        Our_combat_score_lst.append(Our_combat_score)
        Enemy_combat_score_lst.append(Enemy_combat_score)
        if (i%10==0):
            print("i={}".format(i),end="   ")
            print(sum(Our_combat_score_lst) / len(Our_combat_score_lst),end="   ")
            print(sum(Enemy_combat_score_lst) / len(Enemy_combat_score_lst))
    print(sum(Our_combat_score_lst)/len(Our_combat_score_lst))
    print(sum(Enemy_combat_score_lst)/len(Enemy_combat_score_lst))
