# # # for loops

# # for i in range(5):
# #     print(i)

# # # checking even or odd
# # n=int(input("Enter the number:"))
# # if n%2==0:
# #     print("Even")
# # else:
# #     print("odd")

# # # another range (1,100)

# # for i in range (1,101):
# #     if i%2==0:
# #         print(i,"Even")
# #     else:
# #         print(i,"Odd")

# # functioning 

# def my_func():
#     print("hello world")
# my_func()

# def naming (fname):
#     print(fname + "kumar")
# naming("bipin")


# # play fname and lname
# def naming (fname,lname):
#     print(fname + " " + lname)
# naming("bipin","kumar")
# naming("sameer","kumar")

# # some
# def my_function(*kids):
#   print("The youngest child is " + kids[2])

# my_function("Emil", "Tobias", "Linus")

# arbitrary arguments ( *args)

def lopp (*kidds):
    print("the youngest child is "+kidds[2])
lopp("raj","geari","gharei")

# keywords arguments 

def ads(child3,child2,child1):
    print("The youngest child is "+child3)
ads(child1="uise",child2="jiai",child3="kaldj")

# arbitraray keywords arguments (**kwargs)

def pool(**kook):
    print("they hit him all the way"+kook["lnmae"])
pool(fname="raj", lname="uerak")

