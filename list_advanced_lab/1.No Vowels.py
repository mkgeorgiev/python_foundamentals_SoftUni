text = input()
vowels_list = ["a", "e", "i", "u", "o"]
print("".join([el for el in text if not el.lower() in vowels_list]))
