from number import *
import random


def create_number(maxv: int) -> Number:
    pre = random.randint(1, 100)
    if pre < 50:  # 整数
        return Number(str(random.randint(1, maxv - 1)))
    elif 50 < pre < 75:  # 分数
        num = Number('')
        up = random.randint(1, int(maxv / 2))
        num.frac = Fraction(up, random.randint(up, maxv))
        return num
    else:
        num = Number('')
        left = random.randint(1, maxv - 1)
        up = random.randint(1, int(maxv / 2))
        down = random.randint(up, maxv - 1)
        num.frac = Fraction(
            left * down + left,
            down
        )
        return num


def create_char() -> str:
    ch = ['+', '-', '×', '÷']
    return ch[random.randint(0, 3)]


def create_lis(maxv: int) -> list:
    nums = [3, 5, 7]
    li = []
    for i in range(nums[random.randint(0, 2)]):
        if i % 2 == 0:
            num = create_number(maxv)
            li.append(num)
        else:
            li.append(create_char())
    return li


def add_bracket(li: list) -> None:
    if len(li) < 7:
        return
    tnum = [0, 2, 4]
    index = random.randint(0, 2)
    li.insert(tnum[index], '(')
    li.insert(tnum[index] + 4, ')')
