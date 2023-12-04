import random
import time
from copy import deepcopy


from utils import check,get_data
from strategy import *
def get_res(Our_combat,Enemy_combat):
    Our_combat_score=0
    Enemy_combat_score = 0
    for i in Our_combat:
        if i.rK==1:
            Our_combat_score+=1
    for i in Enemy_combat:
        if i.bK==1:
            Enemy_combat_score+=1
    Our_combat_score=(Our_combat_score)/len(Our_combat)*100
    Enemy_combat_score=(Enemy_combat_score)/len(Enemy_combat)*100
    return  Our_combat_score,Enemy_combat_score

if __name__=='__main__':
    #init data
    Our_combat_score_lst= []
    Enemy_combat_score_lst = []
    start=time.time()
    for i in range(30000):
        Our_combat,Enemy_combat=get_data(5,5)
        idx=0
        while True:
            idx+=1
            Our_combat_score,Enemy_combat_score=get_res(Our_combat, Enemy_combat)
            # print("第{}轮,{},{}".format(idx, Our_combat_score, Enemy_combat_score))
            if Our_combat_score*Enemy_combat_score==0:
                # print("第{}轮,{},{}".format(idx, Our_combat_score, Enemy_combat_score))
                break
            # out_lst, enemy_lst = randomized_strategy(Our_combat, Enemy_combat)
            out_lst=Formation_optimization_stratery_our(Our_combat, Enemy_combat)
            enemy_lst = Formation_optimization_stratery_enemy(Our_combat, Enemy_combat)
            update(Our_combat,Enemy_combat,out_lst, enemy_lst,1,1)
        Our_combat_score_lst.append(Our_combat_score)
        Enemy_combat_score_lst.append(Enemy_combat_score)
        if (i%10==0):
            print(time.time()-start)
            start=time.time()
            print("i={}".format(i),end="   ")
            print(sum(Our_combat_score_lst) / len(Our_combat_score_lst),end="   ")
            print(sum(Enemy_combat_score_lst) / len(Enemy_combat_score_lst))
    print(sum(Our_combat_score_lst)/len(Our_combat_score_lst))
    print(sum(Enemy_combat_score_lst)/len(Enemy_combat_score_lst))
