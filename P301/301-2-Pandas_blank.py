##############################################################################
##  Introduction to Pandas
##---------------------------------------------------------------------------- 
"""
   * We will learn how to use pandas for data analysis. 
     You can think of pandas as an extremely powerful version of Excel, 
     with a lot more features. 
     
   * We will cover:
     - Series
     - DataFrames
     - Missing Data
     - GroupBy
     - Merging,Joining,and Concatenating
     - Operations
     - Data Input and Output
"""
##############################################################################
##  Series
##----------------------------------------------------------------------------
"""
   * The first main data type we will learn about for pandas is the Series 
     data type. Let's import Pandas and explore the Series object.
   
   * A Series is very similar to a NumPy array (in fact it is built on top of 
     the NumPy array object). 
   
   * What differentiates the NumPy array from a Series, is that a Series can 
     have axis labels, meaning it can be indexed by a label, instead of just 
     a number location. 
     
   * It also doesn't need to hold numeric data, it can hold any arbitrary 
     Python Object.
"""
import numpy as np
import pandas as pd

##  Creating a Series
##  You can convert a list,numpy array, or dictionary to a Series:





##  Using Lists




##  NumPy Arrays




##  Dictionary




##  Data in a Series
"""
   * A pandas Series can hold a variety of object types.
"""



##  Even functions (although unlikely that you will use this)




## Using an Index
"""
   * The key to using a Series is understanding its index. 
   * Pandas makes use of these index names or numbers by allowing for fast 
     look ups of information (works like a hash table or dictionary).
"""



##  Operations are then also done based off of index:




##############################################################################
##  DataFrames
##---------------------------------------------------------------------------- 
"""
   * DataFrames are the workhorse of pandas and are directly inspired by 
     the R programming language. 
     
   * We can think of a DataFrame as a bunch of Series objects put together 
     to share the same index. 
"""



##############################################################################
##  Selection and Indexing
##---------------------------------------------------------------------------- 
"""
   * Let's learn the various methods to grab data from a DataFrame. 
"""



##  Pass a list of column names



##  SQL Syntax (NOT RECOMMENDED!)



##  DataFrame Columns are just Series



##  Creating a new column


##  Removing Columns


##  Not inplace unless specified!


##  Can also drop rows this way:

    
##  Selecting Rows


##  Or select based off of position instead of label 


##  Selecting subset of rows and columns 



##############################################################################
##  Conditional Selection
##---------------------------------------------------------------------------- 
"""
   * An important feature of pandas is conditional selection using bracket 
     notation, very similar to numpy.
"""



##  For two conditions you can use | and & with parenthesis:

    
##############################################################################
##  More Index Details
##---------------------------------------------------------------------------- 
"""
   * Let's discuss some more features of indexing, including resetting the 
     index or setting it something else. 
     
   * We'll also talk about index hierarchy.
"""



##  Reset to default 0,1...n index




##############################################################################
##  Multi-Index and Index Hierarchy
##---------------------------------------------------------------------------- 
"""
   * Let us go over how to work with Multi-Index, first we'll create a quick 
     example of what a Multi-Indexed DataFrame would look like.
"""

##  Index Levels



##  Now let's show how to index this! 
##  For index hierarchy we use df.loc[], if this was on the columns axis, 
##  you would just use normal bracket notation df[]. 
##  Calling one level of the index returns the sub-dataframe.




##############################################################################
##  Missing Data
##---------------------------------------------------------------------------- 
"""
   * Let's show a few convenient methods to deal with Missing Data in pandas.
"""




##############################################################################
##  Groupby
##---------------------------------------------------------------------------- 
"""
   * The groupby method allows you to group rows of data together and call 
     aggregate functions.
"""


##  Create dataframe



##  Now you can use the .groupby() method to group rows together based off 
##  of a column name. 
"""
   * For instance let's group based off of Company. 
   * This will create a DataFrameGroupBy object.
"""



