from os import replace
import string

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    # reading file string and setting it to variable
    with open(file) as opened_file:
        file_string = opened_file.read()
    
    # make all letters lowercase
    lowercase = file_string.lower()

    # delete all punctuation
    punctuation = string.punctuation + "’"
    replace_w_space = ["\n", "—", "  "]
    zero_punctuation = lowercase
    for char in punctuation:
        if char in zero_punctuation:
            zero_punctuation = zero_punctuation.replace(char, "")
    for char in replace_w_space:
        if char in zero_punctuation:
            zero_punctuation = zero_punctuation.replace(char, " ")
    word_dict = {}
    word_list = zero_punctuation.split(" ")
    for word in word_list:
        if word in STOP_WORDS:
            continue
        elif word == "":
            continue
        elif word in word_dict.keys():
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    return print(word_dict[''])



if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
