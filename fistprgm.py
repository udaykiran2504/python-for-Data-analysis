#this is my first program
print("""this is my first program ever in python 
 in this program i am going to implement 
 1. variables 
 2.operators
 3.user input
 4.type casting
 5.conditional statements""")
print("this program is take and enter details of a student")
name =input("enter name of the student:")
print(type(name))
standard = input("enter standard if the student :")
idcard_no = int(input("enter idcard number:"))

print("enter marks of the students:")
a =int(input("enter tel marks:"))
b =int(input("enter hin marks:"))
c =int(input("enter eng marks:"))
d =int(input("enter maths marks"))
e =int(input("enter sci marks: "))
f =int(input("enter soc marks :"))

g = a+b+c+d+e+f
print("name of the student :",name)
print("class pf the student : ",standard)
print("id card no of the student :",idcard_no)
print("total marks of the student :",g)

if g<=40:
    print("student has scored grade F")
elif g>40 and g<99:
    print("student has scored grade c")
elif g>=100 and g<120:
    print("student has scored grade B")
elif g>=121 and g<139:
    print("student scored A")
elif g >= 140 and g<=150:
    print("student has scored grade A+")

else:
    print("invalid details has been entered")




