import music_finder
from help import validate

# ht, bintree, janr_matrix = music_finder.init('file1.csv', 'file2.csv')
ht, bt = music_finder.init('file1.csv', 'file2.csv')

login = 'admin'
password = '123'

ct = music_finder.Cartoteca(ht, bt)

#Сохраняет файлы
music_finder.rewrite_files(ct,'file1.csv', 'file2.csv')

ct.ht.add(['Valerchik','16','0'])
ct.ht.delete(['Valerchik','16','0'])

ct.bintree.add(['ABKdw','BIeh','smt','AE'])# Добавить в бинарное дерево

ct.bintree.add_list([
						['ABKdw','BIeh','smt','AE'],
						['Chpok','BIeh','smt','AYE']
					])# Добавить в бинарное дерево

print(['ABKdw','BIeh','YZm','AE'] in ct.find(29, 'AE'))
ct.bintree.delete(['ABKdw','BIeh','YZm','AE'])# Удалить из бинарного дерева
print(['ABKdw','BIeh','YZm','AE'] in ct.find(29, 'AE'))

# print(validate(''))
# print(validate(' '))
# print(validate(' Jora'))
# print(validate('Jora'))
# print(validate('Jora1'))