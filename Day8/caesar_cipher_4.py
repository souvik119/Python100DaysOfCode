from caesar_art import logo

#selection of 26 alphabets
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#print caesar cipher in ascii art by importing from caesar_art file
print(logo)

def caesar(text, shift, direction):
    result = ""

    #handling shift greater than 26 which will result in indexoutofbounderror 
    shift %= 26

    for letter in text:
        #handle symbols other than 26 letters
        if letter in alphabet:
            position = alphabet.index(letter)
            if direction == "encode":
                new_position = position + shift
                #handle index error and make the conversion circular
                if new_position > 25:
                    result += alphabet[new_position-26]
                else:
                    result += alphabet[new_position]
            else:
                new_position = position - shift
                # negative index is auto converted to circular due to list property of negative index
                result += alphabet[new_position]
        else:
            result += letter
    
    print(f"The {direction}d text is {result}")


should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    cont_ans = input("Type 'yes' if you want to go again. Otherwise type 'no'\n")
    if cont_ans == "no":
        should_continue = False
        print("GoodBye!")