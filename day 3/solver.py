MAX_W = 1500
MAX_H = 1500

Area = [[0 for x in range(MAX_W)] for y in range(MAX_H)]

def InitArea():
	for i in range(0,MAX_W):
		for j in range(0,MAX_H):
			Area[i][j] == 0
	
def ClaimArea(info):
	#Parse Info
	tmp1 = info.split(' @ ')
	index = tmp1[0]
	
	tmp2 = tmp1[1].split(': ')
	
	tmp3 = tmp2[0].split(',')
	tmp4 = tmp2[1].split('x')
	
	x = int(tmp3[0])
	y = int(tmp3[1])
	
	w = int(tmp4[0])
	h = int(tmp4[1])
	
	
	for i in range(0,w):
		for j in range(0,h):
			if Area[x + i][y + j] != 0:
				Area[x + i][y + j] = 2
			else:
				Area[x + i][y + j] = 1
	
def Part1Result():
	result = 0
	for i in range(0,MAX_W):
		for j in range(0,MAX_H):
			if Area[i][j] == 2:
				result += 1
	return result

def CheckClaim(info):
	#Parse Info
	tmp1 = info.split(' @ ')
	index = tmp1[0]
	
	tmp2 = tmp1[1].split(': ')
	
	tmp3 = tmp2[0].split(',')
	tmp4 = tmp2[1].split('x')
	
	x = int(tmp3[0])
	y = int(tmp3[1])
	
	w = int(tmp4[0])
	h = int(tmp4[1])
	
	for i in range(0,w):
		for j in range(0,h):
			if Area[x + i][y + j] != 1:
				return False
	
	return True
	
if __name__ == '__main__':
	pfile = open('input.txt', 'r')
	data = pfile.read()
	infoList = data.split('\n')
	InitArea()
	for info in infoList:
		ClaimArea(info)
	
	print '#Part 1:'
	print 'Result: %d' % Part1Result()
	
	print '\nPart2:'
	for info in infoList:
		if CheckClaim(info) == True:
			print 'Found fine claim: %s' % info
	
	
