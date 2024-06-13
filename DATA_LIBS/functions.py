def convert_to_fahrenheit(temp):
    return temp *9/5+32

def calculate_student_avg(row):
    zbir_otceni = row['Grade Math'] + row['Grade English'] + row['Grade History'] + row['Grade Science']
    prosek = zbir_otceni /4
    return round(prosek, 2)

def categorize_students(row):
    if  row['Average'] <7:
        return 'Slab Student'
    elif row['Average'] >= 7 and row['Average'] < 8.5:
        return 'Dobar Student'
    elif row['Average'] >= 8.5:
        return "Odlicen Student"
    else:
        return 'Greska'
    

'''def count_data_keyword(row):
    br_povtoruvanja = row['LinkedIn Description'].count('data')
    return br_povtoruvanja'''

def count_data_keyword(description:str):
    br_povtoruvanja = description.lower().count('data')
    return br_povtoruvanja

