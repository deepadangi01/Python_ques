n=int(input("enter terms of fabbnocii se.."))
n1=0
n2=1
print(n1,n2,end=" ")
#n is no of numbers
# for i in range(n-2):
#     n3=n1+n2
#     print(n3,end=" ")
#     n1=n2
#     n2=n3

# n terms of numbers
while n1+n2<=n:
    n3=n1+n2
    print(n3,end=" ")
    n1=n2
    n2=n3

