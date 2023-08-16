# 1 - How to print all names of a person
name_1 = {'first': "Lawi", 'second': "Olel"}
name_2 = {'third': "Odhiambo", 'fourth': "Otieno"}

all_names = {**name_1, **name_2}
print("#####1######")
print(all_names)
print() #Allow 1 line space

# 2 - How to print only 3 names of a person
name_1 = {'first': "Lawi", 'second': "Olel"}
name_2 = {'second': "Odhiambo", 'third': "Otieno"}

only_3 = {**name_1, **name_2}
print("######2#####")
print(only_3)