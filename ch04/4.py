"""
if - elif - else 結構

  if condition 1:
    #<若 condition 1 為真, 則執行此區塊>
  elif condition 2:
    #<若 condition 2 為真, 則執行此區塊>
  ...
  else:
    #<若條件都不成立, 執行程式區塊N, 則執行此區塊>

"""

a = 50

if(a > 0):
  print("a is positive ")
elif (a == 0):
  print("a is zero ")
else:
  print("a is negative ")


"""
請依據使用者書熱的成績, 判定成績等第
90以上: A
80 - 89: B
70 - 78: C
60 - 69: D
未滿60: E
"""

score = int(input("Input the score: "))

if(score >= 90):
  print("A ")   
elif(score >= 80 and score < 90):
  print("B ")
elif (score >= 70 and score < 80):
  print("C ")
elif (score >= 60 and score < 70):
  print("D ")
else:
  print("E ")



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