##  You can save this object as a new variable:

    
##  And then call aggregate methods off the object:

    
##  More examples of aggregate methods:

    


##############################################################################
##  Merging, Joining, and Concatenating
##---------------------------------------------------------------------------- 
"""
   * There are 3 main ways of combining DataFrames together: Merging, Joining 
     and Concatenating. 
"""



##############################################################################
##  Concatenation
##---------------------------------------------------------------------------- 
"""
   * Concatenation basically glues together DataFrames. 
   
   * Keep in mind that dimensions should match along the axis you are 
     concatenating on. 
     
   * You can use pd.concat() and pass in a list of DataFrames to concatenate 
     together. 
"""



##############################################################################
##  Merging
##---------------------------------------------------------------------------- 
"""
   * The merge() function allows you to merge DataFrames together using a 
     similar logic as merging SQL Tables together. 
"""

##  Example DataFrames





##  Or to show a more complicated example:

    



##############################################################################
##  Joining
##---------------------------------------------------------------------------- 
"""
   * Joining is a convenient method for combining the columns of two 
     potentially differently-indexed DataFrames into a single result DataFrame. 
"""




##############################################################################
##  Operations
##---------------------------------------------------------------------------- 
"""
   * There are lots of operations with pandas that will be really useful to 
     you, but don't fall into any distinct category.
"""



##  Info on Unique Values




##  Selecting Data
##  Select from DataFrame using criteria from multiple columns



##  Applying Functions





##  Permanently Removing a Column


##  Get column and index names


##  Sorting and Ordering a DataFrame


##  Find Null Values or Check for Null Values



##  Drop rows with NaN Values



##  Filling in NaN values with something else




##############################################################################
##  Data Input and Output
##---------------------------------------------------------------------------- 
"""
   * This notebook is the reference code for getting input and output, 
     pandas can read a variety of file types using its pd.read_ methods. 
"""
import numpy as np
import pandas as pd

## CSV
##   CSV Input


##   CSV Output


##  Excel
"""
   * Pandas can read and write excel files, keep in mind, this only imports 
     data. 
     
   * Not formulas or images, having images or macros may cause this read_excel 
     method to crash. 
"""

##    Excel Input

##    Excel Output


##  HTML
"""
   * You may need to install htmllib5,lxml, and BeautifulSoup4. 
   
   * In your terminal/command prompt run:
 
       conda install lxml
       conda install html5lib
       conda install BeautifulSoup4
 
     Then restart Jupyter Notebook.
     (or use pip install if you aren't using the Anaconda Distribution)

   * Pandas can read table tabs off of html. 
"""

##    HTML Input
"""
   * Pandas read_html() function will read tables off of a webpage and return 
     a list of DataFrame objects.
"""


##  SQL (Optional)
"""
   * The pandas.io.sql module provides a collection of query wrappers to 
     both facilitate data retrieval and to reduce dependency on DB-specific 
     API. 
     
   * Database abstraction is provided by SQLAlchemy if installed. 
   
   * In addition you will need a driver library for your database. 
     - Examples of such drivers are psycopg2 for PostgreSQL or 
       pymysql for MySQL. 
     - For SQLite this is included in Python’s standard library by default. 
       You can find an overview of supported drivers for each SQL dialect in 
       the SQLAlchemy docs.

   * If SQLAlchemy is not installed, a fallback is only provided for sqlite 
     (and for mysql for backwards compatibility, but this is deprecated and 
     will be removed in a future version). 
     
   * This mode requires a Python database adapter which respect the 
     Python DB-API.
 
   * The key functions are:
     - read_sql_table(table_name, con[, schema, ...])	
       > Read SQL database table into a DataFrame.
     - read_sql_query(sql, con[, index_col, ...])	
       > Read SQL query into a DataFrame.
     - read_sql(sql, con[, index_col, ...])	
       > Read SQL query or database table into a DataFrame.
     - DataFrame.to_sql(name, con[, flavor, ...])	
       > Write records stored in a DataFrame to a SQL database.
"""
