import random
from copy import deepcopy

from utils import find_max,find_enemy_alive,find_our_alive,update,get_target_score


def randomized_strategy_our(Our_combat,Enemy_combat):
    alive=find_enemy_alive(Enemy_combat)
    Our_combat=len(Our_combat)
    Enemy_combat=len(Enemy_combat)
    out_lst=[[0 for _ in range(Enemy_combat)] for _ in range(Our_combat)]
    for i in range(Our_combat):
        j=random.choice(alive)
        out_lst[i][j]=1
    return out_lst
def randomized_strategy_enemy(Our_combat,Enemy_combat):
    alive=find_our_alive(Our_combat)
    Our_combat=len(Our_combat)
    Enemy_combat=len(Enemy_combat)
    enemy_lst=[[0 for _ in range(Our_combat)] for _ in range(Enemy_combat)]

    for i in range(Our_combat):
        j=random.choice(alive)
        enemy_lst[i][j]=1
    return enemy_lst

def Unit_Greed_strategy_our(Our_combat,Enemy_combat):

    out_lst=[[0 for _ in range(len(Enemy_combat))] for _ in range(len(Our_combat))]

    for i in range(len(Our_combat)):

        j=find_max(Our_combat[i],Enemy_combat)
        out_lst[i][j]=1

    return out_lst

def Unit_Greed_strategy_enemy(Our_combat,Enemy_combat):

    enemy_lst=[[0 for _ in range(len(Our_combat))] for _ in range(len(Enemy_combat))]

    for i in range(len(Enemy_combat)):

        j=find_max(Enemy_combat[i],Our_combat)
        enemy_lst[i][j]=1

    return enemy_lst

def Formation_optimization_stratery_our(Our_combat,Enemy_combat):

    max_score=-10000
    max_lst=None
    import itertools
    # 定义一个包含0-9的列表
    numbers = list(range(len(Our_combat)))
    # print(numbers)
    for i in itertools.product(numbers, repeat=len(Our_combat)):
        lst=list(i)
        out_lst = [[0 for _ in range(len(Enemy_combat))] for _ in range(len(Our_combat))]
        for i in range(len(lst)):
            out_lst[i][lst[i]]=1

        tmp_enemy=deepcopy(Enemy_combat)
        update(Our_combat,tmp_enemy,out_lst,[],0,1)
        our_score,_=get_target_score(Our_combat,tmp_enemy)
        if our_score>=max_score:
            max_score=our_score
            max_lst=lst
    lst = max_lst
    # print(lst)
    out_lst = [[0 for _ in range(len(Enemy_combat))] for _ in range(len(Our_combat))]
    for i in range(len(lst)):
        out_lst[i][lst[i]] = 1
    return out_lst


def Formation_optimization_stratery_enemy(Our_combat,Enemy_combat):

    max_score=-10000
    max_lst=None
    import itertools
    # 定义一个包含0-9的列表
    numbers = list(range(len(Our_combat)))
    # print(numbers)
    for i in itertools.product(numbers, repeat=len(Our_combat)):
        lst=list(i)
        enemy_lst = [[0 for _ in range(len(Our_combat))] for _ in range(len(Enemy_combat))]
        for i in range(len(lst)):
            enemy_lst[i][lst[i]]=1
        tmp_our=deepcopy(Our_combat)
        update(tmp_our,Enemy_combat,[],enemy_lst,1,0)
        _,enemy_score=get_target_score(tmp_our,Enemy_combat)
        if enemy_score>=max_score:
            max_score=enemy_score
            max_lst=lst
    lst = max_lst
    enemy_lst = [[0 for _ in range(len(Our_combat))] for _ in range(len(Enemy_combat))]
    for i in range(len(lst)):
        enemy_lst[i][lst[i]] = 1
    return enemy_lst

if __name__=="__main__":
    import itertools

    # 定义一个包含0-9的列表
    numbers = list(range(10))

    for i in itertools.product(numbers, repeat=10):
        print(i)


