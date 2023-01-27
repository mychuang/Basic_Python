#計算園面積
import math # python 內建數學模組

pi = 3.1415926
pi_math = math.acos(-1.0)

radius = int(input("input radius: "))

print("circle area: {0}".format(radius*radius*pi))
print("circle area: {0}".format(radius*radius*pi_math))

