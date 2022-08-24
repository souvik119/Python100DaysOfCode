import pandas

def csv_to_dict(file):
    df = pandas.read_csv(file)
    nato_dict = {row["letter"]:row["code"] for (index, row) in df.iterrows()}
    return nato_dict

def nato_code(user_word, nato_dict):
    result_code = [nato_dict[key] for key in user_word]
    print(f"NATO phonetic code is : {result_code}")

def main():
    nato_dict = csv_to_dict("nato_phonetic_alphabet.csv")
    user_word = input("Enter a word: ")
    nato_code(user_word.upper(), nato_dict)

main()