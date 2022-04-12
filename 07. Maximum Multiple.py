number = int(input())
boundary = int(input())
count = 0

for i in range(boundary+1):
    if i % number == 0 and i >= count:
        count = i
    else:
        continue

print(count)
