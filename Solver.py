# class Block(object):
#     def __init__(self, center):
#         self.center = center
#         self.top_left = None
#         self.top_right = None
#         self.bottom_left = None
#         self.bottom_right = None
#         self.sum = 0

#     def add_numbers(self):
#         self.sum = self.top_right + self.top_left + self.bottom_right + self.bottom_left

#     def set_value(self, position, value):
#         if(position == 'tl'):
#             self.top_left = value
#         elif(position == 'tr'):
#             self.top_right = value
#         elif(position == 'bl'):
#             self.bottom_left = value
#         elif(position == 'br'):
#             self.bottom_right = value
#         else:
#             print('invalid position')

#     def compare_numbers(self):
#         self.add_numbers()
#         return self.center == self.sum

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

        loop = True

        while loop:
            print('\n')
            i_coord = input('What is the ith coord of the known number? ')
            j_coord = input('What is the jth coord of the known number? ')
            num = input('What is the number at (' + i_coord + ', ' + j_coord + ')? ')
            self.update_cell(i_coord, j_coord, num)
            more = input('Are there more known numbers? (yes/no/y/n): ')
            if(more == 'yes' or more == 'y'):
                loop = True
            elif(more == 'no' or more == 'n'):
                loop = False
            else:
                print('Not a valid response, try again')

    def update_cell(self, i, j, num):
        i = int(i) - 1
        j = int(j) - 1
        self.grid[i][j] = int(num)

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


class Sujiko_Solver(object):
    def __init__(self, grid):
        self.grid = grid
        self.solve()

    def solve(self):
        print(grid.grid)
        result = grid.compare_block_to_center('tl')
        print(result)


grid = Sujiko_Grid()
Sujiko_Solver(grid)
