"""
搜尋1000 以內的質數:
Tips: 質數, 只能被自己跟1整除

pesudo code:

while(var < 1000):
    status = True
    if (var 被自己跟1以外的數字 整除):
        var 不是質數
        status = False
        
    if(status == True):
        var 是質數
    
    var = var + 1
"""

var = 2
while(var <= 1000):
    status = True
    count = 2
    while(count < var):
        if(var % count == 0):
            status = False
            break
        count += 1
    
    if(status == True):
        print("{:d} is 質數".format(var))
    var +=1