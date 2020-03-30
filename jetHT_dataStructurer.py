#=========================================================================================
# jetHTplots.py --------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------
# Author(s): Brendan Regnery -------------------------------------------------------------
#-----------------------------------------------------------------------------------------

# modules
import ROOT as root
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg') #prevents opening displays (fast), must use before pyplot
import matplotlib.pyplot as plt
import h5py
import uproot

# import modules from other directories
import style.histogramsettings as settings
import fitting.rootpdfs as pdf
import fitting.fitwithroot as fit

# enter batch mode in root (so python can access displays)
root.gROOT.SetBatch(True)

#=========================================================================================
# Load Data ------------------------------------------------------------------------------
#=========================================================================================

# list of files
fnames = []
path = "root://cmseos.fnal.gov//store/user/bregnery/JetHT/crab_run2017B_JetHT/200317_121342/0000/BESToutputs_"
fileNums = np.arange(1,123,1)
for fileNum in fileNums:
    filePath = path + str(fileNum) + ".root"
    if fileNum == 23 or fileNum == 32 or fileNum == 109: continue
    fnames.append(filePath)
path = "root://cmseos.fnal.gov//store/user/bregnery/JetHT/crab_run2017C_JetHT/200317_130258/0000/BESToutputs_"
del fileNums
fileNums = np.arange(1,189,1)
for fileNum in fileNums:
    filePath = path + str(fileNum) + ".root"
    if fileNum == 65 or fileNum == 121: continue
    fnames.append(filePath)
path = "root://cmseos.fnal.gov//store/user/bregnery/JetHT/crab_run2017D_JetHT/200317_130526/0000/BESToutputs_"
del fileNums
fileNums = np.arange(1,88,1)
for fileNum in fileNums:
    filePath = path + str(fileNum) + ".root"
    fnames.append(filePath)
path = "root://cmseos.fnal.gov//store/user/bregnery/JetHT/crab_run2017E_JetHT/200317_130702/0000/BESToutputs_"
del fileNums
fileNums = np.arange(1,206,1)
for fileNum in fileNums:
    filePath = path + str(fileNum) + ".root"
    fnames.append(filePath)
path = "root://cmseos.fnal.gov//store/user/bregnery/JetHT/crab_run2017F_JetHT/200317_130746/0000/BESToutputs_"
del fileNums
fileNums = np.arange(1,254,1)
for fileNum in fileNums:
    filePath = path + str(fileNum) + ".root"
    fnames.append(filePath)


# access all the trees and make a data frame
print "Saved file names, beginning to make dataframe"
numIter = 0
for arrays in uproot.pandas.iterate(fnames, "run/jetTree", flatten=False):
    if numIter == 0 :
        jetDF = arrays
    else:
        jetDF = jetDF.append(arrays, ignore_index = True)
    numIter += 1

#=========================================================================================
# Save Jet Information -------------------------------------------------------------------
#=========================================================================================

jetDF.to_pickle("jetHT_2017.pkl")

print "Mischief Managed"
