#Set data type methods

a={1,2,3}
b={3,4,5,6}

#print(a.union(b))     #.union =a or b under single list show

#print(a.intersection(b)) #.interselection is a or b same valu is print

"""
ex>.difference(a-b), (b-a)

print(a.difference(b))

>common element is out,then last valu(b) element not show...


ex1>.issubclass
print(a.issubset(b)) #

#(a belong/match to b)
a={1,2,3}
b={1,2,3,4,5}
>is true/match
"""
print(a.isdisjoint(b))
#when a&b value is common..its faulse
#when a&b value is not common..its  True
