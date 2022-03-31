number = input()
digits = [int(x) for x in number]
digits.sort(reverse=True)
result = ''
for d in digits:
    result += str(d)
print(result)





