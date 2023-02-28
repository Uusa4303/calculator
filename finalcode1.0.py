while True:
    
    num1=float(input('enter  first number: \n'))
    num2=float(input('enter second number: \n'))
    print("1.addition 2.subtraction 3.multiplication 4.division")
    opt =float(input("enter the operation (number) you want to do \n"))
    if opt ==1:
        print(num1+num2)
    elif opt==2:
        print(num1-num2)
    elif opt==3:
        print(num1*num2)
    elif opt==4:
        print(num1/num2)
        
    
    else:
        print('Please enter a valuable operation.')
    
    break