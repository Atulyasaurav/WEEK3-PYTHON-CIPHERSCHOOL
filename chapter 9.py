############################################## Intro of list comprehension ##################################################

# create a list of (0,10) its square
l1 = []
for i in range(0,11):

    l1.append(i**2)
print(l1)

# same thing but with the help of list comprehension
l2 = [i**2 for i in range(0,11)] 
print(l2)


# creating a list (0,10) negative
l1 = []
for i in range(0,11):
    l1.append(-i)
print(l1)

# now same , with the help of list comprehension
l1 = [-i for i in range(0,11)]
print(l1)


# create a list containg the first letter of another list
l1 = ["atulya","saurab","ahisanchit"]
l2 = []
for i in l1:
    l2.append(i[0])
print(l2)

# now by list comprehension
l1 = [i[0] for i in l1]
print(l1)

######################################### exercise 1 ############################################################
l1 = ["abc","tuv","xyz"]
l2 = []
for i in l1:
    l2.append(i[::-1])
print(l2)

# by list comprehension
l3 = [i[::-1] for i in l1]
print(l3)


###############################################if element by list comprehension #################################################

# create a list of even numb

l1 =[]
l2 = list(range(1,11))
print(l2)
for i in l2:
    if i % 2 == 0:
        l1.append(i)
print(l1)


# now by using list comprehension
l3 = [i for i in l2 if i % 2==0]
print(l3)

# we use range instead of variable
l3 = [i for i in range(1,21) if i % 2==0]
print(l3)

# now create an odd no list
l3 = [i for i in range(1,11) if i % 2 != 0] 
print(l3)

############################################################ exercise 2 ################################################################################
def f(a):
    b = [ ]
    l1 = [1,2.3,3,4,"a",{1:2},(1,2),{1,2},True]
    b = [str(i) for i in l1 if (type(i) == int or type(i) == float)]
    # print(b)
    return b
print(f(l1))

############################################################## List comprehension with if else ####################################################################
# create  a list if even *2 or odd -1
l1 = [1,2,3,4,5,6,7,8,9]
l2 = []
for i in l1:
    if i % 2 ==0:
        l2.append(i*2)
    else:
        l2.append(-i)
print(l2)

# by list comprehension
l2= [ i*2 if (i % 2== 0) else -i for i in l1]
print(l2)

################################################################ nested list comprehension ##################################################################################
# sample = [[1,2,3],[1,2,3],[1,2,3]]
l1 =[ ]
for i in range(3):
    l1.append([1,2,3])
print(l1)

# by comprehension 
l5 = [[i for i in range(1,4)] for i in range(3)]
print(l5)