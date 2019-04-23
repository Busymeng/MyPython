#####################################################################
##  Case Study 2 - Translations of Hamlet
##

"""
   * In this case study, we will find and visualize summary statistics of 
     the text of different translations of Hamlet. 
   * For this case study, functions count_words_fast, read_book, and 
     word_stats are already defined as in the Case 2 Language Processing.
   * book_titles is a nested dictionary, containing book titles within 
     authors within languages, all of which are strings. These books are 
     all stored online, and are accessed throughout this case study. 
     
"""

"""
   Exercise 1
   * In this exercise, we will first read in and store each translation of 
     Hamlet.
   * Define hamlets as a pandas dataframe with columns language and text.
   * Add an if statement to check if the title is equal to 'Hamlet'.
   * Store the results from read_book(inputfile) to text.
   * Consider: How many translations are there? 
     Which languages are they translated into?
"""
hamlets =  ## Enter code here! ##
book_dir = "Books"
title_num = 1
for language in book_titles:
    for author in book_titles[language]:
        for title in book_titles[language][author]:
            if : ## Enter code here! ##
                inputfile = data_filepath+"Books/"+language+"/"+author+ \
                            "/"+title+".txt"
                text =  ## Enter code here! ##
                hamlets.loc[title_num] = language, text
                title_num += 1
                
                
"""
   Exercise 2
   * In this exercise, we will summarize the text for a single translation 
     of Hamlet in a pandas dataframe. The language and text of the first 
     translation of Hamlet in hamlets is given in the code section.
   * Find the dictionary of word frequency in text by calling 
     count_words_fast(). Store this as counted_text.
   * Create a pandas dataframe named data.
   * Using counted_text, define two columns in data:
     - word, consisting of each unique word in text.
     - count, consisting of the number of times each word in word is 
       included in the text.
"""
language, text = hamlets.iloc[0]
# Enter your code here.




"""
   Exercise 3
   * In this exercise, we will continue to define summary statistics for a 
     single translation of Hamlet. The solution code from the previous 
     section is already included here.
   * Add a column to data named length, defined as the length of each word.
   * Add another column named frequency, which is defined as follows for 
     each word in data:
     - If count > 10, frequency is frequent.
     - If 1 < count <= 10, frequency is infrequent.
     - If count == 1, frequency is unique.
"""

language, text = hamlets.iloc[0]

counted_text = count_words_fast(text)

data = pd.DataFrame({
    "word": list(counted_text.keys()),
    "count": list(counted_text.values())
})

# Enter your code here.



"""
   Exercise 4
   * In this exercise, we will summarize the statistics in data into a 
     smaller pandas dataframe. The solution code from the previous section 
     is already included here.
   * Create a pandas dataframe named sub_data including the following columns:
     - language, which is the language of the text.
     - frequency, which is a list containing the strings "frequent", 
       "infrequent", and "unique".
     - mean_word_length, which is the mean word length of each value in 
       frequency.
     - num_words, which is the total number of words in each frequency 
       category.
"""
language, text = hamlets.iloc[0]

counted_text = count_words_fast(text)

data = pd.DataFrame({
    "word": list(counted_text.keys()),
    "count": list(counted_text.values())
})

data["length"] = data["word"].apply(len)

data.loc[data["count"] > 10,  "frequency"] = "frequent"
data.loc[data["count"] <= 10, "frequency"] = "infrequent"
data.loc[data["count"] == 1,  "frequency"] = "unique"

# Enter your code here.

    
    
    
"""
   Exercise 5
   * In this exercise, we will join all the data summaries for text Hamlet 
     translation.
   * The previous code for summarizing a particular translation of Hamlet is 
     consolidated into a single function called summarize_text. Create a 
     pandas dataframe grouped_data consisting of the results of 
     summarize_text for translation of Hamlet in hamlets.
     - Use a for loop across the row indices of hamlets to assign each 
       translation to a new row.
     - Obtain the ith row of hamlets to variables using the .iloc method, and 
       assign the output to variables language and text.
     - Call summarize_text using language and text, and assign the output to 
       sub_data.
     - Use the pandas .append() function to append to pandas dataframes 
       row-wise to grouped_data.
"""    
def summarize_text(language, text):
    counted_text = count_words_fast(text)

    data = pd.DataFrame({
        "word": list(counted_text.keys()),
        "count": list(counted_text.values())
    })
    
    data.loc[data["count"] > 10,  "frequency"] = "frequent"
    data.loc[data["count"] <= 10, "frequency"] = "infrequent"
    data.loc[data["count"] == 1,  "frequency"] = "unique"
    
    data["length"] = data["word"].apply(len)
    
    sub_data = pd.DataFrame({
        "language": language,
        "frequency": ["frequent","infrequent","unique"],
        "mean_word_length": data.groupby(by = "frequency")["length"].mean(),
        "num_words": data.groupby(by = "frequency").size()
    })
    
    return(sub_data)
    
# Enter your code here.

    
    
    
"""
   Exercise 6
   * In this exercise, we will plot our results and look for differences 
     across each translation.
   * Plot the word statistics of each translations on a single plot. 
     Note that we have already done most of the work for you.
   * Consider: do the word statistics differ by translation?
"""     
colors = {"Portuguese": "green", "English": "blue", "German": "red"}
markers = {"frequent": "o","infrequent": "s", "unique": "^"}
import matplotlib.pyplot as plt
for i in range(grouped_data.shape[0]):
    row = grouped_data.iloc[i]
    plt.plot(row.mean_word_length, row.num_words,
        marker=markers[row.frequency],
        color = colors[row.language],
        markersize = 10
    )

color_legend = []
marker_legend = []
for color in colors:
    color_legend.append(
        plt.plot([], [],
        color=colors[color],
        marker="o",
        label = color, markersize = 10, linestyle="None")
    )
for marker in markers:
    marker_legend.append(
        plt.plot([], [],
        color="k",
        marker=markers[marker],
        label = marker, markersize = 10, linestyle="None")
    )
plt.legend(numpoints=1, loc = "upper left")

plt.xlabel("Mean Word Length")
plt.ylabel("Number of Words")

# show your plot using `plt.show`!    
 
    
