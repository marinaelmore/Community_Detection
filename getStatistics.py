import sys, os,commands
def main():
	run("input/facebook/facebook_1.txt")

def run(me=""):

	text_stats = open('textfile.txt', 'w')
	text_file = open(me, 'r');

	for i in range (0,2):
		line = text_file.next()
		text_stats.write(line)

	text_stats.close()

	return me


if __name__ == "__main__":
    main()