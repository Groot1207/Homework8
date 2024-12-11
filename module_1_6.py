my_dict = {'mom': 1969, 'dad': 1967, 'sister': 2004}
print(my_dict)
print(my_dict['mom'])
print(my_dict.get('brother'))
my_dict.update({'wife': 1997,
               'daughter': 2016})
print(my_dict)
my_dict.pop('wife')
print(my_dict)

my_set = {1, 2, 3, 4, 8, 1, 3, 4, 9, 'яблоко', True}
print(my_set)
my_set.update({5, 6})
my_set.discard(9)
print(my_set)
