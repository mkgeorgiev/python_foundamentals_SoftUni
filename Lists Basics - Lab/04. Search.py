n = int(input())
key_word = input()
list_of_text = []
list_with_key_word = []
for text in range(n):
    string_of_text = input()
    list_of_text.append(string_of_text)
    if key_word in string_of_text:
        list_with_key_word.append(string_of_text)
print(list_of_text)
print(list_with_key_word)
