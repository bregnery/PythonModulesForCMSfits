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

# enter batch mode in root (so python can ancncess displays)
root.gROOT.SetBatch(True)

#==================================================================================
# Load Data ///////////////////////////////////////////////////////////////////////
#==================================================================================

# read data from file into a numpy array
fewzdata = numpy.loadtxt("LeadMu26-HighMass-50bin-xs", usecols=range(0,8) )

# extract necessary information
mass = fewzdata[:,0]
nctMu26for110to310ncnc = fewzdata[:,5]
errorNctMu26ncnc = fewzdata[:,6]

#==================================================================================
# Make Histograms /////////////////////////////////////////////////////////////////
#==================================================================================

# Set style options
settings.setSimpleStyle()

# Stat Box options
root.gStyle.SetOptStat(0)

# make root histogram variables
nctMu26for110to310ExponcncHist = root.TH1F("nctMu26for110to310ExponcncHist","Cross Section for NLO CT ncnc",50,110,310)
settings.setHistTitles(nctMu26for110to310ExponcncHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section")

nctMu26for110to310ChebyshevncncHist = root.TH1F("nctMu26for110to310ChebyshevncncHist","Cross Section for NLO CT ncnc",50,110,310)
settings.setHistTitles(nctMu26for110to310ChebyshevncncHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section")

nctMu26for110to310DimitrincncHist = root.TH1F("nctMu26for110to310DimitrincncHist","Cross Section for NLO CT ncnc",50,110,310)
settings.setHistTitles(nctMu26for110to310DimitrincncHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section")

nctMu26for110to310BwExponcncHist = root.TH1F("nctMu26for110to310BwExponcncHist","Cross Section for NLO CT ncnc",50,110,310)
settings.setHistTitles(nctMu26for110to310BwExponcncHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section")

nctMu26for110to310RelBwExponcncHist = root.TH1F("nctMu26for110to310RelBwExponcncHist","Cross Section for NLO CT ncnc",50,110,310)
settings.setHistTitles(nctMu26for110to310RelBwExponcncHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section")

nctMu26for110to310PerExpoBwncncHist = root.TH1F("nctMu26for110to310PerExpoBwncncHist","Cross Section for NLO CT ncnc",50,110,310)
settings.setHistTitles(nctMu26for110to310PerExpoBwncncHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section")

nctMu26for110to310PerExpoRelBwncncHist = root.TH1F("nctMu26for110to310PerExpoRelBwncncHist","Cross Section for NLO CT ncnc",50,110,310)
settings.setHistTitles(nctMu26for110to310PerExpoRelBwncncHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section")

nctMu26for110to310DimitriRelBwncncHist = root.TH1F("nctMu26for110to310DimitriRelBwncncHist","Cross Section for NLO CT ncnc",50,110,310)
settings.setHistTitles(nctMu26for110to310DimitriRelBwncncHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section")

nctMu26for110to310ModDimitriRelBwncncHist = root.TH1F("nctMu26for110to310ModDimitriRelBwncncHist","Cross Section for NLO CT ncnc",50,110,310)
settings.setHistTitles(nctMu26for110to310ModDimitriRelBwncncHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section")

# fill the histograms
for num, xsec, error in zip(range(len(nctMu26for110to310ncnc) ), nctMu26for110to310ncnc, errorNctMu26ncnc):
   # must add one because histogram bins start at 1 not 0
   binNum = num + 1

   nctMu26for110to310ExponcncHist.SetBinContent(binNum, xsec)
   nctMu26for110to310ExponcncHist.SetBinError(binNum, error)
   nctMu26for110to310ChebyshevncncHist.SetBinContent(binNum, xsec)
   nctMu26for110to310ChebyshevncncHist.SetBinError(binNum, error)
   nctMu26for110to310DimitrincncHist.SetBinContent(binNum, xsec)
   nctMu26for110to310DimitrincncHist.SetBinError(binNum, error)
   nctMu26for110to310BwExponcncHist.SetBinContent(binNum, xsec)
   nctMu26for110to310BwExponcncHist.SetBinError(binNum, error)
   nctMu26for110to310RelBwExponcncHist.SetBinContent(binNum, xsec)
   nctMu26for110to310RelBwExponcncHist.SetBinError(binNum, error)
   nctMu26for110to310PerExpoBwncncHist.SetBinContent(binNum, xsec)
   nctMu26for110to310PerExpoBwncncHist.SetBinError(binNum, error)
   nctMu26for110to310PerExpoRelBwncncHist.SetBinContent(binNum, xsec)
   nctMu26for110to310PerExpoRelBwncncHist.SetBinError(binNum, error)
   nctMu26for110to310DimitriRelBwncncHist.SetBinContent(binNum, xsec)
   nctMu26for110to310DimitriRelBwncncHist.SetBinError(binNum, error)
   nctMu26for110to310ModDimitriRelBwncncHist.SetBinContent(binNum, xsec)
   nctMu26for110to310ModDimitriRelBwncncHist.SetBinError(binNum, error)

# adjust histogram settings
settings.setDataPoint(nctMu26for110to310ExponcncHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26for110to310ChebyshevncncHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26for110to310DimitrincncHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26for110to310BwExponcncHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26for110to310RelBwExponcncHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26for110to310PerExpoBwncncHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26for110to310PerExpoRelBwncncHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26for110to310DimitriRelBwncncHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26for110to310ModDimitriRelBwncncHist, root.kBlack, root.kFullDotLarge)

#==================================================================================
# Fit the Histograms //////////////////////////////////////////////////////////////
#==================================================================================

# initial values of fit parameters
parameters = numpy.array([0.0711, 4688, 0.0787])
chebyshevParameters = numpy.array([396, -11.2, 0.0515, -0.000024, -0.0000005, 0.0000000015, -0.0000000000013]) #[62, -1.3, 0.005, -0.000006, 0.00000001, -0.00000000005, 0.00000000000007])
dimitriParameters = numpy.array([0.2968, -0.7566, -2.261, 0.6513]) #[4688, 0.01, -0.079, 0.0001])
bwExpoParameters = numpy.array([0.379, -0.0053])
relBwExpoParameters = numpy.array([0.379, -0.0053])
perExpoBwParameters = numpy.array([23, 1.89, 1.96, -0.7])
perExpoRelBwParameters = numpy.array([150000, 1.87, 3, -0.8])
dimitriRelBwParameters = numpy.array([150, 1.65, -0.7])
modDimitriRelBwParameters = numpy.array([168, 1.92, 0.6, -0.44])

# parameter limits
perExpoBwParLimits = numpy.array([[1, 1.5, 2.5],[3, -1.2, 1.2]])
perExpoRelBwParLimits = numpy.array([[1, 1.5, 2.5],[3, -1.2, 1.2]])
dimitriRelBwParLimits = numpy.array([[2, -1.2, 1.2]])
modDimitriRelBwParLimits = numpy.array([[1, 1.5, 2.5],[3, -1.2, 1.2]])
chebyshevParLimits = numpy.array([[3, -0.0001, 0],[4, -0.000001, 0],[5, 0, 0.00000001],[6, -0.00000000001, 0]])

# fit with root
fitfunc = fit.fitTH1(nctMu26for110to310ExponcncHist, 110, 310, parameters, pdf.expopdf, "R", root.kRed)  
fitfuncChebyshev = fit.fitTH1withParLimits(nctMu26for110to310ChebyshevncncHist, 110, 310, chebyshevParameters, pdf.chebyshev, "R", root.kRed,
                                           chebyshevParLimits)  
fitfuncDimitri = fit.fitTH1(nctMu26for110to310DimitrincncHist, 110, 310, dimitriParameters, pdf.modifiedDimitripdf, "R", root.kRed)  
fitfuncBwExpo = fit.fitTH1(nctMu26for110to310BwExponcncHist, 110, 310, bwExpoParameters, pdf.bwExpo, "R", root.kRed) 
fitfuncRelBwExpo = fit.fitTH1(nctMu26for110to310RelBwExponcncHist, 110, 310, relBwExpoParameters, pdf.relBwExpo, "R", root.kRed) 
fitfuncPerExpoBw = fit.fitTH1withParLimits(nctMu26for110to310PerExpoBwncncHist, 110, 310, perExpoBwParameters, pdf.perExpoBw, "R", root.kRed, 
                                           perExpoBwParLimits)
fitfuncPerExpoRelBw = fit.fitTH1withParLimits(nctMu26for110to310PerExpoRelBwncncHist, 110, 310, perExpoRelBwParameters, pdf.perExpoRelBw, 
                                              "R", root.kRed, perExpoRelBwParLimits)
fitfuncDimitriRelBw = fit.fitTH1withParLimits(nctMu26for110to310DimitriRelBwncncHist, 110, 310, dimitriRelBwParameters, pdf.dimitriRelBw, 
                                              "R", root.kRed, dimitriRelBwParLimits)
fitfuncModDimitriRelBw = fit.fitTH1withParLimits(nctMu26for110to310ModDimitriRelBwncncHist, 110, 310, modDimitriRelBwParameters, 
                                                 pdf.modDimitriRelBw, "R", root.kRed, modDimitriRelBwParLimits)

#==================================================================================
# Draw Plots //////////////////////////////////////////////////////////////////////
#==================================================================================

# make a TCanvas and a histogram plot with residuals
residualExpoCanvas = root.TCanvas("residualCanvas", "residualCanvas")
settings.makeResidualHist(residualExpoCanvas, nctMu26for110to310ExponcncHist, nctMu26for110to310ExponcncHist.GetXaxis().GetTitle(), 
                          "(data - fit)/ data", 1, "PE", root.kBlue, fitfunc)

residualChebyshevCanvas = root.TCanvas("residualChebyshevCanvas", "residualChebyshevCanvas")
settings.makeResidualHist(residualChebyshevCanvas, nctMu26for110to310ChebyshevncncHist, nctMu26for110to310ChebyshevncncHist.GetXaxis().GetTitle(), 
                          "(data - fit)/ data", 1, "PE", root.kBlue, fitfuncChebyshev)

residualDimitriCanvas = root.TCanvas("residualDimitriCanvas", "residualDimitriCanvas")
settings.makeResidualHist(residualDimitriCanvas, nctMu26for110to310DimitrincncHist, nctMu26for110to310DimitrincncHist.GetXaxis().GetTitle(), 
                          "(data - fit)/ data", 1, "PE", root.kBlue, fitfuncDimitri)

residualBwExpoCanvas = root.TCanvas("residualBwExpoCanvas", "residualBwExpoCanvas")
settings.makeResidualHist(residualBwExpoCanvas, nctMu26for110to310BwExponcncHist, nctMu26for110to310BwExponcncHist.GetXaxis().GetTitle(), 
                          "(data - fit)/ data", 1, "PE", root.kBlue, fitfuncBwExpo)

residualRelBwExpoCanvas = root.TCanvas("residualRelBwExpoCanvas", "residualRelBwExpoCanvas")
settings.makeResidualHist(residualRelBwExpoCanvas, nctMu26for110to310RelBwExponcncHist, nctMu26for110to310RelBwExponcncHist.GetXaxis().GetTitle(), 
                          "(data - fit)/ data", 1, "PE", root.kBlue, fitfuncRelBwExpo)

residualPerExpoBwCanvas = root.TCanvas("residualPerExpoBwCanvas", "residualPerExpoBwCanvas")
settings.makeResidualHist(residualPerExpoBwCanvas, nctMu26for110to310PerExpoBwncncHist, nctMu26for110to310PerExpoBwncncHist.GetXaxis().GetTitle(), 
                          "(data - fit)/ data", 1, "PE", root.kBlue, fitfuncPerExpoBw)

residualPerExpoRelBwCanvas = root.TCanvas("residualPerExpoRelBwCanvas", "residualPerExpoRelBwCanvas")
settings.makeResidualHist(residualPerExpoRelBwCanvas, nctMu26for110to310PerExpoRelBwncncHist, 
                          nctMu26for110to310PerExpoRelBwncncHist.GetXaxis().GetTitle(), 
                          "(data - fit)/ data", 1, "PE", root.kBlue, fitfuncPerExpoRelBw)

residualDimitriRelBwCanvas = root.TCanvas("residualDimitriRelBwCanvas", "residualDimitriRelBwCanvas")
settings.makeResidualHist(residualDimitriRelBwCanvas, nctMu26for110to310DimitriRelBwncncHist, 
                          nctMu26for110to310DimitriRelBwncncHist.GetXaxis().GetTitle(), 
                          "(data - fit)/ data", 1, "PE", root.kBlue, fitfuncDimitriRelBw)

residualModDimitriRelBwCanvas = root.TCanvas("residualModDimitriRelBwCanvas", "residualModDimitriRelBwCanvas")
settings.makeResidualHist(residualModDimitriRelBwCanvas, nctMu26for110to310ModDimitriRelBwncncHist, 
                          nctMu26for110to310ModDimitriRelBwncncHist.GetXaxis().GetTitle(), 
                          "(data - fit)/ data", 1, "PE", root.kBlue, fitfuncModDimitriRelBw)

