# 2. have parameters no return

'''
def func_naeme(param1, param2, ....) :
    คำสั่ง 1
    คำสั่ง 2
    ....
'''

def showHi(your_name) :
    print('..................')
    print(f'สวัสดี {your_name} !') 
    print('....................')

def sumnum(n1, n2) :
    print('..................')
    print(f'ผลบวกของ {n1} และ {n2} คือ {n1 + n2}')
    print('....................')

showHi('สมชาย') #ข้อมูลที่ส่งให้ parameter เรียก argument
showHi('สมศรี')
sumnum(10, 20)
showHi('Sobat')