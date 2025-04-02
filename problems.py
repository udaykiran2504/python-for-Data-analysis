# 1st problem

for i in range(1,6):
    for j in range(1,i+1):
    #we can replace j with * or i to get different outputs
        print(j, end="  ")
    print( )


  # problem 2
print("this is problem 2")
for i in range(1, 6):
    for j in range(6, i,-1):
        print(j, end="  ")
    print()

# problem 3 reverse triangle
print("this is problem 3")
for i in range(1,6):
    for j in range(5,i,-1):
        print(" ", end=" ")
    for k in range(i):
        print("*", end=" ")

    print( )

    # problem 4 reverse triangle
print("this is problem 4")
for i in range(1,6):
    for j in range(1,i+1):
    #we can replace j with * or i to get different outputs
        print("*", end="  ")
    print( )

for i in range(5,0,-1):
    for k in range(0,i-1):
        print("*", end="  ")
    print( )

 
 # problem 6 reverse triangle
for u in range(1,11):
     for k in range(1,u+1):
         print(u*k, end=" ")
     print( )