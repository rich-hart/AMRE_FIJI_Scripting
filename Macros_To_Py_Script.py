#!/usr/bin/env python
# encoding: utf-8
"""
Macros_To_Py_Script.py


Make sure the default options that you want have been recorded by the Fiji macro.  That way they will always have the right configuation when the script is running

"""

import sys
import os

from ij import IJ

dir_path= "/Users/richardhart/Dropbox/AMRE/"
file_name="2013-08-03-96dpiPrintTesting-DifferentZheights-Sample.png"

def main():
	
	
	IJ.open(dir_path+file_name) #IJ.open("/Users/richardhart/Dropbox/AMRE/2013-08-03-96dpiPrintTesting-DifferentZheights-Sample.png")
	
	IJ.selectWindow(file_name) #IJ.selectWindow("2013-08-03-96dpiPrintTesting-DifferentZheights-Sample.png")
	
	IJ.run("Options...", "iterations=1 count=1 edm=Overwrite") #setting binary mask options
	
	IJ.run("Make Binary") #converting a picture o a binary image. 

	IJ.run("Watershed")	#Watershed breaks appart blobs in a binary image into smaller pieces
	
	IJ.run("Set Measurements...", "area mean standard modal min centroid center perimeter bounding fit shape feret's integrated median skewness kurtosis area_fraction stack redirect=None decimal=3") #Specifying what measurements to take 
	
	IJ.run("Analyze Particles...", "size=0-Infinity circularity=0.00-1.00 show=Ellipses display clear include") #taking measurements
	
	IJ.selectWindow("Results") #Making sure the results are selected so the window's data will be saved
	
	IJ.saveAs("Results", dir_path + "Results.txt"); #IJ.saveAs("/Users/richardhart/Dropbox/AMRE/Results.txt")

if __name__ == '__main__':
	main()

