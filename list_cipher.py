from random import randint
import string
import load_dictionary

# write a short message that doesn't contain punctuation o numbers
input_message = "Panek at east end of chapel slides"

message = ''
for char in input_message:
    if char in string.ascii_letters:
        message += char

print(message, "\n")
message = ''.join(message.split())

# open dictionary file
word_list = load_dictionary.load('dict.txt')

# build vocabulary word list with hidden message
vocab_list = []
for letter in message:
    size = randint(6, 10)
    for word in word_list:
        if len(word) == size and word[2].lower() == letter.lower() and word not in vocab_list:
            vocab_list.append(word)
            break

if len(vocab_list) < len(message):
    print("Word List is too small. Try larger dictionary or shorter message!")
else:
    print("Vocabulary words for Unit 1: \n", *vocab_list, sep="\n")
