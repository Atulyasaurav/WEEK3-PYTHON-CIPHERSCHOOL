###################################### intro to set ################################################
#  unordered colledtion of unique items
# this is an empty set
s = { } 
# if we store a element twice then the set consider only once
a = {1,2,3,4,2}
print(a)
# also we cant do slicing in set
# print(s[0]) we can't

# how to remove duplicate from lisst
l = [1,2,3,4,5,6,7,6,4,2,1,3,5,7,4,3,2]
# this will convert lisst into set
s2 = set(l)
print(s2)
# now we will convert set into list
# this willl convert list into set
s2 = list(set(l))

# some methods for set

# how to add value to the set
a.add(10)
print(a)




# how to delet value from the set
a.remove(10)
print(a)




# remove
# but
# if we remove some value which doesnt exist in the set , then it will show some error
# to solve the we can use some discard methods
a.discard(11)
print(a)




#clear
a.clear()
print(a)



#copy
a = {1,23,4,5,6,7,9}
s1 = a.copy()
print(s1)

#storing of number
# we can store int, str, or float
s = {1,1.1,"aaa"}
print(s)
# but we can store list or dict in set
# s = {1,2,4,{1:2},[1]}


########################################################## more about set in python #########################################################
# IN keyword:
# to check the item is present in the set or not
s = {1,2,3,4,5,6,7,8,9}
if 3 in s:
    print("present")
else:
    print("not present")


#loop in set:
for i in s:
    print(i)

i = 0
while i < len(s)+1:
    print(i)
    i+=1
# removing duplicate

l = [1,2,3,4,3,2,1]
s = set(l)
print(s)
l = list(set(s))
print(l)




# set maths

# 1 unions
s1 = {1,2,3,4}
s2 = {3,4,5,6}
# this is for unioon of two set 
s3 = s1 | s2
print(s3)

# 2 intersectioin

s1 = {1,2,3,4}
s2 = {3,4,5,6}
# this is for intersection of two sets
s3 = s1 & s2
print(s3)



