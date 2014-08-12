import sys, os,commands
def main():
	run("facebook/facebook_1.txt")

def run(me=""):
	os.chdir('/home/armysummer/tangelo_html/community_detection/')
	
	path = 'input/' + me;
	dataset, input_file = me.split('/')
	level = int(input_file[len(input_file)-5:len(input_file)-4]) + 1
	stat_file =  "input/" + dataset + '/' + dataset + "_stat.txt"
	
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
	
	#Modularity Stats
	line = curr_stats.next()
	old_mod, new_mod = line.split(' New')
	final_stats.write('<br>' + old_mod)
	final_stats.write('<br>New' + new_mod + "</p>")


	final_stats.close()
	initial_stats.close()
	curr_stats.close()

	return me


if __name__ == "__main__":
    main()