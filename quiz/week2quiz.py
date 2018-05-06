'''
Insert method of LinkedList class
'''
def insert(self, data, index):
    '''
    inserts data at index position
    '''
    n = self.head
    _______ = Node(data)
    counter = 0

    while n.next != None:
        if counter == index:
            new.next = n.next
            ______.next = new
        n = n.next

'''
A common implementation of a queue, is done by using two stacks.
Since a queue has a FIFO structure, the head, which is the element removed,
is at the opposite end of the queue where we add a new element. 
Two stack implementation allow us tow "flip" the order of the elements,
hence allowing us to access the head for popping in one stack,
and last item for adding in the other stack.

Fill in blanks
'''
class Queue:
    def __init__(self):
        '''
        instantiate Queue with two stacks
        '''
        self.stack1 = []
        self.stack2 = []
    def enqueue(self, element):
        '''
        enqueue (push) new element
        '''
        self.stack1.append(element)
    def dequeue(self):
        '''
        dequeue (pop) the queue by poping the correct stack (list)
        '''
        if not self.stack2:
            while self._______:
                self.stack2.append(self._______.pop())
        return self._______.pop()

'''
Insertionsort implementation
'''

def insertion_sort(array):
    for index in range(1, len(array)):
        position = index
        cur = array[index]

        while position > 0 and array[position-1] > cur:
            # add appropriate line of code here
            # add appropriate line of code here

        array[position] = cur

    return array
