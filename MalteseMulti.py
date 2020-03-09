import csv

def main():
	with open("C:/Users/Chris/Documents/Research/MalteseCanopy-Flight-Plans/Maltese-Eden-60m/EdenWood-80-40-60m-merged.csv",'r') as csv_file:
		#open reader and create writer file
		csv_reader = csv.reader(csv_file, delimiter = ",")



		#First File at Nadir
		csv_nadir = csv.writer(open("EdenWood-80-60-50m-merged_Nadir.csv","w+",newline=''),delimiter=',')
		csv_oblique1 = csv.writer(open("EdenWood-80-40-60m-merged_Oblique1.csv","w+",newline=''),delimiter=',')
		csv_oblique2 = csv.writer(open("EdenWood-80-40-60m-merged_Oblique2.csv","w+",newline=''),delimiter=',')
		csv_oblique3 = csv.writer(open("EdenWood-80-40-60m-merged_Oblique3.csv","w+",newline=''),delimiter=',')
		csv_oblique4 = csv.writer(open("EdenWood-80-40-60m-merged_Oblique4.csv","w+",newline=''),delimiter=',')
		
		#write header row to new file to all files
		fieldnames = next(csv_reader)
		csv_nadir.writerow(fieldnames)
		csv_oblique1.writerow(fieldnames)
		csv_oblique2.writerow(fieldnames)
		csv_oblique3.writerow(fieldnames)
		csv_oblique4.writerow(fieldnames)

		#iterate through main file and create 5 new files
		for line in csv_reader:
		#get heading and convert to a flaot
			heading = float(line[3])
			if heading <0:
				heading = 360 + heading
			heading90 = (heading + 90)%360
			heading180 = (heading + 180)%360
			heading270 = (heading + 270)%360
			

			#DONE
			#write nadir file (basically duplicate)
			rowNadir = [line[0],line[1],line[2],str(heading),line[4],line[5],line[6],line[7],line[8],line[9],line[10],line[11],line[12],line[13],line[14],line[15],line[16],line[17],line[18],line[19],line[20],line[21],line[22],line[23],line[24],line[25],line[26],line[27],line[28],line[29],line[30],line[31],line[32],line[33],line[34],line[35],line[36],line[37]]
			csv_nadir.writerow(rowNadir)
			#DONE
			#write oblique 1 (-45 at same heading)
			oblique1 = [line[0],line[1],line[2],str(heading),line[4],line[5],line[6],str(-45),line[8],line[9],line[10],line[11],line[12],line[13],line[14],line[15],line[16],line[17],line[18],line[19],line[20],line[21],line[22],line[23],line[24],line[25],line[26],line[27],line[28],line[29],line[30],line[31],line[32],line[33],line[34],line[35],line[36],line[37]]
			csv_oblique1.writerow(oblique1)

			#write oblique 2 (-45 at heading+90)
			oblique2 = [line[0],line[1],line[2],str(heading90),line[4],line[5],line[6],str(-45),line[8],line[9],line[10],line[11],line[12],line[13],line[14],line[15],line[16],line[17],line[18],line[19],line[20],line[21],line[22],line[23],line[24],line[25],line[26],line[27],line[28],line[29],line[30],line[31],line[32],line[33],line[34],line[35],line[36],line[37]]
			csv_oblique2.writerow(oblique2)

			#write oblique 3 (-45 at heading+180)
			oblique3 = [line[0],line[1],line[2],str(heading180),line[4],line[5],line[6],str(-45),line[8],line[9],line[10],line[11],line[12],line[13],line[14],line[15],line[16],line[17],line[18],line[19],line[20],line[21],line[22],line[23],line[24],line[25],line[26],line[27],line[28],line[29],line[30],line[31],line[32],line[33],line[34],line[35],line[36],line[37]]
			csv_oblique3.writerow(oblique3)

			#write oblique 4 (-45 at heading+270)
			oblique4 = [line[0],line[1],line[2],str(heading270),line[4],line[5],line[6],str(-45),line[8],line[9],line[10],line[11],line[12],line[13],line[14],line[15],line[16],line[17],line[18],line[19],line[20],line[21],line[22],line[23],line[24],line[25],line[26],line[27],line[28],line[29],line[30],line[31],line[32],line[33],line[34],line[35],line[36],line[37]]
			csv_oblique4.writerow(oblique4)


		













main()		
	
	
