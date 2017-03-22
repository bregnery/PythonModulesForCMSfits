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
fewzdata = numpy.loadtxt("LeadMu26-HighMass-50bin-xs", usecols=range(0,8) )

# extract necessary information
mass = fewzdata[:,0]
nctMu26for110to310cc = fewzdata[:,3]
errorNctMu26cc = fewzdata[:,4]

#==================================================================================
# Make Histograms /////////////////////////////////////////////////////////////////
#==================================================================================

# Set style options
settings.setSimpleStyle()

# Stat Box options
root.gStyle.SetOptStat(0)

# make root histogram variables
nctMu26for110to310ExpoccHist = root.TH1F("nctMu26for110to310ExpoccHist","Cross Section for NLO CT cc",50,110,310)
settings.setHistTitles(nctMu26for110to310ExpoccHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section")

nctMu26for110to310ChebyshevccHist = root.TH1F("nctMu26for110to310ChebyshevccHist","Cross Section for NLO CT cc",50,110,310)
settings.setHistTitles(nctMu26for110to310ChebyshevccHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section")

nctMu26for110to310DimitriccHist = root.TH1F("nctMu26for110to310DimitriccHist","Cross Section for NLO CT cc",50,110,310)
settings.setHistTitles(nctMu26for110to310DimitriccHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section")

nctMu26for110to310BwExpoccHist = root.TH1F("nctMu26for110to310BwExpoccHist","Cross Section for NLO CT cc",50,110,310)
settings.setHistTitles(nctMu26for110to310BwExpoccHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section")

nctMu26for110to310RelBwExpoccHist = root.TH1F("nctMu26for110to310RelBwExpoccHist","Cross Section for NLO CT cc",50,110,310)
settings.setHistTitles(nctMu26for110to310RelBwExpoccHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section")

nctMu26for110to310PerExpoBwccHist = root.TH1F("nctMu26for110to310PerExpoBwccHist","Cross Section for NLO CT cc",50,110,310)
settings.setHistTitles(nctMu26for110to310PerExpoBwccHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section")

nctMu26for110to310PerExpoRelBwccHist = root.TH1F("nctMu26for110to310PerExpoRelBwccHist","Cross Section for NLO CT cc",50,110,310)
settings.setHistTitles(nctMu26for110to310PerExpoRelBwccHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section")

nctMu26for110to310DimitriRelBwccHist = root.TH1F("nctMu26for110to310DimitriRelBwccHist","Cross Section for NLO CT cc",50,110,310)
settings.setHistTitles(nctMu26for110to310DimitriRelBwccHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section")

nctMu26for110to310ModDimitriRelBwccHist = root.TH1F("nctMu26for110to310ModDimitriRelBwccHist","Cross Section for NLO CT cc",50,110,310)
settings.setHistTitles(nctMu26for110to310ModDimitriRelBwccHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section")

# fill the histograms
for num, xsec, error in zip(range(len(nctMu26for110to310cc) ), nctMu26for110to310cc, errorNctMu26cc):
   # must add one because histogram bins start at 1 not 0
   binNum = num + 1

   nctMu26for110to310ExpoccHist.SetBinContent(binNum, xsec)
   nctMu26for110to310ExpoccHist.SetBinError(binNum, error)
   nctMu26for110to310ChebyshevccHist.SetBinContent(binNum, xsec)
   nctMu26for110to310ChebyshevccHist.SetBinError(binNum, error)
   nctMu26for110to310DimitriccHist.SetBinContent(binNum, xsec)
   nctMu26for110to310DimitriccHist.SetBinError(binNum, error)
   nctMu26for110to310BwExpoccHist.SetBinContent(binNum, xsec)
   nctMu26for110to310BwExpoccHist.SetBinError(binNum, error)
   nctMu26for110to310RelBwExpoccHist.SetBinContent(binNum, xsec)
   nctMu26for110to310RelBwExpoccHist.SetBinError(binNum, error)
   nctMu26for110to310PerExpoBwccHist.SetBinContent(binNum, xsec)
   nctMu26for110to310PerExpoBwccHist.SetBinError(binNum, error)
   nctMu26for110to310PerExpoRelBwccHist.SetBinContent(binNum, xsec)
   nctMu26for110to310PerExpoRelBwccHist.SetBinError(binNum, error)
   nctMu26for110to310DimitriRelBwccHist.SetBinContent(binNum, xsec)
   nctMu26for110to310DimitriRelBwccHist.SetBinError(binNum, error)
   nctMu26for110to310ModDimitriRelBwccHist.SetBinContent(binNum, xsec)
   nctMu26for110to310ModDimitriRelBwccHist.SetBinError(binNum, error)

# adjust histogram settings
settings.setDataPoint(nctMu26for110to310ExpoccHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26for110to310ChebyshevccHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26for110to310DimitriccHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26for110to310BwExpoccHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26for110to310RelBwExpoccHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26for110to310PerExpoBwccHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26for110to310PerExpoRelBwccHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26for110to310DimitriRelBwccHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26for110to310ModDimitriRelBwccHist, root.kBlack, root.kFullDotLarge)

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
perExpoBwParLimits = numpy.array([[1, 1.5, 2.5],[3, -0.6, 1.2]])
perExpoRelBwParLimits = numpy.array([[1, 1.5, 2.5],[3, -1.2, 1.2]])
dimitriRelBwParLimits = numpy.array([[2, -1.2, 1.2]])
modDimitriRelBwParLimits = numpy.array([[1, 1.5, 2.5],[3, -1.2, 1.2]])
chebyshevParLimits = numpy.array([[3, -0.0001, 0],[4, -0.000001, 0],[5, 0, 0.00000001],[6, -0.00000000001, 0]])

# fit with root
fitfunc = fit.fitTH1(nctMu26for110to310ExpoccHist, 110, 310, parameters, pdf.expopdf, "R", root.kRed)  
fitfuncChebyshev = fit.fitTH1withParLimits(nctMu26for110to310ChebyshevccHist, 110, 310, chebyshevParameters, pdf.chebyshev, "R", root.kRed,
                                           chebyshevParLimits)  
fitfuncDimitri = fit.fitTH1(nctMu26for110to310DimitriccHist, 110, 310, dimitriParameters, pdf.modifiedDimitripdf, "R", root.kRed)  
fitfuncBwExpo = fit.fitTH1(nctMu26for110to310BwExpoccHist, 110, 310, bwExpoParameters, pdf.bwExpo, "R", root.kRed) 
fitfuncRelBwExpo = fit.fitTH1(nctMu26for110to310RelBwExpoccHist, 110, 310, relBwExpoParameters, pdf.relBwExpo, "R", root.kRed) 
fitfuncPerExpoBw = fit.fitTH1withParLimits(nctMu26for110to310PerExpoBwccHist, 110, 310, perExpoBwParameters, pdf.perExpoBw, "R", root.kRed, 
                                           perExpoBwParLimits)
fitfuncPerExpoRelBw = fit.fitTH1withParLimits(nctMu26for110to310PerExpoRelBwccHist, 110, 310, perExpoRelBwParameters, pdf.perExpoRelBw, 
                                              "R", root.kRed, perExpoRelBwParLimits)
fitfuncDimitriRelBw = fit.fitTH1withParLimits(nctMu26for110to310DimitriRelBwccHist, 110, 310, dimitriRelBwParameters, pdf.dimitriRelBw, 
                                              "R", root.kRed, dimitriRelBwParLimits)
fitfuncModDimitriRelBw = fit.fitTH1withParLimits(nctMu26for110to310ModDimitriRelBwccHist, 110, 310, modDimitriRelBwParameters, 
                                                 pdf.modDimitriRelBw, "R", root.kRed, modDimitriRelBwParLimits)

#==================================================================================
# Draw Plots //////////////////////////////////////////////////////////////////////
#==================================================================================

# make a TCanvas and a histogram plot with residuals
residualExpoCanvas = root.TCanvas("residualCanvas", "residualCanvas")
settings.makeResidualHist(residualExpoCanvas, nctMu26for110to310ExpoccHist, nctMu26for110to310ExpoccHist.GetXaxis().GetTitle(), 
                          "(data - fit)/ data", 1, "PE", root.kBlue, fitfunc)

residualChebyshevCanvas = root.TCanvas("residualChebyshevCanvas", "residualChebyshevCanvas")
settings.makeResidualHist(residualChebyshevCanvas, nctMu26for110to310ChebyshevccHist, nctMu26for110to310ChebyshevccHist.GetXaxis().GetTitle(), 
                          "(data - fit)/ data", 1, "PE", root.kBlue, fitfuncChebyshev)

residualDimitriCanvas = root.TCanvas("residualDimitriCanvas", "residualDimitriCanvas")
settings.makeResidualHist(residualDimitriCanvas, nctMu26for110to310DimitriccHist, nctMu26for110to310DimitriccHist.GetXaxis().GetTitle(), 
                          "(data - fit)/ data", 1, "PE", root.kBlue, fitfuncDimitri)

residualBwExpoCanvas = root.TCanvas("residualBwExpoCanvas", "residualBwExpoCanvas")
settings.makeResidualHist(residualBwExpoCanvas, nctMu26for110to310BwExpoccHist, nctMu26for110to310BwExpoccHist.GetXaxis().GetTitle(), 
                          "(data - fit)/ data", 1, "PE", root.kBlue, fitfuncBwExpo)

residualRelBwExpoCanvas = root.TCanvas("residualRelBwExpoCanvas", "residualRelBwExpoCanvas")
settings.makeResidualHist(residualRelBwExpoCanvas, nctMu26for110to310RelBwExpoccHist, nctMu26for110to310RelBwExpoccHist.GetXaxis().GetTitle(), 
                          "(data - fit)/ data", 1, "PE", root.kBlue, fitfuncRelBwExpo)

residualPerExpoBwCanvas = root.TCanvas("residualPerExpoBwCanvas", "residualPerExpoBwCanvas")
settings.makeResidualHist(residualPerExpoBwCanvas, nctMu26for110to310PerExpoBwccHist, nctMu26for110to310PerExpoBwccHist.GetXaxis().GetTitle(), 
                          "(data - fit)/ data", 1, "PE", root.kBlue, fitfuncPerExpoBw)

residualPerExpoRelBwCanvas = root.TCanvas("residualPerExpoRelBwCanvas", "residualPerExpoRelBwCanvas")
settings.makeResidualHist(residualPerExpoRelBwCanvas, nctMu26for110to310PerExpoRelBwccHist, 
                          nctMu26for110to310PerExpoRelBwccHist.GetXaxis().GetTitle(), 
                          "(data - fit)/ data", 1, "PE", root.kBlue, fitfuncPerExpoRelBw)

residualDimitriRelBwCanvas = root.TCanvas("residualDimitriRelBwCanvas", "residualDimitriRelBwCanvas")
settings.makeResidualHist(residualDimitriRelBwCanvas, nctMu26for110to310DimitriRelBwccHist, 
                          nctMu26for110to310DimitriRelBwccHist.GetXaxis().GetTitle(), 
                          "(data - fit)/ data", 1, "PE", root.kBlue, fitfuncDimitriRelBw)

residualModDimitriRelBwCanvas = root.TCanvas("residualModDimitriRelBwCanvas", "residualModDimitriRelBwCanvas")
settings.makeResidualHist(residualModDimitriRelBwCanvas, nctMu26for110to310ModDimitriRelBwccHist, 
                          nctMu26for110to310ModDimitriRelBwccHist.GetXaxis().GetTitle(), 
                          "(data - fit)/ data", 1, "PE", root.kBlue, fitfuncModDimitriRelBw)

