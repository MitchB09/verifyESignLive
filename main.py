import os, sys, csv, validatePackage, createPackageJson
from datetime import datetime

dirName = os.path.dirname(__file__)
filePath = os.path.join(dirName, "packagesToCheck.csv")
f = open(os.path.join(dirName, "badPackages1.csv"),"w+")

with open(filePath, newline="\n") as csvfile:
	reader = csv.reader(csvfile, delimiter=",")
	
	for row in reader:
		if validatePackage.validateSentPackagePackage(row[2], row[0],  datetime(2018, 8, 25)):
			print("Correct Package")
		else:
			f.write(",".join(row) + "\n")
			print("Package did not pass validation")

f.close()
createPackageJson.createJsonForPackages()