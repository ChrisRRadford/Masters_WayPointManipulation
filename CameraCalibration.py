import csv
from operator import itemgetter
from math import sin, cos, sqrt, atan2, radians, degrees

#Number of WP Cannot Exceed 10
def main():
	with open("..\FlightPlans\CameraCalibration.csv",'r') as csv_file:
		#open reader and create writer file
		csv_reader = csv.reader(csv_file, delimiter = ",")
		print(type(csv_reader))
		csv_writer = csv.writer(open("CamreaCalibrationModified.csv","w+",newline=''),delimiter=',')
		
		#write header row to new file
		csv_writer.writerow(next(csv_reader))
		#read everything into list of rows
		#---------------------Tier 1
		#iterate through first pass 
		for line in csv_reader:
			#get heading and convert to a flaot
			heading = float(line[3])
			if heading <0:
				heading = 360 + heading
			# heading90 = (heading + 90)%360
			#create modified row 
			row = [line[0],line[1],line[2],str(heading),line[4],line[5],line[6],line[7],line[8],line[9],line[10],line[11],line[12],line[13],line[14],line[15],line[16],line[17],line[18],line[19],line[20],line[21],line[22],line[23],line[24],line[25],line[26],line[27],line[28],line[29],line[30],line[31],line[32],line[33],line[34],line[35],line[36],line[37]]
			csv_writer.writerow(row)
		
		csv_file.seek(0)
		next(csv_reader)
		#Rotate 90
		for line in csv_reader:
			heading = float(line[3])
			if heading <0:
				heading = 360 + heading
			heading90 = (heading + 90)%360

			#create modified row 
			row = [line[0],line[1],line[2],str(heading90),line[4],line[5],line[6],line[7],line[8],line[9],line[10],line[11],line[12],line[13],line[14],line[15],line[16],line[17],line[18],line[19],line[20],line[21],line[22],line[23],line[24],line[25],line[26],line[27],line[28],line[29],line[30],line[31],line[32],line[33],line[34],line[35],line[36],line[37]]
			csv_writer.writerow(row)	
		
		csv_file.seek(0)
		next(csv_reader)
		#rotate -90
		for line in csv_reader:
			heading = float(line[3])
			if heading <0:
				heading = 360 + heading
			headingNeg90 = (heading - 90)%360

			#create modified row 
			row = [line[0],line[1],line[2],str(headingNeg90),line[4],line[5],line[6],line[7],line[8],line[9],line[10],line[11],line[12],line[13],line[14],line[15],line[16],line[17],line[18],line[19],line[20],line[21],line[22],line[23],line[24],line[25],line[26],line[27],line[28],line[29],line[30],line[31],line[32],line[33],line[34],line[35],line[36],line[37]]
			csv_writer.writerow(row)

		#---------------------Tier 2
		csv_file.seek(0)
		next(csv_reader)
		#iterate through first pass 
		for line in csv_reader:
			#get heading and convert to a flaot
			heading = float(line[3])
			if heading <0:
				heading = 360 + heading
			# heading90 = (heading + 90)%360
			#create modified row 
			row = [line[0],line[1],str(22.86),str(heading),line[4],line[5],line[6],line[7],line[8],line[9],line[10],line[11],line[12],line[13],line[14],line[15],line[16],line[17],line[18],line[19],line[20],line[21],line[22],line[23],line[24],line[25],line[26],line[27],line[28],line[29],line[30],line[31],line[32],line[33],line[34],line[35],line[36],line[37]]
			csv_writer.writerow(row)


		csv_file.seek(0)
		next(csv_reader)
		#rotate 90 
		for line in csv_reader:
			heading = float(line[3])
			if heading <0:
				heading = 360 + heading
			heading90 = (heading + 90)%360

			#create modified row 
			row = [line[0],line[1],str(22.86),str(heading90),line[4],line[5],line[6],line[7],line[8],line[9],line[10],line[11],line[12],line[13],line[14],line[15],line[16],line[17],line[18],line[19],line[20],line[21],line[22],line[23],line[24],line[25],line[26],line[27],line[28],line[29],line[30],line[31],line[32],line[33],line[34],line[35],line[36],line[37]]
			csv_writer.writerow(row)

		csv_file.seek(0)
		next(csv_reader)
		#rotate -90 
		for line in csv_reader:
			heading = float(line[3])
			if heading <0:
				heading = 360 + heading
			headingNeg90 = (heading - 90)%360

			#create modified row 
			row = [line[0],line[1],str(22.86),str(headingNeg90),line[4],line[5],line[6],line[7],line[8],line[9],line[10],line[11],line[12],line[13],line[14],line[15],line[16],line[17],line[18],line[19],line[20],line[21],line[22],line[23],line[24],line[25],line[26],line[27],line[28],line[29],line[30],line[31],line[32],line[33],line[34],line[35],line[36],line[37]]
			csv_writer.writerow(row)		

		#---------------------Tier 3
		csv_file.seek(0)
		next(csv_reader)
		#iterate through first pass 
		for line in csv_reader:
			#get heading and convert to a flaot
			heading = float(line[3])
			if heading <0:
				heading = 360 + heading
			# heading90 = (heading + 90)%360
			#create modified row 
			row = [line[0],line[1],str(27.43),str(heading),line[4],line[5],line[6],line[7],line[8],line[9],line[10],line[11],line[12],line[13],line[14],line[15],line[16],line[17],line[18],line[19],line[20],line[21],line[22],line[23],line[24],line[25],line[26],line[27],line[28],line[29],line[30],line[31],line[32],line[33],line[34],line[35],line[36],line[37]]
			csv_writer.writerow(row)

		csv_file.seek(0)
		next(csv_reader)
		for line in csv_reader:
			heading = float(line[3])
			if heading <0:
				heading = 360 + heading
			heading90 = (heading + 90)%360

			#create modified row 
			row = [line[0],line[1],str(27.43),str(heading90),line[4],line[5],line[6],line[7],line[8],line[9],line[10],line[11],line[12],line[13],line[14],line[15],line[16],line[17],line[18],line[19],line[20],line[21],line[22],line[23],line[24],line[25],line[26],line[27],line[28],line[29],line[30],line[31],line[32],line[33],line[34],line[35],line[36],line[37]]
			csv_writer.writerow(row)	

		csv_file.seek(0)
		next(csv_reader)
		#rotate -90 
		for line in csv_reader:
			heading = float(line[3])
			if heading <0:
				heading = 360 + heading
			headingNeg90 = (heading - 90) %360

			#create modified row 
			row = [line[0],line[1],str(27.43),str(headingNeg90),line[4],line[5],line[6],line[7],line[8],line[9],line[10],line[11],line[12],line[13],line[14],line[15],line[16],line[17],line[18],line[19],line[20],line[21],line[22],line[23],line[24],line[25],line[26],line[27],line[28],line[29],line[30],line[31],line[32],line[33],line[34],line[35],line[36],line[37]]
			csv_writer.writerow(row)


		#--------ADDING OBLIQUES

		#Pass Coordinates to be sorted into strips
		csv_file.seek(0)
		next(csv_reader)

		# get waypoint coordiantes
		coordinateList = []
		#add all coordinates in csv to a single list
		for line in csv_reader:
			coordinateList.append([line[0],line[1]])

		coordStrips = SortStrips(csv_reader,coordinateList)
		

		#-------------Output Check
		#print resultant strip
		print("Strip List")
		count = 1
		for strip in coordStrips:
			print(count, str(len(strip)))
			count += 1

		#Determine which outputs can be used for oblique iamgery

		obliqueCoordList = Oblique(coordStrips)

		#------------------Determine Center point and head for each point to be added

		#Determine center point of all the coordaintes
		centerPoint = CenterPoint(coordinateList)
		#Iterate through each oblique Wp, determine heading, and add write to final file
		for coord in obliqueCoordList:
			heading = centralHeading(coord,centerPoint)

			row = [coord[0],coord[1],str(27.43),str(heading),str(0.2),str(0),str(2),str(-45),str(1),str(0),str(-1),str(0),str(-1),str(0),str(-1),str(0),str(-1),str(0),str(-1),str(0),str(-1),str(0),str(-1),str(0),str(-1),str(0),str(-1),str(0),str(-1),str(0),str(-1),str(0),str(-1),str(0),str(-1),str(0),str(-1),str(0)]
			csv_writer.writerow(row)




