
import string
from operator import itemgetter


def add_word( word_map, word ):

    if word not in word_map:
        word_map[ word ] = 0

    word_map[ word ] += 1


def build_map( in_file, word_map ):

    for line in in_file:
        word_list = line.split()
        for word in word_list:
            word = word.strip().strip(string.punctuation)
            # Answer (b)
            word = word.lower()
            # Answer (a)
            if word=="":
                continue
            add_word( word_map, word )
        

def display_map( word_map ):

    word_list = list()

    for word, count in word_map.items():
        word_list.append( (word, count) )

    freq_list = sorted( word_list, key=itemgetter(1) )

    print( "\n{:15s}{:5s}".format( "Word", "Count" ) )
    print( "-"*20 )
    for item in freq_list:
        print( "{:15s}{:>5d}".format( item[0], item[1] ) )


def open_file():

    try:
        in_file = open( "document1.txt", "r" )
        
    except IOError:
        print( "\n*** unable to open file ***\n" )
        in_file = None

    return in_file


word_map = dict()
in_file = open_file()

if in_file != None:

    build_map( in_file, word_map )
    display_map( word_map )
    in_file.close()


