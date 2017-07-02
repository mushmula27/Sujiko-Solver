class Sujiko_Grid(object):
    def __init__(self):
        self.block_map = {
            'tl': [(0, 0), (0, 1), (1, 0), (1, 1)],
            'tr': [(0, 1), (0, 2), (1, 1), (1, 2)],
            'bl': [(1, 0), (1, 1), (2, 0), (2, 1)],
            'br': [(1, 1), (1, 2), (2, 1), (2, 2)]
        }

        tl = input('What is the top left target number? ')
        tr = input('What is the top right target number? ')
        bl = input('What is the bottom left target number? ')
        br = input('What is the bottom right target number? ')

        self.center_vals = {
            'tl': int(tl),
            'tr': int(tr),
            'bl': int(bl),
            'br': int(br)
        }

        self.grid = [
            [None, None, None],
            [None, None, None],
            [None, None, None]
        ]
        self.min_val = 1
        self.max_val = len(self.grid) * len(self.grid[0])

        loop = True

        while loop:
            print('\n')
            cont = input('Are there more known numbers? (yes/no/y/n): ')
            if(cont == 'no' or cont == 'n'):
                loop = False
                break

            i_coord = input('What is the ith coord of the known number? ')
            j_coord = input('What is the jth coord of the known number? ')
            num = input('What is the number at (' + i_coord + ', ' + j_coord + ')? ')
            i_coord = int(i_coord) - 1
            j_coord = int(j_coord) - 1
            num = int(num)
            self.update_cell(i_coord, j_coord, num)
            more = input('Are there more known numbers? (yes/no/y/n): ')
            if(more == 'yes' or more == 'y'):
                loop = True
            elif(more == 'no' or more == 'n'):
                loop = False
            else:
                print('Not a valid response, try again')

    def update_cell(self, i, j, num):
        self.grid[i][j] = num

    def find_block_sum(self, block):
        coords = self.block_map[block]
        if not coords:
            return False

        sum = 0
        for coord in coords:
            num = self.grid[coord[0]][coord[1]]
            if not num:
                return False
            sum = sum + num;
        return sum

    def compare_block_to_center(self, block=None):
        if block:
            result = self.find_block_sum(block)
            return result == self.center_vals[block]
        return False

    def is_solved(self):
        for block in ['tl', 'tr', 'bl', 'br']:
            valid = self.compare_block_to_center(block)
            if not valid:
                return False

        return True

    def is_legal_move(self, val):
        for row in self.grid:
            for cell_val in row:
                if cell_val == val:
                    return False
        return True

class Sujiko_Solver(object):
    def __init__(self, grid):
        self.grid = grid
        self.solve()
        print('\n')
        print('Solution:')
        print('\n')
        print(self.grid.grid[0])
        print(' ', str(self.grid.center_vals['tl']) + ',', self.grid.center_vals['tr'])
        print(self.grid.grid[1])
        print(' ', str(self.grid.center_vals['bl']) + ',', self.grid.center_vals['br'])
        print(self.grid.grid[2])
        print('\n')

    def solve(self):
        solved = False

        if self.grid.is_solved():
            solved = True
        else:
            candidate_cell = self.get_empty_cell()
            cell_val = self.grid.min_val

            while not solved and cell_val <= self.grid.max_val:
                if self.grid.is_legal_move(cell_val):

                    self.grid.update_cell(
                                            candidate_cell[0],
                                            candidate_cell[1],
                                            cell_val
                                        )

                    if self.solve():
                        solved = True
                    else:
                        self.grid.update_cell(
                                            candidate_cell[0],
                                            candidate_cell[1],
                                            None
                                        )
                cell_val = cell_val + 1

        return solved

    def get_empty_cell(self):
        for i, row in enumerate(self.grid.grid):
            for y, cell in enumerate(row):
                if cell is None:
                    return (i, y)

grid = Sujiko_Grid()
Sujiko_Solver(grid)
