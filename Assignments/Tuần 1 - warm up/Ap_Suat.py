from decimal import *

f = float(input())

x = f*0.453592/2.54**2

getcontext().prec = 6

print(Decimal(x).normalize())
