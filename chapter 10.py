######################################################################## dictionary comprehension ###################################################
d1={num:num*2 for num in range(1,11)}
print(d1)

d2 = { f" Multiply of this {i}  is ": i*2 for i in range(1,11)}
print(d2)
for p,q in d2.items():
    print(f"{p} is {q}")

################################################################ if else comprehension ##########################################################
d={ }
for i in range(1,11):
    if i % 2 ==0:
        d[i]="even"
    else:
print(d)



d1 = {i:("even" if i% 2 == 0 else "odd") for i in range(1,11)}
print(d1)

######################################################### set comprehension #################################################################################
s1 = {1}
for i in range(1,11):
    s1.add(i)
print(s1)
print(type(s1))



s1 = {i for i in range(1,11)}
print(s1)
print(type(s1))