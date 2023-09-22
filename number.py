import sys

class Number:
    #属性
    left:int=0
    up:int=0
    down:int=1
    isFu:bool=False
    def __init__(self,string:str) -> None:
        li=str_to_num(string=string)
        self.left=li[0]
        self.up=li[1]
        self.down=li[2]
        pass
    def __str__(self) -> str:
        #假分数转真分数
        if self.up>self.down:
            self.left=int(self.up/self.down)
            self.up=self.up%self.down
        #约分
        approx(self)
        if self.isFu==True:
            return '-xx'
        if self.up==0:
            return f'{self.left}'
        if self.left==0:
            return f'{self.up}/{self.down}'
        return f'{self.left}\'{self.up}/{self.down}'
    #化为假分数，用于简化计算
    def to_fake(self)->None:
        self.up+=(self.left*self.down)
        self.left=0
    
def plus(number1:Number,number2:Number) -> Number:#加法运算
    result=Number('')
    number1.to_fake()
    number2.to_fake()
    #通分
    general_points(number1,number2)

    #计算
    result.up=number1.up+number2.up
    result.down=number1.down
    
    #假分数转真分数
    if result.up>result.down:
        result.left=int(result.up/result.down)
        result.up=result.up%result.down
    #约分
    approx(result)
    return result

def approx(number:Number)->None:#约分
    a,b=get_factor(number.up,number.down)
    number.up=int(number.up/a)
    number.down=int(number.down/a)
    if number.down!=0 and number.down==number.up:
        number.left+=1
        number.up=0
        number.down=1
    return

def general_points(number1:Number,number2:Number)->None:#通分
    number1.to_fake()
    number2.to_fake()
    a,b=get_factor(number1.down,number2.down)
    c1=int(b/number1.down)
    c2=int(b/number2.down)
    number1.up*=c1
    number2.up*=c2
    number1.down=number2.down=b

def get_factor(a:int,b:int) -> (int,int):#获取f最大公约数和最小公倍数
    Min = min(a,b)
    max_f = 1
    for i in range(1,int(Min+1)):
        if a%i == 0 and b%i == 0:
            max_f = i
    min_b = a*b / max_f
    return  int(max_f),int(min_b) #max_f最大公约数，min_b最小公倍数

def minus(number1:Number,number2:Number)->Number: #减法
    if is_max(number1,number2)==False and is_equals(number1,number2)==False:
        result=Number('')
        result.isFu=True
        return result
    #通分
    general_points(number1,number2)
    result=Number('')
    result.up=number1.up-number2.up
    result.down=number1.down
    #假分数转真分数
    if result.up>result.down:
        result.left=int(result.up/result.down)
        result.up=result.up%result.down
    #约分
    approx(result)
    return result

def multiply(number1:Number,number2:Number)->Number:#乘法
    
    general_points(number1,number2)#通分
    result=Number('')
    result.up=number1.up*number2.up
    result.down=number1.down*number2.down
    #假分数转真分数
    if result.up>result.down:
        result.left=int(result.up/result.down)
        result.up=result.up%result.down
    #约分
    approx(result)
    return result
def divide(number1:Number,number2:Number)->Number:#除法
    general_points(number1,number2)#通分
    result=Number('')
    result.up=number1.up*number2.down
    result.down=number1.down*number2.up
    #假分数转真分数
    if result.up>result.down:
        result.left=int(result.up/result.down)
        result.up=result.up%result.down
    #约分
    approx(result)
    return result

    

def is_max(number1:Number,number2:Number)->bool:#左边数字是否大于右边
    #化为假分数
    number1.to_fake()
    number2.to_fake()
    #通分
    general_points(number1,number2)
    return number1.up>number2.up

def is_equals(number1:Number,number2:Number)->bool:
    #化为假分数
    number1.to_fake()
    number2.to_fake()
    #通分
    general_points(number1,number2)
    return number1.up==number2.up

def str_to_num(string:str) -> list[int]:
    li=[0,0,1]
    if len(string)==0:
        return li
    try:
        li[0]=int(string)
    except ValueError:
        if '/' not in string:
            print('数据字符串格式错误')
            sys.exit(0)
        elif '\'' in string:
            tmp=str.split(string,'\'')
            try:
                li[0]=int(tmp[0])
            except ValueError:
                print('数据字符串格式错误')
                sys.exit(0)
            tmp=str.split(tmp[1],'/')
            try:
                li[1]=int(tmp[0])
                li[2]=int(tmp[1])
            except ValueError:
                print('数据字符串格式错误')
                sys.exit(0)
        else:
            tmp=str.split(string,'/')
            try:
                li[1]=int(tmp[0])
                li[2]=int(tmp[1])
            except ValueError:
                print('数据字符串格式错误')
                sys.exit(0)
    return li
