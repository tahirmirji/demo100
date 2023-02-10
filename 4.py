
# def getdata():
#     count=0
#     while(count<3):
#         count=count+1
#         name = input("\n Enter the details of Employee \nEnter your name:") 
#         age = int(input("Enter your age:"))  
#         salary = float(input("Enter your salary:  ")) 
#     display(name,age,salary)
# def display(name,age,salary):
#         print("name",name,"age",age,"salary",salary)
# getdata()
list1=[]
def getdata():
    print("Enter your details\n")
    for var in range(1):
        name = input("Enter your name: ") # string
        list1.append(name)
        
        age = int(input("Enter your age: "))  # integer
        list1.append(age)
        
        salary = float(input("Enter your salary: ")) # float
        list1.append(salary)

def display():
    if(len(list1)>0):
        for i in list1:
            print(i)
    else:
        print('No elements in list')
        
        
def removeelements():
   
    if(len(list1)>0):
        display()
        element=input('Type the element to remove:')
        list1.remove(element)
        print('Removed ',element,' successfully\n')
    else:
        print('No elements in list to remove')
        
    
while(1):
    print('Choose your option:\n1.Insert\n2.Remove\n3.Display\n4.Exit\n')
    choice=int(input('Choose an option: '))
    if(choice==1):
        getdata()
    if(choice==2):
        removeelements()
    if(choice==3):
        display()
    if(choice==4):
        choice=input('Are you sure you want to exit?\n 1. Yes \n 2. No\n ')
        if(choice==1):
            break
            



