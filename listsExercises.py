# # Exercise 7
# num_list = [3, 5, 7, 9, 8, 6]
# num_factor = 4
# new_list = []
# for num in num_list:
#     total = num * num_factor
#     new_list.append(total)
# print(new_list)

# # Exercise 8

# list1 = [2, 4, 5]
# list2 = [2, 3, 6]
# new_num_list = []

# i = 0
# while i < len(list1):
#     total = list1[i] * list2[i]
#     new_num_list.append(total)
#     i += 1
# print(new_num_list)


# Exercise 9 & 10
# list2d_1 = [[1, 3], [2, 4], [5, 6]]
# list2d_2 = [[5, 2], [1, 0], [7, 8]]
# result2d = []
# inner_list = []
# outer_count = 0
# inner_count = 0
# while outer_count < len(list2d_1):
#     while inner_count < len(list2d_1[outer_count]):
#         total = list2d_1[outer_count][inner_count] + list2d_2[outer_count][inner_count]
        
#         inner_list.append(total)
#         inner_count += 1
#     result2d.append(inner_list)
#     outer_count += 1
#     inner_list = []
#     inner_count = 0
# print(result2d)

# Exercise 11

multi_list = [5, "Cainan", 3, "dog", 9, "dog", "cat", 9]
new_list = []
for item in multi_list:
    if not(item in new_list):
        new_list.append(item)

print(new_list)   

# Bonus Exercise

matrix_1 = [[5,6],
            [7,8]]
matrix_2 = [[2,3],
            [4,3]]

matrix_product = [[],
                  []]