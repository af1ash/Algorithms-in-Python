

class LinkedQueue():
    """ FIFO Queue implementation using a singly linked list for storage. """

    class _Node():
        """ Lightweight, nonpublic class for storing a singly linked node. """
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        """ Create an empty Queue. """
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        """ Return the number of elements in the Queue. """
        return self._size

    def is_empty(self):
        """ Return True if the Queue is empty. """
        return self._size == 0

    def first(self):
        """ Return (but do not remove) the element at the top of the Queue. 
        Raise Empty exception if the Queue is empty
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._head._element

    def dequeue(self):
        """ Remove and return the element from the top of the Queue(i.e., LIFO)
        Raise Empty exception if the Queue is empty
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return answer

    def enqueue(self, e):
        """ Add elements e to the top of the Queue. """
        newest = self._Node(e, None)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        
        self._tail = newest
        self._size += 1
