def allteams(filename):
	import csv
	with open(filename,'r') as csvfile:
		reader=csv.reader(csvfile)
		next(reader,None) #skipheaders
		#create a nested list containing each team's w/l
		global allteams
		allteams=[]
		testcount=0
		for row in reader:
			if [row[1],0,0] not in allteams:
				allteams.append([row[1],0,0])

		#print(allteams)
		#print(len(allteams))

def conferences(filename):
	import csv
	with open(filename,'r') as csvfile:
		reader=csv.reader(csvfile)
		next(reader,None)
		global east
		global west
		east=[]
		west=[]
		#why did the order of the for loops matter???
		for row in reader:
			for team in allteams:
				if team[0]==row[0]:
					team.append(row[2])

		for team in allteams:
			if team[3]=="West":
				west.append(team)
			else:
				east.append(team)
		#print(west)
		#print(east)

def update(filename):
	import csv
	with open(filename,'r') as csvfile:
		reader=csv.reader(csvfile)
		next(reader,None) #skipheaders
		for row in reader:
			for team in west:
				#win
				if team[0]==row[1] and row[5]=="Home":
					team[1]+=1
				elif team[0]==row[2] and row[5]=="Away":
					team[1]+=1
				#lose
				elif team[0]==row[2] and row[5]=="Home":
					team[2]+=1
				elif team[0]==row[1] and row[5]=="Away":
					team[2]+=1

			for team in east:
				#win
				if team[0]==row[1] and row[5]=="Home":
					team[1]+=1
				elif team[0]==row[2] and row[5]=="Away":
					team[1]+=1
				#lose
				elif team[0]==row[2] and row[5]=="Home":
					team[2]+=1
				elif team[0]==row[1] and row[5]=="Away":
					team[2]+=1

	print(east)
	print(west)


allteams("scores.csv")
conferences("div.csv")
update("scores.csv")
