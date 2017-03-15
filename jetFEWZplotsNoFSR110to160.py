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
fewzdata = numpy.loadtxt("LeadMu26-13tev-xs", usecols=range(0,9) )

# extract necessary information
mass = fewzdata[:,0]
nctMu261jet = fewzdata[:,7]
errorNctMu261jet = fewzdata[:,8]

#==================================================================================
# Make Histograms /////////////////////////////////////////////////////////////////
#==================================================================================

# Set style options
settings.setSimpleStyle()

# Stat Box options
root.gStyle.SetOptStat(0)

# make root histogram variables
nctMu26Expo1jetHist = root.TH1F("nctMu26Expo1jetHist","Cross Section for NLO CT 1jet",50,110,160)
settings.setHistTitles(nctMu26Expo1jetHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section")

nctMu26Chebyshev1jetHist = root.TH1F("nctMu26Chebyshev1jetHist","Cross Section for NLO CT 1jet",50,110,160)
settings.setHistTitles(nctMu26Chebyshev1jetHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section")

nctMu26Dimitri1jetHist = root.TH1F("nctMu26Dimitri1jetHist","Cross Section for NLO CT 1jet",50,110,160)
settings.setHistTitles(nctMu26Dimitri1jetHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section")

nctMu26BwExpo1jetHist = root.TH1F("nctMu26BwExpo1jetHist","Cross Section for NLO CT 1jet",50,110,160)
settings.setHistTitles(nctMu26BwExpo1jetHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section")

nctMu26RelBwExpo1jetHist = root.TH1F("nctMu26RelBwExpo1jetHist","Cross Section for NLO CT 1jet",50,110,160)
settings.setHistTitles(nctMu26RelBwExpo1jetHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section")

nctMu26PerExpoBw1jetHist = root.TH1F("nctMu26PerExpoBw1jetHist","Cross Section for NLO CT 1jet",50,110,160)
settings.setHistTitles(nctMu26PerExpoBw1jetHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section")

nctMu26PerExpoRelBw1jetHist = root.TH1F("nctMu26PerExpoRelBw1jetHist","Cross Section for NLO CT 1jet",50,110,160)
settings.setHistTitles(nctMu26PerExpoRelBw1jetHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section")

nctMu26DimitriRelBw1jetHist = root.TH1F("nctMu26DimitriRelBw1jetHist","Cross Section for NLO CT 1jet",50,110,160)
settings.setHistTitles(nctMu26DimitriRelBw1jetHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section")

nctMu26ModDimitriRelBw1jetHist = root.TH1F("nctMu26ModDimitriRelBw1jetHist","Cross Section for NLO CT 1jet",50,110,160)
settings.setHistTitles(nctMu26ModDimitriRelBw1jetHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section")

# fill the histograms
for num, xsec, error in zip(range(len(nctMu261jet) ), nctMu261jet, errorNctMu261jet):
   # must add one because histogram bins start at 1 not 0
   binNum = num + 1

   nctMu26Expo1jetHist.SetBinContent(binNum, xsec)
   nctMu26Expo1jetHist.SetBinError(binNum, error)
   nctMu26Chebyshev1jetHist.SetBinContent(binNum, xsec)
   nctMu26Chebyshev1jetHist.SetBinError(binNum, error)
   nctMu26Dimitri1jetHist.SetBinContent(binNum, xsec)
   nctMu26Dimitri1jetHist.SetBinError(binNum, error)
   nctMu26BwExpo1jetHist.SetBinContent(binNum, xsec)
   nctMu26BwExpo1jetHist.SetBinError(binNum, error)
   nctMu26RelBwExpo1jetHist.SetBinContent(binNum, xsec)
   nctMu26RelBwExpo1jetHist.SetBinError(binNum, error)
   nctMu26PerExpoBw1jetHist.SetBinContent(binNum, xsec)
   nctMu26PerExpoBw1jetHist.SetBinError(binNum, error)
   nctMu26PerExpoRelBw1jetHist.SetBinContent(binNum, xsec)
   nctMu26PerExpoRelBw1jetHist.SetBinError(binNum, error)
   nctMu26DimitriRelBw1jetHist.SetBinContent(binNum, xsec)
   nctMu26DimitriRelBw1jetHist.SetBinError(binNum, error)
   nctMu26ModDimitriRelBw1jetHist.SetBinContent(binNum, xsec)
   nctMu26ModDimitriRelBw1jetHist.SetBinError(binNum, error)

# adjust histogram settings
settings.setDataPoint(nctMu26Expo1jetHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26Chebyshev1jetHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26Dimitri1jetHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26BwExpo1jetHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26RelBwExpo1jetHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26PerExpoBw1jetHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26PerExpoRelBw1jetHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26DimitriRelBw1jetHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26ModDimitriRelBw1jetHist, root.kBlack, root.kFullDotLarge)

#==================================================================================
# Fit the Histograms //////////////////////////////////////////////////////////////
#==================================================================================

# initial values of fit parameters
parameters = numpy.array([0.0711, 4688, 0.0787])
chebyshevParameters = numpy.array([396, -11.2, 0.0515, -0.000024, -0.0000005, 0.0000000015, -0.0000000000013]) #[62, -1.3, 0.005, -0.000006, 0.00000001, -0.00000000005, 0.00000000000007])
dimitriParameters = numpy.array([0.2968, -0.7566, -2.261, 0.6513]) #[4688, 0.01, -0.079, 0.0001])
bwExpoParameters = numpy.array([0.379, -0.0053])
relBwExpoParameters = numpy.array([0.379, -0.0053])
perExpoBwParameters = numpy.array([11, 1.91, 1.96, -0.59])
perExpoRelBwParameters = numpy.array([73000, 1.91, 3.5, -0.84])
dimitriRelBwParameters = numpy.array([77, 1.5, -0.57])
modDimitriRelBwParameters = numpy.array([77, 1.96, 1.5, -0.57])

# parameter limits
perExpoBwParLimits = numpy.array([[1, 1.5, 2.5],[3, -1.2, -0.12]])
perExpoRelBwParLimits = numpy.array([[1, 1.5, 2.5],[3, -1.2, -0.12]])
dimitriRelBwParLimits = numpy.array([[2, -1.2, -0.12]])
modDimitriRelBwParLimits = numpy.array([[1, 1.5, 2.5],[3, -1.2, -0.12]])
chebyshevParLimits = numpy.array([[3, -0.0001, 0],[4, -0.000001, 0],[5, 0, 0.00000001],[6, -0.00000000001, 0]])

# fit with root
fitfunc = fit.fitTH1(nctMu26Expo1jetHist, 110, 160, parameters, pdf.expopdf, "R", root.kRed)  
fitfuncChebyshev = fit.fitTH1withParLimits(nctMu26Chebyshev1jetHist, 110, 160, chebyshevParameters, pdf.chebyshev, "R", root.kRed,
                                           chebyshevParLimits)  
fitfuncDimitri = fit.fitTH1(nctMu26Dimitri1jetHist, 110, 160, dimitriParameters, pdf.modifiedDimitripdf, "R", root.kRed)  
fitfuncBwExpo = fit.fitTH1(nctMu26BwExpo1jetHist, 110, 160, bwExpoParameters, pdf.bwExpo, "R", root.kRed) 
fitfuncRelBwExpo = fit.fitTH1(nctMu26RelBwExpo1jetHist, 110, 160, relBwExpoParameters, pdf.relBwExpo, "R", root.kRed) 
fitfuncPerExpoBw = fit.fitTH1withParLimits(nctMu26PerExpoBw1jetHist, 110, 160, perExpoBwParameters, pdf.perExpoBw, "R", root.kRed, 
                                           perExpoBwParLimits)
fitfuncPerExpoRelBw = fit.fitTH1withParLimits(nctMu26PerExpoRelBw1jetHist, 110, 160, perExpoRelBwParameters, pdf.perExpoRelBw, 
                                              "R", root.kRed, perExpoRelBwParLimits)
fitfuncDimitriRelBw = fit.fitTH1withParLimits(nctMu26DimitriRelBw1jetHist, 110, 160, dimitriRelBwParameters, pdf.dimitriRelBw, 
                                              "R", root.kRed, dimitriRelBwParLimits)
fitfuncModDimitriRelBw = fit.fitTH1withParLimits(nctMu26ModDimitriRelBw1jetHist, 110, 160, modDimitriRelBwParameters, 
                                                 pdf.modDimitriRelBw, "R", root.kRed, modDimitriRelBwParLimits)

#==================================================================================
# Draw Plots //////////////////////////////////////////////////////////////////////
#==================================================================================

# make a TCanvas and a histogram plot with residuals
residualExpoCanvas = root.TCanvas("residualCanvas", "residualCanvas")
settings.makeResidualHist(residualExpoCanvas, nctMu26Expo1jetHist, nctMu26Expo1jetHist.GetXaxis().GetTitle(), 
                          "(data - fit)/ data", 1, "PE", root.kBlue, fitfunc)

residualChebyshevCanvas = root.TCanvas("residualChebyshevCanvas", "residualChebyshevCanvas")
settings.makeResidualHist(residualChebyshevCanvas, nctMu26Chebyshev1jetHist, nctMu26Chebyshev1jetHist.GetXaxis().GetTitle(), 
                          "(data - fit)/ data", 1, "PE", root.kBlue, fitfuncChebyshev)

residualDimitriCanvas = root.TCanvas("residualDimitriCanvas", "residualDimitriCanvas")
settings.makeResidualHist(residualDimitriCanvas, nctMu26Dimitri1jetHist, nctMu26Dimitri1jetHist.GetXaxis().GetTitle(), 
                          "(data - fit)/ data", 1, "PE", root.kBlue, fitfuncDimitri)

residualBwExpoCanvas = root.TCanvas("residualBwExpoCanvas", "residualBwExpoCanvas")
settings.makeResidualHist(residualBwExpoCanvas, nctMu26BwExpo1jetHist, nctMu26BwExpo1jetHist.GetXaxis().GetTitle(), 
                          "(data - fit)/ data", 1, "PE", root.kBlue, fitfuncBwExpo)

residualRelBwExpoCanvas = root.TCanvas("residualRelBwExpoCanvas", "residualRelBwExpoCanvas")
settings.makeResidualHist(residualRelBwExpoCanvas, nctMu26RelBwExpo1jetHist, nctMu26RelBwExpo1jetHist.GetXaxis().GetTitle(), 
                          "(data - fit)/ data", 1, "PE", root.kBlue, fitfuncRelBwExpo)

residualPerExpoBwCanvas = root.TCanvas("residualPerExpoBwCanvas", "residualPerExpoBwCanvas")
settings.makeResidualHist(residualPerExpoBwCanvas, nctMu26PerExpoBw1jetHist, nctMu26PerExpoBw1jetHist.GetXaxis().GetTitle(), 
                          "(data - fit)/ data", 1, "PE", root.kBlue, fitfuncPerExpoBw)

residualPerExpoRelBwCanvas = root.TCanvas("residualPerExpoRelBwCanvas", "residualPerExpoRelBwCanvas")
settings.makeResidualHist(residualPerExpoRelBwCanvas, nctMu26PerExpoRelBw1jetHist, 
                          nctMu26PerExpoRelBw1jetHist.GetXaxis().GetTitle(), 
                          "(data - fit)/ data", 1, "PE", root.kBlue, fitfuncPerExpoRelBw)

residualDimitriRelBwCanvas = root.TCanvas("residualDimitriRelBwCanvas", "residualDimitriRelBwCanvas")
settings.makeResidualHist(residualDimitriRelBwCanvas, nctMu26DimitriRelBw1jetHist, 
                          nctMu26DimitriRelBw1jetHist.GetXaxis().GetTitle(), 
                          "(data - fit)/ data", 1, "PE", root.kBlue, fitfuncDimitriRelBw)

residualModDimitriRelBwCanvas = root.TCanvas("residualModDimitriRelBwCanvas", "residualModDimitriRelBwCanvas")
settings.makeResidualHist(residualModDimitriRelBwCanvas, nctMu26ModDimitriRelBw1jetHist, 
                          nctMu26ModDimitriRelBw1jetHist.GetXaxis().GetTitle(), 
                          "(data - fit)/ data", 1, "PE", root.kBlue, fitfuncModDimitriRelBw)

