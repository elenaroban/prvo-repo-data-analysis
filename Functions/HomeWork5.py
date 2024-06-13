#Вежба 1: Напиши програма за печатење на броевите од 1 до 10.
'''lista = [1,2,3,4,5,6,7,8,9,10]
print (lista)'''

#Вежба 2: Напиши програма за пресметување и печатење на збирот на сите броеви од 1 до 10.

'''zbir = sum (lista[0:10])
print(f'Vkupniot iznos e: {zbir}')'''
#print(f'Vkupniot iznos e: {sum (lista[0:10])}')

#Вежба 3: Напиши програма за печатење на квадратите на броевите од 1 до 10

'''for element in lista:
    print(element*element)'''

#Вежба 4, 5 и 6 (комбинирана): Напиши програма за наоѓање и печатење на најголемиот, најмалиот и просекот на листа од броеви.

'''najgolem = max(lista)
najmal = min(lista)
prosek = zbir/ len(lista)

print(f'{najgolem} e najgolemiot broj vo listata')
print(f'{najmal} e najmaliot broj vo listata')
print(f'{prosek} e prosecniot broj vo listata')'''

#Вежба 7: Напиши програма за пребројување и печатење на бројот на парни броеви во листа.
#Вежба 8: Напиши програма за пребројување и печатење на бројот на непарни броеви во листа.

'''lista_parni = []
lista_neparni = []

for element in lista:
    if element%2==0:
        lista_parni.append (element)
    else:
        lista_neparni.append (element)

print (len(lista_parni),f'{lista_parni} se parni broevi')
print (len(lista_neparni),f'{lista_neparni} ne se parni broevi')'''

#Вежба 9: Напиши програма што ќе бара од корисникот да внесе 5 броеви и да ги зачува во листа. Потоа, испечати го збирот на тие броеви.

'''lista = []

for brojac in range (5):
    broj = int(input ('Vnesete broj:'))
    lista.append(broj)
print (sum(lista))'''

#Вежба 10: Напиши програма што ќе бара од корисникот да внесува серија на броеви сè додека не внесе '0'. Зачувај ги броевите во листа и потоа испечати ја листата.

'''lista = []
broj = int(input ('Vnesete broj:'))
while broj > 0:
    broj = int(input('Vnesete broj:'))
    if broj == 0:
        print ('brojot e ednakov na nula i ciklusot ke zavrsi')
        break'''

#Вежба 11: Напиши програма што ќе бара од корисникот да внесе реченица. Раздели ја реченицата на зборови и зачувај ги во листа. Потоа, испечати го должината на секој збор во листата.

'''recenica = input('Vnesete recenica: ')
lista_recenica = recenica.split(' ')
print (lista_recenica)

for element in lista_recenica:
    print (len(element))'''

#Вежба 12: Напиши програма што ќе бара од корисникот да внесе серија на броеви. Зачувај ги броевите во листа и потоа испечати го најголемиот број во листата.


'''lista = []

for brojac in range (4):
    broj = int(input ('Vnesete broj:'))
    lista.append(broj)
print(lista)
print (max(lista))'''

#Вежба 13: Напиши програма што ќе бара од корисникот да внесе серија на броеви. Зачувај ги броевите во листа и потоа испечати ја средната вредност на броевите

'''lista = []

for brojac in range (4):
    broj = int(input ('Vnesete broj:'))
    lista.append(broj)
avg =(sum(lista)/len(lista))
print(lista)
print(avg)'''

#Вежба 14: Напиши програма што ќе бара од корисникот да внесе реченица. Раздели ја реченицата на зборови и зачувај ги во листа. Потоа, испечати ги зборовите во обратен редослед.

'''recenica = input (('Vnesete recenica: '))
razdeli_recenica=recenica.split (" ")
print (razdeli_recenica[::-1])'''


#Вежба 15: Напиши програма што ќе бара од корисникот да внесе реченица. Раздели ја реченицата на зборови и зачувај ги во листа. Потоа, испечати го бројот на зборови кои започнуваат со гласна буква.

recenica = input (('Vnesete recenica: '))
razdeli_recenica=recenica.split(" ")
print(razdeli_recenica)
for element in razdeli_recenica:
    if element == ('A,E,I,O,U'):
        razdeli_recenica.append (element)
        print (len(razdeli_recenica))


#Вежба 16: Напиши програма што ќе бара од корисникот да внесе серија на броеви. Зачувај ги броевите во листа и потоа испечати само парните броеви од листата.


'''lista_paren= []

for brojac in range (10):
    broj = int(input ('Vnesete broj:'))
    
    if broj % 2==0:
        lista_paren.append(broj)
        print(lista_paren)'''
    
    