#- Sort all the WP into respective strips
#- Requires csv_read and a coordinate list
#- Returns a list of lists with each strip containing its respective WP.
def SortStrips(csv_reader,coordinateList):
	#---------------------Obliques
	#Take coordinate list (list of lists) and add coordinates to lists reprenting a s ingle stip

	#Get the rise over run from the first two coordinates.
	rise = float(coordinateList[0][1]) - float(coordinateList[1][1])
	run = float(coordinateList[0][0]) - float(coordinateList[1][0])
	masterslope = rise/run

	#---Strip List set Up
	#add first two coordiantes to a strip
	templist = [coordinateList[0],coordinateList[1]]
	coordStrips = [templist]
	stripCount = 0
	switch = False


	#----------Iteration
	#iterate through remaining coordiantes and compare
	for coord1,coord2 in zip(coordinateList[1:-1:], coordinateList[2::]):
		#if previous waypoint was found to be on a new strip
		if switch == True:
			coordStrips[stripCount].append(coord2)

			rise = float(coord2[1]) - float(coord1[1])
			run = float(coord2[0]) - float(coord1[0])
			masterslope = rise/run

			switch = False
			continue
		#print(coord1,coord2)
		rise = float(coord2[1]) - float(coord1[1])
		run = float(coord2[0]) - float(coord1[0])
		slope = rise/run
		diff = abs(masterslope-slope)
		#they are in the same strip, add to current strip
		if diff < 0.5:
			coordStrips[stripCount].append(coord2)
		#new strip
		else:
			
			stripCount+= 1
			coordStrips.append([coord2])
			switch = True
	return(coordStrips)			

