# dict1={
#     123:["ajay",7899564231],
#     456:["vijay",589644444],
#     789:["sagar",526874364]
# }
# dict1[789][1]=9932489545
# print(dict1)
# dict1[564]=["deepa",45632158]
# print(dict1)
# dict1.update({123:["xyz",20036589]})
# print(dict1)
# dict1[456].pop()
# print(dict1)

r={}
n=int(input("how many record you want to ??"))
for i in range(n):
    addhar=int(input("enter your adhar no "))
    name=input("enter your name ")
    mob=input("enter your mobile no ")
    add=input("enter ")
    d={"name":name,"mobile":mob}
    r[addhar]=d
print(r)

r=['address','bhopal']
print(r)



