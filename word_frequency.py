import string

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has',
    'he', 'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to',
    'were', 'will', 'with'
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
    zero_punctuation = lowercase
    for char in punctuation:
        if char in zero_punctuation:
            zero_punctuation = zero_punctuation.replace(char, "")

    # replace certain characters with a single white space
    replace_w_space = ["\n", "—", "  "]
    for char in replace_w_space:
        if char in zero_punctuation:
            zero_punctuation = zero_punctuation.replace(char, " ")

    # initialize variables for later, and split my string into a list
    word_count = {}
    max_length = 1
    word_list = zero_punctuation.split(" ")

    for word in word_list:
        # flow control for string we don't need to count
        if word in STOP_WORDS:
            continue
        elif word == "":
            continue

        # check if word is in dict from above, then either add the word
        # or 1 to the key's value
        elif word in word_count.keys():
            word_count[word] += 1
        else:
            word_count[word] = 1

        # used to find the length of the longest word for later use
        if len(word) > max_length:
            max_length = len(word)

    # create a list of keys sorted in descending order based on their key value
    words_by_freq = sorted(word_count, key=word_count.get, reverse=True)

    for word in words_by_freq:
        frequency = word_count[word]
        # determine number of spaces needed to align the | character
        spaces = (max_length - len(word)) * " "
        # determine number of stars and number of spaces to align stars
        if frequency < 10:
            stars = "  " + frequency * "*"
        else:
            stars = " " + frequency * "*"
        # finish by printing an f-string for each word
        print(f" {spaces}{word} | {frequency}{stars}")


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
