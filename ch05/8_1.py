"""
practice: 好多星星2
輸入一個數字N，依照"特殊"規律印出星星們。

input :
1
output :
*

input :
5
output :
*
***
*****
*******
*********

pesudo code:

while(var <= N):

    當var = 1: print("*") 1 = (1*2-1)次
    當var = 2: print("*") 3 = (2*2-1)次 
    當var = 3: print("*") 5 = (3*2-1)次
    ... 
    ||
    while(畫*次數 <= (var*2-1) ):
        print("*") 
    
    var += 1
"""

N = float(input("N = "))
var = 0
while(var <= N):
    plt = 1
    while(plt <= var*2-1):
        print("*", end="")
        plt += 1
    print("")
    var += 1