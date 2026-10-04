# Check whether a list contains duplicate elements. If a duplicate is found, exit the loop and print the duplicate.
# items = ["red", "blue", "green", "red", "yellow"]
items = ["red", "blue", "green", "red", "yellow"]

seen = []

for item in items:
    if item in seen:
        print("Duplicate found:", item)
        break
    seen.append(item)