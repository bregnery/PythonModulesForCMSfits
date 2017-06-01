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
fewzdata = numpy.loadtxt("LeadMu26-NNLO-xs", usecols=range(0,11) )

# extract necessary information
mass = fewzdata[:,0]
nctMu26nnlocc = fewzdata[:,3]
errorNctMu26cc = fewzdata[:,4]

#==================================================================================
# Make Histograms /////////////////////////////////////////////////////////////////
#==================================================================================

# Set style options
settings.setSimpleStyle()

# Stat Box options
root.gStyle.SetOptStat(0)

# make root histogram variables
nctMu26nnloExpoccHist = root.TH1F("nctMu26nnloExpoccHist","Cross Section for NNLO cc",50,110,160)
settings.setHistTitles(nctMu26nnloExpoccHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section")

nctMu26nnloChebyshevccHist = root.TH1F("nctMu26nnloChebyshevccHist","Cross Section for NNLO cc",50,110,160)
settings.setHistTitles(nctMu26nnloChebyshevccHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section")

nctMu26nnloDimitriccHist = root.TH1F("nctMu26nnloDimitriccHist","Cross Section for NNLO cc",50,110,160)
settings.setHistTitles(nctMu26nnloDimitriccHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section")

nctMu26nnloBwExpoccHist = root.TH1F("nctMu26nnloBwExpoccHist","Cross Section for NNLO cc",50,110,160)
settings.setHistTitles(nctMu26nnloBwExpoccHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section")

nctMu26nnloRelBwExpoccHist = root.TH1F("nctMu26nnloRelBwExpoccHist","Cross Section for NNLO cc",50,110,160)
settings.setHistTitles(nctMu26nnloRelBwExpoccHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section")

nctMu26nnloPerExpoBwccHist = root.TH1F("nctMu26nnloPerExpoBwccHist","Cross Section for NNLO cc",50,110,160)
settings.setHistTitles(nctMu26nnloPerExpoBwccHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section")

nctMu26nnloPerExpoRelBwccHist = root.TH1F("nctMu26nnloPerExpoRelBwccHist","Cross Section for NNLO cc",50,110,160)
settings.setHistTitles(nctMu26nnloPerExpoRelBwccHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section")

nctMu26nnloDimitriRelBwccHist = root.TH1F("nctMu26nnloDimitriRelBwccHist","Cross Section for NNLO cc",50,110,160)
settings.setHistTitles(nctMu26nnloDimitriRelBwccHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section")

nctMu26nnloModDimitriRelBwccHist = root.TH1F("nctMu26nnloModDimitriRelBwccHist","Cross Section for NNLO cc",50,110,160)
settings.setHistTitles(nctMu26nnloModDimitriRelBwccHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section")

# fill the histograms
for num, xsec, error in zip(range(len(nctMu26nnlocc) ), nctMu26nnlocc, errorNctMu26cc):
   # must add one because histogram bins start at 1 not 0
   binNum = num + 1

   nctMu26nnloExpoccHist.SetBinContent(binNum, xsec)
   nctMu26nnloExpoccHist.SetBinError(binNum, error)
   nctMu26nnloChebyshevccHist.SetBinContent(binNum, xsec)
   nctMu26nnloChebyshevccHist.SetBinError(binNum, error)
   nctMu26nnloDimitriccHist.SetBinContent(binNum, xsec)
   nctMu26nnloDimitriccHist.SetBinError(binNum, error)
   nctMu26nnloBwExpoccHist.SetBinContent(binNum, xsec)
   nctMu26nnloBwExpoccHist.SetBinError(binNum, error)
   nctMu26nnloRelBwExpoccHist.SetBinContent(binNum, xsec)
   nctMu26nnloRelBwExpoccHist.SetBinError(binNum, error)
   nctMu26nnloPerExpoBwccHist.SetBinContent(binNum, xsec)
   nctMu26nnloPerExpoBwccHist.SetBinError(binNum, error)
   nctMu26nnloPerExpoRelBwccHist.SetBinContent(binNum, xsec)
   nctMu26nnloPerExpoRelBwccHist.SetBinError(binNum, error)
   nctMu26nnloDimitriRelBwccHist.SetBinContent(binNum, xsec)
   nctMu26nnloDimitriRelBwccHist.SetBinError(binNum, error)
   nctMu26nnloModDimitriRelBwccHist.SetBinContent(binNum, xsec)
   nctMu26nnloModDimitriRelBwccHist.SetBinError(binNum, error)

# adjust histogram settings
settings.setDataPoint(nctMu26nnloExpoccHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26nnloChebyshevccHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26nnloDimitriccHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26nnloBwExpoccHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26nnloRelBwExpoccHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26nnloPerExpoBwccHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26nnloPerExpoRelBwccHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26nnloDimitriRelBwccHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26nnloModDimitriRelBwccHist, root.kBlack, root.kFullDotLarge)

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
modDimitriRelBwParameters = numpy.array([340, 1.9, -1.8, 0.4])

# parameter limits
perExpoBwParLimits = numpy.array([[1, 1.5, 2.5],[3, -0.6, -0.12]])
perExpoRelBwParLimits = numpy.array([[1, 1.5, 2.5],[3, -1.2, -0.12]])
dimitriRelBwParLimits = numpy.array([[2, -9, 7]])
modDimitriRelBwParLimits = numpy.array([[1, 1.5, 2.8]]) #,[3, -1.2, -0.12]])
chebyshevParLimits = numpy.array([[3, -0.0001, 0],[4, -0.000001, 0],[5, 0, 0.00000001],[6, -0.00000000001, 0]])

# fit with root
fitfunc = fit.fitTH1(nctMu26nnloExpoccHist, 110, 160, parameters, pdf.expopdf, "R", root.kRed)  
fitfuncChebyshev = fit.fitTH1withParLimits(nctMu26nnloChebyshevccHist, 110, 160, chebyshevParameters, pdf.chebyshev, "R", root.kRed,
                                           chebyshevParLimits)  
fitfuncDimitri = fit.fitTH1(nctMu26nnloDimitriccHist, 110, 160, dimitriParameters, pdf.modifiedDimitripdf, "R", root.kRed)  
fitfuncBwExpo = fit.fitTH1(nctMu26nnloBwExpoccHist, 110, 160, bwExpoParameters, pdf.bwExpo, "R", root.kRed) 
fitfuncRelBwExpo = fit.fitTH1(nctMu26nnloRelBwExpoccHist, 110, 160, relBwExpoParameters, pdf.relBwExpo, "R", root.kRed) 
fitfuncPerExpoBw = fit.fitTH1withParLimits(nctMu26nnloPerExpoBwccHist, 110, 160, perExpoBwParameters, pdf.perExpoBw, "R", root.kRed, 
                                           perExpoBwParLimits)
fitfuncPerExpoRelBw = fit.fitTH1withParLimits(nctMu26nnloPerExpoRelBwccHist, 110, 160, perExpoRelBwParameters, pdf.perExpoRelBw, 
                                              "R", root.kRed, perExpoRelBwParLimits)
fitfuncDimitriRelBw = fit.fitTH1withParLimits(nctMu26nnloDimitriRelBwccHist, 110, 160, dimitriRelBwParameters, pdf.dimitriRelBw, 
                                              "R", root.kRed, dimitriRelBwParLimits)
fitfuncModDimitriRelBw = fit.fitTH1withParLimits(nctMu26nnloModDimitriRelBwccHist, 110, 160, modDimitriRelBwParameters, 
                                                 pdf.modDimitriRelBw, "R", root.kRed, modDimitriRelBwParLimits)

#==================================================================================
# Draw Plots //////////////////////////////////////////////////////////////////////
#==================================================================================

# make a TCanvas and a histogram plot with residuals
residualExpoCanvas = root.TCanvas("residualCanvas", "residualCanvas")
settings.makeResidualHist(residualExpoCanvas, nctMu26nnloExpoccHist, nctMu26nnloExpoccHist.GetXaxis().GetTitle(), 
                          "(fewz - fit)/ fewz", 1, "PE", root.kBlue, fitfunc)

residualChebyshevCanvas = root.TCanvas("residualChebyshevCanvas", "residualChebyshevCanvas")
settings.makeResidualHist(residualChebyshevCanvas, nctMu26nnloChebyshevccHist, nctMu26nnloChebyshevccHist.GetXaxis().GetTitle(), 
                          "(fewz - fit)/ fewz", 1, "PE", root.kBlue, fitfuncChebyshev)

residualDimitriCanvas = root.TCanvas("residualDimitriCanvas", "residualDimitriCanvas")
settings.makeResidualHist(residualDimitriCanvas, nctMu26nnloDimitriccHist, nctMu26nnloDimitriccHist.GetXaxis().GetTitle(), 
                          "(fewz - fit)/ fewz", 1, "PE", root.kBlue, fitfuncDimitri)

residualBwExpoCanvas = root.TCanvas("residualBwExpoCanvas", "residualBwExpoCanvas")
settings.makeResidualHist(residualBwExpoCanvas, nctMu26nnloBwExpoccHist, nctMu26nnloBwExpoccHist.GetXaxis().GetTitle(), 
                          "(fewz - fit)/ fewz", 1, "PE", root.kBlue, fitfuncBwExpo)

residualRelBwExpoCanvas = root.TCanvas("residualRelBwExpoCanvas", "residualRelBwExpoCanvas")
settings.makeResidualHist(residualRelBwExpoCanvas, nctMu26nnloRelBwExpoccHist, nctMu26nnloRelBwExpoccHist.GetXaxis().GetTitle(), 
                          "(fewz - fit)/ fewz", 1, "PE", root.kBlue, fitfuncRelBwExpo)

residualPerExpoBwCanvas = root.TCanvas("residualPerExpoBwCanvas", "residualPerExpoBwCanvas")
settings.makeResidualHist(residualPerExpoBwCanvas, nctMu26nnloPerExpoBwccHist, nctMu26nnloPerExpoBwccHist.GetXaxis().GetTitle(), 
                          "(fewz - fit)/ fewz", 1, "PE", root.kBlue, fitfuncPerExpoBw)

residualPerExpoRelBwCanvas = root.TCanvas("residualPerExpoRelBwCanvas", "residualPerExpoRelBwCanvas")
settings.makeResidualHist(residualPerExpoRelBwCanvas, nctMu26nnloPerExpoRelBwccHist, 
                          nctMu26nnloPerExpoRelBwccHist.GetXaxis().GetTitle(), 
                          "(fewz - fit)/ fewz", 1, "PE", root.kBlue, fitfuncPerExpoRelBw)

residualDimitriRelBwCanvas = root.TCanvas("residualDimitriRelBwCanvas", "residualDimitriRelBwCanvas")
settings.makeResidualHist(residualDimitriRelBwCanvas, nctMu26nnloDimitriRelBwccHist, 
                          nctMu26nnloDimitriRelBwccHist.GetXaxis().GetTitle(), 
                          "(fewz - fit)/ fewz", 1, "PE", root.kBlue, fitfuncDimitriRelBw)

residualModDimitriRelBwCanvas = root.TCanvas("residualModDimitriRelBwCanvas", "residualModDimitriRelBwCanvas")
settings.makeResidualHist(residualModDimitriRelBwCanvas, nctMu26nnloModDimitriRelBwccHist, 
                          nctMu26nnloModDimitriRelBwccHist.GetXaxis().GetTitle(), 
                          "(fewz - fit)/ fewz", 1, "PE", root.kBlue, fitfuncModDimitriRelBw)

