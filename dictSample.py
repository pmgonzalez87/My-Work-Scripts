#!/usr/bin/env python3
car = {'model': 'Explorer', 'manuf': 'Ford', 
        'price': 50000}
user = {
        'username': 'justincase',
        'firstname': 'justin',
        'lastname': 'Case',
        'lastmame': 'Chase',
        '4-digit-SSN': 666
}

print(car)
print("The car model is", car['model'])
print("Username is", user['username'])
print("Users full name is", user['lastname'] + ', ' + user['firstname'])