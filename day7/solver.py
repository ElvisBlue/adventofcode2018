pointList = []
NUMBER_OF_WORKERS = 5

class Point:
	incomeList = []
	outcomeList = []
	name = ''
	def __init__(self, name):
		self.name = name
		self.incomeList = []
		self.outcomeList = []
	
	def addPointIncome(self, pointName):
		self.incomeList.append(pointName)
		
	def addPointOutcome(self, pointName):
		self.outcomeList.append(pointName)
		
class Worker:
	isBusy = False
	workingStep = ''
	timeWorking = 0
	name = ''
	def __init__(self, name):
		self.isBusy = False
		self.workingStep = ''
		self.timeWorking = 0
		self.name = name
		
	def IncreaseTimeWorking(self):
		self.timeWorking += 1
		timeNeedWorking = ord(self.workingStep) - 0x41 + 60
		#print 'Worker ' + self.name + ' is working at %s' % self.workingStep
		if self.timeWorking > timeNeedWorking:
			#print 'Worker %s stop working at %s' % (self.name, self.workingStep)
			self.isBusy = False
		
	def SetWorkingAt(self, step):
		self.isBusy = True
		self.workingStep = step
		self.timeWorking = 0
		#print 'Worker %s start working at %s' % (self.name, self.workingStep)
	
	def FreeWorker(self):
		self.isBusy = False
		self.workingStep = ''
		self.timeWorking = 0
		
def ParsePoint(data):
	for line in data:
		#Step C must be finished before step A can begin.
		pointFrom = line[5]
		pointTo = line[36]
		point = GetPointByName(pointFrom)
		point2 = GetPointByName(pointTo)
		if point == None:
			point = Point(pointFrom)
			pointList.append(point)
			
		point.addPointOutcome(pointTo)
		
		if point2 == None:
			point2 = Point(pointTo)
			pointList.append(point2)
		point2.addPointIncome(pointFrom)
	
def Flood(queue, result):
	if len(queue) == 0:
		return
	point = GetPointByName(queue[0])
	result.append(queue[0])
	del queue[0]
	
	for outcomePoint in point.outcomeList:
		outcomePointObj = GetPointByName(outcomePoint)
		outcomePointObj.incomeList.remove(point.name)
		if len(outcomePointObj.incomeList) == 0:
			queue.append(outcomePoint)
	point.outcomeList = []
	queue.sort()
	Flood(queue, result)
		
def TopologicalSort():
	#Kahn's algo
	queue = []
	result = []
	
	for point in pointList:
		if len(point.incomeList) == 0:
			queue.append(point.name)
	
	queue.sort()
	Flood(queue, result)
	return result
	
def Flood2(queue, time, workerFree, workerWorking):
	while len(queue) == 0 or len(workerFree) == 0:
		time += 1
		#print '==== Time = %d ====' % time
		if len(workerWorking) == 0:
			return time
		
		newWorkerWorking = workerWorking[:]
		for worker in workerWorking:
			worker.IncreaseTimeWorking()
			if worker.isBusy == False:
				workerFree.append(worker)
				newWorkerWorking.remove(worker)
				workingPointObj = GetPointByName(worker.workingStep)
				for outPoint in workingPointObj.outcomeList:
					outPointObj = GetPointByName(outPoint)
					outPointObj.incomeList.remove(worker.workingStep)
					if len(outPointObj.incomeList) == 0:
						queue.append(outPoint)
						queue.sort()
				worker.FreeWorker()
		workerWorking = newWorkerWorking
		
	#print 'next queue is :' + str(queue)
	#print 'There are %d available worker(s)' % len(workerFree)
	#print 'There are %d worker(s) is working' % len(workerWorking)
	
	newqueue = queue[:]
	for point in queue:
		if len(workerFree) == 0:
			break
		worker = workerFree.pop(0)
		worker.SetWorkingAt(point)
		workerWorking.append(worker)
		newqueue.remove(point)
	
	queue = newqueue
	return Flood2(queue, time, workerFree, workerWorking)

def SolvePart2():
	workerFree = []
	workerWorking = []
	time = -1
	queue = []
	#init worker pool
	for i in range(1, NUMBER_OF_WORKERS + 1):
		worker = Worker('#' + str(i))
		workerFree.append(worker)
	
	for point in pointList:
		if len(point.incomeList) == 0:
			queue.append(point.name)
	queue.sort()
	return Flood2(queue, time, workerFree, workerWorking)
	
def GetPointByName(name):
	for point in pointList:
		if point.name == name:
			return point
	return None

def PrintPart1(result):
	print '#Part1:'
	print 'Result: %s' % ''.join(result)

def PrintPart2(result):
	print '#Part2:'
	print 'Result: %d' % result
	
if __name__ == '__main__':
	#init something
	pointList = []
	pfile = open('input.txt', 'r')
	data = pfile.read().split('\n')
	ParsePoint(data)
	result_p1 = TopologicalSort()
	PrintPart1(result_p1)
	#Load point again
	ParsePoint(data)
	result_p2 = SolvePart2()
	PrintPart2(result_p2)
