# -*- coding: utf-8 -*-
# @Author: Chase Weimer
# @Date:   2018-09-13 12:03:34
# @Last Modified by:   kacml
# @Last Modified time: 2018-09-13 13:08:53

from datetime import datetime

class Row(object):
	"""docstring for Row"""
	def __init__(self, pfp, prod_cd, plant_cd, eng):
		#super(Row, self).__init__()
		self.pfp = pfp
		self.prod_cd = prod_cd
		self.plant_cd = plant_cd
		self.eng = eng

	def desc(self):
		print("PFP Number: " + self.pfp)
		print("Prod Code: " + self.prod_cd)
		print("Plant Code: " + self.plant_cd)
		print("Engineer: " + self.eng)


print("Preparing good data")
good_data_src = open("./PFPtoEngineerFQIPlantEngineer.txt", "r")
good_data = set()

for line in good_data_src:
	line_list = line.split(",")
	line_list = [ i.strip("\n").strip("\"") for i in line_list ]

	if len(line_list) == 4:
		good_data.add(Row(pfp=line_list[0], prod_cd=line_list[1], plant_cd=line_list[2], eng=line_list[3]))
	else:
		print("Good data: Row has wrong dimensions")
print("Good data prepared")

print("Preparing real data")
real_data_src = open("./legit_data.txt", "r")
real_data = set()

for line in real_data_src:
	line_list = line.split(",")
	line_list = [ i.strip("\n").strip("\"") for i in line_list ]
	if len(line_list) == 4:
		real_data.add(Row(pfp=line_list[0], plant_cd=line_list[1], prod_cd=line_list[2], eng=line_list[3]))
	else:
		print("Real data: Row has wrong dimensions")

print("Real data prepared")

print(Row(pfp="WH18A", plant_cd="C", prod_cd="T32", eng="VOSS") in real_data)

