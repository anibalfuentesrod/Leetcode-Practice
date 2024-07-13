#!/usr/bin/python3

list = [1, 2, 3, 4, 5, 6, 7, 8]

new_list = []

def return_list():
    for i in list:
        if i % 2 == 0:
            new_list.append(i)


    print(new_list)

print(return_list())
