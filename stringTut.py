# Ask for a sting
orig_string = input("Convert to Acronym: ")
# Convert to uppercase
orig_string = orig_string.upper()
# Convert to a list
list_of_words = orig_string.split()
# Cycle though the list
for word in list_of_words:
    # Get the 1st letter of the word & eliminate newline
    print(word[0], end="")
# Add a newline
print()
