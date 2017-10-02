import string
import csv
with open("Crime.csv", 'r') as myfile:
	reader = csv.reader(myfile)
	for row in reader:
		d=dict()
		d[row[8]]=row[7]
		print(d)
	for value in d:
		d1=dict()
		print(value)
		print(type(value))
		d1[value]=d.get(value,0)+1
		print(d1)
