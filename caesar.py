import sys
import fileinput

alphabet = "abcdefghijklmnopqrstuvwxyzæøå"

def shift(length):
    def shiftcurry(letter):
        if letter in alphabet:
            old_index = alphabet.index(letter)
            new_index = (old_index + length) % len(alphabet)
            return alphabet[new_index]
        else:
            return letter
    return shiftcurry

def encrypt(key, word):
    length = alphabet.index(key)
    return map(shift(length), word)

def decrypt(key, word):
    length = alphabet.index(key)
    return map(shift(-length), word)

def print_iterator(iter):
    s = ""
    for x in iter:
        s = s + str(x)
    return s

def encrypt_str(key, word):
    return "".join(encrypt(key, word))

def decrypt_str(key, word):
    return "".join(decrypt(key, word))

def demo():
    print("Finn nøkkelen og det krypterte ordet for følgende:")
    # print("".join(encrypt('c', 'xyz')))
    print("".join(encrypt('h', 'zeppelin')))
    print("".join(encrypt('m', 'fransiserkul')))
    print("".join(encrypt('z', 'pizza')))
    print("".join(encrypt('z', 'Dette er _test!!')))

def printhelp():
    helptext = """
    Usage examples:
     - Encrypt with 't' from file:
         python3 caesar.py encrypt t source.txt
     - Encrypt with 'q' from stdin:
         echo "encrypt me" | python caesar.py encrypt q
     - Decrypt using 'l':
         python3 caesar.py decrypt l source.txt
    """
    print(helptext)

def mkencryptfun():
    if len(sys.argv) < 3:
        raise ValueError("Not enough arguments.")
    mode = sys.argv[1]
    key = sys.argv[2]
    # print(mode)
    # print(mode == "encrypt")
    if mode == "encrypt":
        return lambda line: encrypt_str(key, line)
    elif mode == "decrypt":
        return lambda line: decrypt_str(key, line)
    else:
        raise ValueError("Invalid input mode: <{}>".format(mode))

def main():
    if "--help" in sys.argv:
        printhelp()
        return
    try:
        encryptfun = mkencryptfun()
        for line in fileinput.input(sys.argv[3:]):
            print(encryptfun(line), end='')
    except ValueError:
        printhelp()
        raise

if __name__ == '__main__':
    main()
