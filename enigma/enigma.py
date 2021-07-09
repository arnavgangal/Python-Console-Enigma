from string import ascii_uppercase
from rotors.rotor import Rotor


class Enigma:
    """ Encapsulates the machine's state, encrypts/decrypts messages"""

    reflector_permutation = "IXUHFEZDAOMTKQJWNSRLCYPBVG"
    rotor_permutations = ["EKMFLGDQVZNTOWYHXUSPAIBRCJ", "AJDKSIRUXBLHWTMCQGZNPYFVOE", "BDFHJLCPRTXVZNYEIWGAKMUSQO"]

    _rotor_array: list[Rotor]

    def __init__(self, cipher):
        self._rotor_array = []
        for i in range(len(Rotor.rotor_permutations)):
            offset_char = cipher[i]
            offset = ascii_uppercase.find(offset_char)
            self._rotor_array.append(Rotor(Enigma.rotor_permutations[i], offset))

    def encrypt(self, message):
        toreturn = ""
        # Break the string up into chars
        for elem in message:
            # Check if element is a space
            if elem == ' ':
                toreturn += elem
                continue

            # Before the character is encrypted, advance rotors
            self.increase_offset()

            islower = False  # Boolean to store if char is uppercase or lower case
            if elem.islower():
                islower = True
                elem = elem.upper()  # Make upper case

            # Forward pass on rotors
            for i in reversed(range(len(self._rotor_array))):
                elem = self._rotor_array[i].forward_pass(elem)

            # Pass output to reflector
            index = ascii_uppercase.find(elem)  # Get the index of the letter in alphabet
            elem = self.reflector_permutation[index]  # Return char at that index of permutation

            # Back pass on rotors
            for i in range(len(self._rotor_array)):
                elem = self._rotor_array[i].back_pass(elem)

            # Pass into output string
            if islower:
                toreturn += elem.lower()
            else:
                toreturn += elem

        return toreturn

    def increase_offset(self):
        if self._rotor_array[2].increase_offset():  # If increasing fast rotor by one yields true, carry
            if self._rotor_array[1].increase_offset():  # If increasing medium by one yields true, carry
                self._rotor_array[0].increase_offset()
