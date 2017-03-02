#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# FEWZplots.py ////////////////////////////////////////////////////////////////////
#==================================================================================
# This program reads data from a file and makes histograms ////////////////////////
#==================================================================================

# modules
import ROOT as root
import numpy

# enter batch mode in root (so python can access displays)
root.gROOT.SetBatch(True)

#==================================================================================
# Load Data ///////////////////////////////////////////////////////////////////////
#==================================================================================

# read data from file into a numpy array
fewzdata = numpy.loadtxt("LeadMu26-PhotonRecomb-13tev-xs", usecols=range(0,12) )

# extract necessary information
mass = fewzdata[:,0]
nctPhotonFull = fewzdata[:,9]
nctMu26Full = fewzdata[:,5]

#==================================================================================
# Make Histograms /////////////////////////////////////////////////////////////////
#==================================================================================

# Stat Box options
root.gStyle.SetOptStat(0)

# make root histogram data files
nctPhotonFullHist = root.TH1F("nctPhotonFullHist","",50,110,160)
nctPhotonFullHist.GetXaxis().SetTitle("Dimuon Mass [GeV/c^{2}]")
nctPhotonFullHist.GetYaxis().SetTitle("Cross Section")

# fill the histograms
for num, xsec in zip(range(1,51),nctPhotonFull):
   nctPhotonFullHist.SetBinContent(num, xsec)

# histogram data point settings
nctPhotonFullHist.SetLineStyle(0)
nctPhotonFullHist.SetMarkerStyle(8)

#==================================================================================
# Draw Plots //////////////////////////////////////////////////////////////////////
#==================================================================================

# make a TCanvas and draw the histograms
canvas = root.TCanvas()
nctPhotonFullHist.Draw("P")

# Save the Plots
canvas.SaveAs("Hist_nctPhotonFull.png")
