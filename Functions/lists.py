#lista = []
#lista = [1,2,3,4,5,6,'nov element']
#print(lista)
'''print(lista[2])
print(lista[-1])
print(lista[1:5])'''

'''for element in lista:
    print(element*2)'''
'''
print(lista[6])
print(lista[-2])
print(lista[4:9])'''

#lista.pop()
#lista.pop(2)
#lista.remove('nov element')
#lista.clear()
#print(lista)



'''lista_parni = []
lista_ne_parni = []

br_povtoruvanja = int(input('Vnesete kolku pati sakate da vnesete broj:'))
for brojac in range (br_povtoruvanja):
    broj = int(input ('Vnesete broj:'))
    if broj % 2 ==0:
        lista_parni.append(broj)
    else:
        lista_ne_parni.append(broj)
print(f'Parni broevi{lista_parni}') 
print(f'Ne parni broevi{lista_ne_parni}'''

'''lista = []
broevi = int(input ('Vnesete boj na broevi sto sakate da gi vnesete:'))
for brojac in range (broevi):
    broj = int(input ('Vnesete broj:'))
    lista.append(broj)
print (f'Vasata vnesena lista e {lista}')
for broj in lista:
    print(f'Dobieniot rezultat e {broj*3}')'''

#Korisnikot da moze da vnesuva kolku proizvodi saka tolku i za sekoj proizvod da vnese i cena. Otkako ke se vnesat site proizvodi da se ispecati kolku vkupno treba korisnikot da plati

'''lista = []
vkupna_suma = 0
br_na_proizvodi = int(input('Vnesete broj na broizvodi sto ke gi kupite:'))
for brojac in range (br_na_proizvodi):
    proizvod = input('Vnesete tip na proizvod:')
    cena = int(input('Vnesete cena na produktot'))
    lista.append(proizvod)
    vkupna_suma = vkupna_suma + cena
for proizvod in lista:
    print (f'Vie gi kupivte slednite proizvodi {proizvod}')
print(f'Vkupnata suma za plakjanje e:{vkupna_suma}')'''
    
'''lista = [1,2,3,4,5,6,5,4,12,3,5,78,5]
#lista[0] =15
#mesto_element = lista.index('nov element')
br_povtoruvanje = lista.count(5)
max_broj = max(lista)
min_broj = min(lista)
suma_broevi = sum(lista)
print(suma_broevi)

br_elementi = len(lista)
print(br_elementi)
'''
lista = [1,2,3,4,5,6,5,4,12,3,5,78,5]

'''element_za_pronaogjanje = 12
for brojac in range(len(lista)):
    if element_za_pronaogjanje ==lista[brojac]:
     print(f'Indeksot na e elementot e {brojac}')
     break'''

#prebrojuvanje na element

'''element_za_povtoruvanja = 5
br_povtoruvanja = 0
for element in lista:
    if element_za_povtoruvanja == element:
        br_povtoruvanja = br_povtoruvanja+1 
print(f'Elementot {element_za_povtoruvanja} se pojavuva {br_povtoruvanja} pati')
'''
# Najgolem i najmal broj
'''najgolem_broj = 0
for element in lista:
    if element > najgolem_broj:
        najgolem_broj = element

print(f'Najgolemiot broj e {najgolem_broj}')

najmal_broj = lista[0]
for element in lista:
    if element < najmal_broj:
        najmal_broj = element
print(f'Najmaliot broj e {najmal_broj}')'''

# sobiranje na site elementi
'''suma = 0
for element in lista:
    suma = suma + element # suma+=element
print(f'Vkupnata suma na elementite e {suma}')'''

# od string lista i od lista string
'''
tekst = 'Lorem Ipsum is simply dummy text'
tekst = tekst.replace(',', '')
lista_tekst = tekst.split(' ')
print (lista_tekst)'''
'''lista_tekst = ['Lorem', 'Ipsum', 'is', 'simply', 'dummy', 'text']
spoen_tekst = ';'.join(lista_tekst)
print(spoen_tekst)'''

# sortiranje na lista
lista_tekst = ['lorem', 'ipsum', 'is', 'simply', 'dummy', 'text']
lista_tekst.sort(reverse=True)
print(lista_tekst)