
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.previous = None

class Linkedlist:
    def __init__(self, *values):
        self.head = Node()
        self.initializer(*values)
        self.tail = None


    def add(self, value):
        """
        param:  value   

        appends only an element to the end
        returns void
        """
        new_node = Node(value)      # initialize the value first with a new node
        current = self.head         # makes the context that
                                    # we are handling the current node
                                    # while also initialize the next node regardless

        while current.next is not None:
            current = current.next
        while current.previous is not None:
            current = current.previous


        current.previous = current  # point to self
        current.next = new_node     # shift context to right

    def printlist(self):
        """
        prints things the list
        returns void
        """

        # store it in cache then traverse to the next node
        tempCache = []
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
            tempCache.append(current_node.value)
        print(tempCache) 

        
    def deleteThis(self, index):
        """
        param:  index   

        deletes the index specified
        returns void
        """
        current_node = self.head

        # go to the node
        current_index = 0
        last_node = current_node                # set to self node
        while current_index-1 != index:
            last_node = current_node
            current_node = current_node.next
            current_index +=1
            
        # after arriving here, delete
        last_node.next = current_node.next







    def initializer(self, *values):
        """
        param:      *values

        pass some values here to initialize the first values
        """
        if len(values) != 0:
            for iii in values:
                self.add(iii)











# operations
pogi = Linkedlist(123,345,456)
pogi.printlist()

# add multiple, then print
buffers = [909,123,4,5,6,7,8]
for bbb in buffers:
    pogi.add(bbb)
pogi.printlist()


# deletion
pogi.deleteThis(8)
pogi.deleteThis(3)
pogi.printlist()

