# import sys, getopt, re, json, io, math, os, tangelo, callDelite

# def main():
# 	run("facebook")

# def run(me=""):

# 	dataSet=me
# 	sys.stdout = open('file.txt', 'w')
# 	inputDirectory = "/home/armysummer/tangelo_html/community_detection/input/"+dataSet+"/"
# 	outputDirectory = "/home/armysummer/tangelo_html/community_detection/output/"+dataSet+"/"
	
# 	os.system('rm -rf ' + outputDirectory + '*')

# 	g = Graph() 

# 	#Directory List
# 	dirs = os.listdir(inputDirectory)
# 	dirs.sort()
# 	fileList=open('/home/armysummer/tangelo_html/jen/Research/AHPCRC-networks/pythonScript/fileList.txt', 'w')
# 	for files in dirs:
# 		fileList.write(files)
# 		fileList.write('\n')
# 	fileList.close()
	
# 	size=len(dirs)
# 	os.chdir(inputDirectory)
# 	for i in range(size):
# 		g.createDict(dirs[i])
# 		g.createJsonFile(i, dataSet) 
# 		g.clearAll
# 		print "end round"
# 	print "Dataset : ", dataSet

# 	return

# class Graph:
# 	graph={}

# 	def __init__(self): 
# 		self.graph={}

# 	def createDict(self, file_path): 
# 		count =0
# 		masterList=[]
# 		tempDict={}
# 		otherDict={}
# 		otherList=[]
# 		List =[]
# 		weightDictNode={}
# 		selfLink={}
# 		allNodes=[]

# 		b = open(file_path, 'r')
# 		for line in b.readlines():
# 			if not line.lstrip().startswith('n') and not line.lstrip().startswith('o'):
# 				parts = line.split()
# 				node1=parts[0]
# 				node2=parts[1]
# 				weight=parts[2]
# 				if len(parts)>=4 :
# 					optional_value=parts[3]
# 				else:
# 					optional_value=None

# 				node1=int(node1)
# 				node2=int(node2)
# 				weight=float(weight)

# 				if node1 not in allNodes:
# 					allNodes.append(node1)
# 				if node2 not in allNodes:
# 					allNodes.append(node2)
# 				if node1 == node2:
# 					selfLink[node1]=weight

# 				tempDict["" "source" ]= node1
# 				tempDict["" "target"  ]= node2
# 				tempDict["" "weight" ]= weight
# 				List.append(tempDict.copy())

# 		for i in range(len(allNodes)):
# 			otherDict["" "label" ]=allNodes[i]
# 			otherDict["" "group"]=allNodes[i]^2
# 			otherList.append(otherDict.copy())

# 		b.close()
	
# 		self.graph["" "links"]=List
# 		print "# links ", len(self.graph['links'])
# 		self.graph["" "nodes"]=otherList
# 		print "# nodes ", len(self.graph['nodes'])
# 		self.graph["" "self_loop"]=selfLink
# 		print "# self links: ", len(self.graph['self_loop'])
	

# 	def createJsonFile(self, index, name):
# 		outputDirectory="/home/armysummer/tangelo_html/community_detection/output/"+name
# 		if os.path.isdir("/home/armysummer/tangelo_html/community_detection/output/") == False:
# 			os.system('mkdir /home/armysummer/tangelo_html/community_detection/output/')
# 			os.chmod("/home/armysummer/tangelo_html/community_detection/output/", 0777)
# 		if os.path.isdir(outputDirectory) == False:
# 			makeFolder = 'mkdir '+outputDirectory
# 			os.system(makeFolder)
# 			os.chmod(outputDirectory, 0777)

# 		print json, "\n"
# 		print outputDirectory, "\n"
# 		index=str(index)
# 		jsonFile=outputDirectory+"/"+name+"_"+index+".json"
# 		with open (jsonFile, "w") as outfile:
#   			outfile.write(unicode(json.dumps(self.graph, sort_keys = False, skipkeys=True, ensure_ascii=True, check_circular=True, 
#   				allow_nan=True, cls=None, indent=1, separators=None, encoding='utf-8', default=None)))
#   		outfile.close()
#   		os.chmod(jsonFile, 0777)

