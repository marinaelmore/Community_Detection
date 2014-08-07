import sys, getopt, re, json, io, math, os, tangelo, callDelite

def main():
	run("numLayers.txt:input/facebook")
	run("fileList.txt:input")

def run(me=""):
	root = "/home/armysummer/tangelo_html/community_detection/"
	textFile, inputDirectory = me.split(':')
	os.system('rm' + root + textFile)
	inputDirectory = root + inputDirectory
	dirs = os.listdir(inputDirectory)
	dirs.sort()
	fileList=open('/home/armysummer/tangelo_html/community_detection/' + textFile, 'w')
	for files in dirs:
		fileList.write(files)
		fileList.write('\n')
	fileList.close()


if __name__ == "__main__":
    main()