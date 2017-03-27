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
fewzdata = numpy.loadtxt("LeadMu26-HighMass-100bin-xs", usecols=range(0,8) )

# extract necessary information
mass = fewzdata[:,0]
nctMu26for110to310Full = fewzdata[:,1]
errorNctMu26Full = fewzdata[:,2]

#==================================================================================
# Make Histograms /////////////////////////////////////////////////////////////////
#==================================================================================

# Set style options
settings.setSimpleStyle()

# Stat Box options
root.gStyle.SetOptStat(0)

# make root histogram variables
nctMu26for110to310ExpoFullHist = root.TH1F("nctMu26for110to310ExpoFullHist","Cross Section for NLO CT Full ",100,110,310)
settings.setHistTitles(nctMu26for110to310ExpoFullHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section")

nctMu26for110to310ChebyshevFullHist = root.TH1F("nctMu26for110to310ChebyshevFullHist","Cross Section for NLO CT Full ",100,110,310)
settings.setHistTitles(nctMu26for110to310ChebyshevFullHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section")

nctMu26for110to310BernsteinFullHist = root.TH1F("nctMu26for110to310BernsteinFullHist","Cross Section for NLO CT Full ",100,110,310)
settings.setHistTitles(nctMu26for110to310BernsteinFullHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section")

nctMu26for110to310DimitriFullHist = root.TH1F("nctMu26for110to310DimitriFullHist","Cross Section for NLO CT Full ",100,110,310)
settings.setHistTitles(nctMu26for110to310DimitriFullHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section")

nctMu26for110to310BwExpoFullHist = root.TH1F("nctMu26for110to310BwExpoFullHist","Cross Section for NLO CT Full ",100,110,310)
settings.setHistTitles(nctMu26for110to310BwExpoFullHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section")

nctMu26for110to310RelBwExpoFullHist = root.TH1F("nctMu26for110to310RelBwExpoFullHist","Cross Section for NLO CT Full ",100,110,310)
settings.setHistTitles(nctMu26for110to310RelBwExpoFullHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section")

nctMu26for110to310PerExpoBwFullHist = root.TH1F("nctMu26for110to310PerExpoBwFullHist","Cross Section for NLO CT Full ",100,110,310)
settings.setHistTitles(nctMu26for110to310PerExpoBwFullHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section")

nctMu26for110to310PerExpoRelBwFullHist = root.TH1F("nctMu26for110to310PerExpoRelBwFullHist","Cross Section for NLO CT Full ",100,110,310)
settings.setHistTitles(nctMu26for110to310PerExpoRelBwFullHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section")

nctMu26for110to310DimitriRelBwFullHist = root.TH1F("nctMu26for110to310DimitriRelBwFullHist","Cross Section for NLO CT Full ",100,110,310)
settings.setHistTitles(nctMu26for110to310DimitriRelBwFullHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section")

nctMu26for110to310ModDimitriRelBwFullHist = root.TH1F("nctMu26for110to310ModDimitriRelBwFullHist","Cross Section for NLO CT Full ",100,110,310)
settings.setHistTitles(nctMu26for110to310ModDimitriRelBwFullHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section")

# fill the histograms
for num, xsec, error in zip(range(len(nctMu26for110to310Full) ), nctMu26for110to310Full, errorNctMu26Full):
   # must add one because histogram bins start at 1 not 0
   binNum = num + 1

   nctMu26for110to310ExpoFullHist.SetBinContent(binNum, xsec)
   nctMu26for110to310ExpoFullHist.SetBinError(binNum, error)
   nctMu26for110to310ChebyshevFullHist.SetBinContent(binNum, xsec)
   nctMu26for110to310ChebyshevFullHist.SetBinError(binNum, error)
   nctMu26for110to310BernsteinFullHist.SetBinContent(binNum, xsec)
   nctMu26for110to310BernsteinFullHist.SetBinError(binNum, error)
   nctMu26for110to310DimitriFullHist.SetBinContent(binNum, xsec)
   nctMu26for110to310DimitriFullHist.SetBinError(binNum, error)
   nctMu26for110to310BwExpoFullHist.SetBinContent(binNum, xsec)
   nctMu26for110to310BwExpoFullHist.SetBinError(binNum, error)
   nctMu26for110to310RelBwExpoFullHist.SetBinContent(binNum, xsec)
   nctMu26for110to310RelBwExpoFullHist.SetBinError(binNum, error)
   nctMu26for110to310PerExpoBwFullHist.SetBinContent(binNum, xsec)
   nctMu26for110to310PerExpoBwFullHist.SetBinError(binNum, error)
   nctMu26for110to310PerExpoRelBwFullHist.SetBinContent(binNum, xsec)
   nctMu26for110to310PerExpoRelBwFullHist.SetBinError(binNum, error)
   nctMu26for110to310DimitriRelBwFullHist.SetBinContent(binNum, xsec)
   nctMu26for110to310DimitriRelBwFullHist.SetBinError(binNum, error)
   nctMu26for110to310ModDimitriRelBwFullHist.SetBinContent(binNum, xsec)
   nctMu26for110to310ModDimitriRelBwFullHist.SetBinError(binNum, error)

# adjust histogram settings
settings.setDataPoint(nctMu26for110to310ExpoFullHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26for110to310ChebyshevFullHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26for110to310BernsteinFullHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26for110to310DimitriFullHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26for110to310BwExpoFullHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26for110to310RelBwExpoFullHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26for110to310PerExpoBwFullHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26for110to310PerExpoRelBwFullHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26for110to310DimitriRelBwFullHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26for110to310ModDimitriRelBwFullHist, root.kBlack, root.kFullDotLarge)

#==================================================================================
# Fit the Histograms //////////////////////////////////////////////////////////////
#==================================================================================

# initial values of fit parameters
parameters = numpy.array([0.0711, 4688, 0.0787])
chebyshevParameters = numpy.array([2400, -18, 1.7, -0.16, 0.015, -0.0013, 0.00009, 0.0000016, -0.000004, 0.000002, -0.00000007])
bernsteinParameters = numpy.array([3, 2, 1, 0.6, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]) 
dimitriParameters = numpy.array([0.2968, -0.7566, -2.261, 0.6513]) #[4688, 0.01, -0.079, 0.0001])
bwExpoParameters = numpy.array([0.379, -0.0053])
relBwExpoParameters = numpy.array([0.379, -0.0053])
perExpoBwParameters = numpy.array([107, 1.94, 1.46, -0.54])
perExpoRelBwParameters = numpy.array([870000, 1.94, 2.3, -0.6])
dimitriRelBwParameters = numpy.array([965.2, 0.548, -0.37069])
modDimitriRelBwParameters = numpy.array([709, 1.94, 0.2, -0.29])

# parameter limits
perExpoBwParLimits = numpy.array([[1, 1.5, 2.5],[3, -0.6, 1.0]])
perExpoRelBwParLimits = numpy.array([[1, 1.5, 2.5],[3, -1.2, 1.2]])
dimitriRelBwParLimits = numpy.array([[2, -1.2, 1.2]])
modDimitriRelBwParLimits = numpy.array([[1, 1.5, 2.5],[3, -1.2, 1.2]])

# fit with root
fitfunc = fit.fitTH1(nctMu26for110to310ExpoFullHist, 110, 310, parameters, pdf.expopdf, "R", root.kRed)  
fitfuncChebyshev = fit.fitTH1(nctMu26for110to310ChebyshevFullHist, 110, 310, chebyshevParameters, pdf.chebyshev, "R", root.kRed)  
fitfuncBernstein = fit.fitTH1(nctMu26for110to310BernsteinFullHist, 110, 310, bernsteinParameters, pdf.bernstein, "R", root.kRed)  
fitfuncDimitri = fit.fitTH1(nctMu26for110to310DimitriFullHist, 110, 310, dimitriParameters, pdf.modifiedDimitripdf, "R", root.kRed)  
fitfuncBwExpo = fit.fitTH1(nctMu26for110to310BwExpoFullHist, 110, 310, bwExpoParameters, pdf.bwExpo, "R", root.kRed) 
fitfuncRelBwExpo = fit.fitTH1(nctMu26for110to310RelBwExpoFullHist, 110, 310, relBwExpoParameters, pdf.relBwExpo, "R", root.kRed) 
fitfuncPerExpoBw = fit.fitTH1withParLimits(nctMu26for110to310PerExpoBwFullHist, 110, 310, perExpoBwParameters, pdf.perExpoBw, "R", root.kRed, 
                                           perExpoBwParLimits)
fitfuncPerExpoRelBw = fit.fitTH1withParLimits(nctMu26for110to310PerExpoRelBwFullHist, 110, 310, perExpoRelBwParameters, pdf.perExpoRelBw, 
                                              "R", root.kRed, perExpoRelBwParLimits)
fitfuncDimitriRelBw = fit.fitTH1withParLimits(nctMu26for110to310DimitriRelBwFullHist, 110, 310, dimitriRelBwParameters, pdf.dimitriRelBw, 
                                              "R", root.kRed, dimitriRelBwParLimits)
fitfuncModDimitriRelBw = fit.fitTH1withParLimits(nctMu26for110to310ModDimitriRelBwFullHist, 110, 310, modDimitriRelBwParameters, 
                                                 pdf.modDimitriRelBw, "R", root.kRed, modDimitriRelBwParLimits)

#==================================================================================
# Draw Plots //////////////////////////////////////////////////////////////////////
#==================================================================================

# make a TCanvas and a histogram plot with residuals
residualExpoCanvas = root.TCanvas("residualCanvas", "residualCanvas")
settings.makeResidualHist(residualExpoCanvas, nctMu26for110to310ExpoFullHist, nctMu26for110to310ExpoFullHist.GetXaxis().GetTitle(), 
                          "(fewz - fit)/ fewz", 1, "PE", root.kBlue, fitfunc)

residualChebyshevCanvas = root.TCanvas("residualChebyshevCanvas", "residualChebyshevCanvas")
settings.makeResidualHist(residualChebyshevCanvas, nctMu26for110to310ChebyshevFullHist, nctMu26for110to310ChebyshevFullHist.GetXaxis().GetTitle(), 
                          "(fewz - fit)/ fewz", 1, "PE", root.kBlue, fitfuncChebyshev)

residualBernsteinCanvas = root.TCanvas("residualBernsteinCanvas", "residualBernsteinCanvas")
settings.makeResidualHist(residualBernsteinCanvas, nctMu26for110to310BernsteinFullHist, nctMu26for110to310BernsteinFullHist.GetXaxis().GetTitle(), 
                          "(fewz - fit)/ fewz", 1, "PE", root.kBlue, fitfuncBernstein)

residualDimitriCanvas = root.TCanvas("residualDimitriCanvas", "residualDimitriCanvas")
settings.makeResidualHist(residualDimitriCanvas, nctMu26for110to310DimitriFullHist, nctMu26for110to310DimitriFullHist.GetXaxis().GetTitle(), 
                          "(fewz - fit)/ fewz", 1, "PE", root.kBlue, fitfuncDimitri)

residualBwExpoCanvas = root.TCanvas("residualBwExpoCanvas", "residualBwExpoCanvas")
settings.makeResidualHist(residualBwExpoCanvas, nctMu26for110to310BwExpoFullHist, nctMu26for110to310BwExpoFullHist.GetXaxis().GetTitle(), 
                          "(fewz - fit)/ fewz", 1, "PE", root.kBlue, fitfuncBwExpo)

residualRelBwExpoCanvas = root.TCanvas("residualRelBwExpoCanvas", "residualRelBwExpoCanvas")
settings.makeResidualHist(residualRelBwExpoCanvas, nctMu26for110to310RelBwExpoFullHist, nctMu26for110to310RelBwExpoFullHist.GetXaxis().GetTitle(), 
                          "(fewz - fit)/ fewz", 1, "PE", root.kBlue, fitfuncRelBwExpo)

residualPerExpoBwCanvas = root.TCanvas("residualPerExpoBwCanvas", "residualPerExpoBwCanvas")
settings.makeResidualHist(residualPerExpoBwCanvas, nctMu26for110to310PerExpoBwFullHist, nctMu26for110to310PerExpoBwFullHist.GetXaxis().GetTitle(), 
                          "(fewz - fit)/ fewz", 1, "PE", root.kBlue, fitfuncPerExpoBw)

residualPerExpoRelBwCanvas = root.TCanvas("residualPerExpoRelBwCanvas", "residualPerExpoRelBwCanvas")
settings.makeResidualHist(residualPerExpoRelBwCanvas, nctMu26for110to310PerExpoRelBwFullHist, 
                          nctMu26for110to310PerExpoRelBwFullHist.GetXaxis().GetTitle(), 
                          "(fewz - fit)/ fewz", 1, "PE", root.kBlue, fitfuncPerExpoRelBw)

residualDimitriRelBwCanvas = root.TCanvas("residualDimitriRelBwCanvas", "residualDimitriRelBwCanvas")
settings.makeResidualHist(residualDimitriRelBwCanvas, nctMu26for110to310DimitriRelBwFullHist, 
                          nctMu26for110to310DimitriRelBwFullHist.GetXaxis().GetTitle(), 
                          "(fewz - fit)/ fewz", 1, "PE", root.kBlue, fitfuncDimitriRelBw)

residualModDimitriRelBwCanvas = root.TCanvas("residualModDimitriRelBwCanvas", "residualModDimitriRelBwCanvas")
settings.makeResidualHist(residualModDimitriRelBwCanvas, nctMu26for110to310ModDimitriRelBwFullHist, 
                          nctMu26for110to310ModDimitriRelBwFullHist.GetXaxis().GetTitle(), 
                          "(fewz - fit)/ fewz", 1, "PE", root.kBlue, fitfuncModDimitriRelBw)

