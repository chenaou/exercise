from main import *


def test_demo1():
    # 参数输入不完全
    main(['demo1', '-n', '10'])


def test_demo2():
    # 少量生成测试
    main(['demo2', '-n', '10', '-r', '10'])


def test_demo3():
    # 少量生成交换参数测试
    main(['demo3', '-r', '10', '-n', '10'])


def test_demo4():
    # 大量生成测试
    main(['demo4', '-r', '1000', '-n', '1000'])


def test_demo5():
    # 错误数量测试
    main(['demo5', '-n', '-1', '-r', '10'])


def test_demo6():
    # 普通的答案校对
    main(['demo6', '-e', 'Exercises.txt', '-a', 'Answers.txt'])


def test_demo7():
    # 校对参数换位置
    main(['demo7', '-a', 'Answers.txt', '-e', 'Exercises.txt'])


def test_demo8():
    # 问题文件不正确
    main(['demo8', '-e', 'Answers.txt', '-a', 'Answers.txt'])


def test_demo9():
    # 答案文件不正确
    main(['demo9', '-e', 'Exercises.txt', '-a', 'Exercises.txt'])


def test_demo10():
    # 文件路径不正确
    main(['demo10', '-e', '66.txt', '-a', '111.txt'])


if __name__ == '__main__':
    test_demo2()
