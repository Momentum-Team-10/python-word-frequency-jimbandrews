import string
# file = "praise_song_for_the_day.txt"
text = "Here’s what you’ll learn in this tutorial:"
zero_punctuation = text
for char in string.punctuation:
    if char in text:
        zero_punctuation = zero_punctuation.replace(char, "")

print(zero_punctuation)

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