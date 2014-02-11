"""
Contains visualization data scripts

author: jazmin
"""

#To-DO Create a Visuals module that holds all the visualization TASKS
import matplotlib.pyplot as plt
from stats import *
import numpy as np

#Debug Timer Wrappers
from wrappers import debug

@debug
def FeatureVsCost(data, var):
		try:
			new_data = data.getColumn(var)
			plt.scatter(new_data, data.cost)
			print "Plotting " + var + " vs cost plot"
			plt.xlabel(data.lookUp(var = var)[0])
			plt.ylabel("Cost in dollars")
			plt.savefig("../visuals/feature_v_cost/" + data.lookUp(var = var)[0].replace(" ", "_") + ".png")
		except:
			print "Plotting " + var + " failed"

@debug
def AllFeatureVsCost(data):
	for i in range (len(data.features)):
		FeatureVsCost(data,"V" + str(i))

@debug
def GraphPmf(data, save, bins, show = True):
	
	if len(set(data)) == 1: 
		print "Only one Bin Found"
		return	
	pmf = ts2.MakePmfFromList(data)

	new_dats = ts2.BinData(data, min(data), max(data), bins)
	bin_pmf = ts2.MakePmfFromList(list(new_dats))

	tp.SubPlot(2, 1, 1)
	tp.Hist(pmf)
	tp.Config(title='Naive Pmf')

	tp.SubPlot(2, 1, 2)
	tp.Hist(bin_pmf)
	tp.Config(title='Binned Hist')

	if show:
		tp.Show()
	tp.Save(filename = save, formats = "jpg")

def GraphCostCdf(pmf):
	cdf = ts2.MakeCdfFromPmf(pmf)
	tp.Cdf(cdf)
	tp.Config(title='CDF')
	tp.Show()

def GraphCostPdf(data):
	pdf = thinkstats2.EstimatedPdf(data)
	xs = np.linspace(min(data), max(data), 101)
	kde_pmf = pdf.MakePmf(xs)
	tp.Pmf(kde_pmf)
	tp.Config(title='KDE PMF')
	td.Show()
