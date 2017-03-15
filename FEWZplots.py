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
fewzdata = numpy.loadtxt("LeadMu26-PhotonRecomb-13tev-xs", usecols=range(0,14) )

# extract necessary information
mass = fewzdata[:,0]
nctPhotonFull = fewzdata[:,10]
errorNctPhotonFull = fewzdata[:,11]
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

nctPhotonRelBwExpoFullHist = root.TH1F("nctPhotonRelBwExpoFullHist","Cross Section for NLO CT Full with FSR",50,110,160)
settings.setHistTitles(nctPhotonRelBwExpoFullHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section")

nctPhotonPerExpoBwFullHist = root.TH1F("nctPhotonPerExpoBwFullHist","Cross Section for NLO CT Full with FSR",50,110,160)
settings.setHistTitles(nctPhotonPerExpoBwFullHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section")

nctPhotonPerExpoRelBwFullHist = root.TH1F("nctPhotonPerExpoRelBwFullHist","Cross Section for NLO CT Full with FSR",50,110,160)
settings.setHistTitles(nctPhotonPerExpoRelBwFullHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section")

nctPhotonDimitriRelBwFullHist = root.TH1F("nctPhotonDimitriRelBwFullHist","Cross Section for NLO CT Full with FSR",50,110,160)
settings.setHistTitles(nctPhotonDimitriRelBwFullHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section")

nctPhotonModDimitriRelBwFullHist = root.TH1F("nctPhotonModDimitriRelBwFullHist","Cross Section for NLO CT Full with FSR",50,110,160)
settings.setHistTitles(nctPhotonModDimitriRelBwFullHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section")

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
   nctPhotonRelBwExpoFullHist.SetBinContent(binNum, xsec)
   nctPhotonRelBwExpoFullHist.SetBinError(binNum, error)
   nctPhotonPerExpoBwFullHist.SetBinContent(binNum, xsec)
   nctPhotonPerExpoBwFullHist.SetBinError(binNum, error)
   nctPhotonPerExpoRelBwFullHist.SetBinContent(binNum, xsec)
   nctPhotonPerExpoRelBwFullHist.SetBinError(binNum, error)
   nctPhotonDimitriRelBwFullHist.SetBinContent(binNum, xsec)
   nctPhotonDimitriRelBwFullHist.SetBinError(binNum, error)
   nctPhotonModDimitriRelBwFullHist.SetBinContent(binNum, xsec)
   nctPhotonModDimitriRelBwFullHist.SetBinError(binNum, error)

# adjust histogram settings
settings.setDataPoint(nctPhotonExpoFullHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctPhotonChebyshevFullHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctPhotonDimitriFullHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctPhotonBwExpoFullHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctPhotonRelBwExpoFullHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctPhotonPerExpoBwFullHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctPhotonPerExpoRelBwFullHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctPhotonDimitriRelBwFullHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctPhotonModDimitriRelBwFullHist, root.kBlack, root.kFullDotLarge)

#==================================================================================
# Fit the Histograms //////////////////////////////////////////////////////////////
#==================================================================================

# initial values of fit parameters
parameters = numpy.array([0.0711, 4688, 0.0787])
chebyshevParameters = numpy.array([396, -11.2, 0.0515, -0.000024, -0.0000005, 0.0000000015, -0.0000000000013]) #[62, -1.3, 0.005, -0.000006, 0.00000001, -0.00000000005, 0.00000000000007])
dimitriParameters = numpy.array([0.2968, -0.7566, -2.261, 0.6513]) #[4688, 0.01, -0.079, 0.0001])
bwExpoParameters = numpy.array([0.379, -0.0053])
relBwExpoParameters = numpy.array([0.379, -0.0053])
perExpoBwParameters = numpy.array([107, 1.94, 1.46, -0.54])
perExpoRelBwParameters = numpy.array([870000, 1.94, 2.3, -0.6])
dimitriRelBwParameters = numpy.array([965.2, 0.548, -0.37069])
modDimitriRelBwParameters = numpy.array([965.2, 1.94, 0.548, -0.37069])

# parameter limits
perExpoBwParLimits = numpy.array([[1, 1.5, 2.5],[3, -0.6, -0.12]])
perExpoRelBwParLimits = numpy.array([[1, 1.5, 2.5],[3, -1.2, -0.12]])
dimitriRelBwParLimits = numpy.array([[2, -1.2, -0.12]])
modDimitriRelBwParLimits = numpy.array([[1, 1.5, 2.5],[3, -1.2, -0.12]])
chebyshevParLimits = numpy.array([[3, -0.0001, 0],[4, -0.000001, 0],[5, 0, 0.00000001],[6, -0.00000000001, 0]])

# fit with root
fitfunc = fit.fitTH1(nctPhotonExpoFullHist, 110, 160, parameters, pdf.expopdf, "R", root.kRed)  
fitfuncChebyshev = fit.fitTH1withParLimits(nctPhotonChebyshevFullHist, 110, 160, chebyshevParameters, pdf.chebyshev, "R", root.kRed,
                                           chebyshevParLimits)  
fitfuncDimitri = fit.fitTH1(nctPhotonDimitriFullHist, 110, 160, dimitriParameters, pdf.modifiedDimitripdf, "R", root.kRed)  
fitfuncBwExpo = fit.fitTH1(nctPhotonBwExpoFullHist, 110, 160, bwExpoParameters, pdf.bwExpo, "R", root.kRed) 
fitfuncRelBwExpo = fit.fitTH1(nctPhotonRelBwExpoFullHist, 110, 160, relBwExpoParameters, pdf.relBwExpo, "R", root.kRed) 
fitfuncPerExpoBw = fit.fitTH1withParLimits(nctPhotonPerExpoBwFullHist, 110, 160, perExpoBwParameters, pdf.perExpoBw, "R", root.kRed, 
                                           perExpoBwParLimits)
fitfuncPerExpoRelBw = fit.fitTH1withParLimits(nctPhotonPerExpoRelBwFullHist, 110, 160, perExpoRelBwParameters, pdf.perExpoRelBw, 
                                              "R", root.kRed, perExpoRelBwParLimits)
fitfuncDimitriRelBw = fit.fitTH1withParLimits(nctPhotonDimitriRelBwFullHist, 110, 160, dimitriRelBwParameters, pdf.dimitriRelBw, 
                                              "R", root.kRed, dimitriRelBwParLimits)
fitfuncModDimitriRelBw = fit.fitTH1withParLimits(nctPhotonModDimitriRelBwFullHist, 110, 160, modDimitriRelBwParameters, 
                                                 pdf.modDimitriRelBw, "R", root.kRed, modDimitriRelBwParLimits)

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

residualRelBwExpoCanvas = root.TCanvas("residualRelBwExpoCanvas", "residualRelBwExpoCanvas")
settings.makeResidualHist(residualRelBwExpoCanvas, nctPhotonRelBwExpoFullHist, nctPhotonRelBwExpoFullHist.GetXaxis().GetTitle(), 
                          "(data - fit)/ data", 1, "PE", root.kBlue, fitfuncRelBwExpo)

residualPerExpoBwCanvas = root.TCanvas("residualPerExpoBwCanvas", "residualPerExpoBwCanvas")
settings.makeResidualHist(residualPerExpoBwCanvas, nctPhotonPerExpoBwFullHist, nctPhotonPerExpoBwFullHist.GetXaxis().GetTitle(), 
                          "(data - fit)/ data", 1, "PE", root.kBlue, fitfuncPerExpoBw)

residualPerExpoRelBwCanvas = root.TCanvas("residualPerExpoRelBwCanvas", "residualPerExpoRelBwCanvas")
settings.makeResidualHist(residualPerExpoRelBwCanvas, nctPhotonPerExpoRelBwFullHist, 
                          nctPhotonPerExpoRelBwFullHist.GetXaxis().GetTitle(), 
                          "(data - fit)/ data", 1, "PE", root.kBlue, fitfuncPerExpoRelBw)

residualDimitriRelBwCanvas = root.TCanvas("residualDimitriRelBwCanvas", "residualDimitriRelBwCanvas")
settings.makeResidualHist(residualDimitriRelBwCanvas, nctPhotonDimitriRelBwFullHist, 
                          nctPhotonDimitriRelBwFullHist.GetXaxis().GetTitle(), 
                          "(data - fit)/ data", 1, "PE", root.kBlue, fitfuncDimitriRelBw)

residualModDimitriRelBwCanvas = root.TCanvas("residualModDimitriRelBwCanvas", "residualModDimitriRelBwCanvas")
settings.makeResidualHist(residualModDimitriRelBwCanvas, nctPhotonModDimitriRelBwFullHist, 
                          nctPhotonModDimitriRelBwFullHist.GetXaxis().GetTitle(), 
                          "(data - fit)/ data", 1, "PE", root.kBlue, fitfuncModDimitriRelBw)

