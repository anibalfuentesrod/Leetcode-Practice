#!/usr/bin/python3

og_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def sum_of_even_nums():
    total = 0
    for i in og_list:
        if i % 2 == 0:
            total += i
    
    print(total)

sum_of_even_nums()