#Da se kreira dictionary so 3 elementi po vas izbor i da se ispecati posledniot element
'''x_dictionary = {
    'ovosje1':'banana',
    'ovosje2': 'jabolko',
    'ovosje3':'krusa'}
x_dictionary.pop('ovosje1')
x_dictionary.pop('ovosje2')
print(x_dictionary)'''

#Da se kreiara prazen dictionary, korisnikot da vnese 2 broevi koi ke se dodadt vo dictionary. Da se izvrsat 4te osnovni matematicki operacii i da se dodadat rezultatite vo dictionary vo razlicni keys

'''prazen_dictionary = {}
broj1 = int(input('Vnesete go prviot broj: '))
broj2 = int(input('Vnesete go vtoriot broj: '))


prazen_dictionary['sobiranje']=[broj1+broj2]
prazen_dictionary['odzemanje']=[broj1-broj2]
prazen_dictionary['mnozenje']=[broj1*broj2]
prazen_dictionary['delenje']=[broj1/broj2]

print(prazen_dictionary)'''

#Da se kreira programa vo koja korisnikot ke moze da vnesuva licni podatoci i otceni za odreden ucenik, da se vnesuva ime na predmetot i otcenata. Site podatoci da se zacuvaat vo dictionary. 
#Otkako ke bidat vneseni site podatoci da se presmeta prosekot na ucenikot i da se ispecati. *Bonus: adaptirajte ja programata da moze da raboti za cel klas, ne samo za eden ucenik

'''klas_dictionary= {}

ime=input('Vnesete ime : ')
predmet=input('Vnesete Predmet: ')
ocena=int(input('Vnesete Ocena : '))
predmet1=input('Vnesete Predmet1: ')
ocena1=int(input('Vnesete Ocena : '))
predmet2=input('Vnesete Predmet2: ')
ocena2=int(input('Vnesete Ocena : '))

klas_dictionary['ime']=ime  
klas_dictionary['predmet']=predmet
klas_dictionary['ocena']=ocena
klas_dictionary['predmet1']=predmet1
klas_dictionary['ocena1']=ocena
klas_dictionary['predmet2']=predmet2
klas_dictionary['ocena2']=ocena

ocenki = []

for elements in klas_dictionary:   
    ocenki.append(int(ocena))
    ocenki.append(int(ocena1))
    ocenki.append(int(ocena2))   

average = sum(ocenki)/len(ocenki)

print(klas_dictionary)
print('Prosecnata ocena e: ',average)'''
       


# 1Da se kreira programa koja ke bide za potrebide vo nekoja prodavnica. Da se kreira dictionary koj ke ima 2 indexi, produkti, ceni koi kkao podatoci ke imaat prazni listi.
# 2Koristnikot da moze da vnesuva produkti i ceni na produktite se dodeka ne izbere deka poveke ne saka da vnese. 
# 3Koga ke prestane da vnesuva produkti da se presmeta kolku treba da plati i da se zacuva vo nov index. 
#Da mu se dade opcija na korisnikot da plati, d a se presmeta dali treba da se vrati kusur ili ne. 
#Ako treba da se zacuva vo dictionary kolku kusur treba da se vrati. Ako ne treba da se zacuva deka smetkata e platena.

'''prodavnica_dictionary={'produkti' :[], 'ceni' :[]}


while True:
    produkt = input('Vnesete produkt (ili napisete "stop" za zavrsuvanje): ')
    if produkt.lower() == 'stop':
        break
    cena = int(input('Vnesete cena za {}: '.format(produkt)))
    prodavnica_dictionary['produkti'].append(produkt)
    prodavnica_dictionary['ceni'].append(cena)

print(prodavnica_dictionary)


vkupno_za_naplata = sum(prodavnica_dictionary ['ceni'])
print ('Vasata smetka iznesuva:' ,vkupno_za_naplata)

plakjanje = input('Dali zavrsivte so pazaruvanje? (da/ne): ')
if plakjanje.lower() == 'da':
    vneseni_pari = int(input('Iznosot sto go vnesuvate e: '))
    if vneseni_pari < vkupno_za_naplata:
        print('Nedovolen iznos!')
    elif vneseni_pari == vkupno_za_naplata:
        print('Smetkata e platena!')
    else:
        kusur = vneseni_pari - vkupno_za_naplata
        print('Smetkata e platena, kusur za vrakjanje: {:.2f} den.'.format(kusur))
else:
    print('Smetkata ne e platena.')


'''