# TODO 1 - read starting letter from starting_letter.txt (relative path - ./Input/Letters/starting_letter.txt)
# TODO 2 - replace [name] with name from invited_names.txt (relative path - ./Input/Names/invited_names.txt)
# TODO 3 - create new files in the format letter_for_<name>.txt (relative path - ./Output/ReadyToSend/letter_for_<name>.txt)

STARTING_LETTER = "./Input/Letters/starting_letter.txt"
GUEST_NAMES = "./Input/Names/invited_names.txt"
GUEST_LETTER = "./Output/ReadyToSend/"

def read_starting_letter(letter_path):
    """Reads starting letter and returns the string"""
    with open(letter_path) as f:
        contents = f.read()
    return contents


def get_guest_names(guest_path):
    """Reads invited guest list from invited guest text file and returns a list"""
    guest_list = []
    with open(guest_path) as f:
        for line in f:
            guest_list.append(line.strip())
    return guest_list


def write_letter(letter, guest_list):
    """Writes files to destination folder for each recipient"""
    for guest in guest_list:
        contents = letter.replace("[name]", guest)
        with open(f"{GUEST_LETTER}"+f"letter_for_{guest}.txt", "w") as f:
            f.write(contents)


def main():
    letter = read_starting_letter(STARTING_LETTER)
    guest_list = get_guest_names(GUEST_NAMES)
    write_letter(letter, guest_list)


main()