import string
import csv
d=dict()
d1=dict()
with open("Crime.csv", 'r') as myfile:
	reader = csv.reader(myfile)
	for row in reader:
		print(row)
		d[row[2]]=row[8],row[7]
	print(d)
	for key,value in d.items():
		d1=
	print(d1)
