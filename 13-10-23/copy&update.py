dict_1={1:'a',2:'b',3:'c'}
dict_2={4:'d',5:'d',6:'e'}
dict_3=dict_1.copy()

dict_2.update({4:'c'})
dict_3.update(dict_2)
print(dict_3)
