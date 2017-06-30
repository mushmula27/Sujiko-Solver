class Block(object):
    def __init__(self, center, numbers):
        self.center = center
        self.top_left = numbers[0]
        self.top_right = numbers[1]
        self.bottom_left = numbers[2]
        self.bottom_right = numbers[3]
        self.sum = 0

    def add_numbers(self):
        self.sum = self.top_right + self.top_left + self.bottom_right + self.bottom_left

    def compare_numbers(self):
        self.add_numbers()
        return self.center == self.sum

<<<<<<< HEAD
new_block = Block(17, [1,4,5,6])
=======
new_block = Block(17, [22,4,5,6])
>>>>>>> f79163f7f7b9b6d9cb220fa0fecf06a3106005e8
result = new_block.compare_numbers()
print(result)
