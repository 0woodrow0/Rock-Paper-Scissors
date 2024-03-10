# -*- coding = utf-8 -*-
# @AUTHOR 随风
# Created on 2024/3/9 at 11:56
# @File  : xxx.py
# @software pycharm

# 第四版  这次简单的添加了 while 循环，对局共三局三局两胜。
import random
i = 0
user_win = 0
computer_win = 0
while i <= 3:
    user_input = input("请选择：0 - 剪刀, 1 - 石头, 2 - 布: ")
    computer_input = random.randint(0, 2)
    user_choice = int(user_input)
    computer_choice = int(computer_input)
    print("计算机的选择为", computer_choice)
    if user_choice == computer_choice:
        print("平局")
        print("当前是第%d局共3局" % (i + 1))
    elif user_choice == 0 and computer_choice == 2 \
        or user_choice == 1 and computer_choice == 0\
        or user_choice == 2 and computer_choice == 1\
            or user_choice == 3 and computer_choice == 2:
        print("您赢了")
        user_win = user_win + 1
        print("当前是第%d局共3局" % (i + 1))
    elif user_choice == 2 and computer_choice == 0 \
        or user_choice == 0 and computer_choice == 1\
        or user_choice == 1 and computer_choice == 2\
            or user_choice == 2 and computer_choice == 3:
        print("您输了")
        computer_win = computer_win + 1
        print("当前是第%d局共3局" % (i+1))
    if user_win == 2 or computer_win == 2:
        break
    i = i + 1
