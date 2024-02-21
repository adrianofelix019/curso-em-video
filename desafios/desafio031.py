distance = float(input('Enter the trip distance in KM: '))
ticket_price = 0

if distance <= 200:
    ticket_price = distance * 0.5
else:
    ticket_price = distance * 0.45

print(f'The ticket price is U${ticket_price}')
