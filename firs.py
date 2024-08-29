l1=["ajay","aman","akash","sonam","radha"]
li2=["bhopal","ujjain","bhopal","ratlam","agra"]
st_marks=[45,56,35,23,56,12]
m=max(st_marks)
c=st_marks.count(m)
idx=-1
for i in range(c):
    idx=st_marks.index(m,idx+1)
    print("student name=",l1[idx])
    print("studen address=",li2[idx])
    print("studen marks=",st_marks[idx])