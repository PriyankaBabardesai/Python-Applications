# ===============
# Modules
# ===============
import json as js
import pandas as pd
from tabulate import tabulate
# ===============
# Operations
# ===============

def LoadInputData():
	line = "*"*50
	print(line,"BMI Calculator",line)
	HeightInCm = []
	HeightInM = []
	WeightInKg = []
	
	# STEP 1 : Load data
	#data = {"Gender": "Male", "HeightCm": 171, "WeightKg": 96 }, {"Gender": "Male", "HeightCm": 161, "WeightKg": 85 }, {"Gender": "Male", "HeightCm": 180, "WeightKg": 77 },{"Gender": "Female", "HeightCm": 166, "WeightKg": 62}, {"Gender": "Female", "HeightCm": 150, "WeightKg": 70},{"Gender": "Female", "HeightCm": 167, "WeightKg": 82}
	fd = open('data2.json','r')
	data = js.load(fd)
	loadData = js.dumps(data)
	dataInDict = js.loads(loadData)
	print("Given Input Data : ")
	print(dataInDict)
	print()
	
	# STEP 2 : Separate out the Height
	for iCounter1 in range(len(dataInDict)):
		HeightInCm.append(dataInDict[iCounter1]["HeightCm"])
	
	# STEP 3 : Separate out the Weight
	for iCounter2 in range(len(dataInDict)):
		WeightInKg.append(dataInDict[iCounter2]["WeightKg"])
	
	# STEP 4 : Convert Height in Meters
	for iCounter3 in HeightInCm:
		HeightInMtr = iCounter3/100
		HeightInM.append(HeightInMtr)
	
	return HeightInM,WeightInKg

def CalculateBMI(HeightInM , WeightInKg):
	BMIList = []
	BMICategory =[]
	BMIRisk = []
	
	Category = ["Underweight", "Normal weight", "Overweight", "Moderately obese", "Severely obese", "Very severely obese"]
	HealthRisk = ["Malnutrition risk", "Low risk", "Enhanced risk", "Medium risk", "High risk", "Very high risk"]
	
	# STEP 5 : Calculate BMI
	for iCounter1 in range(len(HeightInM)):
		BMI = WeightInKg[iCounter1]/(HeightInM[iCounter1] * HeightInM[iCounter1])
		BMIList.append(BMI)
		
	# STEP 6 : Calculate BMI Category and Health Risk	
		if BMI <= 18.4:
			BMICategory.append(Category[0])
			BMIRisk.append(HealthRisk[0])
			
		elif BMI>=18.5 and BMI<= 24.9:
			BMICategory.append(Category[1])
			BMIRisk.append(HealthRisk[1])
			
		elif BMI>=25 and BMI<= 29.9:
			BMICategory.append(Category[2])
			BMIRisk.append(HealthRisk[2])
			
		elif BMI>=30 and BMI<= 34.9:
			BMICategory.append(Category[3])
			BMIRisk.append(HealthRisk[3])
			
		elif BMI>=35 and BMI<= 39.9:
			BMICategory.append(Category[4])
			BMIRisk.append(HealthRisk[4])
			
		else:
			BMICategory.append(Category[5])
			BMIRisk.append(HealthRisk[5])
		
	# STEP 8 : Show the output	
	dataForDF = {"Height In Meter": HeightInM, "Weight in Kg": WeightInKg, "BMI" : BMIList, "BMI Category": BMICategory, "Health Risk": BMIRisk}
	#print(dataForDF)
	
	df = pd.DataFrame(dataForDF)
	print("***************	BMI Calculator : All the details of person ******************")
	print(tabulate(df, headers = 'keys', tablefmt = 'psql'))
	
	# STEP 9 : Counting total number of overweight people
	iCntOverWeight =0
	for iCounter2 in range(len(BMICategory)):
		if BMICategory[iCounter2] == "Overweight":
			iCntOverWeight = iCntOverWeight+1
	print("")
	print("Number of Overweight people are : ",iCntOverWeight)
	
def main():
	HeightInM, WeightInKg = LoadInputData()
	CalculateBMI(HeightInM , WeightInKg)
	
if __name__ == "__main__":
	main()
	

	
