import csv
import string
import pylab
from operator import itemgetter

def open_file():
    ''' Comment goes here.''' 
#    fn = input("Enter a filename of the song data: ")
    fn = "songdata_small.csv"
    fp = open(fn,'r')
    return fp

def read_stopwords():
    ''' Comment goes here.''' 
#    fn = input("Enter a filename of the stop words: ")
    fn = "stopwords.txt"
    fp = open(fn,'r')
    
    sw = set()
    for line in fp:
        line = line.strip()
        sw.add(line)
        
    return sw
        

def validate_word(word, stopwords):
    ''' Comment goes here.''' 
    if word.isalpha():
        if word not in stopwords:
            return True
        else:
            return False
    return False
            

def process_lyrics(lyrics, stopwords):
    ''' Comment goes here.''' 
    lyrics = lyrics.split()
    
    nly = set()
    for w in lyrics:
        w = w.lower()
        w = w.strip(string.punctuation).strip(string.whitespace)
        if validate_word(w,stopwords):
            nly.add(w)
            
    return nly
    

def read_data(fp, stopwords):
    ''' Comment goes here.''' 
    reader = csv.reader(fp)
    next(reader)
    
    singers = {}
    for row in reader:
        singer = row[0]
        song = row[1]
        lyrics = row[2]
        lyrics = process_lyrics(lyrics,stopwords)
        update_dictionary(singers,singer,song,lyrics)
      
    return singers
        

def update_dictionary(data_dict, singer, song, words):
    ''' Comment goes here.''' 
    if singer in data_dict:
        if song not in data_dict[singer]:
            data_dict[singer][song] = words
    else:
        data_dict[singer] = {song:words}
        
def calculate_average_word_count(data_dict):
    ''' Comment goes here.''' 
    avg_dict = {}
    
    for singer, songs in data_dict.items():
        total_words = set()
        
        for song, words in songs.items():
            total_words = total_words | words
            
        avgw = len(total_words)/len(songs)
        avg_dict[singer] = avgw
        
    return avg_dict
        

def find_singers_vocab(data_dict):
    ''' Comment goes here.''' 
    vocab_dict = {}
    
    for singer, songs in data_dict.items():
        total_words = set()
        
        for song, words in songs.items():
            total_words = total_words | words
            
        vocab_dict[singer] = total_words
        
    return vocab_dict



def display_singers(combined_list):
    ''' Comment goes here.''' 
    res_list = sorted(combined_list,reverse=True,key=itemgetter(1,2))
     
    print("{:^80s}".format("Singers by Average Word Count (TOP - 10)"))
    print("{:<20s}{:>20s}{:>20s}{:>20s}".format("Singer",\
          "Average Word Count", "Vocabulary Size", "Number of Songs"))
    print('-' * 80)
    
    for i in range(10):
        if i<len(res_list):
            t = res_list[i]
            print("{:<20s}{:>20.2f}{:>20}{:>20}".format(t[0],t[1],t[3],t[2]))

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
    
    #'Enter a filename for the stopwords: '
    #'Enter a filename for the song data: '
    file = open_file()
    sw = read_stopwords()
    #print(sw)
    #singers = {}
    singers = read_data(file,sw)
    avg_dict = calculate_average_word_count(singers)
    vocab_dict = find_singers_vocab(singers)
    
    comb_list = []
    
    for singer in singers:
        singer_tup = ()
        singer_tup += (singer,)
        singer_tup += (avg_dict[singer],)
        singer_tup += (len(singers[singer]),)
        singer_tup += (len(vocab_dict[singer]),)
        comb_list.append(singer_tup)

    display_singers(comb_list)
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




          