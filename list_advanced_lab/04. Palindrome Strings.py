list_of_words = input().split(" ")
count_of_given_palindrome = list_of_words.count(input())
print([word for word in list_of_words if word == "".join(list(reversed(word)))])

print(f"Found palindrome {count_of_given_palindrome} times")