class Matrix(object):
    
    def __init__(self): # no modification is needed for this method
        """Create and initialize your class attributes."""
        self._matrix = []
        self._rooms = 0
        
    def read_file(self, fp): # fp is a file pointer
        """Build an ajacency matrix that you read from a file fp."""
        pass
    
    def __str__(self):
        """Return the matrix as a string."""
        s = ""
        pass
        return s
    
    def __repr__(self):
        """Call __str__() to return a string for displaying in the console."""
        return self.__str__()
    
    def adjacent(self, index):
        """Return the set of connecting rooms to room specified by index."""
        # Hint: only one line, return something, is needed
        pass
    
    def rooms(self):
        """Return the number of rooms"""
        # Hint: only one line, return something, is needed
        pass