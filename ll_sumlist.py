# Given two numbers represented by two linked list, 
# print the sum list. The sum list is linked list representation of the addition of two input numbers.



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
class LinkedList:
    def __init__(self):
        self.head = None
 
    def push(self,data):
        if self.head is None:
            self.head=Node(data)
        else:
            cur_node= self.head
            while cur_node.next !=None:
                cur_node= cur_node.next
            cur_node.next=Node(data)
 
    def addTwoLists(self, first, second):
        prev = None
        temp = None
        carry = 0

        while(first is not None or second is not None):
 
            fdata = 0 if first is None else first.data
            sdata = 0 if second is None else second.data
            Sum = carry + fdata + sdata
 
            carry = 1 if Sum >= 10 else 0

            Sum = Sum if Sum < 10 else Sum % 10
 
    
            temp = Node(Sum)

            if self.head is None:
                self.head = temp
            else:
                prev.next = temp
 
            prev = temp
            if first is not None:
                first = first.next
            if second is not None:
                second = second.next
 
        if carry > 0:
            temp.next = Node(carry)
 
    def printrev(self, temp):
          
        if temp:
            self.printrev(temp.next)
            print(temp.data, end = '')
        else:
            return 

        
first = LinkedList()
second = LinkedList()
n1=int(input())
while n1>0:
    first.push(n1%10)
    n1=n1//10

# first.printrev(first.head)
n2=int(input())
while n2>0:
    second.push(n2%10)
    n2=n2//10

# second.printrev(second.head)

res = LinkedList()
res.addTwoLists(first.head, second.head)
res.printrev(res.head)