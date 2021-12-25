n = 5
list1 = ["A","B","C","D","E"]
list2 = [1,2,3,4,5]
#pattern-1
for i in range(0, n):
    for j in range(0, i+1):
         print("* ",end="")
    print("\r")
#pattern-2
for i in range(0,len(list2)):
    for j in range(0,5-i):
        print(list2[j],end="")
    print("")
#pattern-3
for i in range(0, len(list1)):
    for j in range(0, i+1):
         print(list1[j],end="")
    print("\r")