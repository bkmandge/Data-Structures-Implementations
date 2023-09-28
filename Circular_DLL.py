"""
base Node & CircularDLL class
create CircularDLL
insert nodes
traverse CircularDLL
reverse traverse CircularDLL
search node
delete node
delete CircularDLL
"""


class Node:
    def __init__(self, value = None):
        self.value = value
        self.prev = None
        self.next = None

    def __str__(self):
        return str(self.value)


class CircularDLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        values = [str(node.value) for node in self]
        return '->'. join(values)

    def __iter__(self):
        tempNode = self.head
        while tempNode:
            yield tempNode
            tempNode = tempNode.next
            if tempNode == self.tail.next:
                break

    def createCircularDLL(self, nodeValue):
        newNode = Node(nodeValue)
        newNode.prev = newNode
        newNode.next = newNode
        self.head = newNode
        self.tail = newNode

    def insertNode(self, nodeValue, location):
        if self.head is None:
            return "No CircularDLL exist!"
        else:
            newNode = Node(nodeValue)
            if location == 0:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.head = newNode
                self.tail.next = newNode
            elif location == 1:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                newNode.next = tempNode.next
                newNode.prev = tempNode
                newNode.next.prev = newNode
                tempNode.next = newNode
            return "Node has been successfully inserted!"

    def traverseCDLL(self):
        if self.head is None:
            return "No CDLL exist!"
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next
                if tempNode == self.tail:
                    break

    def reverseTraverseDLL(self):
        if self.head is None:
            return "No CDLL exist!"
        else:
            tempNode = self.tail
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.prev
                if tempNode == self.head.prev:
                    break

    def searchNode(self, nodeValue):
        if self.head is None:
            return "No CDLL exist!"
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodeValue:
                    return tempNode.value

                if tempNode == self.tail:
                    return "No such node value!"
                tempNode = tempNode.next

    def deleteNode(self, location):
        if self.head is None:
            return "No CDLL exist!"
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = self.tail
                    self.tail.next = self.head
            elif location == 1:
                if self.head == self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = self.head
                    self.head.prev = self.tail
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                tempNode.next = tempNode.next.next
                tempNode.next.prev = tempNode

    def deleteCDLL(self):
        if self.head is None:
            return "No CDLL exist!"
        else:
            self.tail.next = None
            tempNode = self.head
            while tempNode:
                tempNode.prev = None
                tempNode = tempNode.next
            self.head = None
            self.tail = None
        return "CDLL deleted successfully!"


circularDLL = CircularDLL()
circularDLL.createCircularDLL(0)
circularDLL.insertNode(10, 0)
circularDLL.insertNode(20, 1)
circularDLL.insertNode(30, 1)
circularDLL.insertNode(2, 2)

# print(circularDLL)
# circularDLL.traverseCDLL()
circularDLL.reverseTraverseDLL()
# print(circularDLL.searchNode(10))
print(circularDLL)
# circularDLL.deleteNode(3)
# print(circularDLL.deleteCDLL())
