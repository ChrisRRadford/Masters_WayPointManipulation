import csv
import sys

inputFile = sys.argv[1]
saveFile = sys.argv[2]
saveFilePath = saveFile + ".csv"
with open(inputFile) as csv_file:
	#open reader and create writer file
	csv_reader = csv.reader(csv_file, delimiter = ",")
	csv_writer = csv.writer(open(saveFile,"w+",newline=''),delimiter=',')
	
	#write header row to new file
	csv_writer.writerow(next(csv_reader))

	for line in csv_reader:
		#get heading and convert to a flaot
		heading = float(line[3])
		if heading <0:
			heading = 360 + heading
		heading90 = (heading + 90)%360
		heading180 = (heading + 180)%360
		heading270 = (heading + 270)%360
		
		modified_row = [line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[8],line[9],str(5),str(-45),str(1),str(0),str(4),heading90,str(1),str(0),str(4),heading180,str(1),str(0),str(4),heading270,str(1),str(0),line[26],line[27],line[28],line[29],line[30],line[31],line[32],line[33],line[34],line[35],line[36],line[37]]
		csv_writer.writerow(modified_row)


	
sys.stdout.flush()