#Determine Outside Coordiantes to add obliques
def Oblique(StripList):
	#Check to see if outside strips can be used for creating oblique coordinates. 
	strip1len = len(StripList[0])
	strip2len = len(StripList[-1])

	#get everage of middle strips:
	wpSum = 0
	for strips in StripList[1:-1:]:
		wpSum += len(strips)

	#Calculate average strip length of interior strips and according cut off for outer stripe use
	
	#Base Case 1 - StripLength is less 2 or less
	if len(StripList) <= 2:
		coord1 = StripList[0][0]
		coord2 = StripList[0][-1]
		coord3 = StripList[-1][0]
		coord4 = StripList[-1][-1]
		print("Number of strips 2 or less; Outermost corners used")
		print(coord1,coord2,coord3,coord4)
		return[coord1,coord2,coord3,coord4]

	stripAvg = wpSum/(len(StripList)-2)
	cutoff = stripAvg*0.75
	
	coord1 = []
	coord2 = [] 
	coord3 = [] 
	coord4 = []
	#---------------------Four cases for adding obliques
	#Case 1: Neither are sufficient
	if(strip1len < cutoff and strip2len < cutoff):
		#Use the next inner strips
		coord1 = StripList[1][0]
		coord2 = StripList[1][-1]
		coord3 = StripList[-2][0]
		coord4 = StripList[-2][-1]

		print("Neither Outer strips are sufficient. Using first and last inner strip:")
		print(coord1,coord2,coord3,coord4)

	#Case 2: Strip 1 sufficient but not N
	elif(strip1len >= cutoff and strip2len < cutoff):
		coord1 = StripList[0][0]
		coord2 = StripList[0][-1]
		coord3 = StripList[-2][0]
		coord4 = StripList[-2][-1]

		print("First strip sufficient but not last. Using first strip and last inner strip:")
		print(coord1,coord2,coord3,coord4)

	#Case 3: Strip 1 not sufficient but N is
	elif(strip1len < cutoff and strip2len >= cutoff):
		#Use the next inner strips
		coord1 = StripList[1][0]
		coord2 = StripList[1][-1]
		coord3 = StripList[-1][0]
		coord4 = StripList[-1][-1]

		print("Last strip sufficient but not first. Using first inner strip and last strip:")
		print(coord1,coord2,coord3,coord4)
	#Case 4: Both Sufficient
	else:
		coord1 = StripList[0][0]
		coord2 = StripList[0][-1]
		coord3 = StripList[-1][0]
		coord4 = StripList[-1][-1]
		print("Both outer strips are sufficient. Using first and last strip:")
		print(coord1,coord2,coord3,coord4)

	#Determine Center point Bearings from each
	return[coord1,coord2,coord3,coord4]
	

def CenterPoint(coordinateList):
	#value to hold sums
	X = 0
	Y = 0
	Z = 0
	for coords in coordinateList:
		print(coords)
		lat = radians(float(coords[0]))
		lon = radians(float(coords[1]))

		X += cos(lat) * cos(lon)
		Y += cos(lat) * sin(lon)
		Z += sin(lat)              

	#find averages for x y and z
	n = len(coordinateList)
	X = float(X/n)
	Y = float(Y/n)
	Z = float(Z/n)

	

	#convert lat and long in radians to decimal coords
	finalLon = degrees(atan2(Y, X))
	finalLat = degrees(atan2(Z, sqrt(X * X + Y * Y)))
	point = [finalLat,finalLon]

	return point


def centralHeading(pointA,pointB):
	latPA = radians(float(pointA[0]))
	latPB =	radians(float(pointB[0]))

	diffLong = radians(float(pointB[1]) - float(pointA[1]))
	x = (sin(diffLong) * cos(latPB))
	y = (cos(latPA) * sin(latPB)) - (sin(latPA) * cos(latPB) * cos(diffLong))

	initial_bearing = atan2(x, y)
	initial_bearing = degrees(initial_bearing)
	compass_bearing = (initial_bearing + 360) % 360
	return compass_bearing




main()
	
	
