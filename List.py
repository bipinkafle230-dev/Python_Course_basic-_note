

# #list in python
# # data structure
# '''list is :
# ordered , mutable, and different datatypes 
# '''
# details=[
#    'bipin',
#    'sameer',
#    'aadi',
#    'kaluwa',
#    'sandesh'
# ]
# print(details)
# print(type(details))
# hack=len(details )
# print(hack)

# #list append 
# details.append("ram")
# print(details)

# #list insertion
# details.insert(2,"foxman")
# print(details)

# #list removing
# details.remove("kaluwa")
# print(details)

# #list remove from pop()
# details.pop(1)
# print(details)


# # play input and output
# name=input("\nEnter the name:\n")
# print("Hello", name ,"Welcome!")

# name=input("Enter the name:")
# print(f"Hello,{name} Welcome!")

# print(details[2])

# my_list=[1,2,3,4,5]
# my_list[0]=10
# print(my_list)


# list=[1,"string",3.98,True]
# print(list) 

# details=[
#    'bipin',
#    'sameer',
#    'aadi',
#    'kaluwa',
#    'sandesh'
# ]
# print(details)

# details.append(2)
# print(details)
# details.insert(3,"ader")
# print(details)





# #classroom 
# word = input("Enter the words: ")
# vowels = ['a', 'e', 'i', 'o', 'u']
# result = ""

# for char in word:
#     if char.lower() not in vowels:
#         result += char

# print("Without vowels:", result)


# char=input("enter string:")
# for i in char:
#     if i in ['a', 'e', 'i', 'o', 'u']:
#         char=char.replace(i,"")
# print(char)


## some today
fruits=['apple','banana','canberry']
# for i in range(len(fruits)):
#     print(i,fruits[i])
i=0
while i<len(fruits):
    print(i+1,fruits[i])
    i+=1

#nested loop 

student=[["sam","ram"],[23,34]]
print(student)

#numerate:
for index , value in enumerate(fruits):
    print(index,value)

# enumerate
details=[
   'bipin',
   'sameer',
   'aadi',
   'kaluwa',
   'sandesh'
]
print(details)

# enumerate it :

for index , value in enumerate(details): 
    print(index, value)

for index , value in enumerate ( details , start=1):
    print(index, value)


# conat 
list_1=[1,2,4]
list_2=[3,5,7]
list_3=list_1+list_2
print(list_3)

shortcuts = ['Sketch', 'Overlay Avatar', 'Clear Canvas']

for i, action in enumerate(shortcuts, start=1):
    print(f"Shortcut {i}: {action}")
