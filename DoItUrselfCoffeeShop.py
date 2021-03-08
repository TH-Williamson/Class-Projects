print('Welcome to Cup of Joe Joe Joe setup')

menu = []
print('Enter the coffee options for today, type \'done\' to finish:')
while True:
    drink = input()
    if drink == 'done':
        break
    else:
        menu.append(drink)
        
text = '\n'.join(menu)

    
print('Setup complete, ready to take orders')
print('------')

print('Today\'s menu:')
print(text)
print('------')

customer_drinks = {} #turn this into a dictionary, make values oz * price

drink_choice = input('What would the customer like to drink? Type \'done\' to finish:')

price = 0.3

while drink_choice != 'done':
    if drink_choice not in menu:
        print('Invalid choice, please select something from the menu')
        drink_choice = input('What would the customer like to drink? Type \'done\' to finish:\n')
    else:
        drink_size = int(input('Our cups can fit between 8 and 20 oz of coffee. How many oz would they like?\n'))
        drink_cost = drink_size * price
        drink_rnd = round(drink_cost, 3)
        customer_drinks[drink_choice] = drink_rnd
        drink_choice = input('What would the customer like to drink? Type \'done\' to finish:\n')
total_price = 0

for key, value in customer_drinks.items():
    print('one {} oz cup of {}'.format((int(value/0.3)), key))
    total_price += value
    continue

print('The total is', total_price, 'dollars')




    






