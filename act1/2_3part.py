class Node:
    def __init__(self, value=None):
        self.value = value
        self.head = None
        self.tail = None


class Linkedlist:
    def __init__(self):
        self.own = None            # initialize nothing
    def printlist(self, value):


        while self.own.tail != None:
            self.own.tail = new_node
            #pogi1.tail = pogi2      # set previous tail to current address
            #print("pogi1.tail: ", pogi1.tail)       # head : none       address: 000    tail: 123


            new_node.head = self.own
            #pogi2.head = pogi1      # set address to previous 
            #print("pogi2.head", pogi2.head)         # head : 000        address: 123    tail: none

    def insertAtTheLast(self, value):
        new_node = Node(value)      # assume new node

        # create a node if there's no node yet
        if self.own != None:
            self.own = new_node


        #pogi2 = Node(2)         # head : none       address: 123        tail: none


        while self.own.tail != None:
            self.own.tail = new_node
            #pogi1.tail = pogi2      # set previous tail to current address
            #print("pogi1.tail: ", pogi1.tail)       # head : none       address: 000    tail: 123


            new_node.head = self.own
            #pogi2.head = pogi1      # set address to previous 
            #print("pogi2.head", pogi2.head)         # head : 000        address: 123    tail: none

    

        """
        # 2nd node
        # create a new node after reaching last
        #if self.own.tail == None:
            #self.own.tail = new_node.head

        # subsequent node
        while self.own.tail != None:
            self.own = self.own.tail

        ###############################################
        # resume here
        ###############################################
        # if only 1 node yet,
        # set tail to 
        self.own.tail = new_node
        new_node.head = self.own
        """


"""
class Node():
    def __init__(self, value = None):
        self.value = value
        self.head = None
        self.tail = None
 
pogi1 = Node(1)         # head : none       address: 000        tail : none;
pogi2 = Node(2)         # head : none       address: 123        tail: none


pogi1.tail = pogi2      # set previous tail to current address
print("pogi1.tail: ", pogi1.tail)       # head : none       address: 000    tail: 123


pogi2.head = pogi1      # set address to previous 
print("pogi2.head", pogi2.head)         # head : 000        address: 123    tail: none



pogi3 = Node(value)

pogi2.tail = pogi3
pogi3.head = pogi2

"""


noice1 = Linkedlist
Linkedlist
