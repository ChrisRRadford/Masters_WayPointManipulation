from math import sin, cos, sqrt, atan2, radians
from itertools import combinations

#Calculate distances between two GPS coordinates (in DD format)
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

# Convert DMS coordinate into DD coordinate notation
def DMSToDD(coordinate):
	D = int(coordinate[1:3])
	M = int(coordinate[3:5])
	S = float(coordinate[5:])
	DD = D + float(M)/60 + float(S)/3600
	return DD

#get the overall average between all points 
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
	# print("Distances", distances)
	# print(sum(distances) / len(distances)*100000)
	# print("-----------------")
	return (sum(distances) / len(distances)*100000)

	# print("Average Distance", avg_distance, "cm")


singleMission = [
				#WP1
				[
					["N413310.134200",
					 "N413310.132500",
					 "N413310.125600",
					 "N413310.125800", 
					 "N413310.128000"],
					["E215830.758000",
					 "E215830.752000",
					 "E215830.748200",
					 "E215830.750900",
					 "E215830.760800"]
				],
				#WP2
				[
					["N413310.696100",
					"N413310.697400",
					"N413310.694300",
					"N413310.691100",
					"N413310.689400"],
					["E215831.172100",
					"E215831.182400",
					"E215831.185400",
					"E215831.178900",
					"E215831.169500"]
				],
				#WP3
				[
					["N41339.847600",
					"N41339.843100",
					"N41339.843000",
					"N41339.841600",
					"N41339.840600"],
					["E215831.258700",
					"E215831.273100",
					"E215831.266800",
					"E215831.265600",
					"E215831.268000"]
				],
				#WP4
				[
					["N413310.510800",
					"N413310.508200",
					"N413310.507400",
					"N413310.503200",
					"N413310.502200"],
					["E215832.142100",
					"E215832.131200",
					"E215832.126400",
					"E215832.131600",
					"E215832.127300"]
				],
				#WP5
				[
					["N41339.876200",
					"N41339.875600",
					"N41339.874400",
					"N41339.872600",
					"N41339.871100"],
					["E215832.784000",
					"E215832.790400",
					"E215832.779000",
					"E215832.782700",
					"E215832.787200"]
				]
			]

# ----------------------------------

multiMission = [
				#WP1
				[
					["N413310.138400",
					 "N413310.137400",
					 "N413310.135300",
					 "N413310.134200", 
					 "N413310.134000"],
					["E215830.752100",
					 "E215830.752500",
					 "E215830.750600",
					 "E215830.751500",
					 "E215830.753400"]
				],
				#WP2
				[
					["N41339.638100",
					 "N41339.637900",
					 "N41339.637200",
					 "N41339.636300", 
					 "N41339.634300"],
					["E215830.882400",
					 "E215830.880400",
					 "E215830.882900",
					 "E215830.883600",
					 "E215830.879800"]
				],
				#WP3
				[
					["N41339.737200",
					"N41339.735500",
					"N41339.734100",
					"N41339.731700",
					"N41339.730500"],
					["E215832.675100",
					"E215832.672200",
					"E215832.672500",
					"E215832.676000",
					"E215832.675100"]
				],
				#WP4
				[
					["N413310.916600",
					"N413310.913600",
					"N413310.912300",
					"N413310.911900",
					"N413310.910200"],
					["E215831.820600",
					"E215831.822300",
					"E215831.821300",
					"E215831.821300",
					"E215831.812100"]
				],
				#WP5
				[
					["N413310.083600",
					"N413310.079500",
					"N413310.077600",
					"N413310.076200",
					"N413310.074300",],
					["E215831.821200",
					"E215831.824500",
					"E215831.822400",
					"E215831.814500",
					"E215831.815100"]
				]
			]



avgWPDist = []
for waypoints in singleMission:
	avgWPDist.append(WPAvgDist(waypoints))
print(avgWPDist)
print(sum(avgWPDist)/len(avgWPDist),"cm")
print("-----------------")
avgWPDist = []
for waypoints in multiMission:
	avgWPDist.append(WPAvgDist(waypoints))
print(avgWPDist)
print(sum(avgWPDist)/len(avgWPDist),"cm")

#0.00009452