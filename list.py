my_arr=[9,2,4,8,1,5,0,4,2,0,0,7]

def find_number(arr, num):
    i = 0
    while arr[i] != num:
        i += 1
    if  i >= len(arr):
        return "Number not found"
    else:
        return i

def add_number_end(arr, num):
    arr.append(num)
    return arr

def change_number(arr, index, num):
    arr[index] = num
    return arr

def print_list(arr):
    for i in arr:
        print(i)

print_list(my_arr)
print(find_number(my_arr, 5))
print(add_number_end(my_arr, 10))
print(change_number(my_arr, 2, 99))
