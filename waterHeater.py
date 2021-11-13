gasPrice = 0.943317
electricPrice = 0.083096

incomingTemp = float(input('Input Water Temperature: '))
outgoingTemp = float(input('Output Water Temperature: '))
gallons = float(input('Number of Gallons Consumed: '))

btuRequired = (gallons * 8.3) * (outgoingTemp - incomingTemp)
print('')
print('Electric Heating Cost: $' + str(round(((btuRequired / 3412.14163) * electricPrice),2)))
print('')
print('Gas Heating Cost: $' + str(round(gasPrice * (btuRequired / 103046.67269),2)))