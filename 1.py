def modiy_list(lst):
    lst= lst + [10,20]
    lst[1]=99

x=[5,15,25]
modiy_list(x)
print(x)

#This will print ony [5,10,25]
#lst += lst +[10,20]
#this will print [5,99,25,10,20]
