PointList = []
MapX = 400
MapY = 400

class Point:
	X = 0
	Y = 0
	square = 0
	def __init__(self, X, Y):
		self.X = X
		self.Y = Y
		self.square = 0
	
	def CalcDistanceToAxis(self, X, Y):
		return abs(self.X - X) + abs(self.Y - Y)
		

def ParseData(data):
	for line in data:
		lineData = line.split(', ')
		X = int(lineData[0], 10)
		Y = int(lineData[1], 10)
		#safe check
		if (X > MapX) or (Y > MapY):
			print 'Warning: point have X/Y greater than %d/%d.' % (MapX, MapY) 
		
		point = Point(X, Y)
		PointList.append(point)
	
def ScanMap():
	for X in range(0, MapX + 1):
		for Y in range(0, MapY + 1):
			nearPointIndex = -1
			nearDistance = 999
			i = 0
			for point in PointList:
				currentDistance = point.CalcDistanceToAxis(X, Y)
				if currentDistance < nearDistance:
					nearDistance = currentDistance
					nearPointIndex = i
				elif currentDistance == nearDistance:
					i += 1
					continue
				i += 1
					
			if X == 0 or Y == 0 or X == MapX or Y == MapY:
				PointList[nearPointIndex].square = -1 #infinity
			else:
				if PointList[nearPointIndex].square != -1:
					PointList[nearPointIndex].square += 1

#For part 2
def CalcTotalDistance(X, Y):
	totalDistance = 0
	for point in PointList:
		totalDistance += point.CalcDistanceToAxis(X, Y)
	return totalDistance
	

def ScanMap2():
	area = 0
	for X in range(0, MapX + 1):
		for Y in range(0, MapY + 1):
			if CalcTotalDistance(X, Y) < 10000:
				area += 1
	return area
		
def PrintPart1():
	pointIndex = -1
	maxSquare = 0
	i = 0
	for point in PointList:
		if point.square > maxSquare:
			maxSquare = point.square
			pointIndex = i
		i += 1
	print '#Part 1:'
	print 'Point #%d has largest area and it is %d' % (i - 1, maxSquare)

def PrintPart2():
	print '#Part 2:'
	print 'Result: %d' % ScanMap2()
	
if __name__ == '__main__':
	#Init something
	PointList = []
	#Create 400x400 Map
	MapX = 400
	MapY = 400
	
	pfile = open('input.txt', 'r')
	data = pfile.read().split('\n')
	ParseData(data)
	ScanMap()
	PrintPart1()
	PrintPart2()
	
