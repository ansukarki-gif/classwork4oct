# 5. Find the First Repeated Character
# Given a string, find the first character that appears more than once.


text = input("Enter a string: ")

for char in text:
    if text.count(char) > 1:
        print("First repeated character:", char)
        break