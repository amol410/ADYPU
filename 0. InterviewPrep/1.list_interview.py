#4 remove first 5 >> create number from list
# place it back then remove second 5 >> make number from list
# compare both the number and print higher one 

# first number creation code
list1 = [5,4,3,2,5,8,9,3]
index = list1.index(5)
print(index)
list1.pop(index)
new_num_of_list1 = int("".join(map(str,list1)))

# second number creation code
list1.insert(index,5)
list1.reverse()
list1.remove(5)
new_num_of_list2 = int("".join(map(str, list1)))

if new_num_of_list1 > new_num_of_list2:
    print(new_num_of_list1, "is greater than", new_num_of_list2 )
elif new_num_of_list1 == new_num_of_list2:
    print("both are equal")
else:
    print(new_num_of_list2, "is greater than", new_num_of_list2)        






