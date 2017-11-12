# -*- coding: utf-8 -*-
print("""Какой ОС Вы пользуетесь?
1 - Windows 8
2 - Windows 7
3 - Windows Vista
4 - Windows XP
5 - Другая
""")
os = input("Введите число, соответствующее ответу: ")
if os == "1":
    print("Windows 8")
elif os == "2":
    print("Windows 7")
elif os == "3":
    print("Windows Vista")
elif os == "4":
    print("Windows XP")
elif os == "5":
    print("Другая ОС")
elif not os:
    print("Вы не ввели число")
else:
    print("ОС не определена")
input()
