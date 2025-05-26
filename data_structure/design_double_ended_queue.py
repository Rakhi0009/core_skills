class DoubleQueue:

    def __init__(self):
        self.dqueue = []
    
    def enqueue_rear(self,x):
        self.dqueue.append(x)
    
    def dequeue_rear(self):
        if self.dqueue:
            return self.dqueue.pop()
    
    def enqueue_front(self,x):
        self.dqueue.insert(0, x)
    
    def dequeue_front(self):
        if self.dqueue:
            return self.dqueue.pop(0)
    
    def __str__(self):
        return str(self.dqueue)
    
# Example usage
dq = DoubleQueue()
dq.enqueue_rear(1)
dq.enqueue_rear(2)
dq.enqueue_front(0)
print("Queue:", dq)