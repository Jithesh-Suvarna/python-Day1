'''A command-line calculator that supports:

Addition
Subtraction
Multiplication
Division
Modulus
Power
Square Root
Percentage'''

'''🛠 Tech Stack
Python
Git
GitHub'''

'''Learn
Variables
Input/Output
Functions
if-else
Loops
Exception Handling'''

# Calculator
import math

print("Calculator is active\n")
print('''1.Addition\n
2.Subtraction\n
3.Multiplication\n
4.Division\n
5.Modulus\n
6.Power\n
7.Square Root\n
8.Percentage''')



print("Please enter your choice\n")
choice=int(input())

print("please enter the number of digits you want to perform operations on: \n")
n=int(input())

a=[]

for i in range(n):
    print("please enter digit",i+1)
    digit=int(input())
    a.append(digit)

print(a)

for i in a:        #just added for break, no need of this line, you can remove it
    if(choice==1):
        print("Addition of all numbers is: ",sum(a))
        break
    elif(choice==2):
        result=a[0]
        for i in range(1,n):
            result=result-a[i]
        print("Subtraction of all numbers is: ",result)
        break
    
    elif(choice==3):
        result1=a[0]
        for i in range(1,n):
            result1=result1*a[i]
        print("Multiplication of all number is: ",result1)
        break

    elif(choice==4):
        
        div=a[0]
        for i in range(1,n):
            if a[i]==0:

                print("Division by zero is not allowed")
                continue
            div=div/a[i]
        print("Division of all number is: ",div)
        break

    elif(choice==5):
        mod=a[0]
        for i in range(1,n):
            mod=mod%a[i]
        print("Modules of all number is: ",mod)
        break

    elif(choice==6):
        power=[]
        for i in a:
            power1=pow(i,2)
            power.append(power1)
        print("Power of all numbers is: ",power)
        break

    elif(choice==7):
        square=[]
        for i in a:
            root=math.sqrt(i)
            square.append(root)
        print("Squareroot of numbers are: ",square)
        break

    elif(choice==8):
        per=(sum(a)/(n*100))*100
        print("Percentage of all numbers are: ",per)
        break

    else:
        print("invalid choice")
        

