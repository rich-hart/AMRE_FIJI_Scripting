#!/usr/bin/env python
# encoding: utf-8
"""
Example_Script.py



"""

import sys
import os
from ij import IJ

dir_path= "/Users/richardhart/Dropbox/AMRE/"
file_name="2013-08-03-96dpiPrintTesting-DifferentZheights-Sample.png"

def main():
	IJ.open(dir_path+file_name)
	IJ.selectWindow(file_name)
	IJ.run("Options...", "iterations=1 count=1 edm=Overwrite")
	IJ.run("Make Binary")
	IJ.run("Watershed")
	IJ.run("Set Measurements...", "area mean standard modal min centroid center perimeter bounding fit shape feret's integrated median skewness kurtosis area_fraction stack redirect=None decimal=3")
	IJ.run("Analyze Particles...", "size=0-Infinity circularity=0.00-1.00 show=Ellipses display clear include")
	IJ.selectWindow("Results")
	IJ.saveAs("Results", dir_path + "Results.txt");


if __name__ == '__main__':
	main()

