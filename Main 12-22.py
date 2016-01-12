#Final Project

from playingcardclass import *
from graphics import *
from buttonclass import*
from time import *
from GridOne import *
from DeckClass import *

class Memory():

    def __init__(self): #Constructor method for the Memory Game

        self.playingDeck = Deck(18, False)
        self.playingDeck.shuffle()
        self.undrawList= []
        self.cardArray = []
        self.matchText = "It's a match!"
        self.noMatchText = "Sorry, try again."

    def gridCallOne(self, win,numCols, numRows, cardWidth, cardHeight, Deck): #works for levels one and two
        
        grid = Grid(win,0,0,numCols,numRows,cardWidth,cardHeight)

        Deck.shuffle()

        # deal the cards face down
        for y in range(numRows):
            for x in range(numCols):
                im = Image(Point(x, y), "playingcards/b1fv.gif")
                im.draw(win)

        cardsRemainingDeck = []
        self.cardArray = []
        
        for y in range(numCols):
            cardRow = []
            for x in range(numRows):
                card = Deck.dealCard()
                cardRow.append(card)
                cardsRemainingDeck.append(card)
            self.cardArray.append(cardRow)

            
                
        return self.cardArray, cardsRemainingDeck, grid
        
    def flipCard(self,x,y,win):
        
        suit = self.cardArray[x][y].getSuit()
        rank = self.cardArray[x][y].getRank()
        im = Image(Point(x, y), "playingcards/" + suit + str(rank) + ".gif")
        im.draw(win)

        return suit, rank

    def evalCards(self,suitOne,rankOne,rankTwo,suitTwo, win):
##        suitOne, rankOne = positionOne.getSuit(), positionOne.getRank()
##        suitTwo, rankTwo = positionTwo.getSuit(), positionTwo.getRank()
##
        if suitOne == suitTwo and rankOne == rankTwo:
            matchText = Text(Point(5,1), "It's a match!")
            matchText.draw(win)
            return True
        else:
            #return False
            noMatchText = Text(Point(5,2), "It's not a match!")
            noMatchText.draw(win)
            return False

    def flipBack(self,x1,y1,x2,y2,win):
        im = Image(Point(x1, y1), "playingcards/b1fv.gif")
        im.draw(win)
        im = Image(Point(x2, y2), "playingcards/b1fv.gif")
        im.draw(win)
        
        
def OpenMenu(win):

    undrawList = []
    
    prompt = Text(Point(300,200),"Welcome to Memory!")
    prompt.setSize(35)
    prompt.setTextColor("green")
    undrawList.append(prompt)
    
    prompt2 = Text(Point(300,400),"Click start to begin")
    prompt2.setSize(18)
    prompt2.setTextColor("white")
    undrawList.append(prompt2)

    win.setBackground("purple")
    prompt.draw(win)
    sleep(1)
    prompt2.draw(win)
    sleep(.1)

    startButton = Button(win, Point(300,300), 60, 45, "START")
    quitButton = Button(win, Point(600,600), 60, 45, "Quit")

    pt = win.getMouse()
    while not quitButton.isClicked(pt):    #if the quit button hasn't been clicked, commmence while loop
        #if start is clicked....
        if startButton.isClicked(pt):
            print('start clicked')
            for x in undrawList:   
                x.undraw()          #erase everything on the title screen
            startButton.undraw()
            return True         #returning true booleans the next command in the main function
        pt=win.getMouse()
    win.close()


def SecondMenu(win):

    undrawList = []

    '''Text'''
    welcome = Text(Point(300,100), "Do you have what it takes to become\
 the Grand Master?")
    welcome.draw(win)
    undrawList.append(welcome)
    #Set the word 'grandmaster' to flash multi-colored


    '''Play Buttons'''
    level1 = Button(win, Point(200,200), 60, 45, "Level 1")
    undrawList.append(level1)
    
    level2 = Button(win, Point(400,200), 60, 45, "Level 2")
    undrawList.append(level2)
    level2.deactivate()
    
    grandMaster = Button(win, Point(300,300), 160, 45, "Grand Master Level")
    undrawList.append(grandMaster)
    grandMaster.deactivate()
    
    quitButton = Button(win, Point(600,600),60,45, "Quit")
    undrawList.append(quitButton)

    pt = win.getMouse()
    while not quitButton.isClicked(pt):
        if level1.isClicked(pt):
            if levelOneGame(win)==True:
                level2.activate()
        elif level2.isClicked(pt):
            if levelTwoGame(win)==True:
                grandMaster.activate()
        elif grandMaster.isClicked(pt):
            grandMasterGame(win)
        pt = win.getMouse()
    win.close()
    
