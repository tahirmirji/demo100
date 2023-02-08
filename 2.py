def getdata(m1,m2,m3):
    print("Enter your details\n")
    name = input(m1) # string
    age = int(input(m2))  # integer
    salary = float(input(m3)) # float    
    display(name,age,salary)

def display(name,age,salary):
    print("Hello ",name," as your age is ",age," and your salary is ",salary," so we offer you the loan.")


def config():
    msg1=input("Enter msg1 ")
    msg2=input("Enter msg2 ")
    msg3=input("Enter msg3 ")
    getdata(msg1,msg2,msg3)


config()
