def getequation (choice):
    operators = ['+', '-', '/', '*', '%']
    op = ''
    for i in range(len(choice)):
        for j in range(len(operators)):
            if choice[i] == operators[j]:
                op = operators[j]
                opr = j
    equation = choice.split(str(op))
    return(equation, opr)

def  add (left, right):
    answer = int(left) + int(right)
    return(answer)

def  subtract(left, right):
    answer = int(left) - int(right)
    return(answer)

def  divide(left, right):
    answer = int(left) / int(right)
    return(answer)

def  multiply(left, right):
    answer = int(left) * int(right)
    return(answer)

def modulate  (left, right):
    answer = int(left) % int(right)
    return(answer)

print('STOP to end')
stay = True
while stay == True:
    choice = input('Enter Equation: ')
    if choice == 'STOP':
        break
    calc = getequation(choice)
    op = calc[1]
    left = calc[0][0]
    right = calc[0][1]


    if op == 0:
        result = add(left, right)
    elif op == 1:
        result = subtract(left, right)
    elif op == 2:
        result = divide(left, right)
    elif op == 3:
        result = multiply(left, right)
    elif op == 4:
        result = modulate(left, right)
    print('V')
    print(result)