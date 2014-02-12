"""
Main Script for data
"""
import analyze as an
import visuals as vis
import data as dc
import outliers as out
import os

def GetCostForBinnedFeature(dataL, var):
	graphData = []
	for low,high,data in dataL[1:]:
		ranges = "_" + str(low) + "-" + str(high)
		name = d.lookUp(var = var)[0] + ranges + ".jpg"
		name = name.replace(" ","").replace(":","")
		if len(data) <= 2:
			print var + ranges, " does not have multiple data points!"
			continue
		graphData.append((low,high,data))
		path = os.path.join("..","visuals","feature_bin_costs")
		if not os.path.exists(path):
			os.makedirs(path)
		#vis.GraphPmf(data, os.path.join(path, name.replace("/", "")),10000, False)
		vis.GraphCdf(data, os.path.join(path, name.replace("/", "")))

if __name__ == "__main__":
	datasets = {"Hospital Inpatient Stays":"h144d.dat", "Emergency Room Visits":"h144e.dat", "Prescribed Medicines":"h144a.dat", "General Demographics":"h143.dat"}
	#dataset = datasets["Hospital Inpatient Stays"]
	#dataset = datasets["Emergency Room Visits"]
	#dataset = datasets["Prescribed Medicines"]
	#dataset = datasets["General Demographics"]

	d = dc.Data(codebook = dc.H144D, filename = dataset)
	GetCostForBinnedFeature(an.FeatureCostRange(d, "V24", True), "V24")
	#print data
