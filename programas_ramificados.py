name_1 = input('¿Cuál es tu nombre? ')
age_1 = int(input('Ingresa tu edad: '))
gender_1= (input('cual es tu genero m o f: '))
name_2 = input('¿Cuál es tu nombre? ')
age_2 = int(input('Ingresa tu edad: '))
gender_2= (input('cual es tu genero m o f: '))

if age_1 > age_2:
    print(f'{name_1} tiene mas edad que {name_2}.')
elif age_1 < age_2:
    print(f'{name_2} tiene mas edad que {name_1}.')
else:print('ambos son igual de ancianos')

if len(name_1) > len(name_2):
    print(f'{name_1} tiene más caracteres que {name_2}.')
elif len(name_1) < len(name_2):
    print(f'{name_2} tiene más caracteres que {name_1}.')
else: print('tienen la misma cantidad de caracteres')


if gender_1 == gender_2:
    print('Ambos usuarios son del mismo sexo')
if gender_1 == 'f'and gender_2=='m':
    print(f'{name_1} es mujer y {name_2} es hombre.')
if gender_1 == 'm'and gender_2=='f':
    print(f'{name_1} es hombre y {name_2} es mujer.')
else: 
    print('sexo no definido')