sentence = input("Enter a sentence: ")
length = 0
num_words = 0
num_vowels = 0

for char in sentence:
    length += 1
    if char == " ":
        num_words += 1
    elif char in "aeiouAEIOU":
        num_vowels += 1

num_words += 1 # increment num_words to account for the last word

print("Length of sentence:", length)
print("Number of words:", num_words)
print("Number of vowels:", num_vowels)
