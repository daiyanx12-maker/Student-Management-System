class car():
    brand = ''
    model = ''
    color = ''
    price = ''
    fuel_type = ''
    speed = ''
    year = ''

c1 = car()
c1.brand = 'Porshe'
c1.model = '911 Turbo S'
c1.color = 'Jet black metallic'
c1.price = '270,000$'
c1.fuel_type = 'Petrol'
c1.speed = '330km/h'
c1.year = 2025

print(f"Brand: {c1.brand} \nModel: {c1.model} \nColor: {c1.color} \nPrice: {c1.price} \nFule Type: {c1.fuel_type} \nSpeed: {c1.speed} \nYear: {c1.year}")
Name = 'Porshe 911 Turbo S'
HP = 701
sec = 2.4
print(f"The {Name} has a {HP}-hp engine and reaches 60mph in just {sec} seconds ")