def levelOneGame(win):   #sets up a game which calls different game functions
    lvlOneDeck = Deck(8, False)
    memoryGame = Memory()
    
    g1window = GraphWin("Level One", 800,800) #
    g1window.setCoords(-1,5,6,-1)

    levelonetext = Text(Point(2.5,-.7), "Level One..")
    levelonetext.setSize(18)
    levelonetext.setTextColor('blue')
    levelonetext.draw(g1window)
    
    cardArray, playingDeck, grid = memoryGame.gridCallOne(g1window,4,4,.58,.72, lvlOneDeck)
    
    quitButton = Button(g1window, Point(4,4), .5, .6, "Quit")
                   
    click1 = g1window.getMouse() #takes the first card click
    while not quitButton.isClicked(click1):

        
        if -.5 <= click1.getX() <=3.5 and -.5 <= click1.getY() <=3.5:
            
            x1,y1 =(round(click1.getX()),round(click1.getY()))     
            card1suit, card1rank = memoryGame.flipCard(x1,y1,g1window)
            card1 = (card1suit, card1rank)
  
            click2 = g1window.getMouse()            #takes the second card click
            
            while -.5 >= click2.getX() or click2.getX()>= 3.5 or -.5 >= click2.getY() or click2.getY()>= 3.5:  #Makes sure that a click off the grid
                click2=g1window.getMouse()                                                                     #wont throw the game off.

            
            if -.5 <= click2.getX() <=3.5 and -.5 <= click2.getY() <=3.5:  
                x2,y2 =(round(click2.getX()),round(click2.getY()))                 #turns point clicks into column co-ordinates
                while (x1==x2 and y1==y2)==True:
                    click2=g1window.getMouse()
                    x2,y2 =(round(click2.getX()),round(click2.getY()))
                if -.5 <= click2.getX() <=3.5 and -.5 <= click2.getY() <=3.5:
                    x2,y2 =(round(click2.getX()),round(click2.getY()))  
                    card2suit, card2rank = memoryGame.flipCard(x2,y2,g1window)                 #flips that card over
                    card2 = (card2suit, card2rank)

            if card1 == card2:          #compares the card values, proceeds if equal.
                
                Announcement = Text(Point(3,4), "Nice, a match!") #An object to present a text message to a player
                Announcement.setSize(16)
                Announcement.setTextColor('green')
                Announcement.draw(g1window)
                playingDeck.pop()
                playingDeck.pop()

                sleep(.5)
                Announcement.undraw()
                
            elif card1 != card2: #flips the cards back over ifnot a match
                
                sleep(.5)
                memoryGame.flipBack(x1,y1,x2,y2,g1window)
                Announcement = Text(Point(3,4), "Sorry, try again.")
                Announcement.setSize(16)
                Announcement.setTextColor('red')
                Announcement.draw(g1window)
                
                sleep(.5)
                Announcement.undraw()
                    
        if len(playingDeck) == 0:
            WinMessage = Text(Point(2,4), "Congrats, You Win!")
            WinMessage.setSize(24)
            WinMessage.setFace('times roman')
            WinMessage.setTextColor('purple')
            WinMessage.draw(g1window)
            sleep(2)
            g1window.close()
            return True                

            
        click1 = g1window.getMouse()

    g1window.close()
    
