'''from database import sesija,User'''

'''user1 = User(name = 'Elena', age = 30, email = 'elena@ymail.com')
sesija.add(user1)
sesija.commit()'''


from database import sesija, Employee, Product, Sale

def insert_employee(sesija ,full_name, email, age, position, salary, years_in_company):
    emp1 = Employee(full_name=full_name,
                    email=email,
                    age=age,
                    position=position,
                    salary=salary,
                    years_in_company=years_in_company)    
    sesija.add(emp1)
    sesija.commit()
    print(f"Vraboteniot {full_name} e vnesen")
    return emp1

def insert_product(sesija, name, price):
    prod1 = Product(name=name, price=price)
    sesija.add(prod1)
    sesija.commit()
    print(f"Produktot {name} e dodaden")
    return prod1

def insert_sale(sesija, employee_id, product_id):
    sale1 = Sale(employee_id=employee_id, product_id=product_id)
    sesija.add(sale1)
    sesija.commit()
    print("Prodazbata e zabelezana")
    return sale1

print('Novi promeni vo branch')
ime = input("Vnesete go vaseto ime: ")
print(f'Zdravo {ime}')




'''emp = sesija.query(Employee).all()
for employee in emp:
    print(f'{employee.id}. {employee.full_name}- {employee.position}')'''

#employees = sesija.query(Employee).filter_by(position= 'Sales').all()
#employees = sesija.query(Employee).filter_by(position = 'Sales').limit(3).all()



'''for employee in employees:
    print (f'{employee.id}'. {employee.full_name}-{employee.position}')'''

'''employee = sesija.query(Employee).filter_by(years_in_company = 5).first()
employee.salary=50000
sesija.commit()'''

employee = sesija.query(Employee).filter_by(id=7).first()
sesija.delete(employee)
sesija.commit()





