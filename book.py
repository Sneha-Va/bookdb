while True:
    print("select an option from the menu")
    print('1 add student')
    print('2 view all students')
    print('3 search a student')
    print('4 update the student')
    print('5 delete a student')
    print('6 exit')
    
    choice=int(input('enter the option:'))
    if(choice==1):
        print('student enter selected')
    if(choice==2):
        print("view employee")
        
    elif(choice==3):
        print('search a employee')
    elif(choice==4):
        print('update the employee')
        
    elif(choice==5):
        print('delete the employee')
    elif(choice==6):
        print("exit")
        break