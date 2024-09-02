#create a console based projecet employee management system
'''
functionality
1.insert_data()
2.display_data()
3.search_data()
4.search_id()
5.search_gender()
6.filter_record_by_saray()
7.delete_record_id()
8.delete_record_name()
9.modify_record()
10.exit()
'''
#-------insert function------
def insert_data(d):
    n=int(input("how many recond your want to??"))
    for i in range(n):
        eid=int(input("enter id: "))
        enm=input("enter your name: ")
        des=input("enter your designation: ")
        gen=input("enter your gender: ")
        salary=input("enter salary: ")
        d[eid]=[enm,des,gen,salary]
    print(n,"record inserted ")
    return d
#-----------search function------------

def search_data(d):
    name=input("whom do u want to search ,enter her/his name ??")
    if any(d):
        flag=0
        for i,j in d.items():
          if j[0]==name:
              flag+=1
              print("E_id :",i)
              print("E_name :",j[0])
              print("E_designation :",j[1])
              print("E_gender :",j[2])
              print("E_salary :",j[3])  
          if flag==0:
              print("record not found")
          else:
              print(flag,"record found")
    else:
        print("nothing to display")
    return d
#-------------------display function--------------------
              
def display_data(d):
    if any(d):
        for i,j in d.items():
            print("E_id :",i)
            print("E_name :",j[0])
            print("E_designation :",j[1])
            print("E_gender :",j[2])
            print("E_salary :",j[3])
        else:
            print("nothing to display")

#--------------master function---------------
def master(d):
    while True:
        print("-"*30,"EMS" ,"-"*30)
        print("1 for insert data")
        print("2 for display data ")
        print("3 for search data")
        print("10 for exit")
        ch=int(input("enter your choice "))
        if ch == 1:
            d=insert_data(d)
        elif ch == 2:
            d=display_data(d)
        elif ch==3:
            d=search_data(d)
        elif ch==10:
            print("thank you our serve..........")
            break
#------------main function call------------        
d={}
master(d)