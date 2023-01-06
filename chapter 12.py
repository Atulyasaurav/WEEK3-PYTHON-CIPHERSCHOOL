#################################################################### Lambda expression #####################################################
# how many way we create a same fun:
#1
# def f(a):
#     if a % 2 == 0:
#         print(True)
#     else:
#         print(False)
# f(6)

#2 
# def f(a):
#     if a % 2 == 0:
#         return True
#     return False
# print(f(6))

#3 
# def f(a):
#     return a%2 == 0
# print(f(3))

# but , this simplest way to use the lambda expression



a = lambda a : a%2==0
print(a(3))



b = lambda s : s[::-1]
print(b("atulya"))



c = lambda s : s[-1]
print(c("kjdsuhi"))


# use of lambda on if else 

def f(a):
    if len(a)> 5:
        return True
    return False
print(f("atulya"))

def f(a):
    return len(a)>5
print(f("atulya"))

b = lambda s : len(s)>5
print(b("atulya"))


############################################################ enumerate function ############################################################

# enumerate function is used to track the position of function
# eg;
#    when we use for loop in list or dict we only take care about of the value not
    #  bother about the positioon of  the function
    # so to take care of this we use enumerate function


# without enumerate funvtion
l = ["abc","atulya","saurav"]
p = 0
for i in l:
    print(f"{i} : {p}")
    p += 1


# with enumerate function
for pos , j in enumerate(l):
    print(f"{pos} : {j}")

#practises
def f(a,*args):
    if a in args:
        print("yes")
    print("-1")
a = "atulya"
args = ["atulya","saurav","abhisanchit"]
f(a,args)












