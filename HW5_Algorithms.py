##1 When given a list, the program should return a list of all the elements
# that are below the arithmetical mean of the original list.  The arithmetical
# mean is the sum of all elements divided by the number of elements.
def list_total(num_list):
    arith_mean = sum(num_list) / len(num_list)
    new_list = [x for x in num_list if x < arith_mean]
    print(new_list)

##2 When given a list of elements find the two lowest elements.
# They can be equal to each other or different.
def lowest_in_list(item_list):
    item_list.sort()
    print(item_list[:2])

##list_total([1, 2, 3, 3, 2, 1, 3, 1, 10, 4, 5, 4, 5, 5, 5, 5])
##lowest_in_list([1, 2, 3, 3, 2, 3, 10, 4, 5, 4, 5, 5, 5, 5])
##lowest_in_list(['hi', 'hello', 'yo'])
