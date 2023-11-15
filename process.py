import random
from copy import deepcopy


from utils import check,get_data


def randomized_strategy(Our_combat,Enemy_combat):
    out_lst=[[0 for _ in range(Enemy_combat)] for _ in range(Our_combat)]
    for i in range(Our_combat):
        j=random.randint(0, Enemy_combat-1)
        out_lst[i][j]=1
    enemy_lst=[[0 for _ in range(Our_combat)] for _ in range(Enemy_combat)]
    for i in range(Our_combat):
        j=random.randint(0, Our_combat-1)
        enemy_lst[i][j]=1
    return out_lst,enemy_lst
def update(Our_combat:list,Enemy_combat:list,out_lst,enemy_lst):
    pre_Our_combat=deepcopy(Our_combat)
    pre_Enemy_combat=deepcopy(Enemy_combat)

    # 更新我方作战单元
    for j in range(len(pre_Our_combat)):
        tmp=[]
        # 找到要攻击i的地方作战单元
        Enemy=[]
        for i,val in enumerate(enemy_lst):
            if pre_Enemy_combat[i].bK==0:
                continue
            if val[j]==1:
                Enemy.append(i)
        for i in Enemy:
            tmp.append(pre_Enemy_combat[i].pB[j])

        Our_combat[j].rK=pre_Our_combat[j].rK*check(tmp)

    # 更新敌方作战单元
    for i in range(len(pre_Enemy_combat)):
        tmp = []
        # 找到要攻击i的地方作战单元
        our= []
        for j,val in enumerate(out_lst):
            if pre_Our_combat[j].rK==0:
                continue
            if val[i] == 1:
                our.append(j)
        for j in our:
            tmp.append(pre_Our_combat[j].pR[i])
        Enemy_combat[i].bK =pre_Enemy_combat[i].bK * check(tmp)
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
    for i in range(100):
        Our_combat,Enemy_combat=get_data(10,10)

        idx=0
        while idx<11:
            idx+=1

            print("第{}轮,{}".format(idx,get_res(Our_combat,Enemy_combat)))
            out_lst, enemy_lst = randomized_strategy(len(Our_combat), len(Enemy_combat))
            update(Our_combat,Enemy_combat,out_lst, enemy_lst)
        print("\n")
