from datetime import datetime
import time

class Guard:
	totalSleepMinutes = 0
	isSleeping = False
	isWorking = False
	lastSleepingTime = None
	guardID = ""
	minutesMap = None
	
	def __init__(self, ID):
		self.guardID = ID
		self.minutesMap = []
		for i in range(0, 60):
			self.minutesMap.append(0)
		
	def GetGuardID(self):
		return self.guardID
	
	def MapTheMinutesMap(self, startTime, endTime):
		for i in range(startTime.minute, endTime.minute):
			self.minutesMap[i] += 1
	
	def PrintMinutesMap(self):
		print 'map size: %d' % len(self.minutesMap)
		for i in range(0, 60):
			print '%d:%d' % (i ,(self.minutesMap[i]))
	
	def GetMostSleepingMoment(self):
		mmax = 0
		for i in range (0, 60):
			if self.minutesMap[i] > self.minutesMap[mmax]:
				mmax = i
		return mmax
		
	def WakeUp(self, atTime):
		self.isSleeping = False
		if self.isWorking:
			self.totalSleepMinutes += SubDatetime(atTime, self.lastSleepingTime)
			self.MapTheMinutesMap(self.lastSleepingTime, atTime)
	
	def FallsAsSleep(self, atTime):
		self.isSleeping = True
		if self.isWorking:
			self.lastSleepingTime = atTime
		
	def BeginShift(self):
		self.isWorking = True
		
	def EndShift(self):
		self.isWorking = False

		
class Task:
	time = None
	action = ""
	def __init__(self, task):
		tmp = task.split('] ')
		self.time = datetime.strptime(tmp[0], '[%Y-%m-%d %H:%M')
		self.action = tmp[1]
	
	def PrintTask(self):
		print str(self.time) + '\t\t' + self.action
	
	
def SubDatetime(time1, time2):
	return (time1 - time2).total_seconds() / 60.0
	
def GetGuardByID(guardList, guardID):
	for currentGuard in guardList:
		if currentGuard.GetGuardID() == guardID:
			return currentGuard
	
	return None

def GetGuardBeginShiftFromAction(action):
	tmp1 = action.split('Guard #')
	tmp2 = tmp1[1].split(' begins ')
	return tmp2[0]


	
def GetResult(guardList):
	lazyGuard = guardList[0]
	for currentGuard in guardList:
		if currentGuard.totalSleepMinutes > lazyGuard.totalSleepMinutes:
			lazyGuard = currentGuard
	
	#now get most sleeping moment
	print '#Part 1:'
	print 'The most lazy guard is #%s.\nTotal sleeping time is %d minutes.\nThe most sleeping moment at %d minute' % (lazyGuard.GetGuardID(), lazyGuard.totalSleepMinutes, lazyGuard.GetMostSleepingMoment())
	result = int(lazyGuard.GetGuardID()) * lazyGuard.GetMostSleepingMoment()
	print 'Result: %d' % (result)
	
	foundGuard = guardList[0]
	for currentGuard in guardList:
		foundGuardMap = foundGuard.minutesMap
		currentGuardMap = currentGuard.minutesMap
		if currentGuardMap[currentGuard.GetMostSleepingMoment()] > foundGuardMap[foundGuard.GetMostSleepingMoment()]:
			foundGuard = currentGuard
	
	foundGuardMap = foundGuard.minutesMap
	totalSleepTimes = foundGuardMap[foundGuard.GetMostSleepingMoment()]
	Result = int(foundGuard.GetGuardID()) * foundGuard.GetMostSleepingMoment()
	print '\n#Part 2:'
	print 'Found guard #%s sleep %d times at %d minutes.' % (foundGuard.GetGuardID(), totalSleepTimes ,foundGuard.GetMostSleepingMoment())
	print 'Result: %d' % Result

if __name__ == '__main__':
	pfile = open('input.txt', 'r')
	data = pfile.read()
	rawTaskList = data.split('\n')
	taskList = []
	for rawTask in rawTaskList:
		parsedTask = Task(rawTask)
		taskList.append(parsedTask)
	
	#sort the tasklist
	taskList.sort(key=lambda x: x.time, reverse=False)
	
	guardList = []
	
	currentGuard = None
	for currentTask in taskList:
		if currentTask.action == 'falls asleep':
			currentGuard.FallsAsSleep(currentTask.time)
		elif currentTask.action == 'wakes up':
			currentGuard.WakeUp(currentTask.time)
		elif 'begins shift' in currentTask.action:
			if currentGuard != None:
				currentGuard.EndShift()
			newGuardID = GetGuardBeginShiftFromAction(currentTask.action)
			currentGuard = GetGuardByID(guardList, newGuardID)
			if currentGuard == None:
				currentGuard = Guard(newGuardID)
				guardList.append(currentGuard)
			currentGuard.BeginShift()
		else:
			print 'got unknown action: %s' % currentTask.action
	
	GetResult(guardList)
