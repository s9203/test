# -*- coding: utf-8 -*-
import random


def password_generator(count_char=8):
    arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
           'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8',
           '9', '0']
    passw = []
    for i in range(count_char):
        passw.append(random.choice(arr))
    return "".join(passw)


print(password_generator(12))
