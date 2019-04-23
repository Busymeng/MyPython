##############################################################################
##  Introduction to Language Processing
##
"""
   * Patterns within written text are not the same across all authors or 
     languages.

   * This allows linguists to study the language of origin or potential 
     authorship of texts where these characteristics are not directly known 
     such as the Federalist Papers of the American Revolution.
     
   * We will examine the properties of individual books in a book collection 
     from various authors and various languages.
     - More specifically, we will look at book lengths, number of unique words,
       and how these attributes cluster by language of or authorship.
       
   * Project Gutenberg is the oldest digital library of books.
     - It aims to digitize and archive cultural works, and at present,
       contains over 50,000 books, all previously published and now available 
       electronically.

   * We have downloaded a collection of over 100 titles from Project Gutenberg 
     for analysis as a sample library for this case study.

   * The downloaded sample consist of several nested folders.
     - At the top level, we have four languages: English, French, German,
       and Portuguese.
     - For each language, we have from one to four authors each, 13 authors 
       in total.
     - For each author, we have from 1 to 16 books, 102 books in total.
     - Some authors have appeared in several language categories
       because their books are available as translations in several languages.

   * Our goal is to write a function that given a string of text counts 
     the number of times each unique word appears.
     - What's the best way to keep track of these words?
     
   * Because we'd like to associate each word with a counter, 
     Python dictionaries are a very natural choice.
     - Here, the keys are strings, the words containing the input text,
       and the values are numbers that counts indicating how many times
       each word appears in the text.
       
   * Download the Gutenburg book files into a Books folder.
"""
#-----------------------------------------------------------------------------

##############################################################################
##  Counting Words
##
"""
   * Looking at the dictionary, one obvious shortcoming of our current routine
     is that it includes punctuation like periods, or full stops, as part of 
     the word.
     - This would lead to an inflation of the word count because, for example, 
       a word that appears in the middle of the sentence will be counted 
       separately from the same word if it appears at the end of a sentence 
       and is immediately followed by a period.
       
   * Another problem is that if the word appears at the beginning of a 
     sentence, its first letter is capitalized, again giving rise to double 
     counting of some words.            
"""
#-----------------------------------------------------------------------------
text = "This is my test text. " + \
       "We're keeping this text short to keep things managable."
       



#-----------------------------------------------------------------------------
text = "This is my test text. " + \
       "We're keeping this text short to keep things managable."
       

    
#-----------------------------------------------------------------------------   
"""
   * Counting the frequency of objects is such a common operation that Python 
     provides what is known as a counter tool to support rabbit tallies.
     - We first need to import it from the collections module, which
       provides many additional high performance data types.
     - The object returned by counter behaves much like a dictionary,
       although strictly speaking it's a subclass of the Python dictionary
       object.
"""
#-----------------------------------------------------------------------------

    
    
##############################################################################
##  Reading in a Book
##
"""
   * Write a function to read in a book file.           
"""
#-----------------------------------------------------------------------------    

    
##############################################################################
##  Computing Word Frequency Statistics
##
"""
   * Learn how to compute some basic word frequency statistics.
   
   * Given a dictionary or a counter object from the collections module,
     we would like to know how many unique words there are in a given book.
     - We'd also like to return the frequencies of each word, meaning,
       count-specifying how many times each word has appeared.
   
   * Use the word_stats function to compare different translations of the 
     same book.        
     
"""
#-----------------------------------------------------------------------------     
    




##############################################################################
##  Reading Multiple Files
##
"""
   * Learn how to navigate file directories and read in multiple files/books 
     at once
     - We will use os module

   * Get a brief introduction to pandas, which provides additional data 
     structure and data analysis functionalities for Python.   
     - It's especially useful for manipulating numerical tables and time 
       series data.
     - pandas gets its name from the term panel data and used to refer to 
       multi-dimensional structured data sets.
     
"""
#----------------------------------------------------------------------------- 



#-----------------------------------------------------------------------------
"""
   * Get a brief introduction to pandas, which provides additional data 
     structure and data analysis functionalities for Python.   
     - It's especially useful for manipulating numerical tables and time 
       series data.
     - pandas gets its name from the term panel data and used to refer to 
       multi-dimensional structured data sets.    
"""
#-----------------------------------------------------------------------------



#-----------------------------------------------------------------------------




#-----------------------------------------------------------------------------
"""
   * Try to make the author start with uppercase lstter and get rid of .txt
     in the title.
"""
#-----------------------------------------------------------------------------



##############################################################################
##  Plotting Book Statistics
##
"""
   * Learn how to use matplotlib.pyplot to plot the book length and unique 
     word statistics computed in previous example.
     
"""
#-----------------------------------------------------------------------------     

