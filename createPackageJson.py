import os, sys, csv

def _createJsonStringForPackage(packageId):
	return ( 
	"{"
    "\"documentId\": \"\", "
    "\"message\": null, "
    "\"name\": \"PACKAGE_COMPLETE\", "
    "\"packageId\": \"" + packageId + "\", "
    "\"sessionUser\": \"\""
	"}"
    )

def _createFile(orgCode, orgCallbacks):
	if not os.path.exists("callbacks"):
		os.makedirs("callbacks")
	dirName = os.path.dirname(__file__)
	f= open(os.path.join(dirName, "callbacks\\" + orgCode + "_callbacks.json"),"w+")
	f.write("[\n" + str.join(",\n", orgCallbacks) + "\n]")
	f.close()

def createJsonForPackages():
	print("in method!")
	dirName = os.path.dirname(__file__)
	filePath = os.path.join(dirName, "badPackages1.csv")
	print(filePath)

	with open(filePath, newline="\n") as csvfile:
		reader = csv.reader(csvfile, delimiter=",")
		currOrg = ""
		orgCallbacks = []
		for row in reader:
			if currOrg == "":
				currOrg = row[1]
				print("Now Processing: " + currOrg)
			elif currOrg != row[1]:
				_createFile(currOrg, orgCallbacks)
				currOrg = row[1]
				orgCallbacks = []
				print("Now Processing: " + currOrg)
			orgCallbacks.append(_createJsonStringForPackage(row[0]))
		if len(orgCallbacks) > 0:
		  _createFile(currOrg, orgCallbacks)
		print("Done!")