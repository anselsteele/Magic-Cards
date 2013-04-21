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
		line = newfile.readline()
		ctype = line
		if ctype[0] == 'c':
			line = newfile.readline()
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
		if datapoint[0] == '':
			done = True
		else:
			cardlist.append(datapoint)
		if counter >= 13304:
			for element in cardlist:
				cname = element[0]
				cmana = element[1]
				ctype = element[2]
				stats = element[3]
				description = element[4]

				print cname
				print ''
				print cmana
				print ''
				print ctype
				print ''
				print stats
				print ''
				print description 
				print ''
				done = True

		counter = counter + 1
done = False
decklist = []
while done == False:
	card = raw_input('Name a card: ')
	rightname = 'void'
	finished = False
	for element in cardlist:
		rightname = element[0]
		if finished == False:
			print rightname
			print card

			if card == rightname:
				print rightname
				print element[1]
				print element[2]
				print element[3]
				print element[4]
				finished = True
		if finished == True:
			continue

	save = raw_input('Save card? y or n: ')
	if save == 'y':
		decklist.append(rightname)
	else:
		continue
	examine = raw_input('Look at deck? y or n: ')
	if examine == 'y':
		print decklist
	else:
		continue


			


