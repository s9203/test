from decimal import Decimal
from fractions import Fraction
import math
import random

# округление
print('Decimal')
decinumber = Decimal('0.2') - Decimal('12.123')
print(decinumber)

# поддержка дробей
print('Fraction')
fractionnumber = Fraction(1, 2)
print(fractionnumber + Fraction(2, 1) * Fraction(2, 3))

# преобразование числа из системы счисления
print(int("0xa", 16))

# float infinity
print(float('nan'))

# binary (2)
print(bin(255))

# oct (8)
print(oct(382746))

# hex (16)
print(hex(31234353))

# round
print('round %d' % round(2.6345, 2))

# abs
print('abs number %d' % abs(-987))

print('MATH SECTION\n')

# pi (number pi)
print('pi = %f' % math.pi)

# e (const e)
print('e = %f' % math.e)

# radian to degrees
print(math.degrees(math.pi))

# degrees to radians
print(math.radians(180.0))

# exponent (exp)
print('exp(2) = %f' % math.exp(2))

# random
print('random number = %f' % random.random())

# uniform random (pseudo)
print('pseudo random = %f' % random.uniform(1, 10))

# random range
print('random range = %d' % random.randrange(10))

# random from string
print('random from string "apple" = %s' % random.choice('apple'))

# shuffle
shuffle = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 10]
print(random.shuffle(shuffle))
