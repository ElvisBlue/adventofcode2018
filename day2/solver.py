def countChar(txt, c):
	result = 0
	for cc in txt:
		if cc == c:
			result += 1
	return result	

def IsValidTwo(txt):
	ignoreList = []
	for c in txt:
		if c in ignoreList:
			continue
		ignoreList.append(c)
		if countChar(txt, c) == 2:
			return True
	return False
	
def IsValidThree(txt):
	ignoreList = []
	for c in txt:
		if c in ignoreList:
			continue
		ignoreList.append(c)
		if countChar(txt, c) == 3:
			return True
	return False
	
def GetStringIfDifOne(str1, str2):
	if len(str1) != len(str2):
		return None
	
	i = 0
	result = ''
	for c in str1:
		if c == str2[i]:
			result += c
		i += 1
	
	
	if len(result) == (len(str1) - 1):
		return result
	else:
		return None

	
def SolvePart2(IDsList):
	print '#Part 2:'

	result = ''
	i = 0
	for ID in IDsList:
		for t in range(i, len(IDsList)):
			similarID = GetStringIfDifOne(ID, IDsList[t])
			if similarID != None:
				result = similarID
				break
		i += 1
		if result != '':
			break
	
	print 'Result: ' + result
	
if __name__ == '__main__':
	pfile = open('input.txt', 'r')
	data = pfile.read()
	IDsList = data.split('\n')
	Two = 0
	Three = 0
	for ID in IDsList:
		if IsValidTwo(ID):
			Two += 1
		if IsValidThree(ID):
			Three += 1
	print '#Part 1:'
	print 'checksum is %d' % (Two * Three)
	
	SolvePart2(IDsList)
