#Memory Deck

from playingcardclass import*
from random import shuffle
from random import randrange 

class Deck:
   def __init__(self,numCards,GrandMaster):
   #If numCards is not divisible by 4 in the basic levels it will give a number of cards that is divisible by 4
      '''numCards is the number of different images that will be created in the deck (i.e 8 --> 16) because it makes 2 of each card'''
      self.cardList = []
      if GrandMaster:
         for i in numCards:
               x = randrange(1,32)
               c1 = PlayingCard(i, "")
               c2 = PlayingCard(i, "")
               self.cardList.append(c1)
               self.cardList.append(c2)
         
      else:
         suits = ["d", "c", "h", "s"]
         for s in suits:
            for i in range(numCards//4):
               x = randrange(1,13)
               c1 = PlayingCard(x + 1, s)
               c2 = PlayingCard(x + 1, s)
               self.cardList.append(c1)
               self.cardList.append(c2)
         
   def shuffle(self):
      shuffle(self.cardList)

   def dealCard(self): #takes a card from the top of the deck
      return self.cardList.pop()

def main():
   deck = Deck(8, False)
   deck.shuffle()
   deck.addPics()
   i = 1
   for card in deck.cardList:
      print(str(i) + ' ' + str(card))
      i = i + 1

   
   
if __name__== "__main__":
   main()
