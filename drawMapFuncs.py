board = ""
blockedExits = [
    "0,14", "0,13", "0,12", "0,11",
    "1,14", "1,12", "1,11", "1,9", "1,5", "1,3", "1,1",
    "2,14", "2,9", "2,7", "2,5", "2,4", "2,3", "2,2", "2,1",
    "3,14", "3,12", "3,11", "3,9", "3,5", "3,2", "3,1",
    "4,14", "4,12", "4,11", "4,9", "4,8", "4,6", "4,5",
    "5,14", "5,12", "5,11", "5,9", "5,5", "5,4", "5,3", "5,2", "5,0",
    "6,5", "6,2", "6,0",
    "7,11", "7,9", "7,5", "7,4", "7,2",
    "8,14", "8,12", "8,11", "8,9", "8,8", "8,6", "8,5", "8,2", "8,0",
    "9,11", "9,6", "9,5", "9,4", "9,0",
    "10,13", "10,11", "10,9", "10,8", "10,7", "10,6", "10,5", "10,4", "10,2", "10,1", "10,0",
    "11,11", "11,9", "11,8", "11,7", "11,6", "11,5", "11,4", "11,2", "11,1", "11,0",
    "12,13", "12,12", "12,11", "12,5", "12,1",
    "13,13", "13,12", "13,9", "13,8",
    "14,9", "14,8", "14,7", "14,6", "14,5", "14,1"
]

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
