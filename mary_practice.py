import load_dictionary

# write a short message that doesn't contain punctuation or numbers
input_message = "Give your word and we rise"
input_message = ''.join((input_message.split()))

# open names file
names_list = load_dictionary.load('supporters.txt')

list_names = [names_list[0]]

count = 1
for letter in input_message:
    for name in names_list:
        if len(name) > 2 and name not in list_names:
            if count % 2 == 0 and name[2].lower() == letter.lower():
                list_names.append(name)
                count += 1
                break
            elif count % 2 != 0 and name[1].lower() == letter.lower():
                list_names.append(name)
                count += 1
                break

list_names.insert(3, 'Stuart')
list_names.insert(6, 'Jacob')

print("List of court families that support your highness:")
print(*list_names, sep=', ')
