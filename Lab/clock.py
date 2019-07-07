###########################################################################
## clock Date
###########################################################################

class Time(object):
    
    def __init__( self, hour=0, mins=0, secs=0 ):
        """ Construct a clock using three integers. """
        self.__hour = hour
        self.__mins   = mins
        self.__secs  = secs
        
    def __repr__( self ):
        """ Return a string as the formal representation a Date. """
        out_str = "Class Time: {:02d}:{:02d}:{:02d}" \
            .format( self.__hour, self.__mins, self.__secs )
        return out_str
    
    def __str__( self ):
        """ Return a string as the formal representation a Date. """
        out_str = "{:02d}:{:02d}:{:02d}" \
            .format( self.__hour, self.__mins, self.__secs )
        return out_str
    
    def from_str( self, mystr ):

        """ Convert a string (hh:mm:ss) into a Time. """

        hour, mins, secs = [ int( n ) for n in mystr.split(":")]
            
        self.__hour = hour
        self.__mins   = mins
        self.__secs  = secs
        