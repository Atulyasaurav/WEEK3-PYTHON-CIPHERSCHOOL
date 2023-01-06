################################################ Exericse 1 #########################################################A

# def f(a):
#     b ={ }
#     for i in range(1,a+1):
#         b[i] = i*3
#     return b
# print(f(3))

#################################################### word counter ##################################################
def f(a):
    d={ }
    for i in a:
        d[i] = a.count(i)
    return d
print(f("Atulya"))

###################################################### exercise 2 #############################################################################
user_info = { }
Name = input("Enter your name: ")
Age =  int(input("Enter your age"))
Fav_movies = input("Enter your fav_movies name").split(",")
Fav_songs = input("Enter your fav_songs").split(",")
user_info["Name"] = Name
user_info["Age"] = Age
user_info["Fav_movies"] = Fav_movies
user_info["Fav_songs"] = Fav_songs

for key , value in user_info.items():
    print(f"{key} : {value}")


