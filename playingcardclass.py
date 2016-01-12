#playingcardclass.py
# Playing card class for Memory module

class PlayingCard:
    '''PlayingCard is a class that represents a card in a standard 52 card deck
    of playing cards. It has the following instance variables:
        rank: an int holding the rank of the card (1 == ace, 2-10 == 2-10, 11 ==
            jack, 12 == queen, 13 == king)
        suit: a string holding the suit of the card ('d' == diamonds, 'c' ==
            clubs, 'h' == hearts, 's' == spades)'''

    def __init__(self, rank, suit):
        '''Constructor - takes rank and suit'''
        #self.rank will be the variable to indicate rank
        # Assigns the rank of the card as an int 1-13 (1 == ace, 2-10 == 2-10,
        self.rank = rank # 11 == jack, 12 == queen, 13 == king)
        #self.suit will be the variable to indicate suit
        # Assigns the suit of the card as a one letter string ('d' == diamonds,
        self.suit = suit # 'c' == clubs, 'h' == hearts, 's' == spades)

    def getRank(self):
        '''Returns rank of specified PlayingCard object'''
        return self.rank

    def getSuit(self):
        '''Returns suit of specified PlayingCard object'''
        return self.suit

##    def MemValue(self):
##        '''Returns the specified PlayingCard object's value in Black Jack
##        (Ace == 1)'''
##        if self.rank > 10: # Checks if rank variable is greater than 10 (is face card)
##            return 10 # Then resets the value to ten
##        else: # If not a face card
##            return self.rank # Returns value of card
##
##    def __str__(self):
##        '''str() - Returns a string specifying the exact playing card that
##        the PlayingCard object represents.'''
##        # List of strings with indexes corresponding to the int of the rank
##        # that each string represents
##        rankslist = ['0', 'Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
##                     'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
##        # Dictionary of strings with keys corresponding to the string of the
##        # suit that each value represents
##        suitsdict = {'d':'Diamonds', 'c':'Clubs', 'h':'Hearts', 's':'Spades'}
##        # Returns a string displaying the name of the card that was inputted
##        return rankslist[self.rank] + ' of ' + suitsdict[self.suit]
