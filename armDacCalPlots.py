#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# armDacCalPlots.py ///////////////////////////////////////////////////////////////
#==================================================================================
# Author(s): Brendan Regnery //////////////////////////////////////////////////////
#----------------------------------------------------------------------------------
# This program reads data from arm dac calibration files and makes graphs for /////
#    testing various things ///////////////////////////////////////////////////////
#==================================================================================

# Give interpreter a search path

# modules
import ROOT as root
import numpy as np
import matplotlib
matplotlib.use('Agg') #prevents opening displays (fast), must use before pyplot
import matplotlib.pyplot as plt

# import modules from other directories
import style.histogramsettings as settings
import fitting.rootpdfs as pdf
import fitting.fitwithroot as fit

# enter batch mode in root (so python can access displays)
root.gROOT.SetBatch(True)

#==================================================================================
# Load Data ///////////////////////////////////////////////////////////////////////
#==================================================================================

# Access the ARM DAC calibration data
fileList = []
fileList.append(root.TFile("../data/calFile_CFG_THR_ARM_DAC_GE11-X-S-FRASCATI-0008_5-22-16-17.root") )
fileList.append(root.TFile("../data/calFile_CFG_THR_ARM_DAC_GE11-X-S-FRASCATI-0008_5-22-18-47.root") )
fileList.append(root.TFile("../data/calFile_CFG_THR_ARM_DAC_GE11-X-S-FRASCATI-0008_5-22-20-54.root") )
fileList.append(root.TFile("../data/calFile_CFG_THR_ARM_DAC_GE11-X-S-FRASCATI-0008_5-22-22-44.root") )
fileList.append(root.TFile("../data/calFile_CFG_THR_ARM_DAC_GE11-X-S-FRASCATI-0008_5-22-23-57.root") )
fileList.append(root.TFile("../data/calFile_CFG_THR_ARM_DAC_GE11-X-S-FRASCATI-0008_5-23-06-38.root") )
fileList.append(root.TFile("../data/calFile_CFG_THR_ARM_DAC_GE11-X-S-FRASCATI-0008_5-23-9-11.root") )

# Save the dates
date = ["22-16", "22-18", "22-20", "22-22", "22-23", "23-6", "23-9"]
y_pos = np.arange(len(date))

# Save the VFAT IDs
vfatN = list(range(24))
vfatID = ["vfatN0_vfatID6471", "vfatN1_vfatID6135", "vfatN2_vfatID6309", "vfatN3_vfatID6327", "vfatN4_vfatID6329", 
          "vfatN5_vfatID6369", "vfatN6_vfatID6446", "vfatN7_vfatID6153", "vfatN8_vfatID6383", "vfatN9_vfatID6223",
          "vfatN10_vfatID6154", "vfatN11_vfatID6240", "vfatN12_vfatID6323", "vfatN13_vfatID6424", "vfatN14_vfatID6342",
          "vfatN15_vfatID6517", "vfatN16_vfatID6407", "vfatN17_vfatID6137", "vfatN18_vfatID6368", "vfatN19_vfatID6286",
          "vfatN20_vfatID6428", "vfatN21_vfatID6152", "vfatN22_vfatID6379", "vfatN23_vfatID6140"]

# Get Scurve Ensemble Mean and Sigma for VFAT 17, ID 6137, threshold DAC 17
ensMean = []
ensSigma = []
for ivfat in range(len(vfatN) ) :
   tmpEnsMean =[]
   tmpEnsSigma =[]
   for ifile in fileList :
      meanDistr = ifile.Get("VFAT" + str(ivfat) + "/RawData/ScurveMean/gScurveMeanDist_" + vfatID[ivfat] + "_thrDAC17.0")
      sigmaDistr = ifile.Get("VFAT" + str(ivfat) + "/RawData/ScurveSigma/gScurveSigmaDist_" + vfatID[ivfat] + "_thrDAC17.0")
      tmpEnsMean.append(meanDistr.GetMean() )
      tmpEnsSigma.append(sigmaDistr.GetMean() )
   ensMean.append(tmpEnsMean)
   print "Ensemble mean: ", tmpEnsMean
   ensSigma.append(tmpEnsSigma)

#==================================================================================
# Make Graphs /////////////////////////////////////////////////////////////////////
#==================================================================================

# plot VFAT 17, DAC 17.0
plt.figure(1)
plt.errorbar(ensMean, y_pos, xerr=ensSigma, marker='s', mfc='black', mec='black', ms=10, mew=2, ls='')
plt.yticks(y_pos, date)
plt.ylim([-1, 7])
plt.ylabel('Time of ARM DAC Calibration (day, hour)')
plt.xlabel('Mean of Ensemble of S Curves')
plt.title('VFAT 17  DAC=17 S-Curve Ensemble Mean vs Time')
plt.savefig('VFAT17_DAC17_armDacCalibrationStudy.png')
plt.savefig('VFAT17_DAC17_armDacCalibrationStudy.pdf')




