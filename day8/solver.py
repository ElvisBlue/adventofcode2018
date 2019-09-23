class Node:
	child = []
	metadata = []
	name = ''
	def __init__(self, name):
		self.child = []
		self.metadata = []
		self.name = name

def ReadList():
	pfile = open('input.txt', 'r')
	data = pfile.read().split(' ')
	retList = []
	for c in data:
		retList.append(int(c))
	return retList
		
def ParseNode(input, offset, node):
	curr = 0
	delta = 0
	for i in range(0, input[offset]):
		childNode = Node(node.name + '-' + str(i))
		delta += ParseNode(input, offset + delta + 2, childNode)
		node.child.append(childNode)
	
	for i in range(0, input[offset+1]):
		node.metadata.append(input[2+offset+delta+i])
	
	return (2 + input[offset+1] + delta)
		
def SumAllMetaData(node):
	sum = 0
	for metadata in node.metadata:
		sum += metadata
	
	for child in node.child:
		sum += SumAllMetaData(child)
	
	return sum

def GetRoot(node):
	if len(node.child) ==0:
		return SumAllMetaData(node)
	
	root = 0
	for metadata in node.metadata:
		if metadata <= len(node.child):
			root += GetRoot(node.child[metadata-1])
	
	return root
	
if __name__ == '__main__':
	data = ReadList()
	node = Node('0')
	ParseNode(data, 0, node)
	print '#Part 1:'
	print 'Result = %d' % SumAllMetaData(node)
	print '#Part 2:'
	print 'Result = %d' % GetRoot(node)
	
