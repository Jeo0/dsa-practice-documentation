
class Node:
    def __init__(self, value=None):
        self.value = value
        self.head = None
        self.tail = None


class Linkedlist:
    def __init__(self):
        self.own = None            # initialize nothing

    def insertAtTheLast(self, value):
        new_node = Node(value)      # assume new node

        # create a node if there's no node yet
        while self.own != None:
            self.own = new_node


        while self.own.tail != None:
            self.own.tail = 


        ###############################################
        # resume here
        ###############################################
        # if only 1 node yet,
        # set tail to 
        self.own.
