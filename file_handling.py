f = open('data.txt', 'r+')

data = f.readline()

print(data)

f.write('This is a new line')

f.close()