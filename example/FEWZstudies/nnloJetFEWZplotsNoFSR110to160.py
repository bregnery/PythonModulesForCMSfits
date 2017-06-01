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
fewzdata = numpy.loadtxt("LeadMu26-NNLO-xs", usecols=range(0,11) )

# extract necessary information
mass = fewzdata[:,0]
nctMu26nnlo1jet = fewzdata[:,7]
errorNctMu261jet = fewzdata[:,8]

#==================================================================================
# Make Histograms /////////////////////////////////////////////////////////////////
#==================================================================================

# Set style options
settings.setSimpleStyle()

# Stat Box options
root.gStyle.SetOptStat(0)

# make root histogram variables
nctMu26nnloExpo1jetHist = root.TH1F("nctMu26nnloExpo1jetHist","Cross Section for NNLO 1jet",50,110,160)
settings.setHistTitles(nctMu26nnloExpo1jetHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section [pb]")

nctMu26nnloChebyshev1jetHist = root.TH1F("nctMu26nnloChebyshev1jetHist","Cross Section for NNLO 1jet",50,110,160)
settings.setHistTitles(nctMu26nnloChebyshev1jetHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section [pb]")

nctMu26nnloDimitri1jetHist = root.TH1F("nctMu26nnloDimitri1jetHist","Cross Section for NNLO 1jet",50,110,160)
settings.setHistTitles(nctMu26nnloDimitri1jetHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section [pb]")

nctMu26nnloBwExpo1jetHist = root.TH1F("nctMu26nnloBwExpo1jetHist","Cross Section for NNLO 1jet",50,110,160)
settings.setHistTitles(nctMu26nnloBwExpo1jetHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section [pb]")

nctMu26nnloRelBwExpo1jetHist = root.TH1F("nctMu26nnloRelBwExpo1jetHist","Cross Section for NNLO 1jet",50,110,160)
settings.setHistTitles(nctMu26nnloRelBwExpo1jetHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section [pb]")

nctMu26nnloPerExpoBw1jetHist = root.TH1F("nctMu26nnloPerExpoBw1jetHist","Cross Section for NNLO 1jet",50,110,160)
settings.setHistTitles(nctMu26nnloPerExpoBw1jetHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section [pb]")

nctMu26nnloPerExpoRelBw1jetHist = root.TH1F("nctMu26nnloPerExpoRelBw1jetHist","Cross Section for NNLO 1jet",50,110,160)
settings.setHistTitles(nctMu26nnloPerExpoRelBw1jetHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section [pb]")

nctMu26nnloDimitriRelBw1jetHist = root.TH1F("nctMu26nnloDimitriRelBw1jetHist","Cross Section for NNLO 1jet",50,110,160)
settings.setHistTitles(nctMu26nnloDimitriRelBw1jetHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section [pb]")

nctMu26nnloModDimitriRelBw1jetHist = root.TH1F("nctMu26nnloModDimitriRelBw1jetHist","Cross Section for NNLO 1jet",50,110,160)
settings.setHistTitles(nctMu26nnloModDimitriRelBw1jetHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section [pb]")

# fill the histograms
for num, xsec, error in zip(range(len(nctMu26nnlo1jet) ), nctMu26nnlo1jet, errorNctMu261jet):
   # must add one because histogram bins start at 1 not 0
   binNum = num + 1

   nctMu26nnloExpo1jetHist.SetBinContent(binNum, xsec)
   nctMu26nnloExpo1jetHist.SetBinError(binNum, error)
   nctMu26nnloChebyshev1jetHist.SetBinContent(binNum, xsec)
   nctMu26nnloChebyshev1jetHist.SetBinError(binNum, error)
   nctMu26nnloDimitri1jetHist.SetBinContent(binNum, xsec)
   nctMu26nnloDimitri1jetHist.SetBinError(binNum, error)
   nctMu26nnloBwExpo1jetHist.SetBinContent(binNum, xsec)
   nctMu26nnloBwExpo1jetHist.SetBinError(binNum, error)
   nctMu26nnloRelBwExpo1jetHist.SetBinContent(binNum, xsec)
   nctMu26nnloRelBwExpo1jetHist.SetBinError(binNum, error)
   nctMu26nnloPerExpoBw1jetHist.SetBinContent(binNum, xsec)
   nctMu26nnloPerExpoBw1jetHist.SetBinError(binNum, error)
   nctMu26nnloPerExpoRelBw1jetHist.SetBinContent(binNum, xsec)
   nctMu26nnloPerExpoRelBw1jetHist.SetBinError(binNum, error)
   nctMu26nnloDimitriRelBw1jetHist.SetBinContent(binNum, xsec)
   nctMu26nnloDimitriRelBw1jetHist.SetBinError(binNum, error)
   nctMu26nnloModDimitriRelBw1jetHist.SetBinContent(binNum, xsec)
   nctMu26nnloModDimitriRelBw1jetHist.SetBinError(binNum, error)

# adjust histogram settings
settings.setDataPoint(nctMu26nnloExpo1jetHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26nnloChebyshev1jetHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26nnloDimitri1jetHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26nnloBwExpo1jetHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26nnloRelBwExpo1jetHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26nnloPerExpoBw1jetHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26nnloPerExpoRelBw1jetHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26nnloDimitriRelBw1jetHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26nnloModDimitriRelBw1jetHist, root.kBlack, root.kFullDotLarge)

#==================================================================================
# Fit the Histograms //////////////////////////////////////////////////////////////
#==================================================================================

# initial values of fit parameters
parameters = numpy.array([0.0711, 4688, 0.0787])
chebyshevParameters = numpy.array([2450.63, -18.2964, 1.70660, -0.158805, 0.0146300, -0.00129222, 0.0000933257, 0.00000176165, -0.00000408221, -0.00000132960, 0])
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

# fit with root
fitfunc = fit.fitTH1(nctMu26nnloExpo1jetHist, 110, 160, parameters, pdf.expopdf, "R", root.kRed)  
fitfuncChebyshev = fit.fitTH1(nctMu26nnloChebyshev1jetHist, 110, 160, chebyshevParameters, pdf.chebyshev, "R", root.kRed)  
fitfuncDimitri = fit.fitTH1(nctMu26nnloDimitri1jetHist, 110, 160, dimitriParameters, pdf.modifiedDimitripdf, "R", root.kRed)  
fitfuncBwExpo = fit.fitTH1(nctMu26nnloBwExpo1jetHist, 110, 160, bwExpoParameters, pdf.bwExpo, "R", root.kRed) 
fitfuncRelBwExpo = fit.fitTH1(nctMu26nnloRelBwExpo1jetHist, 110, 160, relBwExpoParameters, pdf.relBwExpo, "R", root.kRed) 
fitfuncPerExpoBw = fit.fitTH1withParLimits(nctMu26nnloPerExpoBw1jetHist, 110, 160, perExpoBwParameters, pdf.perExpoBw, "R", root.kRed, 
                                           perExpoBwParLimits)
fitfuncPerExpoRelBw = fit.fitTH1withParLimits(nctMu26nnloPerExpoRelBw1jetHist, 110, 160, perExpoRelBwParameters, pdf.perExpoRelBw, 
                                              "R", root.kRed, perExpoRelBwParLimits)
fitfuncDimitriRelBw = fit.fitTH1withParLimits(nctMu26nnloDimitriRelBw1jetHist, 110, 160, dimitriRelBwParameters, pdf.dimitriRelBw, 
                                              "R", root.kRed, dimitriRelBwParLimits)
fitfuncModDimitriRelBw = fit.fitTH1withParLimits(nctMu26nnloModDimitriRelBw1jetHist, 110, 160, modDimitriRelBwParameters, 
                                                 pdf.modDimitriRelBw, "R", root.kRed, modDimitriRelBwParLimits)

#==================================================================================
# Draw Plots //////////////////////////////////////////////////////////////////////
#==================================================================================

# make a TCanvas and a histogram plot with residuals
residualExpoCanvas = root.TCanvas("residualCanvas", "residualCanvas")
settings.makeResidualHist(residualExpoCanvas, nctMu26nnloExpo1jetHist, nctMu26nnloExpo1jetHist.GetXaxis().GetTitle(), 
                          "(fewz - fit)/ fewz", 1, "PE", root.kBlue, fitfunc)

residualChebyshevCanvas = root.TCanvas("residualChebyshevCanvas", "residualChebyshevCanvas")
settings.makeResidualHist(residualChebyshevCanvas, nctMu26nnloChebyshev1jetHist, nctMu26nnloChebyshev1jetHist.GetXaxis().GetTitle(), 
                          "(fewz - fit)/ fewz", 1, "PE", root.kBlue, fitfuncChebyshev)

residualDimitriCanvas = root.TCanvas("residualDimitriCanvas", "residualDimitriCanvas")
settings.makeResidualHist(residualDimitriCanvas, nctMu26nnloDimitri1jetHist, nctMu26nnloDimitri1jetHist.GetXaxis().GetTitle(), 
                          "(fewz - fit)/ fewz", 1, "PE", root.kBlue, fitfuncDimitri)

residualBwExpoCanvas = root.TCanvas("residualBwExpoCanvas", "residualBwExpoCanvas")
settings.makeResidualHist(residualBwExpoCanvas, nctMu26nnloBwExpo1jetHist, nctMu26nnloBwExpo1jetHist.GetXaxis().GetTitle(), 
                          "(fewz - fit)/ fewz", 1, "PE", root.kBlue, fitfuncBwExpo)

residualRelBwExpoCanvas = root.TCanvas("residualRelBwExpoCanvas", "residualRelBwExpoCanvas")
settings.makeResidualHist(residualRelBwExpoCanvas, nctMu26nnloRelBwExpo1jetHist, nctMu26nnloRelBwExpo1jetHist.GetXaxis().GetTitle(), 
                          "(fewz - fit)/ fewz", 1, "PE", root.kBlue, fitfuncRelBwExpo)

residualPerExpoBwCanvas = root.TCanvas("residualPerExpoBwCanvas", "residualPerExpoBwCanvas")
settings.makeResidualHist(residualPerExpoBwCanvas, nctMu26nnloPerExpoBw1jetHist, nctMu26nnloPerExpoBw1jetHist.GetXaxis().GetTitle(), 
                          "(fewz - fit)/ fewz", 1, "PE", root.kBlue, fitfuncPerExpoBw)

residualPerExpoRelBwCanvas = root.TCanvas("residualPerExpoRelBwCanvas", "residualPerExpoRelBwCanvas")
settings.makeResidualHist(residualPerExpoRelBwCanvas, nctMu26nnloPerExpoRelBw1jetHist, 
                          nctMu26nnloPerExpoRelBw1jetHist.GetXaxis().GetTitle(), 
                          "(fewz - fit)/ fewz", 1, "PE", root.kBlue, fitfuncPerExpoRelBw)

residualDimitriRelBwCanvas = root.TCanvas("residualDimitriRelBwCanvas", "residualDimitriRelBwCanvas")
settings.makeResidualHist(residualDimitriRelBwCanvas, nctMu26nnloDimitriRelBw1jetHist, 
                          nctMu26nnloDimitriRelBw1jetHist.GetXaxis().GetTitle(), 
                          "(fewz - fit)/ fewz", 1, "PE", root.kBlue, fitfuncDimitriRelBw)

residualModDimitriRelBwCanvas = root.TCanvas("residualModDimitriRelBwCanvas", "residualModDimitriRelBwCanvas")
settings.makeResidualHist(residualModDimitriRelBwCanvas, nctMu26nnloModDimitriRelBw1jetHist, 
                          nctMu26nnloModDimitriRelBw1jetHist.GetXaxis().GetTitle(), 
                          "(fewz - fit)/ fewz", 1, "PE", root.kBlue, fitfuncModDimitriRelBw)

