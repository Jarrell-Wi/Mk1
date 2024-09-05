def getequation (choice):
    operators = ['+', '-', '/', '*', '%']
    op = ''
    for i in range(len(choice)):
        for j in range(len(operators)):
            if choice[i] == operators[j]:
                op = j
    equation = choice.split(str(op))
    return(equation, op)

def  add (left, right):
    answer = left + right
    return(answer)

def  subtract(left, right):
    answer = left - right
    return(answer)

def  divide(left, right):
    answer = left / right
    return(answer)

def  multiply(left, right):
    answer = left * right
    return(answer)

def modulate  (left, right):
    answer = left % right
    return(answer)













choice = input('Gimme equation')
calc = getequation(choice)
left = calc[0][0]
right = calc[0][1]
op = calc[1][0]
if op == 0:
    result = add(left, right, op)
elif op == 1:
    result = subtract(left, right, op)
elif op == 2:
    result = divide(left, right, op)
elif op == 3:
    result = multiply(left, right, op)
elif op == 4:
    result = modulate(left, right, op)
print(result)