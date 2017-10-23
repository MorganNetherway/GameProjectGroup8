import movement

def draw(itemx, itemy):

    board = ""
    no_columns = 15
    no_rows = 15
    
    #count will equal column number aka y axis in grid
    
    for count in range(0,no_columns):
        #if count == itemy is checking to see if the column corresponds
        #with the item column

        if count == itemy:
            #if the item is in the last column it printed an extra |
            #i added this if statement to remove that 

            if itemx == 14:
                board += "   |" * (itemx) + " x"
                board += "  "
                board += "\n"
                board += "----" * no_columns
                board += "\n"
            else:
                board += "   |" * (itemx) + " x |" + "   |" * (15 - itemx - 2)
                board += "  "
                board += "\n"
                board += "----" * no_columns
                board += "\n"
        else:
            board += "   |" * (no_columns-1)
            board += "  "
            board += "\n"
            board += "----" * no_columns
            board += "\n"
    print(board)

        
draw(14,13)
