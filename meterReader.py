time = input('Time in seconds for meter to cycle once: ')
wattDraw = (3600 * 6) / float(time)
print('')
print('House is consuming ' + str(int(wattDraw)) + ' watts')
monthlyCost = (float(wattDraw) / 1000) * 24 * 30 * 0.083096
print('')
print('This load costs $' + str(round(monthlyCost,2)) + ' per month to operate')