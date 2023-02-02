"""
practice: 印出金字塔
    *
   ***
  *****
 *******
*********

pesudo code:

while(var <= 5):
    當var = 1: print(" ") 4次
    當var = 2: print(" ") 3次 
    當var = 3: print(" ") 2次
    ...
    ||
    while(畫*次數 <= 5-var):
        print(" ")
    
    while(畫*次數 <= (var*2-1) ):
        print("*") 
    
    var += 1
"""

N = 5
var = 0
while(var <= N):
    spc = 1
    while(spc <= N-var):
        print(" ", end="")
        spc += 1
    
    plt = 1
    while(plt <= var*2-1):
        print("*", end="")
        plt += 1
    print("")
    var += 1