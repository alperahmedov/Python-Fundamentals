text = input()
text2 = input()

for i in range(len(text)):
    if text[i] != text2[i]:
        replacement = text2[i]
        word = text[0:i] + replacement + text[i + 1:]
        text = word

        print(word)
