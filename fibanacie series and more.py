a=0
b=1
n=int(input("enter the up to number :"))
if n==1:
    print(1)
else :
    print(a)
    print(b)
    for i in range(2, n):
        c = a + b
        a = b
        b = c
        print(c)

