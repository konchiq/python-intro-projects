import random
alphabet = ["а","б","в","г","д","е","ё","ж","з","и","й","к","л","м","н","о",
            "п","р","с","т","у","ф","х","ц","ч","ш","щ","ъ","ы","ь","э","ю","я"]

f1 = open('hang_ez.txt', encoding='utf-8')
ez = f1.readlines()
f2 = open('hang_medium.txt', encoding='utf-8')
medium = f2.readlines()
f3 = open('hang_hard.txt', encoding='utf-8')
hard = f3.readlines()

print('Выберете сложность:\n'
      '1 - легкая\n'
      '2 - средняя\n'
      '3 - жесть\n')
level = input()
if level == '1':
    slovo = random.choice(ez)
elif level == '2':
    slovo = random.choice(medium)
elif level == '3':
    slovo = random.choice(hard)
else:
    print('Неправильно выбран уровень сложности')
    raise SystemExit
otvet = ['_'] * (len(slovo) - 1)
print(''.join(otvet))
print('\n')
p = 1
neprav = []
prav = []
while p <= 6:
    buk = input()
    if buk not in alphabet:
        print('Введена нестрочная буква русского алфавита, '
              'попробуйте еще раз')
        continue
    if buk not in slovo:
        p = p + 1
        neprav.append(buk)
    if buk in slovo:
        prav.append(buk)
    if p == 2:
        print('_______/|\_\n')
    if p == 3:
        print('        | \n '
              '       | \n'
              '        | \n'
              '        | \n'
              '_______/|\_\n')
    if p == 4:
        print('   +----+ \n '
              '       | \n '
              '       | \n'
              '        | \n'
              '        | \n'
              '_______/|\_\n')
    if p == 5:
        print('   +----+ \n '
              '  |    | \n '
              '  o    | \n'
              '        | \n'
              '        | \n'
              '_______/|\_\n')
    if p == 6:
        print('   +----+ \n '
              '  |    | \n '
              '  o    | \n'
              '  /|\   | \n'
              '        | \n'
              '_______/|\_\n')
    if p == 7:
        print('   +----+ \n '
              '  |    | \n '
              '  o    | \n'
              '  /|\   | \n'
              '  / \   | \n'
              '_______/|\_\n'
              'ВЫ ПРОИГРАЛИ\n')
    for i in range(len(slovo)):
        if slovo[i] in prav:
            otvet[i] = slovo[i]
    print(''.join(otvet), '\n')
    if '_' not in otvet:
        print('ПОЗДРАВЛЯЕМ, ВЫ ПОБЕДИЛИ\n')
    if len(neprav) > 0:
        print('Неправильные буквы:', ', '.join(neprav))
    if p < 7:
        print('Осталось попыток: ', 7 - p)
    else:
        print('Загаданно слово: ', slovo)
    print('\n')
