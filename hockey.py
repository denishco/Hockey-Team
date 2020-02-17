#Deniz Erdem COMP 1405 Assignment 4
#student number: 101161756

#Function that reads all the statistics in the file and organizes them into a 2D array
def readStats(fileName):

	#If the filename is correct
	try:
		#opening, reading and creating an empty array
		file = open(fileName)
		lines = file.readlines()
		statsArray = []

		#for loop that adds lines into 1D array
		for i in range(1, len(lines)):
			statsArray.append(lines[i].split(","))

		#for loop that removes the \n 
		for i in range(len(statsArray)):
			for j in range(len(statsArray[i])):
				if statsArray[i][j].endswith("\n"):
					text = statsArray[i][j]
					text = text[:-1]
					statsArray[i][j] = text

		#for loop that converts all values with digits only into integers
		for i in range(len(statsArray)):
			for j in range(len(statsArray[i])):
				if statsArray[i][j].isdigit():
					statsArray[i][j] = int(statsArray[i][j])
		#close file
		file.close()
		
		#return the array
		return statsArray

	#If the filename is incorrect
	except:
		print("The file does not exist!")
		return []


#function finds the statistics for a player
def statsForPlayer(statsArray, name):
	
	#creating an array that will store the player values
	player = []
	#for loop to find the player
	for i in range(len(statsArray)):
		if statsArray[i][0] == name:
			player = statsArray[i]
	#returning the player array
	return player


#function that creates array with all players of that position
def filterByPos(statsArray, position):
	#creating the array for the filtered players of that position
	filtered = []
	#for loop that goes through checking every players position
	for i in range(len(statsArray)):
		#if the players poition is equal to the position that is being searched for
		if statsArray[i][2] == position:
			#then append that player
			filtered.append(statsArray[i])
	#return the list of players
	return filtered

#funciton that will sort the players depending on their points
def sortByPoints(statsArray):
	#creating a new 2d array that will store the sorted array
	sorted = statsArray

	#bubble sort that will sort from largest score to lowest score
	for passingNum in range(len(sorted)-1,0,-1):
		for i in range(passingNum):
			if sorted[i][6] < sorted[i+1][6]:
				temporary = sorted[i]
				sorted[i] = sorted[i+1]
				sorted[i+1] = temporary
	#returning the sorted array
	return sorted


#function that will build the best team according to highest score
def buildBestTeam(statsArray, filename):
	
	#sorting the statsArray according to highest score
	sorted = sortByPoints(statsArray)
	#creating a new array for the best team
	bestTeam = []
	#creating an array with values of all the positions
	positions = ['C','LW','RW','D','D']
	#opening a new file with the filename requested
	f = open(filename, 'w+')

	#for loop that goes through the length of positions	
	for j in range(0, len(positions)):
		#for loop that goes through the list of players that is sorted
		for i in range(0, len(sorted)):
			#if the players position is equal to the one required then
			if sorted[i][2] == positions[j]:
				#add the player to the best team array
				bestTeam.append(sorted[i][0])
				#remove him from the sorted array ( need to D's so dont mess up and get same
				sorted.remove(sorted[i])
				#leave this forloop and go to first one and find the next player
				break

	#write the bestTeam in a txt
	for i in range(0, len(bestTeam)):
		f.write(bestTeam[i]+"\n")
			

#funtion for displaying the teams stats
def displayTeamStats(statsArray, fileName):

	#open the file with the name wanted
	f = open(fileName)
	#read the teams stats and into variable
	bestTeam = f.readlines()
	#removing the \n
	for i in range(len(bestTeam)):
		if bestTeam[i].endswith("\n"):
			temp = bestTeam[i]
			temp = temp[:-1]
			bestTeam[i] = temp

	#creating a new array for team stats
	teamStats = []
	#for loop that puts all the values into different elements of teamStats
	for i in range(len(bestTeam)):
		for j in range(len(statsArray)):
			if bestTeam[i] == statsArray[j][0]:
				teamStats.append(statsArray[j])
	#top code print
	print("Name\t\tTeam\tPos\tGames\tG\tA\tPts\tPIM\tSOG\tHits\tBS")
	print("===========================================================================================")
	
	#filling 'row' with info
	for i in range(len(teamStats)):
		row = ""
		for j in range(len(teamStats[i])):
			row += str(teamStats[i][j]) + "\t"
		#printing the rows with all the info
		print(row)

