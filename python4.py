"""
#
# Part: Python ConditionS
#
"""
a = 200
b = 500
if a < b:
    print("a<b is True")
elif a > b:
    print("a>b is True")
else:
    print("Nothing")

if a > b: print("a > b is True")

print("A") if a < b else print("B")

a = 200
b = 50
c = 500
if (a > b) and (c > a):
    print("Both is True")
if a > b or a > c:
    print("Some cond is True")
if not (a > b):
    print("False")
if a > b:
    pass

x = 23
if x > 10:
    print("Let's go")
    if x > 20:
        print("x > 20 is True")
        if x > 20:
                print("x > 20 is True")
                if x > 20:
                    print("x > 20 is True")
                    if x > 20:
                        print("x > 20 is True")