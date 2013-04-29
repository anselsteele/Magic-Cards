from Tkinter import *
import time
cardlist = []
newfile = open("/Users/melquiades/Desktop/magicdata.txt","r")
done = False
counter = 0

master = Tk()
cvs = Canvas(master,width = 700,height = 700)
cvs.pack()

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

	cardinput = raw_input('Name a card: ')
	finished = False
	card = 'not found'
	for element in cardlist:
		rightname = element[0]

		if finished == False:

			cardinput = list(cardinput)
			rightname = list(rightname)
			newinput = []

			concluded = False
			for item in rightname:
				if concluded == False:
					if item == '/':
						concluded = True
					else:
						newinput.append(item)
			rightname = newinput
			comparer = cmp(cardinput,rightname)

			if comparer == -1:
				print element[0]
				print element[1]
				print element[2]
				print element[3]
				print element[4]
				finished = True
				card = cardinput
			else:
				pass

		if finished == True:
			pass

	save = raw_input('Save card? y or n: ')
	copies = input('Number of copies: ')
	if save == 'y':
		card = ''.join(card)
		counter = 0
		while counter < copies:
			decklist.append(card)
			counter = counter + 1
	else:
		pass
	examine = raw_input('Look at deck? y or n: ')
	if examine == 'y':
		print decklist
	else:
		pass
	view = raw_input('View cards in deck? y or n: ')
	if view == 'y':
		xcorner1 = 0
		ycorner1 = 0
		xcorner2 = 105
		ycorner2 = 150

		xdisp = xcorner2 - xcorner1
		ydisp = ycorner2 - ycorner1

		nameratio = ydisp/10

		xnamecoord1 = xcorner1
		ynamecoord1 = ycorner1 + nameratio
		xnamecoord2 = xcorner2
		ynamecoord2 = ynamecoord1 + 30

		middlecoordx = xnamecoord1 + 40
		middlecoordy = ynamecoord1 + 15




		counter = 0
		for item in decklist:
			
			cvs.create_rectangle(xcorner1,ycorner1,xcorner2,ycorner2,fill = 'green')
			cvs.create_rectangle(xnamecoord1,ynamecoord1,xnamecoord2,ynamecoord2,fill = 'red')
			cvs.create_text(middlecoordx,middlecoordy,text = item)
	else:
		pass
master.mainloop()
