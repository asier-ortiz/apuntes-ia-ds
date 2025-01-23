"""
Crear una función que reciba una lista de elementos y devuelva una lista filtrada sin cadenas de texto
Ejemplos:

Recibe [1,2,'a','b'] devuelve [1,2]
Recibe [1,'a','b',0,15] devuelve [1,0,15]
Recibe [1,2,'aasf','1','123',123] devuelve [1,2,123]

"""


def filter_list(data_list):
    filtered_list = []
    for i in data_list:
        if type(i) != str:
            filtered_list.append(i)
    return filtered_list


print(filter_list([1, 2, 'a', 'b']))
print(filter_list([1, 'a', 'b', 0, 15]))
print(filter_list([1, 2, 'aasf', '1', '123', 123]))
