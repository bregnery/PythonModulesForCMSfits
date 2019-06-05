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
date = ["", "22-16", "22-18", "22-20", "22-22", "22-23", "23-6", "23-9", ""]
y_pos = np.arange(7)

# Save the VFAT IDs
vfatN = list(range(24))
vfatID = ["vfatN0_vfatID6471", "vfatN1_vfatID6135", "vfatN2_vfatID6309", "vfatN3_vfatID6327", "vfatN4_vfatID6329", 
          "vfatN5_vfatID6369", "vfatN6_vfatID6446", "vfatN7_vfatID6153", "vfatN8_vfatID6383", "vfatN9_vfatID6223",
          "vfatN10_vfatID6154", "vfatN11_vfatID6240", "vfatN12_vfatID6323", "vfatN13_vfatID6424", "vfatN14_vfatID6342",
          "vfatN15_vfatID6517", "vfatN16_vfatID6407", "vfatN17_vfatID6137", "vfatN18_vfatID6368", "vfatN19_vfatID6286",
          "vfatN20_vfatID6428", "vfatN21_vfatID6152", "vfatN22_vfatID6379", "vfatN23_vfatID6140"]

# Save DAC values and limits for the plot x axis
thrDAC = ["17", "20", "23", "25", "30", "40", "50", "60", "70"]
xlim = [[-6,10],[-6,10],[-6,10],[-6,10],[-5,10],[0,10],[4,15],[4,15],[4,15]]

#==================================================================================
# Loop over DAC values ////////////////////////////////////////////////////////////
#==================================================================================

for iDAC in range(len(thrDAC) ) :

   # Get Scurve Ensemble Mean and Sigma for each DAC
   ensMean = []
   ensSigma = []
   #print thrDAC[iDAC]
   for ivfat in range(len(vfatN) ) :
      tmpEnsMean =[]
      tmpEnsSigma =[]
      for ifile in fileList :
         meanDistr = ifile.Get("VFAT" + str(ivfat) + "/RawData/ScurveMean/gScurveMeanDist_" + vfatID[ivfat] + "_thrDAC" + thrDAC[iDAC] + ".0")
         sigmaDistr = ifile.Get("VFAT" + str(ivfat) + "/RawData/ScurveSigma/gScurveSigmaDist_" + vfatID[ivfat] + "_thrDAC" + thrDAC[iDAC] + ".0")
         tmpEnsMean.append(meanDistr.GetMean() )
         tmpEnsSigma.append(sigmaDistr.GetMean() )
      ensMean.append(tmpEnsMean)
      ensSigma.append(tmpEnsSigma)

   #==================================================================================
   # Make Graphs /////////////////////////////////////////////////////////////////////
   #==================================================================================

   # plot VFAT mean values for each DAC by using subplots
   fig, axs = plt.subplots(3, 8, figsize = (40,30) )
   rowN, colN = 0, 0
   for ivfat in range(len(vfatN) ) :
      # get the correct rows and columns
      if colN == 8: rowN += 1
      if colN == 8: colN = 0
  
      # plot each VFAT time vs ensemble mean 
      axs[rowN, colN].errorbar(ensMean[ivfat], y_pos, xerr=ensSigma[ivfat], marker='s', mfc='black', mec='black', ms=10, mew=2, ls='')
      axs[rowN, colN].plot([0,0], [-1,7], '-.r', lw=3)
      axs[rowN, colN].set_title('VFAT ' + str(ivfat) )
 
      colN += 1

   for ax in axs.flat:
      ax.set_yticklabels(date)
      ax.set_ylim([-1, 7])
      ax.set_xlim(xlim[iDAC])

   # make the figure pretty
   fig.tight_layout(rect=[0.05, 0.03, 0.97, 0.95]) # makes space between plots
   fig.suptitle('CFG_THR_ARM_DAC='+ thrDAC[iDAC] + ' Time vs. S-Curve Ensemble Mean', fontsize=32)
   fig.text(0.5, 0.02, 'Mean of Ensemble of S-Curves [fC]', ha='center', fontsize=28)
   fig.text(0.02, 0.5, 'Time of ARM DAC Calibration (day, hour)', va='center', rotation='vertical', fontsize=28)

   # save the figure
   fig.savefig('DAC' + thrDAC[iDAC] + '_armDacCalibrationStudy.png')
   fig.savefig('DAC' + thrDAC[iDAC] + '_armDacCalibrationStudy.pdf')

print "Made plots for each VFAT and each DAC value"
print "Program was a great success!!!"


