#day-6
'''
#1.)python program to capitalize the frist and last charater of each
#word in astring
s1 = input("enter string:")
fst = s1[0].upper()
lst = s1[-1].upper()
print(fst+s1[1:len(s1)-1]+lst)
'''
'''
#2.)input : 128
n = 128
temp = n
f1 = 0
while n!=0:
    rem = n%10
    chek = temp % rem
    if chek!=0:
        f1 = 1
    n =n//10
if f1==0:
    print("yes")
else:
    print("no")
    '''
'''
#3.)l1 = [1,2,3,4],l2 = [5,6,7,8] add both l1 and l2 ans=[6,8,10,12]
l1 = [1,2,3,4]
l2 = [7,6,5,4]
l3 = []
print(l1[0]+l2[0],l1[1]+l2[1])
for val in range (len(l1)):
    ans=l1[val]+l2[val]
    l3.append(ans)
print(l3)
    


#-->set
#charcterstices of set
#1.)set can be created using{}
#2.) the elements inside set are not indexed
#3.)does not allow duplicate values
#4.)it unorederded
#5.)heterogenous-->accept only unmutable datatypes
#6.) mutable or changable
#eg-1
s1 ={9,89,7.76,8+7j,(8,7,5),"truck",'e'}
print(s1)
#eg-2
s2 = {5,8,98,[9,0]}
print(s2)
#eg-3
#min(),max(),len()
'''
'''
#eg-4
# to add element inside set
s1 = {8,78,67,'u'}
#add()
s1.add(43)
print(s1)
#update()
s1.update([9,0])
print(s1)
#to delete element inside set
s1 = {8,78,67,'u'}
#pop()
s1.pop()
print(s1)
#remove()
s1.remove(78)
print(s1)
#discard()
s1.discard(8976)
print(s1)
'''
'''
#clear()
l1 = []
print(type(l1))
s1 = set()
print(type(s1))
s1 ={8,9,0}
s1.clear()
print(s1)
'''
'''
#join to the set
s1 = {9,8,0}
s2 = {9,90,"card",'y',56}
#union()--> to combine 2 sets
s3 = s1.union(s2)
print(s3)
#intersection()--> to get common elements inside set
s1 = {4,5,6}
s2 = {5,6,7,8}
print(s1.intersection(s2))
#difference
s1 = {4,5,6}
s2 = {5,6,7,8}
print(s1.difference(s2))
print(s2.difference(s1))
print(s1.symmetric_difference(s2))
s2 = {5,6,7,8}
'''
'''
#--->problem:1

s1 = [1,2,3,4,5]
s2 = [6,7,8,9,0]
#n1 = {1,2,3}--->
for val in s1:
    if val in s2:
        str = "its joint set"
print(str)
'''
'''
#-->dictionary
#eg:1
d1 = {1:100,'a':200,4.5:"hello"}
marks_stu1 = {"english":90,"power":90,"stld":90}
print(d1)
print(len(d1))
#char of dictionary
#1.)have to be surrounded by{}
#2.) it have to be in the from of key,value pair
#3.)it is mutable
#4.)duplicate keys are not allowed,duplicate values are allowed
#5.)it is unindexd
#6.)it is orderded
#7.)key does not allow mutable datatypes, values allow mutable datatype
d1 = {1:100,2:200,3:300,4:400}
#to access the values, have to use key
print(d1[1])
#some common functions
#len(),min(),max()
print(min(d1))
print(max(d1))
# to find min ,max based on values
print(min(d1.values()))
print(max(d1.values()))
#dictionary based functions
#to add element(key and value pair) in dict
d1 = {1:100,2:200,3:300,4:400}
#join 2 dictionary
update()
d1 = {1:100,2:200,3:300,4:400}
d2 = {"a":"apple","b":"boy","g":"game"}
d1.update(d2)
print(d1)
'''
'''
#get()
d1 = {1:100,2:200,3:300,4:400}
print(d1[90])
print(d1.get(90))
# to print all the keys
print(d1.keys())
print(type(d1.keys()))
'''
'''
#iterating dictionary
for val in d1:
    print(val)
for val in d1.values():
    print(val)

# to get both key and values
for key,val in d1.items():
    print(key,val)
'''
'''
#problem:1
n =  int(input("enter num of items:"))
integer=[]
float_value = []
string=[]
for val in range(n):
    value = eval(input("enter the values:"))
    if type(val)==int:
        integer.append(value)
    elif type(value)==float:
        float_value.append(value)
    elif type(value)==str:
        string.append(value)
    else:
        print("pls provide data in int,float,string")
print(integer)
print(float_value)
print(string)
'''
# Return a set of elements present in Set A or B, but not both
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# o/p
# {20, 70, 10, 60}
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set3 = set()
for val in set1:
    if val not in set2:
        print(val)
for val in set2:
    if val not in set1:
        set3.add(va1)
print(set3)

        
            

