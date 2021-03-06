#  FILE: callDelite.py
#  AUTHORS: Marina Elmore, Jennifer Hu
#  AHPCRC Summmer Institute 2014
#  -------------------------------------------------
#  This file calls Delite by navigating to the correct directory
#  and booting off Delite on the dataset chosen by the client. 
#  This program generates text files of source-target files that
#  are later passed on to the frontend graphing program


import sys, os,commands
def main():
	run("facebook_combined.txt:facebook:0.01:4")

def run(me=""):
	textFile, dataSet, convergence, thread = me.split(':');
	
	inputDirectory = "/home/armysummer/tangelo_html/community_detection/input/"+dataSet+"/"
	output_path = "/home/armysummer/tangelo_html/community_detection/output/"+dataSet+"/"
	os.system('rm -rf ' + inputDirectory + '*')
	os.system('rm -rf ' + output_path)

	

	delitePath = "./published/OptiGraph/bin/delite CommunityDetectionCompiler /home/armysummer/tangelo_html/community_detection/datasets/"+textFile+ " /home/armysummer/tangelo_html/community_detection/input/" + dataSet + "/"+dataSet+" "+convergence+ " -t"+thread
	os.chdir('/home/armysummer/hyperdsl')
	
	if os.path.isdir(inputDirectory) == False:
		os.chmod("/home/armysummer/tangelo_html/community_detection/input/", 0777)
		makeFolder = 'mkdir '+inputDirectory
		os.system(makeFolder)
		os.chmod(inputDirectory, 0777)
	
	status, output = commands.getstatusoutput(delitePath)
	print status, output
	return me


if __name__ == "__main__":
    main()