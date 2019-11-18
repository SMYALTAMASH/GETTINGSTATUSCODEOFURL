#!/usr/bin/env python3
import os
import re
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
fileName="url.txt"
urllist=[]
validUrl=[]
invalidUrl=[]
Error
if not os.path.isfile(fileName):
	print("file doesn't exist")
	exit(0)
def printlist(listname):
	for name in listname:
		print(name)

with open(fileName) as f:
	for line in f:
		line= line.strip()
		if line == '':
			continue
		if re.match("^http",line):
			urllist.append(line)
		else:
			#append http at the beginning if it doesn't exist to save yourself from error
			urllist.append("http://"+line)

for req in urllist:
	try:
		response = urlopen(req)
	except HTTPError as e:
		print(str(req) + ' ' + str(e.code))
		invalidUrl.append(req)
	except URLError as e:
		print(str(req) + ' ' + str('404'))
		invalidUrl.append(req)
	else:
		print(str(req) + ' ' + str(response.status))
		validUrl.append(req)

print("\n\nvalid URL's are:\n")
printlist(validUrl)
print("\nInvalid URL's are:\n")
printlist(invalidUrl)
print("\nThe King Never Fails To Win His Destiny\n")
