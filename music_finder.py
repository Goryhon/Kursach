from help import *
from math import log2


class hash_table:
	def __init__(self, hash_func):
		self.func = hash_func
		self.table = None
		self.offset = 0


	def fit(self, matrix):
		hashes = [self.func(line) for line in matrix]
		self.offset = min(hashes)

		self.table = [[] for i in range(self.offset, max(hashes) + 1)]

		for i in range(len(hashes)):
			self.table[hashes[i] - self.offset] += [matrix[i]]


	def find_by_hash(self, hash):
		return self.table[hash - self.offset][:]


	def add(self, new_val):
		hash_val = self.func(new_val)
		if(hash_val < self.offset):
			self.table = [[] for i in range(self.offset - hash_val)] + self.table
			self.offset = hash_val
		elif (hash_val > self.offset + len(self.table) - 1):
			self.table = self.table + [[] for i in range(hash_val - (self.offset + len(self.table) - 1))]
		self.table[hash_val - self.offset] += [new_val]

	def delete(self, val):
		ind = self.func(val) - self.offset
		try:
			self.table[ind].remove(val)
		except:
			pass

	def to_str(self):
		ret = ''
		for row in self.table:
			if(len(row) > 0):
				ret += '\n'.join([','.join(el) for el in row]) + '\n'
		return ret


class bintree:
	def __init__(self, func):
		self.bintree = None
		self.janr_matrix = None
		self.janrs = None
		self.counts = None
		self.func = func

	def create(self, lines):

		# Всеразличные жанры и количество песен каждого из них
		all_janrs = []
		counts = []

		for i in lines:
			if not(i[3] in all_janrs):
				all_janrs += [self.func(i)]
				counts += [0]
			counts[all_janrs.index(self.func(i))] += 1
		ziped = zip_zap(all_janrs, counts)
		
		ziped = q_sort(ziped, lambda x: x[1])[::-1]

		# Так должно выглядеть финальное дерево
		self.janrs = [i[0] for i in ziped]
		self.counts = [i[1] for i in ziped]
		

		ltr_janrs = self.ltr(self.janrs)# Так выглядят обход левый верхний правый
		# print('ltr', ltr_janrs)

		val_of_janrs = [ltr_janrs.index(i) for i in self.janrs]# Какое значение должно быть у каждого из жанров чтоб получилось такое дерево
		# print(val_of_janrs)
		self.janr_matrix = [ltr_janrs, val_of_janrs]
		# Заполнение дерева
		self.fit(lines)

	def find_ind_in_bintree(self, val, cur_ind = 0):

		if(cur_ind == 0):
			try:
				val = self.janr_matrix[0].index(val)
			except:
				return None

		if(val == self.janr_matrix[1][cur_ind]):
			return cur_ind
		elif (val < self.janr_matrix[1][cur_ind]):
			return self.find_ind_in_bintree(val, cur_ind*2 + 1)
		else:
			return self.find_ind_in_bintree(val, cur_ind*2 + 2)

	def ltr(self, arr, ind = 0):
		if(ind >= len(arr)):
			return []
		return self.ltr(arr, ind*2 + 1) + [arr[ind]] +  self.ltr(arr, ind*2 + 2)

	def fit(self, matrix):
		self.bintree = [[] for i in self.janrs]
		for i in matrix:
			ind = self.find_ind_in_bintree(self.func(i))
			if not(ind is None):
				self.bintree[ind] += [i]

	def add(self, new_val):
		jr = self.func(new_val)
		if(jr in self.janr_matrix[0]):
			self.counts[self.janrs.index(jr)] += 1
			if(is_sorted(self.counts)):
				self.bintree[self.find_ind_in_bintree(jr)] += [new_val]
				return 
		temp = []
		for i in self.bintree:
			temp += i
		temp += [new_val]
		self.create(temp)

	def add_list(self, new_val_list):
		same_jr = True
		for i in new_val_list:
			if not(self.func in self.janrs):
				same_jr = False
				break
		if(same_jr):
			for i in new_val_list:
				self.add(i)
		else:
			temp = []
			for i in self.bintree:
				temp += i
			temp += new_val_list
			# print(temp)
			self.create(temp)

	def delete(self, val):
		jr = self.func(val)
		if(jr in self.janrs):
			try:
				ind = self.find_ind_in_bintree(jr)
				self.bintree[ind].remove(val)
				self.counts[ind] -= 1
				if(self.counts[ind] <= 0):
					temp = []
					for i in self.bintree:
						temp += i
					self.create(temp)

			except:
				pass


	def to_str(self):
		ret = ''
		for row in self.bintree:
			ret += '\n'.join([','.join(el) for el in row]) + '\n'
		return ret

def work_with_f1(f1_name):
	f1 = open(f1_name, 'r')

	f1_lines = f1.readlines()

	f1_lines = [line[:-1].split(',') for line in f1_lines]
	f1.close()

	ht = hash_table(lambda x: int(x[1]))
	ht.fit(f1_lines)
	ht.table

	return ht


def work_with_f2(f2_name):
	f2 = open(f2_name, 'r')

	f2_lines = f2.readlines()

	f2_lines = [line[:-1].split(',') for line in f2_lines]
	f2.close()

	
	# print('sorted', sorted_janrs)
	bt = bintree(lambda x: x[3])
	bt.create(f2_lines)
	


	return bt

def init(f1_name, f2_name):
	ht = work_with_f1(f1_name)
	bt = work_with_f2(f2_name)
	return ht, bt

def rewrite_files(cart, f1_name, f2_name):
	f1 = open(f1_name, 'w')
	f2 = open(f2_name, 'w')

	f1.write(cart.ht.to_str())
	f2.write(cart.bintree.to_str())

	f1.close()
	f2.close()

class Cartoteca:
	def __init__(self, ht, bintree):
		self.ht = ht
		self.bintree = bintree

	def find(self, age, janr):
		in_age = self.ht.find_by_hash(age)[:]
		names = [i[0] for i in in_age]
		ind = self.bintree.find_ind_in_bintree(janr)
		if not(ind is None):
			in_janr = self.bintree.bintree[ind]
			return [i for i in in_janr if i[0] in names]
		return None
