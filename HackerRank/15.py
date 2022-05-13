""" Linked lists """

#Complete the insert function in your editor so that it creates
# a new Node(pass data as the node constructor argument) and inserts
#  it at the tail of the linked list referenced by the head parameter. 
#Once the new node is added, return the reference to the head node

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class Solution:
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self, head, data):
        newNode = Node(data)
        if not head:
            return newNode
        current = head
        while current.next:
            current = current.next
        current.next = newNode
        return head


mylist = Solution()
T = int(input("Enter the length of the items: "))
head = None
for i in range(T):
    data = int(input("Enter the items: "))
    head = mylist.insert(head, data)
mylist.display(head)