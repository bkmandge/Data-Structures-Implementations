"""

Create two classes:-
1. class Node:- for nodes creation
              1.__init__ :- assign node's VALUE to VALUE & assign NEXT pointer to NONE
              2.__str__ :- to print node values

2. class Linkedlist:- for linking nodes
              1.__init__create HEAD & TAIL POINTERS with NONE value
              2.__iter__ to make linked list iterable, first use iter then only str, else str will show error
              3. __str__ :- to print values of linked list
                    -> instead of this function we can directly use as print([node.value for node in singlyLL]) at the end
              4. def insertNode(self, value, location)
              5. def traverseLL(self)
              6. def searchNode(self, nodeValue)
              7. def deleteNode(self, location) location is node's index value
              8. def deleteSLL(self)
              9. def getNode(self, index):- to get node from specific index
              10. def set_new_value(self, index, value):- to change node's value

create object of LinkedList class
functions created in this class need to be called with Linkedlist object
if variable is not going to be used in program then use _ as var name
    for _ in range()

"""


class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __iter__(self):
        tempNode = self.head
        while tempNode is not None:
            yield tempNode
            tempNode = tempNode.next

    def __str__(self):
        values = [str(node.value) for node in self]
        return '->'.join(values)

    def insertNode(self, value, location):
        newNode = Node(value)

        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:  # first location
                newNode.next = self.head
                self.head = newNode
            elif location == 1:  # last location, 2 -> third location i.e. insert at index 2
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
        self.length += 1

    def traverseLL(self):
        if self.head is None:
            print("SLL does not exist!")
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next

    def searchNode(self, nodeValue):
        if self.head is None:
            print("SLL does not exist!")
        else:
            node = self.head
            while node is not None:
                if node.value == nodeValue:
                    return node.value
                node = node.next
            return "Given value does not exist in SLL!"

    def deleteNode(self, location):
        if self.head is None:
            print("SLL does not exist!")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = None
                    self.tail = None
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next

    def deleteLL(self):
        if self.head is None:
            print("SLL does not exist!")
        else:
            self.head = None
            self.tail = None

    # update / change node's value:- 1. first get node of that index in getNode() & then update value in set_new_value()

    def getNode(self, index):
        if index == -1:
            return self.tail
        if index < -1 or index >= self.length:
            return None
        curNode = self.head
        for _ in range(index):
            curNode = curNode.next
        return curNode  # return curNode.value

    def set_new_value(self, index, value):
        temp = self.getNode(index)
        if temp:
            temp.value = value
            return True
        return False


singlyLL = LinkedList()

singlyLL.insertNode(10, 1)
singlyLL.insertNode(20, 0)
singlyLL.insertNode(30, 1)
singlyLL.insertNode(40, 1)
singlyLL.insertNode(0, 2)
# if __name__ == "main":
#     # printing SLL
print(singlyLL)

# traversal of SLL
#singlyLL.traverseLL()

# searching node value
#print(singlyLL.searchNode(100))

# deleting a node
# singlyLL.deleteNode(2)
# print(singlyLL)

# deleting entire SLL
#print(singlyLL.deleteLL())
print(singlyLL.length)
