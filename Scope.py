#Scope  >the scope defines the accessibility of the python object..

#ex>1  (one scope ex)
c=2+3
print(c)

#ex>2   (Error-same function use same scope,its 2 defferent scope than its error)
def f1():
    c=2+3
print(c)


#ex>3   (two scope)
def f1():
    c=2+3
    print(c)
f1()