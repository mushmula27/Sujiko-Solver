class Block(object):
    def __init__(self, center):
        self.center = center
        self.top_left = None
        self.top_right = None
        self.bottom_left = None
        self.bottom_right = None
        self.sum = 0

    def add_numbers(self):
        self.sum = self.top_right + self.top_left + self.bottom_right + self.bottom_left

    def set_value(self, position, value):
        if(position == 'tl'):
            self.top_left = value
        elif(position == 'tr'):
            self.top_right = value
        elif(position == 'bl'):
            self.bottom_left = value
        elif(position == 'br'):
            self.bottom_right = value
        else:
            print('invalid position')

    def compare_numbers(self):
        self.add_numbers()
        return self.center == self.sum

class Sujiko_Solver(object):
    def __init__(self):
        tl = input('What is the top left target number? ')
        self.tl_block = Block(tl)

        tr = input('What is the top right target number? ')
        self.tr_block = Block(tr)

        bl = input('What is the bottom left target number? ')
        self.bl_block = Block(bl)

        br = input('What is the bottom right target number? ')
        self.br_block = Block(br)

        self.block_map = [
            [[self.tl_block], [self.tl_block, self.tr_block], [self.tr_block]],
            [[self.tl_block, self.bl_block], [self.tl_block, self.tr_block, self.bl_block, self.br_block]],
            [[self.bl_block], [self.bl_block, self.br_block], [self.br_block]]
        ]
        loop = True

        while loop:
            print('\n')
            i_coord = input('What is the ith coord of the known number? ')
            j_coord = input('What is the jth coord of the known number? ')
            num = input('What is the number at (' + i_coord + ', ' + j_coord + ')? ')
            self.update_grid(i_coord, j_coord, num)
            more = input('Are there more known numbers? (yes/no/y/n): ')
            if(more == 'yes' or more == 'y'):
                loop = True
            elif(more == 'no' or more == 'n'):
                loop = False
            else:
                print('Not a valid response, try again')

    def update_grid(self, i, j, num):
        i = int(i) - 1
        j = int(j) - 1
        for block in self.block_map[i][j]:
            print(block.center)

Sujiko_Solver()
