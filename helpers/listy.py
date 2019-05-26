import operator

ratingi_lista = [1, 0, 4, 5, 6]
print(ratingi_lista)
# [1, 0, 4, 5, 6]


ratingi_string = ', '.join(map(str, ratingi_lista))
print(ratingi_string)
# 1, 0, 4, 5, 6


ratingi_ze_string_do_listy = ratingi_string.split(',')
print(ratingi_ze_string_do_listy)
# ['1', ' 0', ' 4', ' 5', ' 6']


ratingi_ze_string_do_listy = [ int(rating) for rating in ratingi_ze_string_do_listy]
print(ratingi_ze_string_do_listy)
# [1, 0, 4, 5, 6]

print(ratingi_ze_string_do_listy[3])
# 5
print(type(ratingi_ze_string_do_listy[3]))
# <class 'int'>
print(type(int('1')))
# <class 'int'>

#===
#pozycja w stringu - czyli nr uzytkownika lub filmu

rating_dict = { k : v for k, v in enumerate(ratingi_ze_string_do_listy)}
print(rating_dict)
# {0: 1, 1: 0, 2: 4, 3: 5, 4: 6}

print(rating_dict[2])
# 4

#sortowanie od największej wartości - w tuple (indeks, wartosc)
sorted_rating_dict = sorted(rating_dict.items(), key=operator.itemgetter(1), reverse=True)

print(sorted_rating_dict)
# [(4, 6), (3, 5), (2, 4), (0, 1), (1, 0)]

print(sorted_rating_dict[0][1])

ratingi_fl_lista = [ 1.3223, 4.235655, 3.12312]
print(ratingi_fl_lista)
# [1.3223, 4.235655, 3.12312]

ratingi_string_fl = ', '.join(map(str, ratingi_fl_lista))
print(ratingi_string_fl)
# 1.3223, 4.235655, 3.12312

rat_ze_str_to_list_fl = ratingi_string_fl.split(',')
print(rat_ze_str_to_list_fl)
# ['1.3223', ' 4.235655', ' 3.12312']

rat_ze_str_to_list_fl = [ float(rating) for rating in rat_ze_str_to_list_fl]
print(rat_ze_str_to_list_fl)
# [1.3223, 4.235655, 3.12312]

print(rat_ze_str_to_list_fl[2])
# 3.12312
print(type(rat_ze_str_to_list_fl[2]))
# <class 'float'>



