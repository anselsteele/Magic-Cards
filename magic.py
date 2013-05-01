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
		xcorner2 = 70
		ycorner2 = 100

		xdisp = xcorner2 - xcorner1
		ydisp = ycorner2 - ycorner1

		nameratio = ydisp/10

		xnamecoord1 = xcorner1
		ynamecoord1 = ycorner1 + nameratio
		xnamecoord2 = xcorner2
		ynamecoord2 = ynamecoord1 + 30


		coordxdisp = xnamecoord2 - xnamecoord1
		coordydisp = ynamecoord2 - ynamecoord1





		counter = 0
		for item in decklist:
			middlecoordx = xnamecoord1 + 40
			middlecoordy = ynamecoord1 + 15

			strlen = len(item)
			fontsize = '13'
			if strlen >= 3:
				fontsize = '13'
			if strlen >= 5:
				fontsize = '12'
			if strlen >= 7:
				fontsize = "11"
			if strlen >= 9:
				fontsize = "10"
			if strlen >= 11: 
				fontsize = "9"
			if strlen >= 13:
				fontsize = "8"
			if strlen >= 15:
				fontsize = "7"
			
			cvs.create_rectangle(xcorner1,ycorner1,xcorner2,ycorner2,fill = 'green')
			cvs.create_rectangle(xnamecoord1,ynamecoord1,xnamecoord2,ynamecoord2,fill = 'red')
			cvs.create_text(middlecoordx,middlecoordy,text = item,font = ("Helvectica",fontsize))

			xcorner1 = xcorner1 + xdisp
			xcorner2 = xcorner2 + xdisp
			xnamecoord1 = xnamecoord1 + coordxdisp
			xnamecoord2 = xnamecoord2 + coordxdisp

			counter = counter + 1

			if counter == 10:
				ycorner1 = ycorner1 + ydisp
				ycorner2 = ycorner2 + ydisp
				ynamecoord2 = ynamecoord2 + ydisp
				ynamecoord1 = ynamecoord1 + ydisp

				xcorner1 = 0
				xcorner2 = 70
				xnamecoord1 = xcorner1
				xnamecoord2 = xcorner2
				counter = 0


master.mainloop()