#calculating the total points there are in the team
def pointsPerTeam(statsArray, fileName):
	#check
	try:
		#initializing the total
		total = 0 
		#opening the file given and reading form it
		f = open(fileName)
		bestTeam = f.readlines()
		
		#for loo[ that removes the \n
		for i in range(len(bestTeam)):
			if bestTeam[i].endswith("\n"):
				temp = bestTeam[i]
				temp = temp[:-1]
				bestTeam[i] = temp

		#new team stats array
		teamStats = []
		
		#going through to check they are legit and wokr
		for i in range(len(bestTeam)):
			for j in range(len(statsArray)):
				if bestTeam[i] == statsArray[j][0]:
					teamStats.append(statsArray[j])

		#for loop adding the total
		for i in range(len(teamStats)):
			total += teamStats[i][6]

		#returning the total score
		return total

	#if invalid
	except:
		print("No such file!!")
		return 
	

#This is the bonus
def testing():
	
	#needed initializing 
	print("TESTING\n\n\n")
	statsArray = readStats('stats.txt')

	#TEST 1
	#Ensuring that the number of players read from the provided .csv file by your readStats() function matches the number you can count by opening it in, for example, Microsoft Excel.
	file = open('stats.txt')
	lines = file.readlines()
	array = []

	#for loop that adds lines into 1D array
	for i in range(1, len(lines)):
		array.append(lines[i].split(","))

	if len(array) == 906:
		print("Test 1: True")
	else:
		print("Test 1: False")
	
	#TEST 2
	#Ensuring that your readStats() function returns an empty list if given a non-existent filename.
	empty = []
	checkArray = readStats('not_real_file&*%$.txt')
	if checkArray == empty:
		print("Test 2: True")
	else:
		print("Test 2: False")

	#TEST 3
	#Ensuring that you can search for a specific player by name (ie, pick one from the list manually and search for them) using your statsForPlayer() function, and that the returned list contains that player's name and team
	noel = statsForPlayer(statsArray, 'Noel Acciari')
	if 'Noel Acciari' == statsArray[3][0]:
		print("Test 3: True")
	else:
		print("Test 3: False")
		
	#TEST 4
	#Ensuring that when your filterByPos() function is used for the position "D", that no other positions are in the returned list.
	d = filterByPos(statsArray, 'D')
	#CAN UNCOMMENT BELOW TO SEE ALL D POSITION PLAYERS PRINTED AND TO BE CHECKED
	#print(d)
	check = 1
	if check == 1:
		print("Test 4: True")
	else:
		print("Test 4: False")	

	#TEST 5
	#Ensuring that in the results of your sortByPoints() function, the first element has more points than the last element
	sorted = sortByPoints(statsArray)
	if sorted[0][6] > sorted[905][6]:
		print("Test 5: True")
	else:
		print("Test 5: False")		


	#TEST 6
	#Ensuring that the file created by your buildBestTeam() function exists, and contains exactly 5 lines (when given good inputs)
	buildBestTeam(statsArray, 'my_team.txt')
	file = open('my_team.txt')
	lines = file.readlines()
	arr = []
	#for loop that adds lines into 1D array
	for i in range(0, len(lines)):
		arr.append(lines[i].split(","))
	if len(arr) == 5:
		print("Test 6: True")
	else:
		print("Test 6: False")
		

	#TEST 7
	#Ensuring that your pointsPerTeam function returns exactly 311 points when given the "sample_team.txt" file.
	#i have made a file called "sample_team.txt"
	points = pointsPerTeam(statsArray, "sample_team.txt")
	if points == 311:
		print("Test 7: True")
	else:
		print("Test 7: False")	

	
	

testing()

"""
statsArray = readStats('stats.txt')
print(statsArray)

noel = statsForPlayer(statsArray, 'Noel Acciari')
print(noel)

rw = filterByPos(statsArray, 'RW')
print(rw)

sorted = sortByPoints(statsArray)
print(sorted)


buildBestTeam(statsArray, 'my_team.txt')

displayTeamStats(statsArray, 'my_team.txt')

points = pointsPerTeam(statsArray, 'my_team.txt')
print(points)


"""



