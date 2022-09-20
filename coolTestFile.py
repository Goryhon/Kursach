from itertools import combinations
from random import shuffle, randint

def generateNames(n, count):
	letters = [chr(i) for i in range(65,91)] + [chr(i) for i in range(97,123)]
	name = list(combinations(letters, n))
	shuffle(name)
	name = [''.join(name) for name in name[:count]]
	i = 0

	while(len(name) < count):
		name += name[i]
		i += 1

	return name

count = 1000
min_age = 10
max_age = 40
min_songs = 1
max_songs = 5

isp = open('Ispolniteli_2.txt', mode = 'r',encoding = 'utf-8')
ispolniteli = isp.read().split(',')
isp.close()


pes = open('Pesni.txt', mode = 'r',encoding = 'utf-8')
pesni = [line[:-1].split(',') for line in pes.readlines()]
pes.close()

names = generateNames(5, count)
f1 = open('file1.csv', 'w')
for i in range(count):
	f1.write(f"{names[i]},{randint(min_age, max_age)},{randint(0, 1)}\n")
f1.close()

shuffle(ispolniteli)
shuffle(pesni)
conter_pes = 0
conter_isp = 0
f2 = open('file2.csv', mode ='w',encoding = 'utf-8')
for name in names:
	for j in range(randint(min_songs, max_songs)):
		f2.write(f"{name},{ispolniteli[conter_isp]},{pesni[conter_pes][0]},{pesni[conter_pes][1]}\n")
		conter_pes += 1
		conter_isp += 1
		if(conter_pes >= len(pesni)):
			shuffle(pesni)
			conter_pes = 0
		if(conter_isp >= len(ispolniteli)):
			shuffle(ispolniteli)
			conter_isp = 0
f2.close()