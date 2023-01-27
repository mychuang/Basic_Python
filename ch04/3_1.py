"""
if (條件式):
    程式區塊 1
else:
    程式區塊 2

三元運算子: 

條件式為true時執行的陳述句 if (條件式) else 條件式為false時執行的陳述句
"""

a = 50;

#if(a%2 == 0):
#  print("a is even")
#else:
#  print("a is odd")

print("a is even") if (a%2 == 0) else print("a is odd")

#

rain = input("It's a rainny day ? (Y/N): ");

#if(rain == 'Y'):
#  print("You should take umbrella ");   
#else:
#  print("You don't need to take umbrella ");

print("You should take umbrella ") if (rain == 'Y') else print("You don't need to take umbrella ")