#   	def clearAll(self):
#   		self.graph.clear()


# if __name__ == "__main__":
#     main()




import sys, getopt, re, json, io, math, os, tangelo, callDelite

def main():
	run("facebook")

def run(me=""):

	dataSet=me
	
	inputDirectory = "/home/armysummer/tangelo_html/community_detection/input/"+dataSet+"/"
	outputDirectory = "/home/armysummer/tangelo_html/community_detection/output/"+dataSet+"/"
	
	os.system('rm -rf ' + outputDirectory + '*')


	
	g = Graph() 

	#Directory List
	dirs = os.listdir(inputDirectory)
	dirs.sort()
	fileList=open('/home/armysummer/tangelo_html/jen/Research/AHPCRC-networks/pythonScript/fileList.txt', 'w')
	for files in dirs:
		fileList.write(files)
		fileList.write('\n')
	fileList.close()
	
	size=len(dirs)
	os.chdir(inputDirectory)
	for i in range(size):
		g.createDict(dirs[i])
		g.createJsonFile(i, dataSet) 
		g.clearAll
		print "end round"
	print "Dataset : ", dataSet

	return

class Graph:
	graph={}

	def __init__(self): 
		self.graph={}

	def createDict(self, file_path): 
		count =0
		masterList=[]
		tempDict={}
		otherDict={}
		otherList=[]
		List =[]
		weightDictNode={}
		selfLink={}

		node1count=0
		node2count=0
		weightcount=0

		branch=[]
		
		lineCount=0
		b = open(file_path, 'r')

		for line in b.readlines():
			lineCount=lineCount+1
			if not line.lstrip().startswith('N') and not line.lstrip().startswith('O'):
				parts = line.split()
				node1=parts[0]
				node2=parts[1]
				weight=parts[2]
				if len(parts)>=4 :
					optional_value=parts[3]
				else:
					optional_value=None

				if lineCount==3:
					node1prev=node1

				node1=int(node1)
				node2=int(node2)
				weight=float(weight)

				node1count=node1count+1
				node2count=node2count+1
				weightcount=weightcount+1

				if node1 == node2:
					selfLink[node1]=weight

				if node1==node1prev:
					if node1 not in branch:
						branch.append(node1)
					if node2 not in branch:
						branch.append(node2)

				tempDict["" "source" ]= node1
				tempDict["" "target"  ]= node2
				tempDict["" "weight" ]= weight
				List.append(tempDict.copy())

				node1prev=node1

		for i in range(len(branch)):
			otherDict["" "label" ]=branch[i]
			otherDict["" "group"]=branch[i]^2
			otherList.append(otherDict.copy())

		b.close()

		self.graph["" "links"]=List
		print "# links in graph dict", len(self.graph['links'])
		self.graph["" "nodes"]=otherList
		print "# nodes with more than one self link", len(self.graph['nodes'])
		#self.graph["" "selfLoop"]=selfLink
		#print "# selfLinks: ", len(self.graph['selfLoop'])
	

	def createJsonFile(self, index, name):
		outputDirectory="/home/armysummer/tangelo_html/community_detection/output/"+name
		if os.path.isdir("/home/armysummer/tangelo_html/community_detection/output/") == False:
			os.system('mkdir /home/armysummer/tangelo_html/community_detection/output/')
			os.chmod("/home/armysummer/tangelo_html/community_detection/output/", 0777)
		if os.path.isdir(outputDirectory) == False:
			makeFolder = 'mkdir '+outputDirectory
			os.system(makeFolder)
			os.chmod(outputDirectory, 0777)

		print json, "\n"
		print outputDirectory, "\n"
		index=str(index)
		jsonFile=outputDirectory+"/"+name+"_"+index+".json"
		with open (jsonFile, "w") as outfile:
  			outfile.write(unicode(json.dumps(self.graph, sort_keys = False, skipkeys=True, ensure_ascii=True, check_circular=True, 
  				allow_nan=True, cls=None, indent=1, separators=None, encoding='utf-8', default=None)))
  		outfile.close()
  		os.chmod(jsonFile, 0777)

  	def clearAll(self):
  		self.graph.clear()


if __name__ == "__main__":
    main()