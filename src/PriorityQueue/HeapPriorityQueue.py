class HeapPriorityQueue(PriorityQueueBase):
    """ A min-oriented priority queue implemented with a binary heap. """

    #-------------------nonpublic behaviors------------------------------
    def _parent(self, j):
        return (j-1) // 2
    
    def _left(self, j):
        return 2*j + 1
    
    def _right(self, j):
        return 2*j + 2
    
    def _has_left(self, j):
        return self._left(j) < len(self._data)  #index beyond end of list?
    
    def _has_right(self, j):
        return self._right(j) < len(self._data) #index beyond end of list?
    
    def _swep(self, i, j):
        """ Swep the elements at indics i and j of array. """
        self._data[i], self._data[j] = self._data[j], self._data[i]
    
    def _upheap(self, j):
        parent = self._parent(j)
        if j > 0 and self._data[j] < self._data[parent]:
            self._swep(j, parent)
            self._upheap(parent)
    
    def _downheap(self, j):
        if self._has_left(j):
            left = self._left(j)
            small_child = left
            if self._has_right(j):
                right = self._right(j)
                if self._data[right] < self._data[left]:
                    small_child = right
            if self._data[small_child] < self._data[j]:
                self._swep(j, small_child)
                self._downheap(small_child)
    