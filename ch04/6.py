"""
電費計算
依照用電類別來計費, 規則如下

家庭用電: 
    100度以下, 每度2元
    101-300度, 每度3元
    301度以上, 每度4元
工業用電: 
    每一契約馬力200元
    實際用電每度2元
營業用電:
    0-300度, 每度5元
    301度以上, 每度6元
"""

#家庭用電
TYPEA1 = 2
TYPEA2 = 3
TYPEA3 = 4
#工業用電
TYPEB1 = 200
TYPEB2 = 2
#營業用電
TYPEC1 = 5
TYPEC2 = 6

print("1: household electricity ")
print("2: Industrial electricity ")
print("3: business electricity ")
t = int(input("Enter your electricity type: (1, 2 or 3)"))

if(t >= 1 and t <=3):
    deg = float(input("Enter degree of electricity: "))

    if(t == 1):
    
        if(deg <= 100):
            fee = deg*TYPEA1
        elif(deg > 100 and deg <= 300):
            fee = 100.0*TYPEA1
            fee = fee + (deg-100.0)*TYPEA2
        else:
            fee = 100.0*TYPEA1
            fee = fee + 200.0*TYPEA2
            fee = fee + (deg-300.0)*TYPEA3

    elif(t == 2):
        c = float(input("Enter contract power "))
        fee = c*TYPEB1 + deg*TYPEB2

    elif(t == 3):
        if(deg <= 300):
            fee = deg*TYPEC1
        else:
            fee = 300.0*TYPEC1
            fee = fee + (deg-300.0)*TYPEC2
    else:
        print("???")

    print("total fee: ", fee)
else:
    print("type error ")