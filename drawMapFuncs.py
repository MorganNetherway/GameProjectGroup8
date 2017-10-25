from movement import blockedExits
board = ""

def showMap(board):
    print(board)

def drawMap(board):
    noColumns = 15
    noRows = 15

    #count will equal column number aka y axis in grid
    for count in range(0,noColumns):
        board += " * |" * (noColumns)
        board += "  "
        board += "\n"
        board += "----" * noColumns
        board += "\n"
    return(board)

def convertToMap(positionList):
    itemX = []
    itemY = []
    finalList = []

    for items in positionList:
        itemX.append(int(items.split(",")[0]))
        itemY.append(int(items.split(",")[1]))

    itemLength = len(itemY)

    for i in range(0, itemLength):
        if itemY[i] == 0:
            start = 1737
            start = start + (itemX[i]*4)
            finalList.append(start)
        elif itemY[i] == 1:
            start = 1613
            start = start + (itemX[i]*4)
            finalList.append(start)
        elif itemY[i] == 2:
            start = 1489
            start = start + (itemX[i]*4)
            finalList.append(start)
        elif itemY[i] == 3:
            start = 1365
            start = start + (itemX[i]*4)
            finalList.append(start)
        elif itemY[i] == 4:
            start = 1241
            start = start + (itemX[i]*4)
            finalList.append(start)
        elif itemY[i] == 5:
            start = 1117
            start = start + (itemX[i]*4)
            finalList.append(start)
        elif itemY[i] == 6:
            start = 1001
            start = start + (itemX[i]*4)
            finalList.append(start)
        elif itemY[i] == 7:
            start = 869
            start = start + (itemX[i]*4)
            finalList.append(start)
        elif itemY[i] == 8:
            start = 745
            start = start + (itemX[i]*4)
            finalList.append(start)
        elif itemY[i] == 9:
            start = 621
            start = start + (itemX[i]*4)
            finalList.append(start)
        elif itemY[i] == 10:
            start = 497
            start = start + (itemX[i]*4)
            finalList.append(start)
        elif itemY[i] == 11:
            start = 373
            start = start + (itemX[i]*4)
            finalList.append(start)
        elif itemY[i] == 12:
            start = 249
            start = start + (itemX[i]*4)
            finalList.append(start)
        elif itemY[i] == 13:
            start = 125
            start = start + (itemX[i]*4)
            finalList.append(start)
        elif itemY[i] == 14:
            start = 1
            start = start + (itemX[i]*4)
            finalList.append(start)
        else:
            pass
    return(finalList)

def printPlayer(positionList, board):
    positionList2 = convertToMap(positionList)
    for position in positionList2:
        if board[position] == "*":
            board = board[:position] + "P" + board[position+1:]
            return(board)
        else:
            pass

def removePlayer(board):
    lastPosition = board.index("P")
    board = board[:lastPosition] + "*" + board[lastPosition+1:]
    return(board)
    
def printWall(positionList, board):
    for position in positionList:
        if board[position] == "*":
            board = board[:position] + "#" + board[position+1:]
        else:
            pass
    return(board)

def movePlayerMap(position):
    global board

    board = removePlayer(board)
    board = printPlayer(position, board)
    return(board)

def initMap(board):
    
    board = drawMap(board)
    board = printWall(convertToMap(blockedExits), board)
    board = printPlayer(["7,0"], board)
    return(board)
    

board = initMap(board)
showMap(board)

