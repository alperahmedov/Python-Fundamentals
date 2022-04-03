sentence = list(input().lower())
words = 0
for index in range(len(sentence)):
    if sentence[index] == "f" and index + 3 <= len(sentence):
        if sentence[index + 1] == "i" and sentence[index + 2] == "s" and sentence[index + 3] == "h":
            words += 1
    if sentence[index] == "s" and index + 3 <= len(sentence):
        if sentence[index + 1] == "a" and sentence[index + 2] == "n" and sentence[index + 3] == "d":
            words += 1
    if sentence[index] == "s" and index + 2 <= len(sentence):
        if sentence[index + 1] == "u" and sentence[index + 2] == "n":
            words += 1
    if sentence[index] == "w" and index + 4 <= len(sentence):
        if sentence[index + 1] == "a" and sentence[index + 2] == "t" and sentence[index + 3] == "e" and sentence[index + 4] == "r":
            words += 1
print(words)