def levelTwoGame(win):          # 8 x 4 Game
    levelTwoDeck = Deck(18, False)
    memoryGame = Memory()
    
    g2window = GraphWin("Level Two", 1400, 600)
    g2window.setCoords(-.5,5,8,-1)

    leveltwotext = Text(Point(2.5,-.7), "Level Two..")
    leveltwotext.setSize(18)
    leveltwotext.setTextColor('orange')
    leveltwotext.draw(g2window)

    cardArray, playingDeck = memoryGame.gridCallOne(g2window, 8, 4, .38, .82, levelTwoDeck)

    quitButton = Button(g2window, Point(5.5,4), .5, .6, "Quit")

    click1 = g2window.getMouse() #takes the first user click
    while not quitButton.isClicked(click1):
        
        if -.5 <= click1.getX() <=7.5 and -.5 <= click1.getY() <=3.5:
            
            x1,y1 =(round(click1.getX()),round(click1.getY()))     
            card1suit, card1rank = memoryGame.flipCard(x1,y1,g2window)
            card1 = (card1suit, card1rank)
  
            click2 = g2window.getMouse()            #takes the second card click

            while -.5 >= click2.getX() or click2.getX()>= 7.5 or -.5 >= click2.getY() or click2.getY()>= 3.5:  #Makes sure that a click off the grid
                click2=g2window.getMouse()                                                                     #wont throw the game off.
                
            x2,y2 =(round(click2.getX()),round(click2.getY()))            #turns point clicks into column co-ordinates  
            card2suit, card2rank = memoryGame.flipCard(x2,y2,g2window)                 #flips that card over
            card2 = (card2suit, card2rank)

            if card1 == card2:          #compares the card values.

                Announcement = Text(Point(4,4), "Nice, a match!") #An object to present a text message to a player
                Announcement.setSize(16)
                Announcement.setTextColor('green')
                Announcement.draw(g2window)
                playingDeck.pop()
                playingDeck.pop()
        

            elif card1 != card2:
                sleep(.5)
                memoryGame.flipBack(x1,y1,x2,y2,g2window)
                Announcement = Text(Point(4,4), "Sorry, try again.")
                Announcement.setSize(16)
                Announcement.setTextColor('red')
                Announcement.draw(g2window)
                    
            sleep(.5)
            Announcement.undraw()
                
        if len(playingDeck) == 0:
            WinMessage = Text(Point(2,4), "Congrats, You Win!")
            WinMessage.setSize(24)
            WinMessage.setFace('times roman')
            WinMessage.setTextColor('purple')
            WinMessage.draw(g2window)
            sleep(2)
            g2window.close()
            return True
            
        click1 = g2window.getMouse()
    g2window.close()
    
def grandMasterGame(win):        #8 x 8
    grandMasterDeck = Deck(32, False)
    memoryGame = Memory()
    
    g3window = GraphWin("GrandMaster Level", 1000, 1000)
    g3window.setCoords(-.5,12,8,-1)

    grandMastertext = Text(Point(2.5,-.7), "Grandmaster Level...Do you have what it takes?")
    grandMastertext.setSize(18)
    grandMastertext.setTextColor('firebrick3')
    grandMastertext.draw(g3window)

    cardArray, playingDeck = memoryGame.gridCallOne(g3window, 8, 8, .39, .40, grandMasterDeck)

    quitButton = Button(g3window, Point(6.5,8.5), .8, .7, "Quit")

    click1 = g3window.getMouse() #takes the first user click
    while not quitButton.isClicked(click1):
        
        if -.5 <= click1.getX() <=7.5 and -.5 <= click1.getY() <=3.5:
            
            x1,y1 =(round(click1.getX()),round(click1.getY()))     
            card1suit, card1rank = memoryGame.flipCard(x1,y1,g3window)
            card1 = (card1suit, card1rank)
  
            click2 = g3window.getMouse()            #takes the second card click

            while -.5 >= click2.getX() or click2.getX()>= 7.5 or -.5 >= click2.getY() or click2.getY()>= 3.5:  #Makes sure that a click off the grid
                click2=g3window.getMouse()                                                                     #wont throw the game off.
                
            x2,y2 =(round(click2.getX()),round(click2.getY()))            #turns point clicks into column co-ordinates  
            card2suit, card2rank = memoryGame.flipCard(x2,y2,g3window)                 #flips that card over
            card2 = (card2suit, card2rank)

            if x1 == x2 and y1 == y2:
                print('same card')

            elif card1 == card2:          #compares the card values.

                Announcement = Text(Point(3,8.5), "Nice, a match!") #An object to present a text message to a player
                Announcement.setSize(20)
                Announcement.setTextColor('green')
                Announcement.draw(g3window)
                playingDeck.pop()
                playingDeck.pop()

            elif card1 != card2:
                sleep(.5)
                memoryGame.flipBack(x1,y1,x2,y2,g3window)
                Announcement = Text(Point(3,8.5), "Sorry, try again.")
                Announcement.setSize(16)
                Announcement.setFace('times roman')
                Announcement.setTextColor('red')
                Announcement.draw(g3window)
                    
            sleep(.5)
            Announcement.undraw()
                
        if len(playingDeck) == 0:
            WinMessage = Text(Point(3,8.5), "Congrats, You Win!")
            WinMessage.setSize(24)
            WinMessage.setFace('times roman')
            WinMessage.setTextColor('purple')
            WinMessage.draw(g3window)
            sleep(2)
            g3window.close()
            return True
            
        click1 = g3window.getMouse()
    g3window.close()
    

def main():

    win = GraphWin("Memory Game", 700,700)

    if OpenMenu(win)==True:
        if SecondMenu(win)==False: #call to first level
            levelOneGame(win)

            
    
    

main()
