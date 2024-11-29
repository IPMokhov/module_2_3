my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

cur_index = 0

while cur_index < len(my_list):

    if my_list[cur_index] < 0:
        break

    if my_list[cur_index] > 0:
        print(my_list[cur_index])
    cur_index = cur_index + 1
