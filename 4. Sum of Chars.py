lines = int(input())
total_sum = 0

for n in range(lines):
    current_letter = input()
    total_sum += ord(current_letter)

print(f"The sum equals: {total_sum}")
