# Str1="Android Operating System" + " is dedicated for smart phone"
# Str2=  Str1 + " - joined"

# print(Str2)

# a1 = 10; b1 = 20; L1=['A']
# a=[a1,b1,L1,"Python"]
# print(a[2])


list1 = []

n = int(input("Enter the n value: "))

print("Enter the elements: ")
for i in range(n):
    list1.append(int(input()))
n=len(list1)


for i in range(n-1,0,-1):
    for j in range(i):
        if(list1[j] > list1[j+1]):
            temp = list1[j]         # temp = 10
            list1[j]=list1[j+1]       # 10=30
            list1[j+1]=temp           # 30=temp
    print(list1)
print(list1)


