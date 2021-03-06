#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ExamplePlots.py /////////////////////////////////////////////////////////////////
#==================================================================================
# This program reads data from a file and makes histograms ////////////////////////
#==================================================================================

# Give interpreter a search path

# modules
import ROOT as root
import numpy

# import modules from other directories
import style.histogramsettings as settings
import fitting.rootpdfs as pdf
import fitting.fitwithroot as fit

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

# Set style options
settings.setSimpleStyle()

# Stat Box options
root.gStyle.SetOptStat(0)

# make root histogram variables
nctPhotonFullHist = root.TH1F("nctPhotonFullHist","Cross Section for NLO CT Full with FSR",50,110,160)
settings.setHistTitles(nctPhotonFullHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section")

# fill the histograms
for num, xsec in zip(range(len(nctPhotonFull) ),nctPhotonFull):
   # bin numbers start at 1
   binNum = num + 1
   nctPhotonFullHist.SetBinContent(binNum, xsec)

# adjust histogram settings
settings.setDataPoint(nctPhotonFullHist, root.kBlack, root.kFullDotLarge)

#==================================================================================
# Fit the Histograms //////////////////////////////////////////////////////////////
#==================================================================================

# specify number of fit parameters
#parameters = numpy.array([0.3, -1, -2, 0.5])
parameters = numpy.array([1, 110, 0.01])

# fit with root
#fit.fitTH1(nctPhotonFullHist, 110, 160, parameters, pdf.dimitripdf, "R", root.kRed)  
fitfunc = fit.fitTH1(nctPhotonFullHist, 110, 160, parameters, pdf.expopdf, "R", root.kRed)  

#==================================================================================
# Draw Plots //////////////////////////////////////////////////////////////////////
#==================================================================================

# make a TCanvas and draw the histograms
#canvas = root.TCanvas()
#nctPhotonFullHist.Draw("P")

# make a TCanvas and a histogram plot with residuals
residualCanvas = root.TCanvas("residualCanvas", "residualCanvas")
settings.makeResidualHist(residualCanvas, nctPhotonFullHist, nctPhotonFullHist.GetXaxis().GetTitle(), 
                          "data - fit", 0, "P", root.kBlue, fitfunc)

# Save the Plots
#canvas.SaveAs("Hist_nctPhotonFull.png")

