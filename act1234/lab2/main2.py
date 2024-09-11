"""
act 4:      arrat of letters
objective:  work with an array of letters
            and perform operators:
                sesarching,
                insertion,
                removal
instructions:
1.  create an array of letters:
    use letters: ['a', 'b', 'c', 'd', 'e', 'f']

2. write functions:
    - insert letter at specified index
    use insert_letter

    - remove a leter by value
    use remove_letter

    - search for a letter in the array
    and return its index (if found otherwise display "not found")
    use search_letter
"""


letters = ['a', 'b', 'c', 'd', 'e', 'f']


def insert_letter(listlist, letter=None, index=0):
    # i dont wnat to use the insert built-in function
    # concept:
    # 1.    divide the array (1 copy left half and 1 copy to the right half)
    # 2.    then insert whatatevber to the left of half at the last elemnet
    # 3.    return the (join the left half and right half)

    # create a copy of the left half and right half
    # hehe tinatamad na me
    leftHalf = listlist[0:index]
    rightHalf = listlist[index:]
    """
    print("leftHalf: " , leftHalf)
    print("righthalf: " , rightHalf)
    """
    leftHalf.append(letter)

    leftHalf.extend(rightHalf)
    return leftHalf


testinsert = insert_letter(letters, "zz", 4)
print(testinsert)

def remove_letter(listlist, letter):
    # concept
    # have a another list
    # just loop through the listlist and dont include letter to the another list
    tempCache = []
    for iii in listlist:
        if iii == letter:
            continue
        tempCache.append(iii)
    return tempCache


testremove = remove_letter(letters, 'd')
print(testremove)


def search_letter(listlist, letter = None):
    for iii in range(len(listlist)):
        if letter == listlist[iii]:
            return iii
    print("not found")
    return None

testsearch = search_letter(letters, 'a')
print(testsearch)
