# Str1="Android Operating System" + " is dedicated for smart phone"
# Str2=  Str1 + " - joined"

# print(Str2)

# a1 = 10; b1 = 20; L1=['A']
# a=[a1,b1,L1,"Python"]
# print(a[2])



List1 = []

n = int(input("Enter the n value: "))

print("Enter the elements: ")
for i in range(n):
    List1.append(int(input()))

for i in range(0,n-2):
    for j in range(1,n):
        if(List1[i] > List1[j]):
            temp = List1[i]         # temp = 10
            List1[i]=List1[j]       # 10=30
            List1[j]=temp           # 30=temp
            print(List1,end=" | ")

            

