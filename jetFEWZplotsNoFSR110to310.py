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

# enter batch mode in root (so python can a1jetess displays)
root.gROOT.SetBatch(True)

#==================================================================================
# Load Data ///////////////////////////////////////////////////////////////////////
#==================================================================================

# read data from file into a numpy array
fewzdata = numpy.loadtxt("LeadMu26-HighMass-100bin-xs", usecols=range(0,9) )

# extract necessary information
mass = fewzdata[:,0]
nctMu26for110to3101jet = fewzdata[:,7]
errorNctMu261jet = fewzdata[:,8]

#==================================================================================
# Make Histograms /////////////////////////////////////////////////////////////////
#==================================================================================

# Set style options
settings.setSimpleStyle()

# Stat Box options
root.gStyle.SetOptStat(0)

# make root histogram variables
nctMu26for110to310Expo1jetHist = root.TH1F("nctMu26for110to310Expo1jetHist","Cross Section for NLO CT 1jet",100,110,310)
settings.setHistTitles(nctMu26for110to310Expo1jetHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section")

nctMu26for110to310Chebyshev1jetHist = root.TH1F("nctMu26for110to310Chebyshev1jetHist","Cross Section for NLO CT 1jet",100,110,310)
settings.setHistTitles(nctMu26for110to310Chebyshev1jetHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section")

nctMu26for110to310Dimitri1jetHist = root.TH1F("nctMu26for110to310Dimitri1jetHist","Cross Section for NLO CT 1jet",100,110,310)
settings.setHistTitles(nctMu26for110to310Dimitri1jetHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section")

nctMu26for110to310BwExpo1jetHist = root.TH1F("nctMu26for110to310BwExpo1jetHist","Cross Section for NLO CT 1jet",100,110,310)
settings.setHistTitles(nctMu26for110to310BwExpo1jetHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section")

nctMu26for110to310RelBwExpo1jetHist = root.TH1F("nctMu26for110to310RelBwExpo1jetHist","Cross Section for NLO CT 1jet",100,110,310)
settings.setHistTitles(nctMu26for110to310RelBwExpo1jetHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section")

nctMu26for110to310PerExpoBw1jetHist = root.TH1F("nctMu26for110to310PerExpoBw1jetHist","Cross Section for NLO CT 1jet",100,110,310)
settings.setHistTitles(nctMu26for110to310PerExpoBw1jetHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section")

nctMu26for110to310PerExpoRelBw1jetHist = root.TH1F("nctMu26for110to310PerExpoRelBw1jetHist","Cross Section for NLO CT 1jet",100,110,310)
settings.setHistTitles(nctMu26for110to310PerExpoRelBw1jetHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section")

nctMu26for110to310DimitriRelBw1jetHist = root.TH1F("nctMu26for110to310DimitriRelBw1jetHist","Cross Section for NLO CT 1jet",100,110,310)
settings.setHistTitles(nctMu26for110to310DimitriRelBw1jetHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section")

nctMu26for110to310ModDimitriRelBw1jetHist = root.TH1F("nctMu26for110to310ModDimitriRelBw1jetHist","Cross Section for NLO CT 1jet",100,110,310)
settings.setHistTitles(nctMu26for110to310ModDimitriRelBw1jetHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section")

# fill the histograms
for num, xsec, error in zip(range(len(nctMu26for110to3101jet) ), nctMu26for110to3101jet, errorNctMu261jet):
   # must add one because histogram bins start at 1 not 0
   binNum = num + 1

   nctMu26for110to310Expo1jetHist.SetBinContent(binNum, xsec)
   nctMu26for110to310Expo1jetHist.SetBinError(binNum, error)
   nctMu26for110to310Chebyshev1jetHist.SetBinContent(binNum, xsec)
   nctMu26for110to310Chebyshev1jetHist.SetBinError(binNum, error)
   nctMu26for110to310Dimitri1jetHist.SetBinContent(binNum, xsec)
   nctMu26for110to310Dimitri1jetHist.SetBinError(binNum, error)
   nctMu26for110to310BwExpo1jetHist.SetBinContent(binNum, xsec)
   nctMu26for110to310BwExpo1jetHist.SetBinError(binNum, error)
   nctMu26for110to310RelBwExpo1jetHist.SetBinContent(binNum, xsec)
   nctMu26for110to310RelBwExpo1jetHist.SetBinError(binNum, error)
   nctMu26for110to310PerExpoBw1jetHist.SetBinContent(binNum, xsec)
   nctMu26for110to310PerExpoBw1jetHist.SetBinError(binNum, error)
   nctMu26for110to310PerExpoRelBw1jetHist.SetBinContent(binNum, xsec)
   nctMu26for110to310PerExpoRelBw1jetHist.SetBinError(binNum, error)
   nctMu26for110to310DimitriRelBw1jetHist.SetBinContent(binNum, xsec)
   nctMu26for110to310DimitriRelBw1jetHist.SetBinError(binNum, error)
   nctMu26for110to310ModDimitriRelBw1jetHist.SetBinContent(binNum, xsec)
   nctMu26for110to310ModDimitriRelBw1jetHist.SetBinError(binNum, error)

# adjust histogram settings
settings.setDataPoint(nctMu26for110to310Expo1jetHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26for110to310Chebyshev1jetHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26for110to310Dimitri1jetHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26for110to310BwExpo1jetHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26for110to310RelBwExpo1jetHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26for110to310PerExpoBw1jetHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26for110to310PerExpoRelBw1jetHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26for110to310DimitriRelBw1jetHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26for110to310ModDimitriRelBw1jetHist, root.kBlack, root.kFullDotLarge)

#==================================================================================
# Fit the Histograms //////////////////////////////////////////////////////////////
#==================================================================================

# initial values of fit parameters
parameters = numpy.array([0.0711, 4688, 0.0787])
chebyshevParameters = numpy.array([4000, -20, 4, -1, 0.3, -0.06, 0.02, -0.004, 0.0009, -0.0002, 0.00003, 0.000003, -0.000006, 0.000002, -0.000002, 0.000001])
dimitriParameters = numpy.array([0.2968, -0.7566, -2.261, 0.6513]) #[4688, 0.01, -0.079, 0.0001])
bwExpoParameters = numpy.array([0.379, -0.0053])
relBwExpoParameters = numpy.array([0.379, -0.0053])
perExpoBwParameters = numpy.array([11, 1.91, 1.96, -0.59])
perExpoRelBwParameters = numpy.array([73000, 1.91, 3.5, -0.84])
dimitriRelBwParameters = numpy.array([77, 1.5, -0.57])
modDimitriRelBwParameters = numpy.array([77, 1.96, 1.5, -0.57])

# parameter limits
perExpoBwParLimits = numpy.array([[1, 1.5, 2.5],[3, -1.2, 1.2]])
perExpoRelBwParLimits = numpy.array([[1, 1.5, 2.5],[3, -1.2, 1.2]])
dimitriRelBwParLimits = numpy.array([[2, -1.2, 1.2]])
modDimitriRelBwParLimits = numpy.array([[1, 1.5, 2.5],[3, -1.2, 1.2]])
chebyshevParLimits = numpy.array([[3, -0.0001, 0],[4, -0.000001, 0],[5, 0, 0.00000001],[6, -0.00000000001, 0]])

# fit with root
fitfunc = fit.fitTH1(nctMu26for110to310Expo1jetHist, 110, 310, parameters, pdf.expopdf, "R", root.kRed)  
fitfuncChebyshev = fit.fitTH1(nctMu26for110to310Chebyshev1jetHist, 110, 310, chebyshevParameters, pdf.chebyshev, "R", root.kRed)  
fitfuncDimitri = fit.fitTH1(nctMu26for110to310Dimitri1jetHist, 110, 310, dimitriParameters, pdf.modifiedDimitripdf, "R", root.kRed)  
fitfuncBwExpo = fit.fitTH1(nctMu26for110to310BwExpo1jetHist, 110, 310, bwExpoParameters, pdf.bwExpo, "R", root.kRed) 
fitfuncRelBwExpo = fit.fitTH1(nctMu26for110to310RelBwExpo1jetHist, 110, 310, relBwExpoParameters, pdf.relBwExpo, "R", root.kRed) 
fitfuncPerExpoBw = fit.fitTH1withParLimits(nctMu26for110to310PerExpoBw1jetHist, 110, 310, perExpoBwParameters, pdf.perExpoBw, "R", root.kRed, 
                                           perExpoBwParLimits)
fitfuncPerExpoRelBw = fit.fitTH1withParLimits(nctMu26for110to310PerExpoRelBw1jetHist, 110, 310, perExpoRelBwParameters, pdf.perExpoRelBw, 
                                              "R", root.kRed, perExpoRelBwParLimits)
fitfuncDimitriRelBw = fit.fitTH1withParLimits(nctMu26for110to310DimitriRelBw1jetHist, 110, 310, dimitriRelBwParameters, pdf.dimitriRelBw, 
                                              "R", root.kRed, dimitriRelBwParLimits)
fitfuncModDimitriRelBw = fit.fitTH1withParLimits(nctMu26for110to310ModDimitriRelBw1jetHist, 110, 310, modDimitriRelBwParameters, 
                                                 pdf.modDimitriRelBw, "R", root.kRed, modDimitriRelBwParLimits)

#==================================================================================
# Draw Plots //////////////////////////////////////////////////////////////////////
#==================================================================================

# make a TCanvas and a histogram plot with residuals
residualExpoCanvas = root.TCanvas("residualCanvas", "residualCanvas")
settings.makeResidualHist(residualExpoCanvas, nctMu26for110to310Expo1jetHist, nctMu26for110to310Expo1jetHist.GetXaxis().GetTitle(), 
                          "(fewz - fit)/ fewz", 1, "PE", root.kBlue, fitfunc)

residualChebyshevCanvas = root.TCanvas("residualChebyshevCanvas", "residualChebyshevCanvas")
settings.makeResidualHist(residualChebyshevCanvas, nctMu26for110to310Chebyshev1jetHist, nctMu26for110to310Chebyshev1jetHist.GetXaxis().GetTitle(), 
                          "(fewz - fit)/ fewz", 1, "PE", root.kBlue, fitfuncChebyshev)

residualDimitriCanvas = root.TCanvas("residualDimitriCanvas", "residualDimitriCanvas")
settings.makeResidualHist(residualDimitriCanvas, nctMu26for110to310Dimitri1jetHist, nctMu26for110to310Dimitri1jetHist.GetXaxis().GetTitle(), 
                          "(fewz - fit)/ fewz", 1, "PE", root.kBlue, fitfuncDimitri)

residualBwExpoCanvas = root.TCanvas("residualBwExpoCanvas", "residualBwExpoCanvas")
settings.makeResidualHist(residualBwExpoCanvas, nctMu26for110to310BwExpo1jetHist, nctMu26for110to310BwExpo1jetHist.GetXaxis().GetTitle(), 
                          "(fewz - fit)/ fewz", 1, "PE", root.kBlue, fitfuncBwExpo)

residualRelBwExpoCanvas = root.TCanvas("residualRelBwExpoCanvas", "residualRelBwExpoCanvas")
settings.makeResidualHist(residualRelBwExpoCanvas, nctMu26for110to310RelBwExpo1jetHist, nctMu26for110to310RelBwExpo1jetHist.GetXaxis().GetTitle(), 
                          "(fewz - fit)/ fewz", 1, "PE", root.kBlue, fitfuncRelBwExpo)

residualPerExpoBwCanvas = root.TCanvas("residualPerExpoBwCanvas", "residualPerExpoBwCanvas")
settings.makeResidualHist(residualPerExpoBwCanvas, nctMu26for110to310PerExpoBw1jetHist, nctMu26for110to310PerExpoBw1jetHist.GetXaxis().GetTitle(), 
                          "(fewz - fit)/ fewz", 1, "PE", root.kBlue, fitfuncPerExpoBw)

residualPerExpoRelBwCanvas = root.TCanvas("residualPerExpoRelBwCanvas", "residualPerExpoRelBwCanvas")
settings.makeResidualHist(residualPerExpoRelBwCanvas, nctMu26for110to310PerExpoRelBw1jetHist, 
                          nctMu26for110to310PerExpoRelBw1jetHist.GetXaxis().GetTitle(), 
                          "(fewz - fit)/ fewz", 1, "PE", root.kBlue, fitfuncPerExpoRelBw)

residualDimitriRelBwCanvas = root.TCanvas("residualDimitriRelBwCanvas", "residualDimitriRelBwCanvas")
settings.makeResidualHist(residualDimitriRelBwCanvas, nctMu26for110to310DimitriRelBw1jetHist, 
                          nctMu26for110to310DimitriRelBw1jetHist.GetXaxis().GetTitle(), 
                          "(fewz - fit)/ fewz", 1, "PE", root.kBlue, fitfuncDimitriRelBw)

residualModDimitriRelBwCanvas = root.TCanvas("residualModDimitriRelBwCanvas", "residualModDimitriRelBwCanvas")
settings.makeResidualHist(residualModDimitriRelBwCanvas, nctMu26for110to310ModDimitriRelBw1jetHist, 
                          nctMu26for110to310ModDimitriRelBw1jetHist.GetXaxis().GetTitle(), 
                          "(fewz - fit)/ fewz", 1, "PE", root.kBlue, fitfuncModDimitriRelBw)

