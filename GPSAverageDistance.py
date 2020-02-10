from math import sin, cos, sqrt, atan2, radians
from itertools import combinations

def haversine(p1,p2):
	# approximate radius of earth in km
	R = 6373.0
	(x1, y1), (x2, y2) = p1, p2
	y1, x1, y2, x2 = map(radians, [y1, x1, y2, x2])


	dlon = y2 - y1
	dlat = x2 - x1

	a = sin(dlat / 2)**2 + cos(x1) * cos(x2) * sin(dlon / 2)**2
	c = 2 * atan2(sqrt(a), sqrt(1 - a))
	distance = R * c

	return(distance)


def DMSToDD(coordinate):
	D = int(coordinate[1:3])
	M = int(coordinate[3:5])
	S = float(coordinate[5:])
	DD = D + float(M)/60 + float(S)/3600
	return DD

def WPAvgDist(WPList):
	#covnert DMS GPS to DD GPS
	latList, longList = WPList[0],WPList[1]
	latListDD, longListDD = [],[]
	for element in latList:
		latListDD.append(DMSToDD(element))

	for element in longList:
		longListDD.append(DMSToDD(element))


	points = list(zip(latListDD,longListDD))
	distances = []

	#iterate over an compare points
	for i in range(0, len(points)):
		for ii in range(0, len(points)):
			distances.append(haversine(points[i],points[ii]))

	#remove all self comparisons
	for element in list(distances):
		if element == 0.0:
			distances.remove(element)
	print("Distances", distances)
	print(sum(distances) / len(distances)*100000)
	print("-----------------")
	return (sum(distances) / len(distances)*100000)

	# print("Average Distance", avg_distance, "cm")


masterList = [
				#WP1
				[
					["N413310.134200",
					 "N413310.132500",
					 "N413310.125600",
					 "N413310.125800", 
					 "N413310.128000"],
					["E215830.7548000",
					 "E215830.7582000",
					 "E215830.748200",
					 "E215830.750900",
					 "E215830.760800"]
				],
				#WP2
				[
					["N41339.624500",
					 "N41339.630600",
					 "N41339.631600",
					 "N41339.635100",
					 "N41339.636800"],
					["E215830.871500",
					 "E215830.865400",
					 "E215830.868800",
					 "E215830.878000",
					 "E215830.881000"]
				],
				#WP3
				[
					["N41339.706800",
					"N41339.711000",
					"N41339.721100",
					"N41339.734400",
					"N41339.734100"],
					["E215832.685900",
					"E215832.669300",
					"E215832.689100",
					"E215832.679900",
					"E215832.674900"]
				],
				#WP4
				[
					["N413310.083800",
					"N413310.078400",
					"N413310.075200",
					"N413310.075600",
					"N413310.070800"],
					["E215831.812300",
					"E215831.826200",
					"E215831.818600",
					"E215831.808600",
					"E215831.811900"]
				],
				#WP5
				[
					["N413310.916700",
					"N413310.911800",
					"N413310.902700",
					"N413310.998000",
					"N413310.995900",],
					["E215831.812300",
					"E215831.815200",
					"E215831.809500",
					"E215831.833000",
					"E215831.824600"]
				]
			]

avgWPDist = []
for waypoints in masterList:
	avgWPDist.append(WPAvgDist(waypoints))

print(sum(avgWPDist)/len(avgWPDist),"cm")

#0.00009452