import sys
MENU = {
"espresso": {
"ingredients": {
"water": 50,
"milk": 0,
"coffee": 18,

},
"cost": 1.50,
},
"latte": {
"ingredients": {
"water": 200,
"milk": 150,
"coffee": 24,
},
"cost": 2.50,
},
"cappuccino": {
"ingredients": {
"water": 250,
"milk": 100,
"coffee": 24,
},
"cost": 3.0,
}
}

profit = 0
resources = {
"water": 300,
"milk": 200,
"coffee": 100,
}


def resource_left(choice, menu, resources):
# Checks how many resources you have left after making a cup of coffee
#
    for i in ('milk','water','coffee'): 
        resources[i] -= menu[choice]["ingredients"][i] 
    return resources

def payment(cost):
# Processes how the payment will go through and if any change is neccesarry 
#   
    print(f'Your total is ${cost}')
    print('Please insert coins ')
    total = .25 * float(input( "How many quarters? "))
    total += .10 * float(input( "How many dimes? "))
    total += .05 * float(input( "How many nickles? "))
    total += .01 * float(input( "How many pennies? "))
    if total >= cost:
        change = round(float(total) - cost, 2)
    else:
        print('Sorry that is not enough money. Money refunded.')
        sys.exit()
    if change > 0:
        print(f'Here is ${change} in change.')
    return total
    
def out(choice, resources, menu):
# Checks if there are enough resources
#
    for i in ("milk","water","coffee"):
        if resources[i] - menu[choice]["ingredients"][i] < 0:
            print('Sorry we are out of ingredients')
            sys.exit()
        


another = 'yes'
while another == 'yes':
    choice = input('What would you like? (espresso, latte, cappuccino): ')
    out(choice, resources, MENU)
    profit += payment(MENU[choice]["cost"])
    resource_left(choice,MENU,resources)
    print(f'Here is your {choice} enjoy.'
    )
    another = input('Would you like another coffee? ')
