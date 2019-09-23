import os
from time import sleep

pointArr = []

class Point:
	pos_x = 0
	pos_y = 0
	vel_x = 0
	vel_y = 0
	def __init__(self, pos_x, pos_y, vel_x, vel_y):
		self.pos_x = pos_x
		self.pos_y = pos_y
		self.vel_x = vel_x
		self.vel_y = vel_y

def ParseLine(line):
	tmp1 = line.split(', ')
	tmp2 = tmp1[0].split('=<')
	pos_x = int(tmp2[1])
	vel_y = int(tmp1[2].replace('>', ''))
	tmp3 = tmp1[1].split('> velocity=<')
	pos_y = int(tmp3[0])
	vel_x = int(tmp3[1])
	point = Point(pos_x, pos_y, vel_x, vel_y)
	return point
	
def PrintPoint(point):
	print 'pos: <%d , %d> ; vel: <%d, %d> ' % (point.pos_x, point.pos_y, point.vel_x, point.vel_y) 

def ReadList():
	pfile = open('input.txt', 'r')
	data = pfile.read().split('\n')
	for line in data:
		point = ParseLine(line)
		pointArr.append(point)

def GetMax():
	max_x = -9999999
	max_y = -9999999
	min_x = 9999999
	min_y = 9999999
	for point in pointArr:
		if point.pos_x > max_x:
			max_x = point.pos_x
		elif point.pos_x < min_x:
			min_x = point.pos_x
			
		if point.pos_y > max_y:
			max_y = point.pos_y
		elif point.pos_y < min_y:
			min_y = point.pos_y
	
	return [max_x, max_y, min_x, min_y]
		
def GetSquare():
	ret = GetMax()
	max_x = ret[0]
	max_y = ret[1]
	min_x = ret[2]
	min_y = ret[3]
			
	return (max_x - min_x) * (max_y - min_y)

def PrintPicture():
	ret = GetMax()
	max_x = ret[0]
	max_y = ret[1]
	min_x = ret[2]
	min_y = ret[3]
	
	#print 'max_x: %d' % max_x
	#print 'max_y: %d' % max_y
	#print 'min_x: %d' % min_x
	#print 'min_y: %d' % min_y
	picture = [['.' for x in range(max_y - min_y + 1)] for y in range(max_x - min_x + 1)]
	
	for point in pointArr:
		#print 'x: %d ; y: %d' % (point.pos_x, point.pos_y)
		picture[point.pos_x - min_x][point.pos_y - min_y] = '#'
	
	for i in range(0, max_y - min_y + 1):
		line = ''
		for j in range(0, max_x - min_x + 1):
			line += picture[j][i]
		print line

def MovingPoint():
	for point in pointArr:
		point.pos_x += point.vel_x
		point.pos_y += point.vel_y
	
def Solve():
	second = 0
	while True:
		os.system('cls')
		print '#Solving part 1 and part 2. Please pay attention' 
		print '%d second(s)' % second
		if GetSquare() < 90000:
			PrintPicture()
			sleep(1)
		MovingPoint()
		second += 1

if __name__ == '__main__':
	ReadList()
	Solve()
