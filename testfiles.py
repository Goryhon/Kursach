from itertools import combinations
from random import shuffle, randint



def generateNames(n, count):
	letters = [chr(i) for i in range(65,91)] + [chr(i) for i in range(97,123)]
	name = list(combinations(letters, n))
	name = [''.join(name) for name in name[:count]]
	i = 0
	while(len(name) < count):
		name += name[i]
		i += 1
	shuffle(name)
	return name

count = 10000

name = generateNames(5, count)
age = [randint(5, 30) for i in range(count)]
sex = [randint(0, 1) for i in range(count)]

author = generateNames(4, count*5)
songs_name = generateNames(3, count*10)
janra = generateNames(2, 10)

#Fill file 1
f1 = open('file1.csv', 'w')
for i in range(count):
	f1.write(f"{name[i]},{age[i]},{sex[i]}\n")
f1.close()


#Create file 2
output = []
counter = 0
for i in name:
	for j in range(1,4):
		output += [[i, author[counter], songs_name[counter], janra[randint(0, len(janra) - 1)]]]
		counter += 1
shuffle(output)

#Fill file 2
f2 = open('file2.csv', 'w')
for zap in output:
	f2.write(f"{zap[0]},{zap[1]},{zap[2]},{zap[3]}\n")
f2.close()
