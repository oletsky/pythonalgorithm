import math
mas=[2,7,15,35,67,109]
n=len(mas)
inp=input("Enter number: ")
c=int(inp)
found=False
low=0
high=n-1
while(low<=high):
    ind=int(math.floor(low+high)/2)
    if mas[ind]==c:
        found=True
        break
    else:
        if c>mas[ind]:
            low=ind+1
        else:
            high=ind-1

if found:
    print('Position: ',ind)
else:
    print('Not found')
