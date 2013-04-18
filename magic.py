from Tkinter import *
import time
cardlist = []
newfile = open("/Users/melquiades/Desktop/magicdata.txt","r")
done = False
counter = 0
while done == False:
  line = newfile.readline()
	cname = line
	line = newfile.readline()
	if line == 'Scheme':
		description = 'Illegal'
		datapoint = [cname, desription]
		cardlist.append(datapoint)
	else:
		cmana = line
		line = newfile.readline
		ctype = str(line)
		if ctype[0] == 'c':
			line = newfile.readline
			stats = line
		else:
			stats = 'none'
		completed = False
		description = ''
		while completed == False:
			line = newfile.readline()
			description = description + line
			if line == '\n':
				completed = True
		datapoint = [cname,cmana,ctype,stats,description]
		if datapoint[0] == '' and datapoint[1] == '':
			done = True
		else:
			cardlist.append(datapoint)
			print cardlist[counter]
			print counter
		counter = counter + 1
print counter
			


