#Short Circuiting

"""
#ex>1
if (True or 5/0):     #True 5/0  is statement...result>"hello"
    print("hello")
else:
    print("welcome")    

#ex>2    
if (True and 5/0):     #resutl> error..cz "and" operator logick
    print("hello")
else:
    print("welcome")   
    
""" 
#ex>3   
if (False and 5/0):     #resutl> welcome
    print("hello")
else:
    print("welcome")     