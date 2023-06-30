##############################################################################
##  OOP - Inheritance
##############################################################################

##############################################################################
## Class Inheritance
"""
   * Three main factors of Object-Oriented Programming:
     - Encapsulation
     - Inheritance
     - Polymorphism
     
   * When we make a class, we indicate the class parent class in parenthesis.
"""



"""
   * By parent class, we meant that we create a hirarchy, an arrangement of 
     classes in a kind of pyramid.
     - The top of the pyramid is the most general classes. It is object class.
                                  
                                  object
               parent class          |               child class
                   ^              MyClass                  |
                   |               /   \                   |
                   |        SubClass  Sub2Class            |
                   |           |                           V
                            SubSubClass 
     
   * The implementation is that classes "higher" in the hirarchy are more 
     general, and those "lower" are more specific, specialization.                          
                              
"""



##############################################################################
##  The find-the-method game
"""
   * Imposing an ordering on classes is interesting. The last piece of puzzle
     is what we call the find-the-method game.
     
   * We know that:
     - Every instance knows which class it was created from. It is stored in
       the instance __class__ attribute.
     - To find an attribute, Python
       > first look in the instance itself for the attribute
       > if the attribute is not in the instance, Python then looks in the
         instance's class for the attribute
         
   * We add a third element,
     - If the attribute is not in the instance and not in the instance's 
       class, then look to the parent class of the instance's class and
       see if the attribute is there.
     - Continue searching classes up the hirarchy, as defined by the class
       definition, until you find the attribute, or upon hitting object.
       Python dicovers there is no such attribute and generate an error.
       
   * Typically, an instance does not have a local copy of a method.
     The instance's class holds the methods, so that all instances of a 
     class share the same methods.
     
   * However, now it is possible to define only some methods in a class 
     and allow the find-the-method game to discover other, already existing
     methods, in parent classses.
"""


##############################################################################
##  Power of Inheritance
"""
   * You are working with a team to develop a graphic display system for
     your company's product. The graphics system allows developers to
     draw figures (triangle, rectangle, circles, etc) to the screen so that
     they can demonstrate the product's capabilities.
     - All the graphics elements are written in classes.
     
   * You are given the task of making a new class, a LableRectangle class. 
     How are you approach this?
     
     (1) You could write a new class from scratch. 
         But that would be a terrible waste of time. There is already a 
         Rectangle class that draws everything except the label that is 
         required.
         
     (2) You could modify the existing Rectangle class.
         But that means that people who already use the classes have to 
         deal with your new label stuff. Plus, you might make an error of the
         changes. That would be bad.
         
     (3) The third alternative is to use inheritance.
         Make a new class, LabelRectangle as a subclass of the existing 
         Rectangle class. Have the new class inherit all the elements of 
         Rectangle, and change only those parts of the drawing involving
         the label in the new class.
         
   * Advantages:
     (1) Your new changes only affect the new class. The existing classes are
         not modified.
     (2) You inherit all the elements of the parent class. If someone updates
         the parent, you inherit those changes automatically.
         
   * Bottom line:
     - Inheritance allows a group of developers to share codes, as well as 
       create new code, in a consistent, unified manner!
"""
##############################################################################
##  "object" class
"""
   * Every class in Python is descended from the object class.
   * If no inheritance is specified when a class is defined, its superclass 
     is object by default.
   * All methods defined in the object class are special methods.
     - __new__() method
       . This is automatically invoked when an object is constructed. 
       . This method then invokes the __init__() method to initialize the 
         object. 
       . Normally you should only override the __init__() method to 
         initialize the data fields defined in the new class.
    
     - __str__() method 
       . It returns a string description for the object. 
       . By default, it returns a string consisting of a class name of which 
         the object is an instance and the object’s memory address in 
         hexadecimal format.
       . Usually you should override the __str__() method so that it returns 
         an informative description for the object.
    - __eq__(other) method 
      . It returns True if two objects are the same. 
      . So, x.__eq__(x) is True, but x.__eq__(y) returns False, because 
        x and y are two different objects even though they may have the 
        same contents.
"""

##############################################################################
##  Inheritance issues
"""
   * Unbound methods
"""




"""
   * When a method is called using the dot-call method, we say the method is
     bound to the class. For a bound method, Python automatically does the
     binding of the calling instance to self.
     
   * However, there are times when we, the programmers need to determine 
     what self is and we pass to the method that particular instance we want.
     In so doing we are making an unbound call.
"""

##  We determine what instance to pass to method



##############################################################################
##  A Class Hirarchy
##----------------------------------------------------------------------------




##----------------------------------------------------------------------------


##############################################################################
##  Subclassing Built-in Types
"""
   * Existing classes are objects and can be subclassed.
"""
##----------------------------------------------------------------------------




##############################################################################
##  Polymorphism and Dynamic Binding
"""
   * Polymorphism means that an object of a subclass can be passed to a 
     parameter of a superclass type. 
   * A method may be implemented in several classes along the inheritance 
     chain. 
     - Python decides which method is invoked at runtime. 
     - This is known as dynamic binding.
"""

##--------- GeometricObject.py -----------------------------------------------




##-------- CircleFromGeometricObject.py --------------------------------------


        
        
##------ RectangleFromGeometricObject.py -----------------------------------




##---------- PolymorphismDemo.py ----------------------------------------------------


