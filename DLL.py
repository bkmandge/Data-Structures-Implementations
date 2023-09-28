"""
1. Node class:- init() -> value, prev & next pointers
2. DLL class:- init(), str(), iter(),
                ***first update next address part & then prev part of each node***
               createDLL() -> set newNode's Prev & Next to None, HEAD & TAIL to newNode
               insertNode() -> set newNode's Prev -> None & do all changes
               traverseDLL() -> same as SLL
               reverseTraverseDLL() -> curNode = self.tail & do reverse traversal -> curNode = curNode.prev
               searchNode() -> same as SLL
               deleteNode() ->  loc== 1 else part:- self.tail = self.tail.prev # set tail with one node before last node
                                self.tail.next = None # last node set to NONE -> to delete this by garbage co.
                                loc == any:- traverse DLL & set
                                    currNode.next = currNode.next.next
                                    currNode.next.prev = currNode
               deleteDoublyLL() - traverse DLL & delete all prev nodes
                                  -> curNode.prev = None, then set HEAD & TAIL to NONE

"""


class ListNode:
    def __init__(self, value=None):
        self.value = value
        self.prev = None
        self.next = None


class DoublyLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        values = [str(node.value) for node in self]
        return '->'.join(values)

    def __iter__(self):
        tempNode = self.head
        while tempNode:
            yield tempNode
            tempNode = tempNode.next

    def createDLL(self, nodeValue):
        newNode = ListNode(nodeValue)
        newNode.prev = None
        newNode.next = None
        self.head = newNode
        self.tail = newNode
        return "DLL created successfully!"

    def insertNode(self, nodeValue, location):
        if self.head is None:
            return "No DLL to insert new node!"
        else:
            newNode = ListNode(nodeValue)
            if location == 0:
                newNode.prev = None
                newNode.next = self.head
                self.head.prev = newNode  # self.head.prev first node's prev reference pointer
                self.head = newNode
            elif location == 1:
                newNode.next = None
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode
            else:
                currNode = self.head
                index = 0
                while index < location - 1:
                    currNode = currNode.next
                    index += 1
                newNode.next = currNode.next
                newNode.prev = currNode
                newNode.next.prev = newNode  # reverse link between next node & new node
                currNode.next = newNode

    def traverseDLL(self):
        if self.head is None:
            return "No DLL exist!"
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next

    def reverseTraversalDLL(self):
        if self.head is None:
            return "No DLL exist!"
        else:
            tempNode = self.tail
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.prev

    def searchDLL(self, nodeValue):
        if self.head is None:
            return "No DLL exist!"
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodeValue:
                    return tempNode.value
                tempNode = tempNode.next
            return "No node present in DLL!"

    def deleteNode(self, location):
        if self.head is None:
            return "No DLL exist to delete node!"
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = None
            elif location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev  # to set tail with one node before last node
                    self.tail.next = None  # last node set to NONE -> to delete this by garbage co.
            else:
                currNode = self.head
                index = 0
                while index < location - 1:
                    currNode = currNode.next
                    index += 1
                currNode.next = currNode.next.next
                currNode.next.prev = currNode

    def deleteDLL(self):
        if self.head is None:
            return "There is not any node in DLL!"
        else:
            tempNode = self.head
            while tempNode:
                tempNode.prev = None
                tempNode = tempNode.next

        self.head = None
        self.tail = None
        return "Deleted DLL successfully!"


doublyLL = DoublyLL()
doublyLL.createDLL(10)
# print(doublyLL)

doublyLL.insertNode(0, 0)
doublyLL.insertNode(2, 1)
doublyLL.insertNode(6, 2)
print(doublyLL)
# doublyLL.traverseDLL()
doublyLL.reverseTraversalDLL()

# print(doublyLL.searchDLL(20))
# doublyLL.deleteNode(1)
# print(doublyLL)
# print(doublyLL.deleteDLL())
