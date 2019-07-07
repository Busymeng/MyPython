##############################################################################
##  Lab#12 Operator Overloading Solution
##----------------------------------------------------------------------------

class Vector(object):
    
    def __init__(self, x = 0.0, y = 0.0):
        """ Construct a vector using 2 values. """
        self.x = x
        self.y = y
        
    def __repr__(self):
        """ Return a string as the formal representation a Date. """
        out_str = "Vector : ({:1.2f}, {:1.2f})".format(self.x, self.y)
        return out_str
    
    def __str__(self):
        """ Return a string as the formal representation. """
        out_str = "The vector is ({:1.2f}, {:1.2f})".format(self.x, self.y)
        return out_str
    
    def __add__(self, v):
        return Vector(self.x+v.x, self.y+v.y)
    
    def __sub__(self, v):
        return Vector(self.x-v.x, self.y-v.y)
    
    def __mul__(self,rhs):
        if isinstance(rhs, float):
            x = self.x * rhs
            y = self.y * rhs
            return Vector(x,y)
        if isinstance(rhs, Vector):
            x = self.x * rhs.x
            y = self.y * rhs.y
            return x+y
    
    def __rmul__(self,rhs):
        #print("In radd")
        return self.__mul__(rhs)
    
    def __eq__(self, v):
        return self.x==v.x and self.y==v.y
    
    def magnitude(self):
        import math
        return math.sqrt(self.x**2.0 + self.y**2.0)
    
    def unit(self):
        import math
        mag = self.magnitude()
        try:
            return Vector(self.x/mag,self.y/mag)
        except ZeroDivisionError:
            print("Cannot convert zero vector to a unit vector.")
  
    
    
    
v1 = Vector()
v2 = Vector(1,2)
v1
v2
v3 = v1 + v2
v3
v4 = v1 - v2
v4
v5 = v4 * 2.0
v6 = v4 * v5
v6
v7 = v5 * v4
v7
v8 = 1.2 * v1
v8

v1 == v8
v8 == v1

v1.magnitude()
Vector(3,4).magnitude()
v9 = Vector(3,4).unit()
v9
v9.magnitude()
v1.unit()
