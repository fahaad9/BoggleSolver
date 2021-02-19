class Word:
    def __init__(self):
        self.letter_sequence = ""
        self.used_board_coordinates = set()

    @classmethod
    def new(cls, row, column):
        word = cls()
        word.used_board_coordinates.add((row, column))
        return word

    @classmethod
    def new_word(cls, word):
        new_word = cls()
        new_word.letter_sequence += word.letter_sequence
        new_word.used_board_coordinates.update(word.used_board_coordinates)
        return new_word

    def add_letter(self, letter, row, column):
        self.letter_sequence += letter
        self.used_board_coordinates.add((row, column))

    def __str__(self):
        return self.letter_sequence

    def __len__(self):
        return len(self.letter_sequence)
