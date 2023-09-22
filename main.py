from io import TextIOWrapper
import sys
from cnum import create_lis,add_bracket
from count import *

max_value=0
quantity=0
exercise_file:TextIOWrapper
answer_file:TextIOWrapper

def main(argv:list[str]):
    if len(argv)!=5:
        print('参数错误!')
        return
    bn=manage(argv[1],argv[2])
    bq=manage(argv[3],argv[4])
    if bn or bq:#生成题目
        index=0
        global quantity
        global max_value
        exer=open('Exercises.txt','w',encoding='utf-8')
        answ=open('Answers.txt','w',encoding='utf-8')
        while index<quantity:
            li=create_lis()
            add_bracket(li)
            reone=get_suffix(li)
            resu=count_suffix(reone)
            if is_rational(resu):
                index+=1
                #写题目
                ti=''
                for val in li:
                    ti+=str(val)
                    ti+=' '
                exer.write(f'{index}. {ti}=\n')
                #写答案
                answ.write(f'{index}. {str(resu)}\n')
        print('生成完毕')
    else:#对答案
        rli,wli=correct()
        with open('Grade.txt','w',encoding='utf-8') as graw:
            graw.write(f'Correct:{len(rli)} {str(rli)}\n')
            graw.write(f'Wrong:{len(wli)} {str(wli)}\n')
        print(f'Correct:{len(rli)} {str(rli)}')
        print(f'Wrong:{len(wli)} {str(wli)}')
#检查是否合理
def is_rational(resu:Number)->bool:
    global max_value
    first=resu.isFu==False
    second=is_max(resu,Number(str(max_value)))==False
    third=(resu.up<=max_value and resu.down<=max_value)
    return first and second and third
def correct()->(list[int],list[int]):
    pro=''
    ans=''
    index=1
    right:list[int]=[]#正确的题目
    wrong:list[int]=[]#错误的题目
    global exercise_file
    global answer_file
    while True:
        pro=exercise_file.readline()
        ans=answer_file.readline()
        if pro=='' or ans=='':
            if pro!=ans:
                print('文件行数不匹配，可能没有按照规范书写答案')
                return right,wrong
            else:
                return right,wrong
        pro.replace(' ','')
        pro.strip()
        ans.strip()
        rtmp=str.split(pro,'=')
        atmp=str.split(ans,' ')
        if rtmp[len(rtmp)-1].strip()==atmp[len(atmp)-1].strip():
            right.append(index)
        else:
            wrong.append(index)
        index+=1
                

def manage(option:str,action:str)->bool:
    if option=='-n':
        try:
            global quantity
            quantity=int(action)
            if quantity<=0:
                print('生成数量不能小于1')
                sys.exit(0)
        except ValueError:
            print('参数应为整数')
            sys.exit(0)
    elif option=='-r':
        try:
            global max_value
            max_value=int(action)
        except ValueError:
            print('参数应为整数')
            sys.exit(0)
    elif option=='-e':
        try:
            global exercise_file
            exercise_file=open(action,'r')
        except FileNotFoundError:
            print('题目文件找不到')
            sys.exit(0)
    elif option=='-a':
        try:
            global answer_file
            answer_file=open(action,'r')
        except:
            print('答案文件不存在')
            sys.exit(0)
    else:
        print('参数错误')
        sys.exit(0)
    return option=='-n'
    

if __name__ == '__main__':
    main(sys.argv)
