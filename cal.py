#choosing an operation
print("Choose an arithmetic operation")
print("1. Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Modulo operation")


x=int(input("OPTION-1/2/3/4/5:"))
lst=[1,2,3,4,5]
#if x==1 or 2 or 3 or 4 or 5:
if x in lst:
    a=float(input("Enter one number:"))
    b=float(input("Enter another number:"))
else:
    print("Invalid input. Please enter a valid option")
              
        
match x:
    case x if x==1:
        print("Addition of",a,"and",b,"is",a+b)
    case x if x==2:
        print("Subtraction of",a,"and",b,"is",a-b)
    case x if x==3:
        print("Multiplication of",a,"and",b,"is",a*b)
    case x if x==4:
        print("Division of",a,"and",b,"is",a/b)
    case x if x==5:
        print("Modulo operation of",a,"and",b,"is",a%b)
