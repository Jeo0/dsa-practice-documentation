"""
guarino
act 3:      list manipulation using python
objective:  wortk with python lists by
                sorting,
                reversing,
                slicing

Instructions:
1.      create a list of random numbers
        use my_list = [12, 4, 56, 17, 8, 99, 23]

2.      Perform the ff. operations
        - sort the list in ascending order
        use: sort_list

        - reverse the ascended list
        use reverse_list

        - extract a slice of the acsceneded list from the 2nd-4th element(inclusive)
        use slice_list
"""

my_list = [12, 4, 56, 17, 8, 99, 23]


###############################################
# sorting
# we ned to lern sorting algos
# this is my trial in implementing bubble sort without copying

# create a copy without using python's inehrent EZPZ features
sort_list = []
for iii in my_list:
    sort_list.append(iii)

lastIndex = len(sort_list)
while lastIndex != 0:
    for index in range(1, lastIndex):    # start at the first index up to the last

        # if previous is greater than te current
        #   swap
        if sort_list[index-1] > sort_list[index]:
            sort_list[index] += sort_list[index-1]                      # = 16
            sort_list[index-1] = sort_list[index] - sort_list[index-1]  # = 4
            sort_list[index] -= sort_list[index-1]                      # = 12
    lastIndex -= 1;

print("sort asc:\t", sort_list)

# if python then just use
# sort_list = my_list.sort()


###############################################
# reversing
# same thing happens however reversed
# leme just copy paste it from the above
# create a copy without using python's inehrent EZPZ features
reverse_list = []
for iii in sort_list:
    reverse_list.append(iii)

lastIndex = len(reverse_list)
while lastIndex != 0:
    for index in range(1, lastIndex):    # start at the first index up to the last

        # if previous is greater than te current
        #   swap
        if reverse_list[index-1] < reverse_list[index]:
            reverse_list[index] += reverse_list[index-1]
            reverse_list[index-1] = reverse_list[index] - reverse_list[index-1]
            reverse_list[index] -= reverse_list[index-1]
    lastIndex -= 1

print("reverse:\t", reverse_list)
# if python then just use
# reverse_list = sort_list.reverse()


###############################################
# slicing
# i dont want to use python jejeje
starting_index = 1
last_index     = 4

# inclusive slicing
slice_list = []
for iii in range(starting_index, last_index):
    slice_list.append(sort_list[iii])
print("sliced list:\t", slice_list)

# if python then just use
# slice_list = sort_list[1:4]