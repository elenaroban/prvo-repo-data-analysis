#1 Da se napravi programa vo koja korisnikot ke vnese 2 broevi i da se proveri dali zbirot e pomal od 100

'''
broj_1 = float (input('vnesete prv sobirok'))
broj_2 = float (input('vnesete vtor sobirok'))
zbir = broj_1 + broj_2
if  zbir < 100: 
    print ('zbirot e pomal od 100')
else:
    print ('zbirot e pogolem od 100')
'''

#2 Da se napravi programa vo koja korisnikot ke vnese godina na ragjanje, ke se presmeta kolku godini e i da se odredi dali e maloleten ili polnoleten
'''
godina_na_ragjanje = float (input('Vnesete godina na ragjanje'))
current_year = float (2024)

if current_year - godina_na_ragjanje > 18:
    print ('Liceto e polnoletno')
else:
    print ('Liceto ne e polnoletno')
'''

#3 Da se napravi programa vo koja korisnikot ke vnese strani na dva pravoagolnici, da se presmeta plostinata i da se proveri koj pravoagolnik e pogolem
'''
a1 = int(input('Vnesi dolzina na strana a1:'))
b1 = int(input('Vnesi dolzina na strana b1:'))
plostina1 = a1 * b1
a2 = int(input('Vnesi dolzina na strana a2:'))
b2 = int(input('Vnesi dolzina na strana b2:'))
plostina2 = a2 * b2

print(f'Pravoagolnikot 1 e {plostina1}, a pravoagolnikot 2 e {plostina2}')

if plostina1 > plostina2:
    print('Pravoagolnikot 1 e pogolem od pravoagolnikot 2')
else:
    print('Pravoagolnikot 2 e pogolem od pravoagolnikot 1')
'''
#4 Da se napravi programa vo koja korisnikot ke vnese goleminite na aglite na triagolnici, i da se proveri dali so tie golemini moze da se kreira triagolnik(zbirot treba da bide 180)
'''
agol1 = int(input ('Vnesete agol 1 od triagolnik'))
agol2 = int(input ('Vnesete agol 2 od triagolnik'))
agol3 = int(input ('Vnesete agol 3 od triagolnik'))
triagolnik = agol1 + agol2 + agol3

if triagolnik ==180:
    print ('Zbirot na aglite e 180 stepeni, moze da se kreira triagolnik')
else:
    print ('Ne moze da se kreira triagolnik, zbirot na aglite ne e 180 stepeni')
'''

#Da se napravi programa vo koja korisnikot ke vnese broj i da se proveri dali toj broj e paren ili ne paren
'''
for i in range(5):
    broj = int(input('Vnesete broj'))

    if broj % 2 == 0:
        print ('Brojot e paren')
    else:
        print ('Brojot ne e paren')
'''
