# button.py
# for lab 8 on writing classes
from graphics import *

class Button:

    """A button is a labeled rectangle in a window.
    It is enabled or disabled with the activate()
    and deactivate() methods. The clicked(pt) method
    returns True if and only if the button is enabled and pt is inside it."""

    def __init__(self, win, center, width, height, label):
        ## as you read through this, ask yourself:  what are the instance variables here?
        ## it would be useful to add comments describing what some of these variables are for...
        """ Creates a rectangular button, eg:
        qb = Button(myWin, centerPoint, width, height, 'Quit') """ 
        w,h = width/2.0, height/2.0
        x,y = center.getX(), center.getY()
        ## you should comment these variables...
        self.xmax, self.xmin = x+w, x-w  #Instance Variable
        self.ymax, self.ymin = y+h, y-h  #Instance Variable
        p1 = Point(self.xmin, self.ymin) 
        p2 = Point(self.xmax, self.ymax) 
        self.rect = Rectangle(p1,p2)     #Instance Variable
        self.rect.setFill('lightgray')   #Instance Variable
        self.rect.draw(win)              #Instance Variable
        self.label = Text(center, label)
        self.label.draw(win)
        self.picture = None
        self.activate() #this line was not there in class today

    def getLabel(self):
        """Returns the label string of this button."""
        return self.label.getText()

    def activate(self):
        """Sets this button to 'active'."""
        self.label.setFill('black') #color the text "black"
        self.rect.setWidth(2)       #set the outline to look bolder
        self.active = True          #set the boolean variable that tracks "active"-ness to True

    ##check 3.  complete the deactivate() method
    def deactivate(self):
        """Sets this button to 'inactive'."""
        self.label.setFill("darkgray") ##color the text "darkgray"
        self.rect.setWidth(2)          ##set the outline to look finer/thinner
        self.active = False            ##set the boolean variable that tracks "active"-ness to False

    ##check 4.  complete the clicked() method
    def isClicked(self, p):
        """Returns true if button active and Point p is inside"""
        ##your code here
        x,y = p.getX(), p.getY()
        if self.active and self.xmin < x < self.xmax:
            if self.ymin < y < self.ymax:
                return True
        return False

    def setPicture(self, playingCard):
        self.picture = playingCard
        
    def undraw(self):
        self.rect.undraw()
        self.label.undraw()

    
##def main():
##    ##check 1. create a graphical window in which to test the Button class
##    gwin = GraphWin("Button Test", 600, 600)
##    button1 = Button(gwin, Point(300,300), 100,50,"Roll Dice")
##    button1.activate()
##    button2 = Button(gwin, Point(500,500), 75, 75,"Quit")
##    button2.deactivate()
##    
##    ##check 2. test the Button constructor method...
##    ##create two Button objects, one for "Roll Dice" and the other for "Quit"
##    ##activate the Roll button
##
##
##    ##check 3. now test the deactivate() method...
##    ##deactivate the "Quit" button
##
##    pt = gwin.getMouse()
##    ##check 4. test the .clicked() method with an if statement
###    button1.isClicked(pt)
##    
##    ##(remove this test code before moving onto the next check)
##
##    ##check 5: 
##    ##loop until the "Quit" button is clicked...
##        ##if the roll button is clicked
##            ##activate the quit button
##        ##take the next mouse click
##    while not button2.isClicked(pt):
##        if button1.isClicked(pt):
##            button2.activate()
##            
##        pt = gwin.getMouse()
##        
##    #we reach this line of code when quit button is clicked b/c loop condition breaks
##    gwin.close() #so close the window, ending the program
##    
if __name__ == "__main__": 
    main()
