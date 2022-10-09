# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

with open('prim_1.txt', 'w', encoding='utf-8') as file:
    file.write('2*x^2 + 5*x^5')
with open('prim_2.txt', 'w', encoding='utf-8') as file:
    file.write('23*x^4 + 9*x^6')

with open('prim_1.txt','r') as file:
    prim_1 = file.readline()
    list_of_prim_1 = prim_1.split()


with open('prim_2.txt','r') as file:
    prim_2 = file.readline()
    list_of_prim_2 = prim_2.split()

print(f'{list_of_prim_1} + {list_of_prim_2}')
sum_prim = list_of_prim_1 + list_of_prim_2

with open('sum_prim.txt', 'w', encoding='utf-8') as file:
    file.write(f'{list_of_prim_1} + {list_of_prim_2}')
