##############################################################################
##  Multi-Index and Index Hierarchy
##---------------------------------------------------------------------------- 
"""
   * While Pandas does provide Panel and Panel4D objects that natively handle 
     three-dimensional and four-dimensional data, a far more common pattern 
     in practice is to make use of hierarchical indexing (also known as 
     multi-indexing) to incorporate multiple index levels within a single 
     index. 
     
   * In this way, higher-dimensional data can be compactly represented
     within the familiar one-dimensional Series and two-dimensional 
     DataFrame objects.
"""
import numpy as np
import pandas as pd

##  A Multiply Indexed Series
"""
   * Let’s start by considering how we might represent two-dimensional data 
     within a one-dimensional Series. 
     
   * For concreteness, we will consider a series of data where each point has 
     a character and numerical key.
"""
##  (1) The bad way


# Select all values from 2010, you’ll need to do some messy 
#  (and potentially slow) munging to make it happen



##  (2) The better way: Pandas MultiIndex




##  (3) MultiIndex as extra dimension
"""
   * The unstack() method will quickly convert a multiplyindexed Series into 
     a conventionally indexed DataFrame.
"""


"""
   * Why would we would bother with hierarchical indexing at all?
     - The reason is simple: just as we were able to use multi-indexing to 
       represent two-dimensional data within a one-dimensional Series, we can 
       also use it to represent data of three or more dimensions in a Series 
       or DataFrame. 
     - Each extra level in a multi-index represents an extra dimension of 
       data; taking advantage of this property gives us much more flexibility 
       in the types of data we can represent.
"""




##  Methods of MultiIndex Creation
"""
   * The most straightforward way to construct a multiply indexed Series or 
     DataFrame is to simply pass a list of two or more index arrays to the 
     constructor.
"""


"""
   * If you pass a dictionary with appropriate tuples as keys, Pandas will 
     automatically recognize this and use a MultiIndex by default.
"""



##  (1) Explicit MultiIndex constructors
"""
   * For more flexibility in how the index is constructed, you can instead 
     use the class method constructors available in the pd.MultiIndex.
"""



"""
   * You can construct the MultiIndex directly using its internal encoding by
     passing levels (a list of lists containing available index values for 
     each level) and labels (a list of lists that reference these labels).
"""



##  (2) MultiIndex level names



##  (3) MultiIndex for columns
"""
   * In a DataFrame, the rows and columns are completely symmetric, and just 
     as the rows can have multiple levels of indices, the columns can have 
     multiple levels as well.
"""
# hierarchical indices and columns


# mock some data


# create the DataFrame




##  Indexing and Slicing a MultiIndex
"""
   * The most straightforward way to construct a multiply indexed Series or 
     DataFrame is to simply pass a list of two or more index arrays to the 
     constructor.
"""
##  (1) Multiply indexed Series



##  (2) Multiply indexed DataFrames


"""
   * You could get around this by building the desired slice explicitly using 
     Python’s builtin slice() function, but a better way in this context is 
     to use an IndexSlice object, which Pandas provides for precisely 
     this situation.
"""





##  Rearranging Multi-Indices
"""
   * One of the keys to working with multiply indexed data is knowing how to 
     effectively transform the data. 
     - There are a number of operations that will preserve all the information
       in the dataset, but rearrange it for the purposes of various 
       computations.
"""
##  (1) Sorted and unsorted indices
"""
   * Many of the MultiIndex slicing operations will fail if the index is 
     not sorted.
"""





##  (2) Stacking and unstacking indices
"""
   * It is possible to convert a dataset from a stacked multi-index to a 
     simple two-dimensional representation, optionally specifying the level 
     to use.
"""



##  (3) Index setting and resetting
"""
   * Another way to rearrange hierarchical data is to turn the index labels 
     into columns; this can be accomplished with the reset_index method.
     
   * For clarity, we can optionally specify the name of the data for the 
     column representation
"""



##  Data Aggregations on Multi-Indices
"""
   * We’ve previously seen that Pandas has built-in data aggregation methods, 
     such as mean(), sum(), and max(). 
     
   * For hierarchically indexed data, these can be passed a level parameter 
     that controls which subset of the data the aggregate is computed on.
"""



##  Index Levels


##  Now let's show how to index this! 
##  For index hierarchy we use df.loc[], if this was on the columns axis, 
##  you would just use normal bracket notation df[]. 
##  Calling one level of the index returns the sub-dataframe.



##############################################################################
##  Combining Datasets: Concat and Append
##---------------------------------------------------------------------------- 
"""
   * Some of the most interesting studies of data come from combining 
     different data sources. 
     
   * These operations can involve anything from very straightforward 
     concatenation of two different datasets, to more complicated 
     database-style joins and merges that correctly handle any overlaps 
     between the datasets.
     
   * We’ll take a look at simple concatenation of Series and DataFrames with 
     the pd.concat function.
"""
import pandas as pd




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



##  Define a function to create a DataFrame of a particular form


#### example DataFrame



##  (1) Recall: Concatenation of NumPy Arrays



##  (2) Simple Concatenation with pd.concat
"""
   * pd.concat() 
     pd.concat(objs, axis=0, join='outer', join_axes=None, ignore_index=False,
               keys=None, levels=None, names=None, verify_integrity=False,
               copy=True)
"""



##  By default, the concatenation takes place row-wise within the DataFrame 
##  (i.e., axis=0).



