

a={'name':'uday','mname':'kiran','lname':'dasari','id':123}
print(type(a))
b={'name':'ud','mname':'ki','lname':'da','id':124}
print(type(b))
for x in a:
    print(x)
for x,y in a.items():
    print(x,':',y)
c={1:{'loc':'tpt','ploc':'gtl'},2:{'edu':'mca'}}
print(type(c))
print(c[2]['edu'])