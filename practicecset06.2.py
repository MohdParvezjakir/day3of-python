# A spam comment is defined as a text containing following keywords: 
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program 
# to detect these spams.

comment=input("commenyt:")
p1="make a lot of money"
p2="buy now"
p3="subscribe this"
p4="click this"
if((p1 in comment)or (p2 in comment)or (p3 in comment)or (p4 in comment)):
    print('thyis is a spam comment')
else:
    print("this comment is not spam")



#write a program to find out given usetname by a user is contain 10 character or not
n=input("username:")
if(len(n)>=10):
    print("yes username has 10 or more charracter")
else:
    print("usernamer must have minimum 10 character")
    
# Write a program which finds out whether a given name is present in a list or not. 

list = ["parvez","faijan","kaif","mohan"]
name=input("enter your name:")
if(name in list ):
    print("yes you are selected ")
else:
    print("you are not in the list")




# Write a program to calculate the grade of a student from his marks from the 
# following scheme: 
# 90 – 100 => Ex 
# 80 – 90 => A 
# 70 – 80 => B 
# 60 – 70  =>C 
# 50 – 60 => D 
# <50        ()
# => F 
name=input("Enter your name:")
marks1=int(input("Enter your marks sub1:"))
marks2=int(input("Enter your marks sub2:"))
marks3=int(input("Enter your marks sub3:"))
total_percentage=(100*(marks1 + marks2 + marks3))/300
if(total_percentage<=100 and total_percentage>=90 and marks1>=33 and marks2>=33 and marks3>=33):
    print("congratulation! you are passed, and your percentage is:",total_percentage,"and yiour grade is \"Exellent\"")
elif(total_percentage>=80 and marks1>=33 and  marks2>=33 and marks3>=33):
    print("congratulation! you are passed, and your percentage is:",total_percentage,"and yiour grade is \"A\"")
elif(total_percentage>=70 and marks1>=33 and  marks2>=33 and marks3>=33):
    print("congratulation! you are passed, and your percentage is:",total_percentage,"and yiour grade is \"B\"")
elif(total_percentage>=60 and marks1>=33 and  marks2>=33 and marks3>=33):
    print("congratulation! you are passed, and your percentage is:",total_percentage,"and yiour grade is \"C\"")
elif(total_percentage>=50 and marks1>=33 and  marks2>=33 and marks3>=33):
    print("congratulation! you are passed, and your percentage is:",total_percentage,"and yiour grade is \"D\"")
elif(total_percentage>=40 and marks1>=33 and  marks2>=33 and marks3>=33):
    print("congratulation! you are passed, and your percentage is:",total_percentage,"and yiour grade is \"()\"")
elif(total_percentage<33 and marks1>=33 and  marks2>=33 and marks3>=33):
    print("yuo are  fail! better lu8ck next timne")




