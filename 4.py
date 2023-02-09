
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

def getdata():
    print("Enter your details\n")
    list1=[]
    for var in range(3):
        name = input("Enter your name: ") # string
        age = int(input("Enter your age: "))  # integer
        salary = float(input("Enter your salary: ")) # float
        list1.append([name,age,salary])
    print(list1)
    display(list1)
def display(LIST1):
    for i in range(3):
        print("Hello ",LIST1[i][0]," as your age is ",LIST1[i][1]," and your salary is ",LIST1[i][2]," so we offer you the loan.")
getdata()



# list1=[]
# list1.append(10)
# print(list1)