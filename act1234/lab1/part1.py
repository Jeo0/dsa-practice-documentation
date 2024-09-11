"""
lab activity 1
    IMPLEMENTING ARRAYS AND LINKED LISTS
objective:
    to understand and implement basic operations
    on arrays and linked lists in python

1 create array:
    - define array of ints in python
    - use list
    - intiailize some arbitrary values
2 array operations:
    write functions:
        - add new element at end of array
        - delete an element by its value
        - print all elements in the array
3 test your functions:
    - add few elemnts in array
    - delete some elements in array
    - print final state of array
"""

def addNewElementAtTheEnd(array, add_these):
    """
            name            treated as
    param:  array           list
    param:  add_these       list
    return:                 void

    adds elements at the end of the array
    """
    # make sure that addThese is a list
    tempAddThese = []
    for iii in add_these:
        tempAddThese.append(iii)
    add_these = tempAddThese

    # add the elements in add_these to the end of array
    for jjj in add_these:
        array.append(jjj)


def deleteElements(array, delete_values):
    """
            name            treated as
    param:  array           list
    param:  delete_values   list
    return:                 void

    deletes elements in the array 
    that matches with the value/s of the delete_values
    """

    
    # makes sure delete_values is a list
    cacheDeleteValues = []
    for iii in delete_values:
        cacheDeleteValues.append(iii)
    delete_values.clear()
    delete_values = cacheDeleteValues


    # marking where in the array that has the value in delete
    markIndex = []
    for aaa in range(len(array)):
        # another search for matching values 
        # in delete_values
        # bruteforce
        for bbb in range(len(delete_values)):
            if array[aaa] == delete_values[bbb]:
                markIndex.append(aaa)


    # sanitize the marked indices 
    # by removing duplicates
    tempDuplicates = []
    for iii in range(len(markIndex)):
        # store if next value in array is not equal to current
        if iii+1 != len(markIndex) and markIndex[iii] != markIndex[iii+1]:
            tempDuplicates.append(markIndex[iii])
        # store the last element regardless
        elif iii+1 == len(markIndex):
            tempDuplicates.append(markIndex[iii])
    markIndex.clear()
    markIndex = tempDuplicates

    # deletion of the marked indices
    deleteCount = 0
    for iii in range(len(markIndex)):
        array.pop(markIndex[iii] - deleteCount)
        deleteCount +=1




def deleteElementsHash(array, delete_values):
    """
            name            treated as
    param:  array           list
    param:  delete_values   list
    return:                 void

    deletes elements in the array 
    that matches with the value/s of the delete_values
    """
    # makes sure delete_values is a list
    cacheDeleteValues = []
    for iii in delete_values:
        cacheDeleteValues.append(iii)
    delete_values.clear()
    delete_values = cacheDeleteValues

    # sort the delete_values from less to bigger value
    delete_values.sort()        # this is may take quite long to write
                                # and it deserves a separate discussion/activity
                                # so lets just resort with this

    # remove duplicates
    # same as with the approach 1
    tempSanitized = []
    iii = 0
    while (iii < len(delete_values)):
        # store if next value in array is not equal to current
        if iii+1 != len(delete_values) and delete_values[iii] != delete_values[iii+1] :
                    tempSanitized.append(delete_values[iii])
        # store the last element regardless
        elif iii+1 == len(delete_values):
            tempSanitized.append(delete_values[iii])
        iii +=1
    delete_values.clear()
    delete_values = tempSanitized


    # create a hash
    # eg. 1:1, 2:2, 25:25
    deleteHash = {}
    for iii in delete_values:
        deleteHash[iii] = iii

    """
    print("===========\ndeleteHash\nkey\tvalue")
    for key, value in deleteHash.items():
        print(key, "\t", value)
    """


    # deletion
    # loop through the array backwards
    # if the current value does not exist in the hashed deletevalues, 
    # pop it
    iii = len(array) - 1
    while(iii >= 0):
        if deleteHash.get(array[iii]) is not None:
            array.pop(iii)
        iii -=1 

    


def printAllElements(array):
    """
            name            treated as
    param:  array           list
    return:                 void

    prints all elements in a list
    """
    print("[", end='')
    index = 0
    while index < len(array):
        print(array[index], end='')
        print("]\n"                         \
                if (index+1 == len(array))  \
                else (", "), end='')
        index +=1






orig_array = [1,2,3,4,5,6,7,1,2,3,4,5]
orig_arrayhash = [1,2,3,4,5,6,7,1,2,3,4,5]

add_array = [75,457,78]
add_arrayhash = [346, 657, 123]

delete = [4,1,2,3,1,4, 234, 75]
deletehash = [4,1,2,1,4]

#########################################
# operations
addNewElementAtTheEnd(orig_array, add_array)
addNewElementAtTheEnd(orig_arrayhash, add_arrayhash)

deleteElements(orig_array, delete)
deleteElementsHash(orig_arrayhash, deletehash)

printAllElements(orig_array)
printAllElements(orig_arrayhash)






