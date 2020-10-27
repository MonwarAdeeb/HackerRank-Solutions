# Enter your code here. Read input from STDIN. Print output to STDOUT
def getkey(x):
    if x.islower():
        return(1,x)
    elif x.isupper():
        return(2,x)
    elif x.isdigit():
        if int(x)%2==1:
            return(3,x)
        else:
            return(4,x)

print(*sorted(input(), key=getkey), sep='')