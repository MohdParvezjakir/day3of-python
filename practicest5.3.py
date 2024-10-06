# Create an empty dictionary. Allow 4 friends to enter their favorite language as 
# value and use key as their names. Assume that the names are unique.

dics ={}
f1=input("\"enter yourname\": ")
l1=input("enter your fav programing language")
dics.update({f1: l1})
f2=input("\"enter yourname\": ")
l2=input("enter your fav programing language")
dics.update({f2:l1})
f3=input("\"enter yourname\": ")
l3=input("enter your fav programing language")
dics.update({f3:l3})
f4=input("\"enter yourname\": ")
l4=input("enter your fav programing language")
dics.update({f4:l4})
print(dics)
name=input("enter your name (to see your fav lang.): ")
print(f"your fav programing language is : {dics[name]}")

 
#if the name of two friends aresame; what will happen in this program
#the value entered later will be updated
#if the lang of two friends are same, what will happen
#the value will same

#can we chjange the value into  a list in a set
# set3 = {1,2,2.3,5,"parvez",["list",6]}
# set3[-1]= 6
#gives a error