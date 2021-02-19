
class Board:
    def __init__(self, letter_list):
        self.side_length = len(letter_list) ** .5
        if self.side_length != int(self.side_length):
            raise Exception("Board must  be a square and have equal sides! (4x4, 5x5...)")
        else:
            self.side_length = int(self.side_length)

        self.board = []

        index = 0
        for row in range(self.side_length):
            self.board.append([])
            for column in range(self.side_length):
                self.board[row].append(letter_list[index])
                index += 1

    def __getitem__(self, row):
        return self.board[row]
