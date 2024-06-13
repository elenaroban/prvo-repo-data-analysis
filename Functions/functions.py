def pecati_zdravo(ime):
    print(f'Zdravo {ime}')
    print('Ovaa poraka e ispecatena od funkcija')

#pecati_zdravo('Elena')
'''ime_od_user = input('Vnesete go vaseto ime ')
pecati_zdravo(ime_od_user)'''


'''def zbir_i_razlika (broj1, broj2, broj3=0):
    rezultat = broj1+broj2+broj3
    razlika = broj2-broj1
   # print(f'Zbirot na broevite {broj1} i {broj2} i {broj3} e {rezultat}')
    return rezultat, razlika


x = int(input('Vnesete go prviot broj: '))
y = int(input('Vnesete go vtoriot broj: '))
z = 15

rez_zbir, rez_razlika = zbir_i_razlika(x,y)
print(f'Rezultatot e {rez_zbir}')
print(f'Razlikata e {rez_razlika}')'''

'''def proveri_polnoletstvo (godini):
    if godini >= 18:
        return True
    else:
        return False
ime = input('Vnesete go vaseto ime: ')
godini = int(input('Vnesete gi vasite godini: '))

if proveri_polnoletstvo (godini):
    print(f'{ime} vie ste polnoleten')
else:
    print(f'{ime} vie ste maloleten')'''

#zadaca 3

'''def presmetka(lista):
    prosek_lsita = sum(lista) / len(lista)
    return prosek_lsita
lista = []
br_oceni = int(input("Vnesete go brojot na ocenki: "))
for x in range(br_oceni):
    ocenka = int(input('Vneste ja ocenkata: '))
    lista.append(ocenka)
kraj = presmetka(lista)
print(f"Prosekot e : {kraj}")'''

try:
    broj1 = int(input('Vnesi broj: '))
    broj2 = int(input('Vnesi broj: '))
    rez = broj1/broj2
    print(rez)
except ZeroDivisionError:
    print('Vnesovte 0 vo eden od broevite')

#podole primerite se isti
'''finally:
    print('Zavsi rizicniot del')

print('Zavsi rizicniot del')'''

#except ValueError:
    #print('Vnesovte nevaliden karakter')

#except IndexError:
    #print('Ne postoi element so toj index')
#except KeyError:
    #print('Ne postoi element so toj index')

# da se vnese ime
# da se vnesat godini


















#zbir(x,y)
#zbir(broj2=x, broj1=y, broj3=13)

'''def zbir (broj1, broj2,broj3):
    rezultat = broj1+broj2+broj3
    print(f'Zbirot na broevite {broj1} i {broj2} e {rezultat}')
'''
#pecati_zdravo('Elena')

'''ime_od_user = input('Vnesete go vaseto ime ')
pecati_zdravo(ime_od_user)'''

'''x = int(input('Vnesete go prviot broj: '))
y = int(input('Vnesete go vtoriot broj: '))'''

#zadaca 1
'''def ime_polnoleten (ime, vozrast):
    if vozrast>= 18:
        print (f'{ime} e polnoleten' )
    else:
        print (f'{ime} e maloleten' )

ime_korisnik = str(input('Vnesete ime: '))
godini = int(input('Vnesete godini: '))
ime_polnoleten(ime_korisnik,godini)'''

#zadaca 2
'''def kalkulacii(broj1, broj2, operacija):
    if operacija == 'plus' :
        rezultat = broj1 + broj2
        print(f"Rezultatot na {broj1} i {broj2} e {rezultat}")
    elif operacija == 'minus':
        rezultat = broj1 - broj2
        print(f"Razlikata na {broj1} i {broj2} e {rezultat}")
    elif operacija == 'mnozenje':
        rezultat = broj1 * broj2
        print(f"produktot na {broj1} i {broj2} e {rezultat}")
    elif operacija == 'delenje':
        rezultat = broj1 / broj2
        print(f"rezultat delenje na {broj1} i {broj2} e {rezultat}")
broj1 = int(input("vnesete go prviot broj: "))
broj2 = int(input("vnesete go vtoriot broj: "))
operacija = input("Vnesete operacija: ")
kalkulacii (broj1, broj2, operacija)
'''




