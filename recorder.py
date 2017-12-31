higherList = []
lowerList = []

print('This was made to prove to my brother that it is a chance each time and not overall')

def getDice():
	highDi = input('Enter the highest dice re-roll: ')
	lowDi = input('Enter the lowerList dice re-roll: ')
	try:
		if int(highDi) < 1 or int(highDi) > 6 or int(lowDi) < 1 or int(lowDi) > 6:
			print('Incorrect format, enter 1,2,3,4,5,6\nRestarting this input')
			getDice()
	except (TypeError, ValueError):
		print('Incorrect format, enter 1,2,3,4,5,6\nRestarting this input\n')
		getDice()
	else:
		higherList.append(int(highDi))
		lowerList.append(int(lowDi))

def stats():
	global advHigh, advLow, higherList, lowerList
	if higherList[-1] > lowerList[-1]:
		print('\nRe-roll worked this trial')
	else:
		print('\nRe-roll did not work this trial')
	highAdvTotal = 0
	lowAdvTotal = 0
	highRatioTotal = 0
	lowRatioTotal = 0
	for (hi,lo) in zip(higherList, lowerList):
		highAdvTotal = highAdvTotal + hi
		lowAdvTotal = lowAdvTotal + lo
		if hi > lo: highRatioTotal += 1# it does not count the same numbers
		elif hi < lo: lowRatioTotal += 1
	#print('higher: '+str(highRatioTotal)+'lower'+str(lowRatioTotal))
	print('Adverage second roll on the higher dice: '+str(highAdvTotal / len(higherList)))
	print('Adverage second roll on the lower dice: '+str(lowAdvTotal / len(lowerList)))
	print('This technique is only working '+str(highRatioTotal)+' out of '+str(lowRatioTotal+highRatioTotal)+' times.\n\n')


while True:
	getDice()
	stats()
