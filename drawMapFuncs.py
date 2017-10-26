from movement import blockedExits
from movement import gates

#initialise board var - this is the string that will
#contain the map
board = ""

#passes board in and prints it out
#used to print final board
def showMap(board):
    print(board)

#the map we are using is 15x15
def drawMap(board):
    noColumns = 15
    noRows = 15

    #count will equal column number aka x axis in grid
    for count in range(0,noColumns):
        board += " . |" * (noColumns)
        board += "  "
        board += "\n"
        board += "----" * noColumns
        board += "\n"
    return(board)

#as the board is a string this function
#takes in a position "x,y" and converts it to
#an index in the board string 
def convertToMap(positionList):
    itemX = []
    itemY = []
    finalList = []

    #["item1x,item1y","item2x,item2y"]
    #adds to x list and y list and changes to int
    #to perform math functions later
    for items in positionList:
        itemX.append(int(items.split(",")[0]))
        itemY.append(int(items.split(",")[1]))

    #the number of items in x and y
    itemLength = len(itemY)
    #startPositions is the index of the first position
    #on each row of the map (index in board string)
    #eg board[1737] = ., board[1613] = .
    startPositions = [1737, 1613, 1489, 1365, 1241, 1117, 993, 869, 745, 621, 497, 373, 249, 125, 1]
    #iterate through items in list
    for i in range(0, itemLength):
        #the y coordinate it between 0,14
        if 0 <= itemY[i] <= 14:
            #the position reference in the game means
            #that the bottom left corner of the map is
            #(0,0) as oppose to top left being (0,0)
            #if y coordinate = 0, then start = 1737
            #if y coordinate = 14, then start = 1
            start = startPositions[itemY[i]]
            #the .s on the map are printed ever 4 characters
            #the x value*4 is how many columns in the * should be
            start = start + (itemX[i]*4)
            #add this int to a list of positions of .s
            finalList.append(start)
    return(finalList)

#passes in a list which contains player position ["x,y"]
def printPlayer(positionList, board):
    positionList2 = convertToMap(positionList)
    for position in positionList2:
        #makes sure that the position is actually free to move to
        if board[position] == ".":
            #print the board up until the point of inserting
            #"P" = player, insert P then concat rest of board string
            board = board[:position] + "P" + board[position+1:]
            return(board)
            #"G" = gate, the player can be on a gate position
            #but the map should print player instead of gate
        elif board[position] == "G":
            board = board[:position] + "P" + board[position+1:]
            return(board)
        else:
            pass
#this function removes the previous player marker from map
#called when updating marker
def removePlayer(board):
    lastPosition = board.index("P")
    board = board[:lastPosition] + "." + board[lastPosition+1:]
    return(board)
#used to print walls on map
#repreesented by #
def printWall(positionList, board):
    for position in positionList:
        if board[position] == ".":
            board = board[:position] + "#" + board[position+1:]
        else:
            pass
    return(board)
#used to print gates on map
#repreesented by #
def printGate(positionList, board):
    for position in positionList:
        if board[position] == ".":
            board = board[:position] + "G" + board[position+1:]
        else:
            pass
    return(board)
#this function is called to move the player marker
#it removes the player marker
#then sets a the updated version
def movePlayerMap(position):
    global board

    board = removePlayer(board)
    board = printPlayer(position, board)
    return(board)
#called at teh start of the program
#["7,0"] is hard coded as start
def initMap(board):
    board = drawMap(board)
    board = printWall(convertToMap(blockedExits), board)
    board = printGate(convertToMap(gates), board)
    board = printPlayer(["7,0"], board)
    return(board)


board = initMap(board)
showMap(board)
