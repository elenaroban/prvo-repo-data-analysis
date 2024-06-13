import requests
import json

convert_number = int(input("Vneste broj na sumi za konvertiranje: "))
number = 0
while number < convert_number:
    valuta_od = input('Vnesete ja valutata od koja sakate da konvertirate: ')
    valuta_vo = input('Vnesete ja valutata vo koja sakate da konvertirate: ')
    vrednost = int(input('Vnesete ja sumata: '))

    get_params = {
     "from":valuta_od,
     "to":valuta_vo,
     "amount":vrednost
}

    response = requests.get(
    url="https://4ae5-46-217-73-34.ngrok-free.app/convert",
    params=get_params
)

    if response.status_code == 200:
        res = json.loads(response.text)
        print(f"Vrednosta e: {res['converted_amount']}")
    else:
         print("Nastana greska!")
    number += 1

