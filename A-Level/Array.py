numbers = []
reverse = []
for i in range(6):
    num = i + 1
    numbers.append(num)
for i in range(5, -1, -1):
    reverse.append(numbers[i])
print(reverse)