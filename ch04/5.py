"""
- 巢狀結構:
  if condition a1:
    #<若 condition a1 為真, 則執行此區塊>
    if condition b:
      #<若 condition b 為真, 則執行此區塊>
    else:
      #<若 condition b 為假, 則執行此區塊>
    
  elif condition a2:
    #<若 condition a2 為真, 則執行此區塊>
    if condition c:
      #<若 condition c 為真, 則執行此區塊>
    else:
      #<若 condition c 為假, 則執行此區塊>
      
  else:
    #<若 a1 & a2 皆為假, 則執行此區塊>
"""

"""
請寫出一個程式, 讓使用者輸入西元年分,
判斷該年是否為閏年
判斷方式: 四年一閏, 逢百不閏, 逢四百又閏 
ex: 
    輸入 2000 : 顯示 Leap Year
    輸入 2100 : 顯示 Not leap Year
"""

year = int(input("Input year: "))

if(year % 4 == 0):
    if(year % 100 == 0):
        if(year % 400 == 0):
            print("Leap Year ")
        else:
            print("Not leap Year ")
    else:
        print("Not leap Year ")
else:
    print("Not leap Year ");