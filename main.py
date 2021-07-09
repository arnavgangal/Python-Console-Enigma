from enigma.enigma import Enigma


def main():
    # assume correct cipher user input
    cipher = input("Enter three letter initial rotor settings in order 'Slow, medium, fast': ")

    machine = initialize_rotors(cipher)

    # Message to be encrypted, using only uppercase letters, lowercase letters, and spaces
    message = input("Message to be encrypted or decrypted: ")
    print(machine.encrypt(message))


def initialize_rotors(cipher):
    """
    Sets up slow, fast, and medium rotors
    :param cipher: Three letter cipher code for rotor positions
    :return: Enigma machine object with rotors set up
    """
    return Enigma(cipher)


if __name__ == '__main__':
    main()
