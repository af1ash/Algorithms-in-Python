import SortTableMap.SortedTableMap as SortedTableMap


class CostPerformanceDatabase(object):
    """ Maintain a database of maximal (cost, performance) pairs. """

    def __init__(self):
        """ Create an empty database. """
        self._M = SortedTableMap()

    def best(self, c):
        """ Return (cost, performance) pair with largest cost not exceeding c.
        Return None if there is on such pair.
        """
        return self._M.find_lt(c)

    def add(self, c, p):
        """ Add new entry with cost c and performance p. """
        # determine if (c, p) is dominated by existing pair
        other = self._M.find_lt(c)
        if other is not None and other[1] >= p:
            return
        self._M[c] = p
        # and now remove any pairs that are dominated by (c, p)
        other = self._M.find_gt(c)
        while other is not None and other[1] <= p:
            del self._M[other[0]]
            other = self._M.find_gt(c)
