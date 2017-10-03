import string
import csv
d=dict()
d1=dict()
with open("Crime.csv", 'r') as myfile:
	reader = csv.reader(myfile)
	for row in reader:
		d[row[2]]=row[8],row[7]
	#for x in d.items():
	#	print(x)
	for key,value in d.items():
		d1[value]=d1.get(value,0)+1
	for x in d1.items():
		print(x)
		
	
