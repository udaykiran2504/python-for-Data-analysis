def sc():
    fc=0
    fwk=0
    max_fwk=10
    print("="*10,"welcome to uk score calculator","="*10)

    while fwk<max_fwk :
        runs=int(input("enter no of runs to add to the total 0-6:"))
        wk=int(input("enter 1 if wicket is fallen:"))
        if runs in [0,1,2,3,4,5,6]:
            fc+=runs
        if wk==1:
            fwk+=wk
        else:
            fwk=wk
        print(fc,'/',fwk)
        if fwk==10:
            print("*"*5,'team is all out THE FINAL SCOTRE IS:',fc,'/',fwk)
        d=input('s to end innings:')
        if d=="s":
            print('end of innings final score is ',fc,'/',fwk)
            break

sc()