import random

random.seed(2023)

class Our_combat_unit:
    def __init__(self,enemy_nums):
        #only 1
        # self.rR = 1#random.uniform(0, 1)#我方编队作战单元的任务价值
        # self.rB = 1#random.uniform(0, 1)#我方编队作战单元在敌方攻击任务中的价值
        # self.rK = 1 #我方编队作战单元的当前状态
        self.rR = random.uniform(0, 1)#我方编队作战单元的任务价值
        self.rB = random.uniform(0, 1)#我方编队作战单元在敌方攻击任务中的价值
        self.rK = 1 #我方编队作战单元的当前状态
        self.pR = [random.uniform(0, 1) for _ in range(enemy_nums)] #我方编队作战单元对应敌方作战单元平台或兵器的毁伤效力
    def __str__(self):
        return f'rR={self.rR}, rB={self.rB}, bR={self.bR}, rK={self.rK}\npR={self.pR}'
class Enemy_combat_unit:
    def __init__(self,our_nums):
        # self.bR = 1#random.uniform(0, 1)#敌方作战单元的任务价值
        # self.bB = 1#random.uniform(0, 1)  #敌方作战单元在我方编队攻击任务中的价值
        self.bR = random.uniform(0, 1)#敌方作战单元的任务价值
        self.bB = random.uniform(0, 1)  #敌方作战单元在我方编队攻击任务中的价值
        self.bK = 1   #敌方作战单元的当前状态
        self.pB = [random.uniform(0, 1) for _ in range(our_nums) ]#敌方作战单元对我方编队作战单元的伤效力
    def __str__(self):
        return f'rR={self.bB}, rB={self.bK}\npB={self.pB}'

# 示例用法


