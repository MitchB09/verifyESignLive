import requests, json
from datetime import datetime

host = "https://apps.esignlive.com"
packageUrl = "/api/packages"

def _getPackage(apiKey, packageId):
	r=requests.get(host + packageUrl + "/" + packageId, 
	headers=
		{"Accept":"application/json", 
		 "Content-Type":"application/json", 
		"Authorization":"Basic " + apiKey }
	)

	if r.status_code == 200:
		return r.json()
	else:
		return None

def validateSentPackagePackage(apiKey, packageId, endOutageDate):
	package = _getPackage(apiKey, packageId)
	if package is None:
		print("PackageId=[" + packageId + "] Not found or deleted")
		return True
	elif package["trashed"]:
		print("PackageId=[" + packageId + "] is trashed")
		return True
	elif "SENT" != package["status"] and datetime.strptime(package["completed"], "%Y-%m-%dT%H:%M:%SZ") <= endOutageDate:
		print("PackageId=[" + packageId + "] Status=[" + package["status"] + "] Trashed=[" + str(package["trashed"]) + "]")
		return False
	elif "SENT" != package["status"] and datetime.strptime(package["completed"], "%Y-%m-%dT%H:%M:%SZ") > endOutageDate:
		print("PackageId=[" + packageId + "] completed after end outage date")
		return True
	else:
		return True
