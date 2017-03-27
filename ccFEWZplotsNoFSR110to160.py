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
fewzdata = numpy.loadtxt("LeadMu26-13tev-xs", usecols=range(0,8) )

# extract necessary information
mass = fewzdata[:,0]
nctMu26cc = fewzdata[:,3]
errorNctMu26cc = fewzdata[:,4]

#==================================================================================
# Make Histograms /////////////////////////////////////////////////////////////////
#==================================================================================

# Set style options
settings.setSimpleStyle()

# Stat Box options
root.gStyle.SetOptStat(0)

# make root histogram variables
nctMu26ExpoccHist = root.TH1F("nctMu26ExpoccHist","Cross Section for NLO CT cc",50,110,160)
settings.setHistTitles(nctMu26ExpoccHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section")

nctMu26ChebyshevccHist = root.TH1F("nctMu26ChebyshevccHist","Cross Section for NLO CT cc",50,110,160)
settings.setHistTitles(nctMu26ChebyshevccHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section")

nctMu26DimitriccHist = root.TH1F("nctMu26DimitriccHist","Cross Section for NLO CT cc",50,110,160)
settings.setHistTitles(nctMu26DimitriccHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section")

nctMu26BwExpoccHist = root.TH1F("nctMu26BwExpoccHist","Cross Section for NLO CT cc",50,110,160)
settings.setHistTitles(nctMu26BwExpoccHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section")

nctMu26RelBwExpoccHist = root.TH1F("nctMu26RelBwExpoccHist","Cross Section for NLO CT cc",50,110,160)
settings.setHistTitles(nctMu26RelBwExpoccHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section")

nctMu26PerExpoBwccHist = root.TH1F("nctMu26PerExpoBwccHist","Cross Section for NLO CT cc",50,110,160)
settings.setHistTitles(nctMu26PerExpoBwccHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section")

nctMu26PerExpoRelBwccHist = root.TH1F("nctMu26PerExpoRelBwccHist","Cross Section for NLO CT cc",50,110,160)
settings.setHistTitles(nctMu26PerExpoRelBwccHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section")

nctMu26DimitriRelBwccHist = root.TH1F("nctMu26DimitriRelBwccHist","Cross Section for NLO CT cc",50,110,160)
settings.setHistTitles(nctMu26DimitriRelBwccHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section")

nctMu26ModDimitriRelBwccHist = root.TH1F("nctMu26ModDimitriRelBwccHist","Cross Section for NLO CT cc",50,110,160)
settings.setHistTitles(nctMu26ModDimitriRelBwccHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section")

# fill the histograms
for num, xsec, error in zip(range(len(nctMu26cc) ), nctMu26cc, errorNctMu26cc):
   # must add one because histogram bins start at 1 not 0
   binNum = num + 1

   nctMu26ExpoccHist.SetBinContent(binNum, xsec)
   nctMu26ExpoccHist.SetBinError(binNum, error)
   nctMu26ChebyshevccHist.SetBinContent(binNum, xsec)
   nctMu26ChebyshevccHist.SetBinError(binNum, error)
   nctMu26DimitriccHist.SetBinContent(binNum, xsec)
   nctMu26DimitriccHist.SetBinError(binNum, error)
   nctMu26BwExpoccHist.SetBinContent(binNum, xsec)
   nctMu26BwExpoccHist.SetBinError(binNum, error)
   nctMu26RelBwExpoccHist.SetBinContent(binNum, xsec)
   nctMu26RelBwExpoccHist.SetBinError(binNum, error)
   nctMu26PerExpoBwccHist.SetBinContent(binNum, xsec)
   nctMu26PerExpoBwccHist.SetBinError(binNum, error)
   nctMu26PerExpoRelBwccHist.SetBinContent(binNum, xsec)
   nctMu26PerExpoRelBwccHist.SetBinError(binNum, error)
   nctMu26DimitriRelBwccHist.SetBinContent(binNum, xsec)
   nctMu26DimitriRelBwccHist.SetBinError(binNum, error)
   nctMu26ModDimitriRelBwccHist.SetBinContent(binNum, xsec)
   nctMu26ModDimitriRelBwccHist.SetBinError(binNum, error)

# adjust histogram settings
settings.setDataPoint(nctMu26ExpoccHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26ChebyshevccHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26DimitriccHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26BwExpoccHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26RelBwExpoccHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26PerExpoBwccHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26PerExpoRelBwccHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26DimitriRelBwccHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26ModDimitriRelBwccHist, root.kBlack, root.kFullDotLarge)

#==================================================================================
# Fit the Histograms //////////////////////////////////////////////////////////////
#==================================================================================

# initial values of fit parameters
parameters = numpy.array([0.0711, 4688, 0.0787])
chebyshevParameters = numpy.array([396, -11.2, 0.0515, -0.000024, -0.0000005, 0.0000000015, -0.0000000000013]) #[62, -1.3, 0.005, -0.000006, 0.00000001, -0.00000000005, 0.00000000000007])
dimitriParameters = numpy.array([0.2968, -0.7566, -2.261, 0.6513]) #[4688, 0.01, -0.079, 0.0001])
bwExpoParameters = numpy.array([0.379, -0.0053])
relBwExpoParameters = numpy.array([0.379, -0.0053])
perExpoBwParameters = numpy.array([17, 1.92, 1.28, -0.49])
perExpoRelBwParameters = numpy.array([130000, 1.89, 2.4, -0.6])
dimitriRelBwParameters = numpy.array([135, 0.548, -0.37069])
modDimitriRelBwParameters = numpy.array([145, 1.94, -0.034, -0.41])

# parameter limits
perExpoBwParLimits = numpy.array([[1, 1.5, 2.5],[3, -0.6, -0.12]])
perExpoRelBwParLimits = numpy.array([[1, 1.5, 2.5],[3, -1.2, -0.12]])
dimitriRelBwParLimits = numpy.array([[2, -1.2, -0.12]])
modDimitriRelBwParLimits = numpy.array([[1, 1.5, 2.5],[3, -1.2, -0.12]])
chebyshevParLimits = numpy.array([[3, -0.0001, 0],[4, -0.000001, 0],[5, 0, 0.00000001],[6, -0.00000000001, 0]])

# fit with root
fitfunc = fit.fitTH1(nctMu26ExpoccHist, 110, 160, parameters, pdf.expopdf, "R", root.kRed)  
fitfuncChebyshev = fit.fitTH1withParLimits(nctMu26ChebyshevccHist, 110, 160, chebyshevParameters, pdf.chebyshev, "R", root.kRed,
                                           chebyshevParLimits)  
fitfuncDimitri = fit.fitTH1(nctMu26DimitriccHist, 110, 160, dimitriParameters, pdf.modifiedDimitripdf, "R", root.kRed)  
fitfuncBwExpo = fit.fitTH1(nctMu26BwExpoccHist, 110, 160, bwExpoParameters, pdf.bwExpo, "R", root.kRed) 
fitfuncRelBwExpo = fit.fitTH1(nctMu26RelBwExpoccHist, 110, 160, relBwExpoParameters, pdf.relBwExpo, "R", root.kRed) 
fitfuncPerExpoBw = fit.fitTH1withParLimits(nctMu26PerExpoBwccHist, 110, 160, perExpoBwParameters, pdf.perExpoBw, "R", root.kRed, 
                                           perExpoBwParLimits)
fitfuncPerExpoRelBw = fit.fitTH1withParLimits(nctMu26PerExpoRelBwccHist, 110, 160, perExpoRelBwParameters, pdf.perExpoRelBw, 
                                              "R", root.kRed, perExpoRelBwParLimits)
fitfuncDimitriRelBw = fit.fitTH1withParLimits(nctMu26DimitriRelBwccHist, 110, 160, dimitriRelBwParameters, pdf.dimitriRelBw, 
                                              "R", root.kRed, dimitriRelBwParLimits)
fitfuncModDimitriRelBw = fit.fitTH1withParLimits(nctMu26ModDimitriRelBwccHist, 110, 160, modDimitriRelBwParameters, 
                                                 pdf.modDimitriRelBw, "R", root.kRed, modDimitriRelBwParLimits)

#==================================================================================
# Draw Plots //////////////////////////////////////////////////////////////////////
#==================================================================================

# make a TCanvas and a histogram plot with residuals
residualExpoCanvas = root.TCanvas("residualCanvas", "residualCanvas")
settings.makeResidualHist(residualExpoCanvas, nctMu26ExpoccHist, nctMu26ExpoccHist.GetXaxis().GetTitle(), 
                          "(fewz - fit)/ fewz", 1, "PE", root.kBlue, fitfunc)

residualChebyshevCanvas = root.TCanvas("residualChebyshevCanvas", "residualChebyshevCanvas")
settings.makeResidualHist(residualChebyshevCanvas, nctMu26ChebyshevccHist, nctMu26ChebyshevccHist.GetXaxis().GetTitle(), 
                          "(fewz - fit)/ fewz", 1, "PE", root.kBlue, fitfuncChebyshev)

residualDimitriCanvas = root.TCanvas("residualDimitriCanvas", "residualDimitriCanvas")
settings.makeResidualHist(residualDimitriCanvas, nctMu26DimitriccHist, nctMu26DimitriccHist.GetXaxis().GetTitle(), 
                          "(fewz - fit)/ fewz", 1, "PE", root.kBlue, fitfuncDimitri)

residualBwExpoCanvas = root.TCanvas("residualBwExpoCanvas", "residualBwExpoCanvas")
settings.makeResidualHist(residualBwExpoCanvas, nctMu26BwExpoccHist, nctMu26BwExpoccHist.GetXaxis().GetTitle(), 
                          "(fewz - fit)/ fewz", 1, "PE", root.kBlue, fitfuncBwExpo)

residualRelBwExpoCanvas = root.TCanvas("residualRelBwExpoCanvas", "residualRelBwExpoCanvas")
settings.makeResidualHist(residualRelBwExpoCanvas, nctMu26RelBwExpoccHist, nctMu26RelBwExpoccHist.GetXaxis().GetTitle(), 
                          "(fewz - fit)/ fewz", 1, "PE", root.kBlue, fitfuncRelBwExpo)

residualPerExpoBwCanvas = root.TCanvas("residualPerExpoBwCanvas", "residualPerExpoBwCanvas")
settings.makeResidualHist(residualPerExpoBwCanvas, nctMu26PerExpoBwccHist, nctMu26PerExpoBwccHist.GetXaxis().GetTitle(), 
                          "(fewz - fit)/ fewz", 1, "PE", root.kBlue, fitfuncPerExpoBw)

residualPerExpoRelBwCanvas = root.TCanvas("residualPerExpoRelBwCanvas", "residualPerExpoRelBwCanvas")
settings.makeResidualHist(residualPerExpoRelBwCanvas, nctMu26PerExpoRelBwccHist, 
                          nctMu26PerExpoRelBwccHist.GetXaxis().GetTitle(), 
                          "(fewz - fit)/ fewz", 1, "PE", root.kBlue, fitfuncPerExpoRelBw)

residualDimitriRelBwCanvas = root.TCanvas("residualDimitriRelBwCanvas", "residualDimitriRelBwCanvas")
settings.makeResidualHist(residualDimitriRelBwCanvas, nctMu26DimitriRelBwccHist, 
                          nctMu26DimitriRelBwccHist.GetXaxis().GetTitle(), 
                          "(fewz - fit)/ fewz", 1, "PE", root.kBlue, fitfuncDimitriRelBw)

residualModDimitriRelBwCanvas = root.TCanvas("residualModDimitriRelBwCanvas", "residualModDimitriRelBwCanvas")
settings.makeResidualHist(residualModDimitriRelBwCanvas, nctMu26ModDimitriRelBwccHist, 
                          nctMu26ModDimitriRelBwccHist.GetXaxis().GetTitle(), 
                          "(fewz - fit)/ fewz", 1, "PE", root.kBlue, fitfuncModDimitriRelBw)

