# ####################################################################### intro to *args or *operator #################################################################
# # this is a function for  adding two inputs
# def f(a,b):
#     return a+b
#     # but if we pass 3 parameter this function will not work
#     # so we use args methods 
# print(f(2,3))

# def f(*args):
#     total = 0
#     for i in args:
#         total += i
#     return total
# print(f(1,2,3,4))

# def f(*args):
#     # this args give us an tuple
#     return type(args)
# print(f(1,3,4))

# ########################################################### *args with normal paramereter ####################################################################################


# def f(*args):
#     m = 1
#     for i in args:
#         m *= i
#     return m
# print(f(1,2,3))

# # parameter when we set a variable 
# # argument when we call a variable
# # if we set an parameter with args we have to give one value to variable num
# def f(n , *args):
#     # if we not pass an value for the num we get errro
#     m = 1
#     print(n) #3 goes to n'''
#     print(args)  #68 goes to args'''
#     for i in args:
#         m *= i
#     return m
# print(f(3,6,8))
# ############################################################################################## args as argumest #########################################################
# #  when we have to pass an pre define set of value or parameter like list 
# def f(*args):
#     m = 1
#     for i in args:
#         m *= i
#     return m
# print(f(7,8))
# # but if we give an parameter
# def f(*args):
#     m = 1
#     for i in args:
#         m *= i
#     return m
# l = [2,3]
# # now this not gonna work
# # to solve this 
# print(f(l))

# def f(*args):
#     m = 1
#     for i in args:
#         m *= i
#     return m
# l = [2,3]

# print(f(*l))   # this * in front of parameter make it unpack

#################################################################################### Exercise 1 #############################################################################


# def z(a,*args):
#     if args:
#         return [i**a for i in args]
#     else:
#         return "its empty"
# a = int(input("enter a no"))
# args = [1,2,3,4,5]
# print(z(a,*args))

###################################################################################### #double star argument / **kwargs/keywordargument  ###############################################################################

#kwarg as a parameter

# def f(**kwarg):
#     return kwarg
# print(f(first_name = "atulya",middle_name = "saurav",last_name = "abhisanchit"))




# def a(**kwargs):
#     for k ,v in kwargs.items():
#         print(f"{k} : {v}")
# a(first_name = "atulya",middle_name = "saurav",last_name = "abhisanchit")


# def a(name,**kwargs):
#     # for k ,v in kwargs.items():
#     #     print(f"{k} : {v}")
#     return name
# print(a("dj",first_name = "atulya",middle_name = "saurav",last_name = "abhisanchit"))

# # dict unpacking
# def f(**kwarg):
#     for k,v in kwarg.items():
#         print(f"{k} : {v}")
# l = {"name":"babli" , "age":5}
# f(**l)

####################################################################### function with all type of parameter ######################################################################
# normal function with parameter
def f(a,b): 
    return a+b
print(f(2,3))

#normal function with default parameter
def f(name="unknown",age = 0):
    print(name)
    print(age)
f()


#IP


# if we want to use all parameter in one function 
#  like[ normal parameter, default parameter, *args, **kwargs]

# then  we follow the sequence   
# 1 normal parameter
# 2 *args
# 3 default parameter
# 4 **kwargs

def f(name,*args,age = 0,**kwargs):
    print( name)
    print( args)
    print(age)
    print(kwargs)
f("atulya", 1,2,3, a=1 , b=2)

# use of normal parameter and default parameter
def f(name,age=0):
    print(age)
    print(name)
f('aaa')


################################################################## Exercise 2 ################################################################
def z(a,**kwarg):
    if kwarg.get("reverse_str") == True:
        return [i[::-1].title() for i in a]
    else:
        return [i.title() for i in a]
l = ["atulya","saurab"]
print(z(l, reverse_str = True))














