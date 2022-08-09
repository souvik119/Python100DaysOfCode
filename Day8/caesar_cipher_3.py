alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Comdine encrypt() and decrypt() functions into a single function called caesar()
def caesar(text, shift, direction):
    result = ""
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            if direction == "encode":
                new_position = position + shift
                if new_position > 25:
                    result += alphabet[new_position-26]
                else:
                    result += alphabet[new_position]
            else:
                new_position = position - shift
                result += alphabet[new_position]
        else:
            result += letter
    
    print(f"The {direction}d text is {result}")

caesar(text, shift, direction)