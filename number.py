from sys import exit
from fractions import Fraction


class Number:
    # 属性
    frac: Fraction
    isFu: bool = False

    def __init__(self, str_: str) -> None:
        li = str_to_num(str_)
        self.frac = Fraction(
            li[0] * li[2] + li[1],
            li[2]
        )

    def __str__(self) -> str:
        if self.frac <= 1:
            return str(self.frac)
        elif self.frac.numerator % self.frac.denominator == 0:
            return f'{int(self.frac)}'
        else:
            return f'{int(self.frac.numerator / self.frac.denominator)}\'{self.frac.numerator % self.frac.denominator}/{self.frac.denominator}'


def str_to_num(string: str) -> list[int]:
    li = [0, 0, 1]
    if len(string) == 0:
        return li
    try:
        li[0] = int(string)
    except ValueError:
        if '/' not in string:
            print('数据字符串格式错误')
            exit(0)
        elif '\'' in string:
            tmp = str.split(string, '\'')
            try:
                li[0] = int(tmp[0])
            except ValueError:
                print('数据字符串格式错误')
                exit(0)
            tmp = str.split(tmp[1], '/')
            try:
                li[1] = int(tmp[0])
                li[2] = int(tmp[1])
            except ValueError:
                print('数据字符串格式错误')
                exit(0)
        else:
            tmp = str.split(string, '/')
            try:
                li[1] = int(tmp[0])
                li[2] = int(tmp[1])
            except ValueError:
                print('数据字符串格式错误')
                exit(0)
    return li
