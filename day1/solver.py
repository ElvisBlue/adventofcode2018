if __name__ == '__main__':
	pfile = open('input.txt', 'r')
	data = pfile.read()
	numberList = data.split('\n')
	
	#Part 1 code
	result = 0
	for x in numberList:
		result += int(x)
	print '#Part 1'
	print 'Result: %d' % result
	
	#Part 2 code
	print '\n#Part 2'
	print 'Running. Please wait...'
	map = []
	sum = 0
	map.append(sum)
	isFound = False
	
	while isFound == False:
		for x in numberList:
			sum += int(x)
			if sum in map:
				isFound = True
				break
			map.append(sum)
	
	print 'Result: %d' % sum
