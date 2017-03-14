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
for num, xsec, error in zip(range(len(nctPhotonFull) ), nctPhotonFull, errorNctPhotonFull):
   # must add one because histogram bins start at 1 not 0
   binNum = num + 1

   nctPhotonExpoFullHist.SetBinContent(binNum, xsec)
   nctPhotonExpoFullHist.SetBinError(binNum, error)
   nctPhotonChebyshevFullHist.SetBinContent(binNum, xsec)
   nctPhotonChebyshevFullHist.SetBinError(binNum, error)
   nctPhotonDimitriFullHist.SetBinContent(binNum, xsec)
   nctPhotonDimitriFullHist.SetBinError(binNum, error)
   nctPhotonBwExpoFullHist.SetBinContent(binNum, xsec)
   nctPhotonBwExpoFullHist.SetBinError(binNum, error)
   nctPhotonPerExpoBwFullHist.SetBinContent(binNum, xsec)
   nctPhotonPerExpoBwFullHist.SetBinError(binNum, error)

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
chebyshevParameters = numpy.array([396, -11.2, 0.0515, -0.000024, -0.0000005, 0.0000000015, -0.0000000000013]) #[62, -1.3, 0.005, -0.000006, 0.00000001, -0.00000000005, 0.00000000000007])
dimitriParameters = numpy.array([0.2968, -0.7566, -2.261, 0.6513]) #[4688, 0.01, -0.079, 0.0001])
bwExpoParameters = numpy.array([0.379, -0.0053])
perExpoBwParameters = numpy.array([107, 1.94, 1.46, -0.54])

# parameter limits
#bwExpoParLimits = numpy.array([[0, 0.2, 1], [1, -0.0073, -0.0033]])
perExpoBwParLimits = numpy.array([[1, 1.5, 2.5],[3, -0.6, -0.12]])
chebyshevParLimits = numpy.array([[3, -0.0001, 0],[4, -0.000001, 0],[5, 0, 0.00000001],[6, -0.00000000001, 0]])

# fit with root
fitfunc = fit.fitTH1(nctPhotonExpoFullHist, 110, 160, parameters, pdf.expopdf, "R", root.kRed)  
fitfuncChebyshev = fit.fitTH1withParLimits(nctPhotonChebyshevFullHist, 110, 160, chebyshevParameters, pdf.chebyshev, "R", root.kRed,
                                           chebyshevParLimits)  
fitfuncDimitri = fit.fitTH1(nctPhotonDimitriFullHist, 110, 160, dimitriParameters, pdf.modifiedDimitripdf, "R", root.kRed)  
fitfuncBwExpo = fit.fitTH1(nctPhotonBwExpoFullHist, 110, 160, bwExpoParameters, pdf.bwExpo, "R", root.kRed) 
fitfuncPerExpoBw = fit.fitTH1withParLimits(nctPhotonPerExpoBwFullHist, 110, 160, perExpoBwParameters, pdf.perExpoBw, "R", root.kRed, 
                                           perExpoBwParLimits)

#==================================================================================
# Draw Plots //////////////////////////////////////////////////////////////////////
#==================================================================================

# make a TCanvas and a histogram plot with residuals
residualExpoCanvas = root.TCanvas("residualCanvas", "residualCanvas")
settings.makeResidualHist(residualExpoCanvas, nctPhotonExpoFullHist, nctPhotonExpoFullHist.GetXaxis().GetTitle(), 
                          "(data - fit)/ data", 1, "PE", root.kBlue, fitfunc)

residualChebyshevCanvas = root.TCanvas("residualChebyshevCanvas", "residualChebyshevCanvas")
settings.makeResidualHist(residualChebyshevCanvas, nctPhotonChebyshevFullHist, nctPhotonChebyshevFullHist.GetXaxis().GetTitle(), 
                          "(data - fit)/ data", 1, "PE", root.kBlue, fitfuncChebyshev)

residualDimitriCanvas = root.TCanvas("residualDimitriCanvas", "residualDimitriCanvas")
settings.makeResidualHist(residualDimitriCanvas, nctPhotonDimitriFullHist, nctPhotonDimitriFullHist.GetXaxis().GetTitle(), 
                          "(data - fit)/ data", 1, "PE", root.kBlue, fitfuncDimitri)

residualBwExpoCanvas = root.TCanvas("residualBwExpoCanvas", "residualBwExpoCanvas")
settings.makeResidualHist(residualBwExpoCanvas, nctPhotonBwExpoFullHist, nctPhotonBwExpoFullHist.GetXaxis().GetTitle(), 
                          "(data - fit)/ data", 1, "PE", root.kBlue, fitfuncBwExpo)

residualPerExpoBwCanvas = root.TCanvas("residualPerExpoBwCanvas", "residualPerExpoBwCanvas")
settings.makeResidualHist(residualPerExpoBwCanvas, nctPhotonPerExpoBwFullHist, nctPhotonPerExpoBwFullHist.GetXaxis().GetTitle(), 
                          "(data - fit)/ data", 1, "PE", root.kBlue, fitfuncPerExpoBw)


