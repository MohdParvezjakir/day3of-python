#problem1: write a program to fint out whether a student has passed or failed if it required a a total of
#40% and least 33 marks in each subject and take marks as an input from the student
list=()
name=input("enter your name:")
m1=int(input("Enter your marks sub 1:"))
m2=int(input("Enter your marks sub 2:"))
m3=int(input("Enter your marks sub 3:"))
m4=int(input("Enter your marks sub 4:"))
#check total percentage
total_percentage=(100*(m1 + m2 + m3 + m4))/400
if(total_percentage>= 40 and m1>33 and m2>33 and m3>33 and m4>33):
    print(f"comguratulation!{name} you are pass, yor percentage is:",total_percentage)
else:
    print("you are failed, try next year")
