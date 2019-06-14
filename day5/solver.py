def ReduceString(strInput):
	result = strInput[0]
	for i in range(1, len(strInput)):
		if (strInput[i].upper() == result[-1:].upper()) and (strInput[i] != result[-1:]):
			result = result[:-1]
		else:
			result += strInput[i]
	
	return result

def RemoveChar(strInput, char2Cnt):
	result = ''
	for c in strInput:
		if c.upper() == char2Cnt.upper():
			continue
		else:
			result += c
	return result
	
def SolvePart1(data):
	print '#Part 1:'
	result = ReduceString(data)
	print 'Result: %d' % len(result)

def SolvePart2(data):
	print '#Part 2:'
	allChar = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	min = 999999999
	for c in allChar:
		counter = len(ReduceString(RemoveChar(data, c)))
		if counter < min:
			min = counter

	print 'Result: %d' % min
	
if __name__ == '__main__':
	pfile = open('input.txt', 'r')
	data = pfile.read()
	SolvePart1(data)
	SolvePart2(data)
