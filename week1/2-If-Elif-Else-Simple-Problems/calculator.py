a = input ("Enter a: ")
b = input ("Enter b: ")
a = int(a)
b = int(b)
oper = input ("Enter operation: ")
print ("Result is: ")
if oper=="+":
    c = a+b
    print (c)
elif oper=="-":
    c = a-b
    print (c)
elif oper=="*":
    c = a*b
    print (c)
elif oper =="/":
    c = a/b
    print (c)
else:
    print ("We do not support that operation.")
