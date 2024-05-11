list=[5,6,7,2,1]
list.append(4) #add 4 in last [5,6,7,2,1,4]
list.pop() #removing last value [5,6,7,2]
list.sort() #sorting the elements in order [1,2,5,6,7]
list.sort(reverse=True) #sorting the values in reverse order [7,6,5,2,1]
list.reverse() #reverse a list [1,2,7,6,5]
list.insert(2,10) #inserting a element 10 at index 2 [5,6,10,7,2,1] 
list.remove(1) #removing 1 from the list [5,6,7,2]
list.pop(3)  # the idx value will be remove [5,6,7,1]
print(list)

tup=(5,6,7,2,1)
print(tup[0:])

tup=(1)
print(type(tup)) #type will be int

tup=("hi")
print(type(tup)) #type will be str

tup=(1,3,4,5)
print(tup.index(5))

a=(int(input()))
b=(int(input()))
c=(int(input()))
# d=[a,b,c]
d=[]
d.append(a)
d.append(b)
d.append(c)
print(d)

list1=[1,2,3,2,1]
copy_list1=list1.copy()
copy_list1.reverse()
if(copy_list1==list1):
    print("polyndrome")
else:
    print("no")

info={
    "key" : "value",
    "name":"seenu",
}

print(info["key"])

count=100
while count>=1:
    print(count)
    count-=1

count=1
while count<=100:
    print(count)
    count+=1

count=1
while count<=10:
    table=2 * count
    print("2 * ", count ,"= ", table)
    count+=1

list=[1,3,4,5,6,7,8,9,1]
index=0
x=1
while  index<len(list):
    if(list[index] == x):
        print("found at :",index)
    else:
        print("not found")
    index+=1

list=[1,14,16,19,21,50]
idx=0
find=19
for i in list:
    if(i==find):
        print("found : ",idx)
        break
    idx+=1
else:
    print("not found")

for i in range (5):
    print(i)

for i in range (1,5):
    print(i)

for i in range (5,10,2):
    print(i)

seq=range(5)
for i in seq:
    print(i)

for i in range(1,101):
    print(i)

for i in range(100,0,-1):
    print(i)

for i in range(1,11):
    mul= 2* i
    print("2 * ", i, " = ", mul)

for i in range(5):
    #empty
    pass
print("some work")

list=[2,3,4,5]
ind=0
count=0
while ind<len(list):
    count+= list[ind]      #count=count+list[ind]
    ind+=1
print(count)

count=1
for i in range(1,5):  #factorial of 4 
    count= count *i 
print(count)


def func(a,b):
    sum= a+b
    return sum
print(func(2,4))

sets={"seenu", 2}
print(sets)