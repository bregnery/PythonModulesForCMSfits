#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# FEWZplots.py ////////////////////////////////////////////////////////////////////
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
nctPhotonExpoFullHist = root.TH1F("nctPhotonExpoFullHist","Cross Section for NLO CT Full with FSR",50,110,160)
settings.setHistTitles(nctPhotonExpoFullHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section")

nctPhotonChebyshevFullHist = root.TH1F("nctPhotonChebyshevFullHist","Cross Section for NLO CT Full with FSR",50,110,160)
settings.setHistTitles(nctPhotonChebyshevFullHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section")

nctPhotonDimitriFullHist = root.TH1F("nctPhotonDimitriFullHist","Cross Section for NLO CT Full with FSR",50,110,160)
settings.setHistTitles(nctPhotonDimitriFullHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section")

# fill the histograms
for num, xsec in zip(range(1, nctPhotonFull.size),nctPhotonFull):
   nctPhotonExpoFullHist.SetBinContent(num, xsec)
   nctPhotonChebyshevFullHist.SetBinContent(num, xsec)
   nctPhotonDimitriFullHist.SetBinContent(num, xsec)

# adjust histogram settings
settings.setDataPoint(nctPhotonExpoFullHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctPhotonChebyshevFullHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctPhotonDimitriFullHist, root.kBlack, root.kFullDotLarge)

#==================================================================================
# Fit the Histograms //////////////////////////////////////////////////////////////
#==================================================================================

# specify number of fit parameters
parameters = numpy.array([0.00713606, 0.00469620, 0.00788091])
chebyshevParameters = numpy.array([61.19, -1.32780, 0.00476652, -0.00000613831, 0.0000000105475, -0.000000000053423, 0.0000000000000786044])
dimitriParameters = numpy.array([0.000000000737327, 10.9999, -0.383586, 0.000942102])

# fit with root
fitfunc = fit.fitTH1(nctPhotonExpoFullHist, 110, 160, parameters, pdf.expopdf, "R", root.kRed)  
fitfuncChebyshev = fit.fitTH1(nctPhotonChebyshevFullHist, 110, 160, chebyshevParameters, pdf.chebyshev, "R", root.kRed)  
fitfuncDimitri = fit.fitTH1(nctPhotonDimitriFullHist, 110, 160, dimitriParameters, pdf.dimitripdf, "R", root.kRed)  

#==================================================================================
# Draw Plots //////////////////////////////////////////////////////////////////////
#==================================================================================

# make a TCanvas and draw the histograms
#canvas = root.TCanvas("canvas", "canvas")
#nctPhotonFullHist.Draw("P")

# make a TCanvas and a histogram plot with residuals
residualExpoCanvas = root.TCanvas("residualCanvas", "residualCanvas")
settings.makeResidualHist(residualExpoCanvas, nctPhotonExpoFullHist, nctPhotonExpoFullHist.GetXaxis().GetTitle(), 
                          "data - fit", 1, "P", root.kBlue, fitfunc)

residualChebyshevCanvas = root.TCanvas("residualChebyshevCanvas", "residualChebyshevCanvas")
settings.makeResidualHist(residualChebyshevCanvas, nctPhotonChebyshevFullHist, nctPhotonChebyshevFullHist.GetXaxis().GetTitle(), 
                          "data - fit", 1, "P", root.kBlue, fitfuncChebyshev)

residualDimitriCanvas = root.TCanvas("residualDimitriCanvas", "residualDimitriCanvas")
settings.makeResidualHist(residualDimitriCanvas, nctPhotonDimitriFullHist, nctPhotonDimitriFullHist.GetXaxis().GetTitle(), 
                          "data - fit", 1, "P", root.kBlue, fitfuncDimitri)

# Save the Plots
#canvas.SaveAs("Hist_nctPhotonFull.png")

