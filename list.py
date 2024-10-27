arrList = [1,2,3,4,5,6]

print("1.Length of List:",len(arrList))
print("\n2.Type of List:",type(arrList))

print("\n3.Second last element of List is", arrList[-2])

print("\n4.Using list slising, The list from 3rd to 5th element is", arrList[2:5])

x = int(input("\n5.Enter Element to be searched: "))
if x in arrList:
    print("Element",x,"found in List")
else: 
    print(x,"does not exist")
    
revArrList = arrList
revArrList.reverse()
print("\n5.Reverse of list is",revArrList)

arrList2 = arrList+[4,5,7,3,5]
print("\n6.New list after concat:",arrList2)

sum = 0
for i in arrList:
    sum +=i
print("\n7.Average of all the numbers in List:",(sum/len(arrList)))

arrList.reverse()
for i in range(len(arrList)):
    arrList[i] = arrList[i]**2
print("\n8.Square of all the numbers in List:",(arrList))

arrList = [1,2,3,4,5,6]

max=0
min=1000
for i in range(len(arrList)):
    if arrList[i]>=max:
        max = arrList[i]
    if arrList[i]<=min:
        min = arrList[i]
print("\n9.Maximum and minimun numbers in List:",max,"and", min)

arrList = [1,2,3,4,5,6,7,4,5,3]
x = int(input("\nEnter Element to be searched: "))
occurence=0
for i in range(len(arrList)):
    if arrList[i]==x:
        occurence +=1
        break
arrList.pop(i)
print("\n10:removal of",x,"in List is", arrList)

print("\n11:\n")
for x in range(1,20):
    if (x%2 == 0):
        print(x)