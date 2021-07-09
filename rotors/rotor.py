from string import ascii_uppercase


class Rotor:
    """
    Stores rotor arrangement and offset
    """

    rotor_permutations = ["EKMFLGDQVZNTOWYHXUSPAIBRCJ", "AJDKSIRUXBLHWTMCQGZNPYFVOE", "BDFHJLCPRTXVZNYEIWGAKMUSQO"]

    _permutation: str
    _inverse_key: str
    _offset: int

    def __init__(self, permutation, offset):
        self._permutation = permutation
        self._offset = offset
        self._inverse_key = self.invert_key()

    def __repr__(self):
        return f'{"".join(self._permutation[self._offset:] + self._permutation[:self._offset])}'

    def invert_key(self):
        toreturn = ""
        for letter in ascii_uppercase:
            index = self._permutation.find(letter)  # Get the index of the letter in the permutation string
            toreturn += ascii_uppercase[index]
        return toreturn

    def forward_pass(self, elem):
        index = (ascii_uppercase.find(elem) + self._offset) % 26  # Get the index of the letter in alphabet
        temp = self._permutation[index]  # Return char at that index of permutation
        temp_index = ascii_uppercase.find(temp)
        return ascii_uppercase[(temp_index - self._offset + 26) % 26]

    def back_pass(self, elem):
        index = (ascii_uppercase.find(elem) + self._offset) % 26  # Get index of letter in alphabet
        temp = self._inverse_key[index]
        temp_index = ascii_uppercase.find(temp)
        return ascii_uppercase[(temp_index - self._offset + 26) % 26]

    def increase_offset(self):
        self._offset += 1  # Increase offset by 1
        if self._offset % 26 == 0:
            self._offset = 0
            return True
        else:
            return False
