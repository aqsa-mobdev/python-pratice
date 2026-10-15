sentence = input("Enter a sentence: ")

unique_characters = set(sentence.replace(" ", ""))

print("Unique Characters:", unique_characters)
print("Total Unique Characters:", len(unique_characters))