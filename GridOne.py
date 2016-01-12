from graphics import *
import math
from buttonclass import*

class Grid:
    """A grid of squares/buttons"""
    def __init__(self, win, startX, startY, numCols, numRows, cardWidth, cardHeight):
        
        """initializes a 2D list of blank button objects"""          
        self.buttonMatrix = [] #Creates a blank list for ButtonMatrix
        self.numCols = numCols #Creates the numCols
        self.numRows = numRows#Creates the numRows
        for y in range(startY,numRows):#within the range of the starting y point and the number of rows
            buttonRow = [] #Blank list for button row
            for x in range(startX,numCols):#within the range of the starting x point and the number of rows
                button = Button(win, Point(x,y),cardWidth,cardHeight,"")
                buttonRow.append(button)
            self.buttonMatrix.append(buttonRow)



    def getClickPos(self, clickPt):
        
        """returns the column and row number of the button that was clicked
           assumes the point clickPt is in/on the grid"""
##        for c in range(self.numCols):
##            for r in range(self.numRows):
##                if self.buttonMatrix[r][c].isClicked(clickPt):
##                    return r,c
        x = round(clickPt.getX())
        y = round(clickPt.getY())
        return y,x

    def setSquareColor(self, x,y,color):
        """set the color of a button at the given x,y"""
        self.buttonMatrix[y][x].setColor(color)

    def setRowColor(self, rowNum,color):
        for i in range(4):
            self.buttonMatrix[rowNum][i].setColor(color)

    def setColColor(self, colNum,color):
        for i in range(4):
            self.buttonMatrix[i][colNum].setColor(color)
            
    def setNeighbors(self,midR,midC,color):
        for i in range(midR - 1, midR + 2):
            for j in range(midC - 1, midC + 2):
                if -0.5 <= i <= 3.5 and -0.5 <= j <= 3.5:
                    self.buttonMatrix[i][j].setColor(color)
    def addPics(self, pictures): #pictures is the Deck of PlayingCards

        for c in range(self.numCols):
            for r in range(self.numRows):
                self.buttonMatrix[r][c].setPicture(pictures.dealCard())
                   
    
def main():
    
    # create the application window
    win = GraphWin("Fun with 2D lists", 600, 600)
    win.setCoords(-3, 22, 22, -3)

    ##add code here that creates a quitButton
    ##(PAY ATTENTION to the win.setCoords() call above when placing your quit button)
    #quitButton = Button(win, Point(20,21),2,1,"Quit")

    grid = Grid(win,0,0,16,20,10,10)
    ##fill in the constructor for the Grid class above and then use it to create a Grid object here
    
 
    pt = win.getMouse()

    while not quitButton.clicked(pt):
        if -.5 <= pt.getX() <=3.5 and -.5 <= pt.getY() <=3.5:

                print(round(pt.getX()),round(pt.getY()))
                row,column = grid.getClickPos(pt)
                print(row,column)

                grid.setSquareColor(column,row,"blue")
                grid.setRowColor(row,"black")
                grid.setColColor(column, "red")
                grid.setNeighbors(row,column, "white")

        pt = win.getMouse()

        
  
    win.close()
    
if __name__ == "__main__":
    main()

