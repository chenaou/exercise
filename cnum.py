import sys
from number import *
# from main import max_value
import random

max_value=10

def create_number(max_value:int)->Number:
    pre=random.randint(1,100)
    if pre<50:#整数
        return Number(
            str(random.randint(1,max_value-1))
        )
    elif pre>50 and pre<75:#分数
        num=Number('')
        num.up=random.randint(1,max_value/2)
        num.down=random.randint(num.up,max_value)
        return num
    else:
        num=Number('')
        num.left=random.randint(1,max_value-1)
        num.up=random.randint(1,max_value/2)
        num.down=random.randint(num.up,max_value)
        return num

def create_char()->str:
    ch=['+','-','×','÷']
    return ch[random.randint(0,3)]
def create_lis()->list:
    nums=[3,5,7]
    li=[]
    for i in range(nums[random.randint(0,2)]):
        global max_value
        if i%2==0:
            num=create_number(max_value)
            approx(num)
            li.append(num)
        else:
            li.append(create_char())
    return li
def add_bracket(li:list)->None:
    if len(li)<7:
        return
    tnum=[0,2,4]
    index=random.randint(0,2)
    li.insert(tnum[index],'(')
    li.insert(tnum[index]+4,')')