##  Duplicate indices
"""
   * One important difference between np.concatenate and pd.concat is that 
     Pandas concatenation preserves indices, even if the result will have 
     duplicate indices.
     
   * While repeated indices is valid within DataFrames, the outcome is often 
     undesirable. 
     - pd.concat() gives us a few ways to handle it.
"""



##  (1) Catching the repeats as an error
"""
   * If you’d like to simply verify that the indices in the result of 
     pd.concat() do not overlap, you can specify the verify_integrity flag.

   * With this set to True, the concatenation will raise an exception if 
     there are duplicate indices.
"""



##  (2) Ignoring the index
"""
   * Sometimes the index itself does not matter, and you would prefer
     it to simply be ignored. 
     
   * You can specify this option using the ignore_index flag.
"""


##  (3) Adding MultiIndex keys
"""
   * Another alternative is to use the keys option to specify a label for the 
     data sources; the result will be a hierarchically indexed series 
     containing the data.
"""


##  (4) Concatenation with joins
"""
   * In practice, data from different sources might have different sets of 
     column names, and pd.concat offers several options in this case.
     
   * By default, the join is a union of the input columns (join='outer'), 
     but we can change this to an intersection of the columns using
     join='inner'.
"""


"""
   * Another option is to directly specify the index of the remaining colums 
     using the join_axes argument, which takes a list of index objects.
"""


##  The append() method
"""
   * Because direct array concatenation is so common, Series and DataFrame 
     objects have an append method that can accomplish the same thing in 
     fewer keystrokes.
"""



"""
   * The append() method in Pandas does not modify the original object—
     instead, it creates a new object with the combined data. 
     
   * It also is not a very efficient method, because it involves creation of 
     a new index and data buffer. 
     - Thus, if you plan to do multiple append operations, it is generally 
       better to build a list of DataFrames and pass them all at once to 
       the concat() function.
"""



##############################################################################
##  Combining Datasets: Merge and Join
##---------------------------------------------------------------------------- 
"""
   * One essential feature offered by Pandas is its high-performance, 
     in-memory join and merge operations. 
     
   * If you have ever worked with databases, you should be familiar with this 
     type of data interaction.
     
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



##  Relational Algebra
"""
   * The behavior implemented in pd.merge() is a subset of what is known as 
     relational algebra, which is a formal set of rules for manipulating 
     relational data, and forms the conceptual foundation of operations 
     available in most databases.
     
   * Pandas implements several of these fundamental building blocks in the 
     pd.merge() function and the related join() method of Series and 
     DataFrames.
"""


##  Categories of Joins
"""
   * The pd.merge() function implements a number of types of joins: 
     the one-to-one, many-to-one, and many-to-many joins. 
     
   * All three types of joins are accessed via an identical call to the 
     pd.merge() interface; the type of join performed depends on the
     form of the input data.
"""

##  (1) One-to-one joins
"""
   * Perhaps the simplest type of merge expression is the one-to-one join, 
     which is in many ways very similar to the column-wise concatenation.
"""



"""
   * Notice that the order of entries in each column is not necessarily 
     maintained.
     
   * Additionally, keep in mind that the merge in general discards the index, 
     except in the special case of merges by index
"""


##  (2) Many-to-one joins
"""
   * Many-to-one joins are joins in which one of the two key columns contains 
     duplicate entries. 
     
   * For the many-to-one case, the resulting DataFrame will preserve those 
     duplicate entries as appropriate.
"""



##  (3) Many-to-many joins
"""
   * Many-to-many joins are a bit confusing conceptually, but are nevertheless 
     well defined. 
     
   * If the key column in both the left and right array contains duplicates, 
     then the result is a many-to-many merge.
"""




##  Specification of the Merge Key
"""
   * Often the column names will not match so nicely, and pd.merge() provides 
     a variety of options for handling this.
"""

##  (1) The on keyword
"""
   * Most simply, you can explicitly specify the name of the key column using 
     the on keyword, which takes a column name or a list of column names
"""


##  (2) The left_on and right_on keywords
"""
   * At times you may wish to merge two datasets with different column names; 
     for example, we may have a dataset in which the employee name is labeled 
     as “name” rather than “employee”. 
     
   * In this case, we can use the left_on and right_on keywords to specify 
     the two column names.
"""


# drop the redundant column "name"



##  (3) The left_index and right_index keywords
"""
   * Sometimes, rather than merging on a column, you would instead like to 
     merge on an index.
"""


"""
   * DataFrames implement the join() method, which performs a merge that 
     defaults to joining on indices.
"""



"""
   * If you’d like to mix indices and columns, you can combine left_index 
     with right_on or left_on with right_index to get the desired behavior.
"""



##  Specifying Set Arithmetic for Joins
"""
   * In all the preceding examples we have glossed over one important 
     consideration in performing a join: the type of set arithmetic used in 
     the join. 
     
   * This comes up when a value appears in one key column but not the other.
"""


"""
   * By default, the result contains the intersection of the two sets of 
     inputs; this is what is known as an inner join.
"""


"""
   * An outer join returns a join over the union of the input columns, and 
     fills in all missing values with NAs.
"""




##  Overlapping Column Names: The suffixes Keyword
"""
   * Finally, you may end up in a case where your two input DataFrames have 
     conflicting column names.
"""



"""
   * If these defaults are inappropriate, it is possible to specify a custom 
     suffix using the suffixes keyword.
"""


