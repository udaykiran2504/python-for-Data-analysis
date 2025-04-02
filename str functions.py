a="uday"
b="uday123"
c="uday 123"
d="uday@123"
e="123"
f="1.21"


print(a.isalnum())
print(b.isalnum())
print(c.isalnum())
print(d.isalnum())

print(a.isalpha())
print(b.isalpha())
print(c.isalpha())
print(f.isalpha())

print(a.isdecimal())
print(e.isdecimal())
print(f.isdecimal())#it is coounting . as a sign


print(b.isdigit())
print(b.isnumeric())
print(a.isupper())
print(a.islower())
print(a.istitle())
print(c.isspace())

h="uday kiran"
print(h.endswith("n"))
print(h.endswith("r",5,8)) #we can also provide range to check

print(h.startswith("u"))
print(h.swapcase())
print(h.strip())
i=" i. am. uday. kiran."
print(i.split("."))
j=h.ljust(20,"*")
print(j)
k=h.rjust(20,"*")
print(k)
print(h.replace("uday","ganesh"))



