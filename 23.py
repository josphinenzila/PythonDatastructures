""" Write a wrapper class for the queue class similar to what we did for stack """

from collections import deque

class Queue():
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)
    
    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.popleft()
        else:
            return None
    
    def get_size(self):
        if len(self.queue) > 0:
            return self.queue[len(self.queue) - 1]
        else:
            return None

    def __str__(self):
        return str(self.queue)


""" Test code for queue """
my_queue = Queue()
my_queue.enqueue(5)
my_queue.enqueue(10)
print(my_queue)
print(my_queue.get_size())
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())




