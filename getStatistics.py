# FILE: getStatistics.py
# AUTHORS: Marina Elmore, Jennifer Hu
# AHPCRC Summmer Institute 2014
# -------------------------------------------------
# This program accesses the text files created by Delite to compile the statistics
# for the efficacy of the Louvain Algorithm. It returns a textfile that is then accessed
# by the display graph algorithm to populate the "Statistics Textbox"
#

import sys, os,commands
def main():
	run("facebook/facebook_1.txt")

def run(me=""):
	#Go to correct directory
	os.chdir('/home/armysummer/tangelo_html/community_detection/')
	
	#Get Paths
	path = 'input/' + me;
	dataset, input_file = me.split('/')
	level = int(input_file[len(input_file)-5:len(input_file)-4]) + 1
	stat_file =  "input/" + dataset + '/' + dataset + "_stat.txt"
	
	#Open Files
	final_stats = open('stats.txt', 'w')
	initial_stats = open(stat_file, 'r')
	curr_stats = open(path, 'r')
	
	
	#Add Title
	title = dataset.title() + " Level " + str(level)
	final_stats.write("<p><b>" + title + "</b><p>")

	final_stats.write("<p><b>Initial Statistics:</b>")

	#Add Initial Stats
	line = initial_stats.next()
	nodes, edges = line.split(' Number')
	final_stats.write('<br>' + nodes)
	final_stats.write('<br>Number' + edges + '</p>')
	final_stats.write('\n')

	#Add Iteration Stats
	final_stats.write("<p><b>Current Statistics:</b>")
	line = curr_stats.next()
	nodes, edges = line.split(' Number')
	final_stats.write('<br>' + nodes)
	final_stats.write('<br>Number' + edges)
	
	#Add modularity Stats
	line = curr_stats.next()
	old_mod, new_mod = line.split(' New')
	final_stats.write('<br>' + old_mod)
	final_stats.write('<br>New' + new_mod + "</p>")

	#Close files
	final_stats.close()
	initial_stats.close()
	curr_stats.close()

	return me


if __name__ == "__main__":
    main()