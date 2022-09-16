with open(r"412Project3.txt", 'r') as fp:
    count = 0
    for line in fp:
        if line != "\n":
            count += 1

print('Total Number of Lines', count)