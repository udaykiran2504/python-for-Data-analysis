#sum of even numbers

sum=0
for i in range(1,51):
    if i % 2 == 0:
     sum +=i
print(sum)


#to write a first 20 numbers and there squares
for a in range (0,21):
    print(a,a**2)


#sum of first 10 odd numbers
for o in range(0,20):
    if o%3==0:
        sum +=o

print("sum of odd numbers ",sum)

#method 2 using while loop

sum=0
w=0
while w<=20:
    if w%2!=0:
        sum +=w
    w +=1
print("mehod 2 :",sum)


#to check numbers divisible by both 8 and 12 in range 1 to 100

for d in range(0,100):
     if d%8==0 and d%12==0 :
       print(d)



# bill printing mechanisam using nested loops

while True:
    name = input("enter the name: ")
    total=0

    while True:
        print('enter amount and quantity')
        amount =float(input("enter amount: "))
        quantity=float(input('enter quantity: '))
        total +=amount*quantity
        print(total)
        repeat=input('click yes/no to continuee :' )

        if repeat=="no" or repeat=="No":
            break
    print("_" * 40)
    print("name of the cus :",name)
    print("_" * 40)
    print("amount ro be paid is :", total)
    print("_" * 40)
    print("thank you for shopping")
    print("_" * 40)
    repeat1 = input('do u want to go to another customer yes/no')
    if repeat1 == "no" or repeat1 == "No":
        break




