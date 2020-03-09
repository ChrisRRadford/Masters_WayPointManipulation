import csv

def main():
	with open("..\FlightPlans\MalteseCross.csv",'r') as csv_file:
		#open reader and create writer file
		csv_reader = csv.reader(csv_file, delimiter = ",")
		csv_writer = csv.writer(open("PortraitModified.csv","w+",newline=''),delimiter=',')
		
		#write header row to new file
		csv_writer.writerow(next(csv_reader))

		for line in csv_reader:
			#get heading and convert to a flaot
			heading = float(line[3])
			if heading <0:
				heading = 360 + heading
			heading90 = (heading + 90)%360
			
			modified_row = [line[0],line[1],line[2],str(heading90),line[4],line[5],line[6],line[7],line[8],line[9],line[10],line[11],line[12],line[13],line[14],line[15],line[16],line[17],line[18],line[19],line[20],line[21],line[22],line[23],line[24],line[25],line[26],line[27],line[28],line[29],line[30],line[31],line[32],line[33],line[34],line[35],line[36],line[37]]
			csv_writer.writerow(modified_row)


main()		