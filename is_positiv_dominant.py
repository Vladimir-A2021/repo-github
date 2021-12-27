def is_positive_dominant(list1):
    return sum(1 if i > 0 else -1 if i < 0 else 0 for i in set(list1)) > 0

list1 = [1, -3, -5, 6, -4]
print(is_positive_dominant(list1))






# def is_positiv_dominant(l):
#     l2 = []
#     l3 = []
#     for i in list1:
#         if i > 0:
#             l2.append(i)
#         else:
#             l3.append(i)
#
#     l4 = set(l2)
#     l5 = set(l3)
#
#     if len(l4) > len(l5):
#         return 'True'
#     else:
#         return 'False'
#
#
#
# list1 = [1, 3, -5, 6, -4]
# print(is_positiv_dominant(list1))



