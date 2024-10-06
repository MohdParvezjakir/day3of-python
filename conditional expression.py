#if elif and else staements are a multiway decision taken by our program due to a certain condition in our code
#syntax of conditional expression
''' if (condition1):
    print(yes)
elif (condition2):
     print(no)
else:
    print(maybe)
    '''
a = int(input("enter your age:"))
if(a>=18):
    print("welcome")

    print("wait")
else:
    print("sorry")


# write a program to find the greatest number in given user input
num1=int(input("Enter your number1 : "))
num2=int(input("Enter your number2: "))
num3=int(input("Enter your number3: "))
num4=int(input("Enter your number4: "))
if(num1>num2 and num1>num3 and num1>num4):
    print(f"the vgreatest number is :{num1}")
elif(num2>num1 and num2>num3 and num2>num4):
    print(f"the vgreatest number is :{num2}")
elif(num3>num1 and num3>num2 and num3>num4):
    print(f"the vgreatest number is :{num3}")
elif(num4>num1 and num4>num2 and num4>num3):
    print(f"the vgreatest number is :{num4}")
else:
    print("number you given is same")


