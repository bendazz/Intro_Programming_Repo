def find_max(my_list):
    max = my_list[0]
    for number in my_list:
        if number > max:
            max = number

    return max
my_list = [3,2,-9,81,0]

print(find_max(my_list))