gallons = float(input('Fuel Tank Capacity (gallons): '))
dose = (((gallons / 10) * 3) * 28.41306) / 59
print('A ' + str(gallons) + ' gallon fuel tank will require ' + str(round(dose, 1)) + ' travel spray bottles worth of fuel treatment')