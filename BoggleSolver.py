import enchant
from Word import Word
from Board import Board
from pprint import pprint


class BoggleSolver:
    def __init__(self, letter_list):
        self.d = enchant.Dict("en_US")
        self.board = Board(letter_list)
        self.min_length = 3
        self.max_length = 8
        self.words = set()

        # Find words from each starting coordinate position
        for row in range(self.board.side_length):
            for column in range(self.board.side_length):
                self.find_words(Word.new(row, column), row, column)

    def find_words(self, word, row, column):
        word.add_letter(self.board[row][column], row, column)

        if self.add_word(word):
            self.words.add(word.letter_sequence)

        for row, column in self.cordinates_word(word, row, column):
            if self.d.check(word.letter_sequence + self.board[row][column]):
                self.find_words(Word.new_word(word), row, column)

    def add_word(self, word):
        return self.min_length <= len(word) <= self.max_length and self.d.check(word.letter_sequence)

    def cordinates_word(self, word, row, column):
        for r in range(row - 1, row + 2):
            for c in range(column - 1, column + 2):
                if 0 <= r < self.board.side_length and 0 <= c < self.board.side_length:
                    if (r, c) not in word.used_board_coordinates:
                        yield r, c


if __name__ == "__main__":
    val = input("Enter your value: ")
    val = list(val)
    boggleSolver = BoggleSolver(val)
    words = boggleSolver.words
    pprint(words)
    print(len(words))
