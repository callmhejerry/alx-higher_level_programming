#!/usr/bin/python3

'''
This Module  adds all arguments to a list
and then save them to a file
'''


from sys import argv
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

#the list object to add to the file
my_list = []

#Adds the arguments in the list [my_list]
if len(argv) > 1:
    for i in range(1, len(argv)):
        my_list.append(argv[i])

filename = "add_item.json"

try:
    result = load_from_json_file(filename)
    result = result + my_list
    save_to_json_file(result, filename)
except Exception:
    save_to_json_file(my_list, filename)
