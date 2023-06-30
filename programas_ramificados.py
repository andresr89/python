name_1 = input('¿Cuál es tu nombre? ')
age_1 = int(input('Ingresa tu edad: '))
name_2 = input('¿Cuál es tu nombre? ')
age_2 = int(input('Ingresa tu edad: '))

if age_1 > age_2:
    print(f'{name_1} es más anciano que {name_2}.')
elif age_1 < age_2:
    print(f'{name_2} es más anciano que {name_1}.')

if len(name_1) > len(name_2):
    print(f'{name_1} tiene más caracteres que {name_2}.')
elif len(name_1) < len(name_2):
    print(f'{name_2} tiene más caracteres que {name_1}.')
