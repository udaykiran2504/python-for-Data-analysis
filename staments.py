
g = a+b+c+d+e+f

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