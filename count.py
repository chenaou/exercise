from cnum import *
from number import *
def get_suffix(infix):
    # 中缀表达式转后缀表达式
    stack = []
    suffix = [] # 后缀表达式
    priority = {'(': 0, ')': 0,
                '+': 1, '-': 1,
                '×': 2, '÷': 2}
    for i in range(len(infix)):
        char = infix[i]
        if char in priority.keys():
            if stack:
                if char not in ['(', ')']:  
                    while stack and (priority[char] <= priority[stack[-1]]) and ((stack[-1] not in ['(', ')'])) :     
                        temp = stack.pop()
                        if temp not in ['(', ')']:
                            suffix.append(temp)
                    stack.append(char)
                elif  char == ')':
                    while stack[-1] !='(':
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
                res = plus(num1,num2)
            elif i == '-':
                res = minus(num1,num2)
                if res.isFu==True:
                    return res
            elif i == '×':
                res = multiply(num1,num2)
            elif i == '÷':
                if is_equals(num2,Number('0')):
                    res=Number('0')
                    res.isFu=True
                    return res
                res = divide(num1,num2)
            else:
                raise print("error!")
            stack.append(res)
        else:
            stack.append(i)
    return stack[0]

