
class PositionalList(_DoublyLinkedBase):
    """ A sequential container of elements allowing positional access. """
    class Position:
        """ An abstraction representing the location of a single element. """
        def __init__(self, container, node):
            """ Constructor should not be invoked by user. """
            self._container = container
            self._node = node
        
        def element(self):
            """ Return the element stored at this Positions. """
            return self._node._element
        
        def __eq__(self, other):
            """ Return True if other is a Position repreesenting the same location. """
            return type(other) is type(self) and other._node is self._node
        
        def __ne__(self, other):
            """ Return True if other does not represent the same location. """
            return not (self == other)
    
    def _validate(self, p):
        """ Return position's node, or raise appropriate error if invalid. """
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type.')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._next is None:
            raise ValueError('p is no longer valid')
        return p._node
    
    def first(self):
         """ Return the first Position in the list (or None if list is empty). """
        return self.
