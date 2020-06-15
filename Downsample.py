#Downsample a folder of image based on given parameter

import cv2
import os
import numpy as np 

#--grab image within loop
# img = cv2.imread("F:\Chapter5_MalteseCross\Tree Canopy\Edenwoods-8040-50m May 31\JPG\DJI_0020.JPG")
def main():
	print("Running")
	files = os.listdir("F:\Chapter5_MalteseCross\Tree Canopy\Edenwoods-8040-50m May 31\JPG")
	path = os.path.abspath("F:\Chapter5_MalteseCross\Tree Canopy\Edenwoods-8040-50m May 31\JPG")

	for file in files:
		# Grab Images
		fileName = os.path.join(path,file)
		if fileName.endswith(".JPG"):
			#downsample
			print("Now samplpling:",file)
			img = cv2.imread(fileName)
			downsampled = downsampling(img)

			#grab file path and join name
			writefile = os.path.join("F:\Chapter5_MalteseCross\Tree Canopy\Downsampled",file)
			cv2.imwrite(writefile,downsampled)

	print("Finished")	


def downsampling(src):
	#-- Downsampling process
	rows, cols, _channels = map(int, src.shape)
	imgUp = cv2.pyrUp(src, dstsize=(cols * 2, rows * 2))
	rows, cols, _channels = map(int, imgUp.shape)
	imgDown = cv2.pyrDown(imgUp, dstsize=(cols // 2, rows // 2))
	return imgDown


main()