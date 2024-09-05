choice = input('>')
operators = ['+', '-', '/', '*', '%']
operator = ''
for i in range(len(choice)):
    for j in range(len(operators)):
        if choice[i] == operators[j]:
            operator == operators[j]
            print(operator)
equation = choice.split(operator)
print(equation)
