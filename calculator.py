def cal():
    c = None
    while True:
        if c is None:
            a = int(input("enter first number:"))
            b = int(input("enter second number:"))
        else:
            a = c
            b = int(input("enter second number:"))

        co = input("select the operator:")
        if co == "+":
            c = a + b
            print('sum of the numbers:', c)
        elif co == "-":
            c = a - b
            print('sub of the numbers:', c)
        elif co == "*":
            c = a * b
            print('mul of the numbers:', c)
        elif co == "/":
            c = a / b
            print('dev of the numbers:', c)
        elif co == "%":
            c = (a / b)*100
            print('percentage of the numbers:', c)
        elif co == "d" or co=="D":
            c = (a / 100)*b
            if b>a:
                print("error")
            else:
                print('applicable discount',c)
                
        d = input("do you wnat to contunuee:")
        if d == 'no':
            print('your final output is :', c)
            break


cal()
