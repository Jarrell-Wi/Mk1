def triangle(rows):
    if rows == 1:
        return(rows)
    return(rows * triangle(rows - 1))

a = int(input('>'))
print(triangle(a))