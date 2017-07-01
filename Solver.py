class SujikoGrid(object):
    def __init__(self):
        self.BlockMap = {
            'tl':[(0,0),(0,1),(1,0),(1,1)],
            'tr':[(0,1),(0,2),(1,1),(1,2)],
            'bl':[(1,0),(1,1),(2,0),(2,1)],
            'br':[(1,1),(1,2),(2,1),(2,2)]
        }

        tl = input('What is the top left bubble value? ')
        tr = input('What is the top right bubble value? ')
        bl = input('What is the bottom left bubble value? ')
        br = input('What is the bottom right bubble value? ')

        self.BubbleVals = {
            'tl':tl,
            'tr':tr,
            'bl':bl,
            'br':br
        }

        self.Grid = [
            [None,None,None],
            [None,None,None],
            [None,None,None]
        ]

        loop = True
        while loop:
            miniloop = True
            row = input('What is the row number of known value? ')
            col = input('What is the column number of known value? ')
            val = input('What is the known value? ')
            self.UpdateGrid(row, col, val)
            #Need to create fn to populate the Grid
            while miniloop:
                check = input('Are there any other known values? (y/n) ')
                if check == 'n':
                    loop = False
                    miniloop = False
                elif check == 'y':
                    loop = True
                    miniloop = False
                else:
                    print('Not a valud response - please select y or n')
                    miniloop = True

    def UpdateGrid(self, row, col, val):
        row = int(row)-1
        col = int(col)-1
        self.Grid[row][col] = val

Solver = SujikoGrid()
print(Solver.Grid)
