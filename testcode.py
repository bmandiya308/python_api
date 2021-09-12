# from functools import reduce
# list_a = range(1,11)
# list_b = range(11,21)
# print(type(list_a))
#
#
# print(type(reduce(lambda x,y: x+y,zip(list_a,list_b))))
# print(reduce(lambda x,y: x+y,zip(list_a,list_b)))
# list_c = filter(lambda x : x if x%2==0 else None,list_a)
# print(type(list_c))
# print(list(list_c))
#
#
# print([x for x  in map(lambda x : x ,list_b) if x%2 == 0])
#
#
# print(map(lambda x : x ,list_b))

##pass by values and refernce

# def funct(element):
#     list_1 = list(element)
#     list_1.append(10)
#     element = tuple(list_1)
#     print(element)
#
#
# docker = (1,2,3,4,5,6,7,8,9)
# funct(docker)
# print(docker)

# with open('Dockerfile','r') as out:
#     #print(out.readlines())
#     for i  in out:
#         print(i)
#         print(out.tell())
#
# import os
#
# dirs = os.listdir(".")
# for i in dirs:
#     if(os.path.isfile(i)):
#         print("File : ",i)
#     elif(os.path.isdir(i)):
#         print("Dir  : ",i)
#     else:
#         print("Not getting anything")


# f = open("Dockerfile", "r")
# print(f.readline())
# print(f.tell())
# print(f.readline())
# print(f.tell())
# print(f.readline())
# print(f.tell())
# f.seek(0,0)
# print(f.readline())
# print(f.tell())




# from filelock import FileLock
#
# with FileLock("Dockerfile.lock"):
#     print("Lock acquired.")
#     with open("Dockerfile") as out:
#         locker = open("Dockerfile")
#         for i in locker:
#             print(i)

from functools import reduce
list_1 = [1,2,3,1,2,3,5,7,8,9,2,14,2,12]
list_2 = [1,2,3,1,2,3,5,7,8,9,2,14,2,12]

print(reduce(lambda x,y: x + y,zip(list_1,list_2)))
