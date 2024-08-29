# wap to create following list at runtime and placeed them all in single list.(list of list)
# 
# list of list
re=int(input("how many record ???"))
st_details=[[],[],[]]
for i in range(re):
    nm=input("enter name :")
    s_ad=input("enter address :")
    m=int(input("enter your marks :"))
    st_details[0].append(nm)
    st_details[1].append(s_ad)
    st_details[3].append(m)
print(st_details)
