#List Slicing & Mutability concept....

#"apple","banana","car","bus"     (list valu)
#   0       1       2     3        (index no.)

"""
#ex>list index no ways show

li=["apple","banana","car","bus"]
print(li[1:3])

.........
#ex> relaces list value

li=["apple","banana","car","bus"]
li[2]="airplan"
print(li)

"""

li=["apple","banana","car","bus"]
li1=li
li2=li[0:4]
li[2]="airplan"
print(li,li1,li2)

#li/li1>poient "li"   ,, li2 >new list create/slicing.....memory allocation