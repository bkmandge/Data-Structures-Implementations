"""
class CircularLL:- Last node links to first node

    Add additional lines

    def __iter__():- additional line -> after yield
        tempNode.next == self.tail.next: # stopping condition
        if node's next ref points to first node, means end of circular linked list then break loop

    def createCircularLL() - add firstNode to create CSLL

    def insertNode():- location == 1: newNode.next = self.head -> to link newly added last node with first node

    def traverseCSLL():- if tempNode == self.tail.next: # stopping condition
                            break
    def searchCSLL():- if tempNode == self.tail.next: # stopping condition
                            break

    def deleteNode():- loc == 0:- else part: self.head = self.head.next,
                                        self.tail.next = self.head # set last node's connection with FIRST node
    def deleteCSLL():- self.tail.next = None # to break circular loop

"""


class ListNode:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)


class CircularSLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self): # to print values of linked list
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.head:  # if node points to first node, means end of circular linked list
                break

    def __str__(self):
        values = [str(node.value) for node in self]
        return '->'.join(values)

    def createCSLL(self, nodeValue):
        node = ListNode(nodeValue)
        node.next = node  # assigning ref of same node to itself i.e. circular
        self.head = node
        self.tail = node
        return "CSLL has been created!"

    def insertNode(self, nodeValue, location):
        newNode = ListNode(nodeValue)

        if self.head is None:
            return "CSLL does not exist!"
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
                self.tail.next = self.head
            elif location == 1:
                newNode.next = self.head
                self.tail.next = newNode
                self.tail = newNode
            else:
                currNode = self.head
                index = 0
                while index < location - 1:
                    currNode = currNode.next
                    index += 1
                nextNode = currNode.next
                currNode.next = newNode
                newNode.next = nextNode
        return "New node has been inserted!"

    def traverseCSLL(self):
        if self.head is None:
            return "No CSLL to traverse!"
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)   # use this before incrementing temp to temp.next if curNode == self.tail: break
                tempNode = tempNode.next
                if tempNode == self.tail.next:  # use this condition after incrementing temp to temp.next
                    break

    def searchNode(self, nodeValue):
        if self.head is None:
            return "CSLL has no nodes to search for!"
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodeValue:
                    return tempNode.value
                tempNode = tempNode.next

                if tempNode == self.tail.next:
                    return "given node value does not exist in CSLL!"

    def deleteNode(self, location):
        if self.head is None:
            return "No CSLL exist to delete node!"
        else:
            if location == 0:
                if self.head == self.tail:  # if there is only one node
                    self.head.next = None  # deleting node's self reference
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.tail.next = self.head  # connection between last node to second node
            elif location == 1:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    tempNode = self.head
                    while tempNode:
                        if tempNode.next == self.tail:  # reaching till node before last node i.e. second last self.tail
                            break
                        tempNode = tempNode.next
                    tempNode.next = self.head
                    self.tail = tempNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                tempNode.next = tempNode.next.next

    def deleteCSLL(self):
        self.head = None
        self.tail.next = None
        self.tail = None


circularSLL = CircularSLL()

# creation
circularSLL.createCSLL(1)
print(circularSLL)

# insertion
circularSLL.insertNode(10, 0)
circularSLL.insertNode(20, 1)
circularSLL.insertNode(30, 1)

print(circularSLL)

# traversal
circularSLL.traverseCSLL()

# searching a node
print(circularSLL.searchNode(10))

# deleting a node
circularSLL.deleteNode(0)
print(circularSLL)


# deleting CSLL
print(circularSLL.deleteCSLL())
