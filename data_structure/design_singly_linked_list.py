# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def get(self, index: int) -> int:
        if not self.head:
            return -1
        curr = self.head
        indx = 0
        while curr:
            if indx == index:
                return curr.val
            curr = curr.next
            indx += 1
        return -1
        
    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        

    def insertTail(self, val: int) -> None:
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
        else:
            curr_node = self.head
            while curr_node.next:
                curr_node = curr_node.next
            curr_node.next = new_node

    def remove(self, index: int) -> bool:
        if not self.head:
            return False
        if index == 0:
            self.head = self.head.next
            return True
        else:
            curr_node = self.head.next
            indx = 1
            prev_node = self.head
            while curr_node:
                if indx == index:
                    prev_node.next = curr_node.next
                    return True
                prev_node = curr_node
                curr_node = curr_node.next
                indx += 1
            return False
                
    def getValues(self) -> List[int]:
        vals = []
        if not self.head:
            return vals
        else:
            curr_node = self.head
            while curr_node:
                vals.append(curr_node.val)
                curr_node = curr_node.next
            return vals
        