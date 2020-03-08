import csv
import string
import pylab
from operator import itemgetter

def open_file(message):
    ''' Comment goes here.''' 
    pass 
    #"File is not found! Try Again!"

def read_stopwords(fp):
    ''' Comment goes here.''' 
    pass
        

def validate_word(word, stopwords):
    ''' Comment goes here.''' 
    pass

def process_lyrics(lyrics, stopwords):
    ''' Comment goes here.''' 
    pass

def read_data(fp, stopwords):
    ''' Comment goes here.''' 
    pass

def update_dictionary(data_dict, singer, song, words):
    ''' Comment goes here.''' 
    pass
        
def calculate_average_word_count(data_dict):
    ''' Comment goes here.''' 
    pass

def find_singers_vocab(data_dict):
    ''' Comment goes here.''' 
    pass

def display_singers(combined_list):
    ''' Comment goes here.''' 
    pass
    #"{:^80s}".format("Singers by Average Word Count (TOP - 10)")
    #"{:<20s}{:>20s}{:>20s}{:>20s}".format("Singer","Average Word Count", "Vocabulary Size", "Number of Songs")
    #'-' * 80

def vocab_average_plot(num_songs, vocab_counts):
    """
    Plot vocab. size vs number of songs graph
    num_songs: number of songs belong to singers (list)
    vocab_counts: vocabulary size of singers (list)
        
    """       
    pylab.scatter(num_songs, vocab_counts)
    pylab.ylabel('Vocabulary Size')
    pylab.xlabel('Number of Songs')
    pylab.title('Vocabulary Size vs Number of Songs')
    pylab.show()

def search_songs(data_dict, words):
    ''' Comment goes here.''' 
    pass

def main():
    ''' Comment goes here.''' 
    pass
    #'Enter a filename for the stopwords: '
    #'Enter a filename for the song data: '
    #'Do you want to plot (yes/no)?: '

#    RULES = """1-) Words should not have any digit or punctuation
#2-) Word list should not include any stop-word"""
                
    #"Search Lyrics by Words"
    #"Input a set of words (space separated), press enter to exit: "
    #'Error in words!'
    #"There are {} songs containing the given words!"
    #"{:<20s} {:<s}"

if __name__ == '__main__':
    main()           
