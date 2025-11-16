#dictionary 

# my_dict={"Samera is ":"a girl"} # key : value pair
# print(type(my_dict))

my_dictionary={
    "name":"samera",
}

print(my_dictionary["name"])#value accessing

my_dictionary["name"]="Sammer"
# print(my_dictionary)

my_dictionary["City"]="KTM" 
print(my_dictionary)

# nested dict
nested_dict={
    "boy":{"name":"Aadi","age":199},
    "Girl":{"name":"laila","age":82},
    "Not":{"name":"iok","age":100}
}
#print(nested_dict)
for v in nested_dict.values():
    print(v)

for v in nested_dict:
    print(v)


