'''x_dictionary = {
    'ime':'Elena',
    'prezime': 'Robanovska',
    'pol':'Female',
    'email':{
        'privaten':'example@gmail.com',
        'sluzben':'example1@gmail.com'
    },
    'tel_broj':[000000 ,111111],
    'maticen_broj':'1233}'''

#x_dictionary.pop('prezime')
#x_dictionary.popitem()
#del x_dictionary('ime')

'''for key in x_dictionary.keys():
    print(x_dictionary[key])'''

'''for value in x_dictionary.values():
    print(value)'''

'''for key, value in x_dictionary.items():
    print(f'index: {key}, value: {value}')


print(x_dictionary)'''
#zemanje podatoci
#print(x_dictionary['email']['privaten'])

'''print(x_dictionary['ime'])
print(x_dictionary['prezime'])
print(f'{x_dictionary['prezime']},{x_dictionary['ime']}')'''

#print(x_dictionary.get('dresa_na_ziveenje', 'Nema adresa'))
#print(x_dictionary.get('email').get('privaten)'))
#dodavanje podatoci
#x_dictionary['maticen_broj'] = '123456784321'
'''nov_dict = {'maticen_broj':'123456784321','pol' : 'Female'}
x_dictionary.update(nov_dict)'''

'''Y_distionary ={
'broj1':8,
'broj2':4
}
Y_distionary["sobiranje"]=Y_distionary["broj1"]+Y_distionary["broj2"]
Y_distionary["odzemanje"]=Y_distionary["broj1"]-Y_distionary["broj2"]
Y_distionary["mnozenje"]=Y_distionary["broj1"]*Y_distionary["broj2"]
Y_distionary["delenje"]=Y_distionary["broj1"]/Y_distionary["broj2"]

print(Y_distionary)
'''

'''user = {}
user["ime"] = input("Vnesete go vaseto ime: ")
user["prezime"] = input("Vnesete go vaseto prezime: ")
user["vozrast"] = int(input("Vnesete gi vashite godini: "))
if user["vozrast"] >= 18:
    user["status"] = "polnoleten"
else:
    user["status"] = "maloleten"
print("Korisnikot e: ", user)'''




import json

'''json_fajl = open('new_file.json','w')
json.dunp(x_dictionary, json_fajl)
print('Zapisano vo fajl')'''
                 
json_fajl = open('new_file.json', 'r')
nov_dictionary = json.load(json_fajl)
print(nov_dictionary)

