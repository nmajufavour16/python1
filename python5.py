# list1 = ["obi", "ada", "eze", "fun", "emeka"]
# list2 = ["favour", "uche", "nmaju"]
# # print(list1 + list2)

# list1.insert(1, "favour")
# # print(list1)

# list1.extend(list2)
# print(list1)

# # for name in list1:
# #     print(name)
    
# # list1.remove("eze")
# # print(list1)

# # list1.remove("favour")
# # print(list1)

# # list1.pop(2)
# # print(list1)

# # list3 = [name for name in list1]
# # print(list3)

# # print(list1, list2, list3)

# # list3 = list1[1::2]
# # print(list3)

# # for name in list1:
# #     list3 = list1[1::2]
# #     print(list3)

# # this checks for and prints the names at even index positions in list1
# list3 = [list1[i] for i in range(len(list1)) if i % 2  == 0]
# print(list3)

# for number in range(50):
#     if number % 5 == 0:
#         print(number)
        
list5 = [number for number in range(51) if number % 5 == 0]
print(list5)