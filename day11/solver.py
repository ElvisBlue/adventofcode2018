SERIAL = 9810

table = [[0 for x in range(301)] for y in range(301)]
sumTable = [[0 for x in range(301)] for y in range(301)]

def CheckSum(x,y):
	rackID = 10+x
	return ((((rackID*y + SERIAL) * rackID)/100) % 10) - 5
	
def InitTable():
	for i in range(1, 301):
		for j in range(1, 301):
			table[j][i] = CheckSum(j, i)

def InitSumTable():
	for i in range(1, 301):
		sumLine = 0
		for j in range(1, 301):
			sumLine += table[j][i]
			sumTable[j][i] = sumLine + sumTable[j][i-1]

def CalcSumArea(x, y, size):
	try:
		return sumTable[x+size-1][y+size-1] + sumTable[x-1][y-1] - sumTable[x-1][y+size-1] - sumTable[x+size-1][y-1]
	except:
		print 'Err: x = %d, y = %d, size = %d' % (x, y, size)
		quit()

def PrintTable(x, y):
	for i in range(1, 6):
		line = ''
		for j in range(1, 6):
			line += str(table[j + x][i + y]) + '\t'
		print line
	
def PrintSumTable(x, y):
	for i in range(1, 6):
		line = ''
		for j in range(1, 6):
			line += str(sumTable[j + x][i + y]) + '\t'
		print line

def SolvePart1():
	#https://en.wikipedia.org/wiki/Summed-area_table
	max = 0
	x = 0
	y = 0
	for i in range(1, 301-3):
		for j in range(1, 301-3):
			if CalcSumArea(j, i, 3) > max:
				max = CalcSumArea(j, i, 3)
				x = j
				y = i
	print '#Part 1'
	print '%d,%d' % (x, y)
	
def SolvePart2():
	max = 0
	x = 0
	y = 0
	s = 0
	for size in range(1,301):
		for i in range(1, 301-size):
			for j in range(1, 301-size):
				if CalcSumArea(j, i, size) > max:
					max = CalcSumArea(j, i, size)
					x = j
					y = i
					s = size
	print '#Part 2'
	print '%d,%d,%d' % (x, y, s)
if __name__ == '__main__':
	InitTable()
	InitSumTable()
	SolvePart1()
	SolvePart2()
