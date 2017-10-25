from movement import blockedExits
from movement import gates
board = ""

def showMap(board):
    print(board)

def drawMap(board):
    noColumns = 15
    noRows = 15

    #count will equal column number aka y axis in grid
    for count in range(0,noColumns):
        board += " . |" * (noColumns)
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
    startPositions = [1737, 1613, 1489, 1365, 1241, 1117, 993, 869, 745, 621, 497, 373, 249, 125, 1]
    for i in range(0, itemLength):
        if 0 <= itemY[i] <= 14:
            start = startPositions[itemY[i]]
            start = start + (itemX[i]*4)
            finalList.append(start)
    return(finalList)

def printPlayer(positionList, board):
    positionList2 = convertToMap(positionList)
    for position in positionList2:
        if board[position] == ".":
            board = board[:position] + "P" + board[position+1:]
            return(board)
        elif board[position] == "G":
            board = board[:position] + "P" + board[position+1:]
            return(board)
        else:
            pass

def removePlayer(board):
    lastPosition = board.index("P")
    board = board[:lastPosition] + "." + board[lastPosition+1:]
    return(board)

def printWall(positionList, board):
    for position in positionList:
        if board[position] == ".":
            board = board[:position] + "#" + board[position+1:]
        else:
            pass
    return(board)

def printGate(positionList, board):
    for position in positionList:
        if board[position] == ".":
            board = board[:position] + "G" + board[position+1:]
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
    board = printGate(convertToMap(gates), board)
    board = printPlayer(["7,0"], board)
    return(board)


board = initMap(board)
#board = drawMap(board)
showMap(board)
#for ch in range(1,1860,4):
    #print(board[ch] + str(ch))
