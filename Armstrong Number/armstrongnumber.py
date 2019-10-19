a=int(input("please enter a number"))
sum=0
final=a

while(a!=0):
    n=a%10
    c=(n**3)
    sum+=c
    a=a//10

if final==sum:
    print("the number is an angstrom number")
else:
    print("the number is not an angstrom number")
