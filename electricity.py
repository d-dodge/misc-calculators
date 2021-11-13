wattage = input('Watts Used: ')
#hours = input('Hours Used per Day: ')
hours = 24
#monthlyCost = (float(wattage) / 1000) * float(hours) * 30 * 0.11266
monthlyCost = (float(wattage) / 1000) * float(hours) * 30 * 0.083096
print('')
print('Device costs $' + str(round(monthlyCost,2)) + ' per month to operate')