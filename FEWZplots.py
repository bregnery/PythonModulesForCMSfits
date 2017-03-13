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
errorNctPhotonFull = fewzdata[:,10]
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

nctPhotonBwExpoFullHist = root.TH1F("nctPhotonBwExpoFullHist","Cross Section for NLO CT Full with FSR",50,110,160)
settings.setHistTitles(nctPhotonBwExpoFullHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section")

nctPhotonPerExpoBwFullHist = root.TH1F("nctPhotonPerExpoBwFullHist","Cross Section for NLO CT Full with FSR",50,110,160)
settings.setHistTitles(nctPhotonPerExpoBwFullHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section")

# fill the histograms
for num, xsec, error in zip(range(1, nctPhotonFull.size), nctPhotonFull, errorNctPhotonFull):
   nctPhotonExpoFullHist.SetBinContent(num, xsec)
   nctPhotonExpoFullHist.SetBinError(num, error)
   nctPhotonChebyshevFullHist.SetBinContent(num, xsec)
   nctPhotonChebyshevFullHist.SetBinError(num, error)
   nctPhotonDimitriFullHist.SetBinContent(num, xsec)
   nctPhotonDimitriFullHist.SetBinError(num, error)
   nctPhotonBwExpoFullHist.SetBinContent(num, xsec)
   nctPhotonBwExpoFullHist.SetBinError(num, error)
   nctPhotonPerExpoBwFullHist.SetBinContent(num, xsec)
   nctPhotonPerExpoBwFullHist.SetBinError(num, error)

# adjust histogram settings
settings.setDataPoint(nctPhotonExpoFullHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctPhotonChebyshevFullHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctPhotonDimitriFullHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctPhotonBwExpoFullHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctPhotonPerExpoBwFullHist, root.kBlack, root.kFullDotLarge)

#==================================================================================
# Fit the Histograms //////////////////////////////////////////////////////////////
#==================================================================================

# initial values of fit parameters
parameters = numpy.array([0.0711, 4688, 0.0787])
chebyshevParameters = numpy.array([405, -12, 0.05, -0.00003, -0.0000005, 0.0000000015, -0.0000000000015]) #[62, -1.3, 0.005, -0.000006, 0.00000001, -0.00000000005, 0.00000000000007])
dimitriParameters = numpy.array([4688, 0.01, -0.079, 0.0001])
bwExpoParameters = numpy.array([2.5, -0.0053])
perExpoBwParameters = numpy.array([1, 2, 0.46, 2])

# parameter limits
perExpoBwParLimits = numpy.array([[1, 1.5, 2.5]])

# debug
print "Parameter number : ", int(perExpoBwParLimits[0][0])

# fit with root
fitfunc = fit.fitTH1(nctPhotonExpoFullHist, 110, 160, parameters, pdf.expopdf, "R", root.kRed)  
fitfuncChebyshev = fit.fitTH1(nctPhotonChebyshevFullHist, 110, 160, chebyshevParameters, pdf.chebyshev, "R", root.kRed)  
fitfuncDimitri = fit.fitTH1(nctPhotonDimitriFullHist, 110, 160, dimitriParameters, pdf.dimitripdf, "R", root.kRed)  
fitfuncBwExpo = fit.fitTH1(nctPhotonBwExpoFullHist, 110, 160, bwExpoParameters, pdf.bwExpo, "R", root.kRed)
fitfuncPerExpoBw = fit.fitTH1withParLimits(nctPhotonPerExpoBwFullHist, 110, 160, perExpoBwParameters, pdf.perExpoBw, "R", root.kRed, 
                              perExpoBwParLimits)

#==================================================================================
# Draw Plots //////////////////////////////////////////////////////////////////////
#==================================================================================

# make a TCanvas and draw the histograms
#canvas = root.TCanvas("canvas", "canvas")
#nctPhotonFullHist.Draw("P")

# make a TCanvas and a histogram plot with residuals
residualExpoCanvas = root.TCanvas("residualCanvas", "residualCanvas")
settings.makeResidualHist(residualExpoCanvas, nctPhotonExpoFullHist, nctPhotonExpoFullHist.GetXaxis().GetTitle(), 
                          "data - fit", 1, "PE", root.kBlue, fitfunc)

residualChebyshevCanvas = root.TCanvas("residualChebyshevCanvas", "residualChebyshevCanvas")
settings.makeResidualHist(residualChebyshevCanvas, nctPhotonChebyshevFullHist, nctPhotonChebyshevFullHist.GetXaxis().GetTitle(), 
                          "data - fit", 1, "PE", root.kBlue, fitfuncChebyshev)

residualDimitriCanvas = root.TCanvas("residualDimitriCanvas", "residualDimitriCanvas")
settings.makeResidualHist(residualDimitriCanvas, nctPhotonDimitriFullHist, nctPhotonDimitriFullHist.GetXaxis().GetTitle(), 
                          "data - fit", 1, "PE", root.kBlue, fitfuncDimitri)

residualBwExpoCanvas = root.TCanvas("residualBwExpoCanvas", "residualBwExpoCanvas")
settings.makeResidualHist(residualBwExpoCanvas, nctPhotonBwExpoFullHist, nctPhotonBwExpoFullHist.GetXaxis().GetTitle(), 
                          "data - fit", 1, "PE", root.kBlue, fitfuncBwExpo)

residualPerExpoBwCanvas = root.TCanvas("residualPerExpoBwCanvas", "residualPerExpoBwCanvas")
settings.makeResidualHist(residualPerExpoBwCanvas, nctPhotonPerExpoBwFullHist, nctPhotonPerExpoBwFullHist.GetXaxis().GetTitle(), 
                          "data - fit", 1, "PE", root.kBlue, fitfuncPerExpoBw)

# Save the Plots
#canvas.SaveAs("Hist_nctPhotonFull.png")

