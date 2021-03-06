"""Looks up Variables off the online MEPS database

author: chris @ sihrc
"""
#Python Modules
from bs4 import BeautifulSoup
from operator import itemgetter
from urllib2 import urlopen 
import sys
#Local Modules
import config
from wrappers import debug

def formatValues(line):
	"""
	Formats the table of values into 3 columns 
	"""
	line.insert(0,["Values", "Unweighted", "Weighted"])
	colLengths = [[],[],[]]
	[[colLengths[i].append(len(cols[i])) for i in xrange(3)] for cols in line]
	maxLengths = [max(col) for col in colLengths]
	
	body = ["\t".join([(maxLengths[x] - len(cols[x])) * " " + cols[x] for x in xrange(3)]) for cols in line]
	return "\n".join(body[:-1]) + "\n\n" + body[-1]

def getDetails(dataset, variable):
	"""
	Takes in the dataset filename and the variable name 
	Performs the HTTP GET Request and returns a information about the feature
	"""

	url = "http://meps.ahrq.gov/data_stats/download_data_files_codebook.jsp?PUFId=%s&varName=%s" % (dataset, variable)
	page = urlopen(url)
	soup = BeautifulSoup(page.read())
	details = []
	for line in soup.findAll('font', {'class':"smallBlack"}):
		details.append(line.text.encode('utf8').strip())
	return dict([("Title", "\n".join(details[:3])), ("Name", details[4]), ("Description", details[6]), ("Format", details[8]), ("Type", details[10]), ("Range", details[12] + "~" + details[14]), ("Values", formatValues([details[n:n+3] for n in xrange(15,len(details),3)]))])

def getValues(dataset, variable):
	"""
	Takes in the dataset filename and the variable name 
	Performs the HTTP GET Request and returns a list of decoded values
	"""
	url = "http://meps.ahrq.gov/data_stats/download_data_files_codebook.jsp?PUFId=%s&varName=%s" % (dataset, variable)
	page = urlopen(url)
	soup = BeautifulSoup(page.read())
	details = []
	for line in soup.findAll('font', {'class':"smallBlack"}):
		details.append(line.text.encode('utf8').strip())
	return "".join(["".join(details[n:n+3]) for n in xrange(15,len(details),3)])

def getValuesCategories(dataset, variable):
	url = "http://meps.ahrq.gov/data_stats/download_data_files_codebook.jsp?PUFId=%s&varName=%s" % (dataset, variable)
	page = urlopen(url)
	soup = BeautifulSoup(page.read())
	details = []
	for line in soup.findAll('font', {'class':"smallBlack"}):
		details.append(line.text.encode('utf8').strip())
	return (15 - len(details))/3

def print_variable(decoded):
	"""
	Format prints decoded values for getDetails
	"""
	for head,body in decoded.iteritems():
		print head
		print "================================================="
		print body
		print "\n"	
@debug
def writeFeatureImportance(model, trainFeature, datafile):
	"""
	Formats and prints the importance of each feature
	author: Jazmin 
	TODO: right now it gets the actual name of the features in a HORRIBLE NOT EFFICIENT WAY make it better
	"""
	importances = zip(range(trainFeature.shape[1]), model.feature_importances_)
	importances.sort(key = itemgetter(1))
	with open(config.path("..", "data", datafile, "featureImportance.py"), "wb") as f:
		f.write("importance = ")
		for featureIndex,importance in importances[::-1]:
			variable = config.feature_dict["H147"][featureIndex]
			f.write(" " + str(variable) + " " + str(importance) + " " + str(dc.getData(datafile)[0][variable][0]) + " \n")

@debug
def lookUpVariable(datafile, variable):
	"""
	Generic Variable look up that prints out everything
	"""
	return print_variable(getDetails(datafile, variable))
if __name__ == "__main__":
	datafile = sys.argv[1]
	# writeFeatureList(datafile)
	# writeChosenFeatures(datafile)
	# lookUpVariable(datafile,"PMEDPY42")
	while (True):
		feature = raw_input()
		print  getDetails(datafile, feature)["Values"]
		print  getDetails(datafile, feature)["Description"]