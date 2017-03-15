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
fewzdata = numpy.loadtxt("LeadMu26-13tev-xs", usecols=range(0,8) )

# extract necessary information
mass = fewzdata[:,0]
nctMu26ncnc = fewzdata[:,5]
errorNctMu26ncnc = fewzdata[:,6]

#==================================================================================
# Make Histograms /////////////////////////////////////////////////////////////////
#==================================================================================

# Set style options
settings.setSimpleStyle()

# Stat Box options
root.gStyle.SetOptStat(0)

# make root histogram variables
nctMu26ExponcncHist = root.TH1F("nctMu26ExponcncHist","Cross Section for NLO CT ncnc",50,110,160)
settings.setHistTitles(nctMu26ExponcncHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section")

nctMu26ChebyshevncncHist = root.TH1F("nctMu26ChebyshevncncHist","Cross Section for NLO CT ncnc",50,110,160)
settings.setHistTitles(nctMu26ChebyshevncncHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section")

nctMu26DimitrincncHist = root.TH1F("nctMu26DimitrincncHist","Cross Section for NLO CT ncnc",50,110,160)
settings.setHistTitles(nctMu26DimitrincncHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section")

nctMu26BwExponcncHist = root.TH1F("nctMu26BwExponcncHist","Cross Section for NLO CT ncnc",50,110,160)
settings.setHistTitles(nctMu26BwExponcncHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section")

nctMu26RelBwExponcncHist = root.TH1F("nctMu26RelBwExponcncHist","Cross Section for NLO CT ncnc",50,110,160)
settings.setHistTitles(nctMu26RelBwExponcncHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section")

nctMu26PerExpoBwncncHist = root.TH1F("nctMu26PerExpoBwncncHist","Cross Section for NLO CT ncnc",50,110,160)
settings.setHistTitles(nctMu26PerExpoBwncncHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section")

nctMu26PerExpoRelBwncncHist = root.TH1F("nctMu26PerExpoRelBwncncHist","Cross Section for NLO CT ncnc",50,110,160)
settings.setHistTitles(nctMu26PerExpoRelBwncncHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section")

nctMu26DimitriRelBwncncHist = root.TH1F("nctMu26DimitriRelBwncncHist","Cross Section for NLO CT ncnc",50,110,160)
settings.setHistTitles(nctMu26DimitriRelBwncncHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section")

nctMu26ModDimitriRelBwncncHist = root.TH1F("nctMu26ModDimitriRelBwncncHist","Cross Section for NLO CT ncnc",50,110,160)
settings.setHistTitles(nctMu26ModDimitriRelBwncncHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section")

# fill the histograms
for num, xsec, error in zip(range(len(nctMu26ncnc) ), nctMu26ncnc, errorNctMu26ncnc):
   # must add one because histogram bins start at 1 not 0
   binNum = num + 1

   nctMu26ExponcncHist.SetBinContent(binNum, xsec)
   nctMu26ExponcncHist.SetBinError(binNum, error)
   nctMu26ChebyshevncncHist.SetBinContent(binNum, xsec)
   nctMu26ChebyshevncncHist.SetBinError(binNum, error)
   nctMu26DimitrincncHist.SetBinContent(binNum, xsec)
   nctMu26DimitrincncHist.SetBinError(binNum, error)
   nctMu26BwExponcncHist.SetBinContent(binNum, xsec)
   nctMu26BwExponcncHist.SetBinError(binNum, error)
   nctMu26RelBwExponcncHist.SetBinContent(binNum, xsec)
   nctMu26RelBwExponcncHist.SetBinError(binNum, error)
   nctMu26PerExpoBwncncHist.SetBinContent(binNum, xsec)
   nctMu26PerExpoBwncncHist.SetBinError(binNum, error)
   nctMu26PerExpoRelBwncncHist.SetBinContent(binNum, xsec)
   nctMu26PerExpoRelBwncncHist.SetBinError(binNum, error)
   nctMu26DimitriRelBwncncHist.SetBinContent(binNum, xsec)
   nctMu26DimitriRelBwncncHist.SetBinError(binNum, error)
   nctMu26ModDimitriRelBwncncHist.SetBinContent(binNum, xsec)
   nctMu26ModDimitriRelBwncncHist.SetBinError(binNum, error)

# adjust histogram settings
settings.setDataPoint(nctMu26ExponcncHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26ChebyshevncncHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26DimitrincncHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26BwExponcncHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26RelBwExponcncHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26PerExpoBwncncHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26PerExpoRelBwncncHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26DimitriRelBwncncHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26ModDimitriRelBwncncHist, root.kBlack, root.kFullDotLarge)

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
perExpoBwParLimits = numpy.array([[1, 1.5, 2.5],[3, -1.2, -0.12]])
perExpoRelBwParLimits = numpy.array([[1, 1.5, 2.5],[3, -1.2, -0.12]])
dimitriRelBwParLimits = numpy.array([[2, -1.2, -0.12]])
modDimitriRelBwParLimits = numpy.array([[1, 1.5, 2.5],[3, -1.2, -0.12]])
chebyshevParLimits = numpy.array([[3, -0.0001, 0],[4, -0.000001, 0],[5, 0, 0.00000001],[6, -0.00000000001, 0]])

# fit with root
fitfunc = fit.fitTH1(nctMu26ExponcncHist, 110, 160, parameters, pdf.expopdf, "R", root.kRed)  
fitfuncChebyshev = fit.fitTH1withParLimits(nctMu26ChebyshevncncHist, 110, 160, chebyshevParameters, pdf.chebyshev, "R", root.kRed,
                                           chebyshevParLimits)  
fitfuncDimitri = fit.fitTH1(nctMu26DimitrincncHist, 110, 160, dimitriParameters, pdf.modifiedDimitripdf, "R", root.kRed)  
fitfuncBwExpo = fit.fitTH1(nctMu26BwExponcncHist, 110, 160, bwExpoParameters, pdf.bwExpo, "R", root.kRed) 
fitfuncRelBwExpo = fit.fitTH1(nctMu26RelBwExponcncHist, 110, 160, relBwExpoParameters, pdf.relBwExpo, "R", root.kRed) 
fitfuncPerExpoBw = fit.fitTH1withParLimits(nctMu26PerExpoBwncncHist, 110, 160, perExpoBwParameters, pdf.perExpoBw, "R", root.kRed, 
                                           perExpoBwParLimits)
fitfuncPerExpoRelBw = fit.fitTH1withParLimits(nctMu26PerExpoRelBwncncHist, 110, 160, perExpoRelBwParameters, pdf.perExpoRelBw, 
                                              "R", root.kRed, perExpoRelBwParLimits)
fitfuncDimitriRelBw = fit.fitTH1withParLimits(nctMu26DimitriRelBwncncHist, 110, 160, dimitriRelBwParameters, pdf.dimitriRelBw, 
                                              "R", root.kRed, dimitriRelBwParLimits)
fitfuncModDimitriRelBw = fit.fitTH1withParLimits(nctMu26ModDimitriRelBwncncHist, 110, 160, modDimitriRelBwParameters, 
                                                 pdf.modDimitriRelBw, "R", root.kRed, modDimitriRelBwParLimits)

#==================================================================================
# Draw Plots //////////////////////////////////////////////////////////////////////
#==================================================================================

# make a TCanvas and a histogram plot with residuals
residualExpoCanvas = root.TCanvas("residualCanvas", "residualCanvas")
settings.makeResidualHist(residualExpoCanvas, nctMu26ExponcncHist, nctMu26ExponcncHist.GetXaxis().GetTitle(), 
                          "(data - fit)/ data", 1, "PE", root.kBlue, fitfunc)

residualChebyshevCanvas = root.TCanvas("residualChebyshevCanvas", "residualChebyshevCanvas")
settings.makeResidualHist(residualChebyshevCanvas, nctMu26ChebyshevncncHist, nctMu26ChebyshevncncHist.GetXaxis().GetTitle(), 
                          "(data - fit)/ data", 1, "PE", root.kBlue, fitfuncChebyshev)

residualDimitriCanvas = root.TCanvas("residualDimitriCanvas", "residualDimitriCanvas")
settings.makeResidualHist(residualDimitriCanvas, nctMu26DimitrincncHist, nctMu26DimitrincncHist.GetXaxis().GetTitle(), 
                          "(data - fit)/ data", 1, "PE", root.kBlue, fitfuncDimitri)

residualBwExpoCanvas = root.TCanvas("residualBwExpoCanvas", "residualBwExpoCanvas")
settings.makeResidualHist(residualBwExpoCanvas, nctMu26BwExponcncHist, nctMu26BwExponcncHist.GetXaxis().GetTitle(), 
                          "(data - fit)/ data", 1, "PE", root.kBlue, fitfuncBwExpo)

residualRelBwExpoCanvas = root.TCanvas("residualRelBwExpoCanvas", "residualRelBwExpoCanvas")
settings.makeResidualHist(residualRelBwExpoCanvas, nctMu26RelBwExponcncHist, nctMu26RelBwExponcncHist.GetXaxis().GetTitle(), 
                          "(data - fit)/ data", 1, "PE", root.kBlue, fitfuncRelBwExpo)

residualPerExpoBwCanvas = root.TCanvas("residualPerExpoBwCanvas", "residualPerExpoBwCanvas")
settings.makeResidualHist(residualPerExpoBwCanvas, nctMu26PerExpoBwncncHist, nctMu26PerExpoBwncncHist.GetXaxis().GetTitle(), 
                          "(data - fit)/ data", 1, "PE", root.kBlue, fitfuncPerExpoBw)

residualPerExpoRelBwCanvas = root.TCanvas("residualPerExpoRelBwCanvas", "residualPerExpoRelBwCanvas")
settings.makeResidualHist(residualPerExpoRelBwCanvas, nctMu26PerExpoRelBwncncHist, 
                          nctMu26PerExpoRelBwncncHist.GetXaxis().GetTitle(), 
                          "(data - fit)/ data", 1, "PE", root.kBlue, fitfuncPerExpoRelBw)

residualDimitriRelBwCanvas = root.TCanvas("residualDimitriRelBwCanvas", "residualDimitriRelBwCanvas")
settings.makeResidualHist(residualDimitriRelBwCanvas, nctMu26DimitriRelBwncncHist, 
                          nctMu26DimitriRelBwncncHist.GetXaxis().GetTitle(), 
                          "(data - fit)/ data", 1, "PE", root.kBlue, fitfuncDimitriRelBw)

residualModDimitriRelBwCanvas = root.TCanvas("residualModDimitriRelBwCanvas", "residualModDimitriRelBwCanvas")
settings.makeResidualHist(residualModDimitriRelBwCanvas, nctMu26ModDimitriRelBwncncHist, 
                          nctMu26ModDimitriRelBwncncHist.GetXaxis().GetTitle(), 
                          "(data - fit)/ data", 1, "PE", root.kBlue, fitfuncModDimitriRelBw)

