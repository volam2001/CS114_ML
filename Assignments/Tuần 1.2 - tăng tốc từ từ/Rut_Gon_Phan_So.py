from fractions import *
n = int(input())
for i in range(n):
    k, t = [int(x) for x in input().split()]
    f = Fraction(k,t)
    if f.denominator != 1:
        print(f.numerator,f.denominator)
    else:
        print(f.numerator)
