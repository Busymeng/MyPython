##############################################################################
##   Functional programming 
##----------------------------------------------------------------------------
"""
   * It decomposes a problem into a set of functions. 
   * Ideally, functions only take inputs and produce outputs, and don’t have 
     any internal state that affects the output produced for a given input.
   * Functional techniques common to many languages: 
     - such as lambda, map, reduce.
"""

#############################################################################
##  Python Anonymous/Lambda Function
##---------------------------------------------------------------------------
"""
   * Sometimes we need to declare a function without any name. 
     The nameless property function is called an anonymous function or 
     lambda function.
     - The reason behind the using anonymous function is for instant use, 
       that is, one-time usage. 
       
   * Normal function is declared using the def function. 
     - Whereas the anonymous function is declared using the lambda keyword.
     
   * In opposite to a normal function, a Python lambda function is a single 
     expression. 
     - But, in a lambda body, we can expand with expressions over 
       multiple lines using parentheses or a multiline string.
       
   * Syntax of lambda function:
       
       lambda: argument_list:expression
       
     - A lambda function can have any number of arguments but return 
       only one value after expression evaluation.
     - We are not required to write explicitly return statements in the 
       lambda function because the lambda internally returns expression value.
"""


## Normal function





## Lambda function





## Lambda function with arguments




##  Pass arbitary arguments and arbitary keyword arguments




# example to print even numbers 






# print even number with a lambda function





"""
   * Lambda functions are more useful when we pass a function as an argument 
     to another function. 
     - We can also use the lambda function with built-in functions such as 
       filter, map, reduce because these functions require another function 
       as an argument.
"""

"""
   filter() function in Python
   
   * In Python, the filter() function is used to return the filtered value. 
     We use this function to filter values based on some conditions.

   * Syntax of filter() function:

       filter(funtion, sequence)
       
     - where,
       function – it is responsible for performing condition checking.
       sequence – Sequence argument can be anything like list, tuple, string.
"""

# Example 1: filter() with lambda function





# Example 2: filter() work with user-defined function




# Example 3: return vowels of a string





# Example 4: Using None as a Function Inside filter()
"""
   * When None is used as the first argument to the filter() function, 
     all elements that are truthy values (gives True if converted to boolean) 
     are extracted.
"""






"""
   map() function in Python
   
   * In Python, the map() function is used to apply some functionality 
     for every element present in the given sequence and generate a new 
     series with a required modification.
     - Ex: for every element present in the sequence, perform cube operation 
       and generate a new cube list.

   * Syntax of map() function:

        map(function,sequence)
        
     - where,
       function – responsible for applied on each element of the sequence
       sequence – Sequence argument can be anything like list, tuple, string
"""

# Example 1: map() with lambda function





# Example 2: map() with built-in function





# Example 3: map() with user-defined function





"""
   reduce() function in Python

   * In Python, the reduce() function is used to minimize sequence elements 
     into a single value by applying the specified condition.

   * The reduce() function is present in the functools module; hence, we 
     need to import it using the import statement before using it.

   * Syntax of reduce() function:

        reduce(function, sequence, initializer)
"""

# Example 1: reduce() with lambda function





# Example 2: reduce() with user-defined function




# Example: reduce() with the built-in function





# useful tips


