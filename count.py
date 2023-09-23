from number import *


def get_suffix(infix):
    # 中缀表达式转后缀表达式
    stack = []
    suffix = []  # 后缀表达式
    priority = {'(': 0, ')': 0,
                '+': 1, '-': 1,
                '×': 2, '÷': 2}
    for i in range(len(infix)):
        char = infix[i]
        if char in priority.keys():
            if stack:
                if char not in ['(', ')']:
                    while stack and (priority[char] <= priority[stack[-1]]) and (stack[-1] not in ['(', ')']):
                        temp = stack.pop()
                        if temp not in ['(', ')']:
                            suffix.append(temp)
                    stack.append(char)
                elif char == ')':
                    while stack[-1] != '(':
                        temp = stack.pop()
                        suffix.append(temp)
                    stack.pop()
                else:
                    stack.append(char)
            else:
                stack.append(char)
        else:
            suffix.append(char)
    while stack:
        temp = stack.pop()
        suffix.append(temp)
    return suffix


def count_suffix(postfix):
    stack = []
    symbol_lis = ['+', '-', '×', '÷']
    for i in postfix:
        if i in symbol_lis:
            num2 = stack.pop()
            num1 = stack.pop()
            if i == '+':
                res = Number('')
                res.frac = num1.frac + num2.frac
            elif i == '-':
                res = Number('')
                res.frac = num1.frac - num2.frac
                if res.frac < 0:
                    res.isFu = True
                    return res
            elif i == '×':
                res = Number('')
                res.frac = num1.frac * num2.frac
            elif i == '÷':
                res = Number('')
                if num2.frac == 0:
                    res.isFu = True
                    return res
                res.frac = num1.frac / num2.frac
            else:
                raise print("error!")
            stack.append(res)
        else:
            stack.append(i)
    return stack[0]

# str_ = ''
# li = create_lis(10)
# add_bracket(li)
# for val in li:
#     str_ += str(val)
# print(str_)
# suf=get_suffix(li)
# re=count_suffix(suf)
# print(re)
