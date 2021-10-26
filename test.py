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
    zero_punctuation = lowercase
    for char in punctuation:
        if char in zero_punctuation:
            zero_punctuation = zero_punctuation.replace(char, "")
    
    word_dict = {}
    word_list = zero_punctuation.split(" ")
    for word in word_list:
        if word in STOP_WORDS:
            continue
        elif word in word_dict.keys():
            word_dict[word] += 1
        else:
            word_dict[word] = 1
        
    return print(word_dict)

print_word_freq()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# import string
# word_dict = {}
# punctuation = string.punctuation
# file_string = open(file).read()
# for symbol in punctuation:
#     if symbol in file_string:
#         zero_punctuation = file_string.replace(symbol, "")
# lowered = zero_punctuation.lower()
# file_list = lowered.split(" ")
# for word in file_list:
#     if word in STOP_WORDS:
#         if word in word_dict.keys():
#             word_dict[word] += 1
#         else:
#             word_dict[word] = 1
# sorted_keys_list = sorted(word_dict.keys(), )

# report_list = []
# for word in word_dict:
#     stars = word_dict[word] * "*"
#     report_list.append(word+" | "+word_dict[word]+" "+stars)
# return print(report_list)