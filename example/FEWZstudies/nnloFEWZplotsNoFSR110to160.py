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
nctMu26nnloFull = fewzdata[:,5]
errorNctMu26Full = fewzdata[:,6]

#==================================================================================
# Make Histograms /////////////////////////////////////////////////////////////////
#==================================================================================

# Set style options
settings.setSimpleStyle()

# Stat Box options
root.gStyle.SetOptStat(0)

# make root histogram variables
nctMu26nnloExpoFullHist = root.TH1F("nctMu26nnloExpoFullHist","Cross Section for NNLO Full ",50,110,160)
settings.setHistTitles(nctMu26nnloExpoFullHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section [pb]")

nctMu26nnloChebyshevFullHist = root.TH1F("nctMu26nnloChebyshevFullHist","Cross Section for NNLO Full ",50,110,160)
settings.setHistTitles(nctMu26nnloChebyshevFullHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section [pb]")

nctMu26nnloBernsteinFullHist = root.TH1F("nctMu26nnloBernsteinFullHist","Cross Section for NNLO Full ",50,110,160)
settings.setHistTitles(nctMu26nnloBernsteinFullHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section [pb]")

nctMu26nnloDimitriFullHist = root.TH1F("nctMu26nnloDimitriFullHist","Cross Section for NNLO Full ",50,110,160)
settings.setHistTitles(nctMu26nnloDimitriFullHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section [pb]")

nctMu26nnloBwExpoFullHist = root.TH1F("nctMu26nnloBwExpoFullHist","Cross Section for NNLO Full ",50,110,160)
settings.setHistTitles(nctMu26nnloBwExpoFullHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section [pb]")

nctMu26nnloRelBwExpoFullHist = root.TH1F("nctMu26nnloRelBwExpoFullHist","Cross Section for NNLO Full ",50,110,160)
settings.setHistTitles(nctMu26nnloRelBwExpoFullHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section [pb]")

nctMu26nnloPerExpoBwFullHist = root.TH1F("nctMu26nnloPerExpoBwFullHist","Cross Section for NNLO Full ",50,110,160)
settings.setHistTitles(nctMu26nnloPerExpoBwFullHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section [pb]")

nctMu26nnloPerExpoRelBwFullHist = root.TH1F("nctMu26nnloPerExpoRelBwFullHist","Cross Section for NNLO Full ",50,110,160)
settings.setHistTitles(nctMu26nnloPerExpoRelBwFullHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section [pb]")

nctMu26nnloDimitriRelBwFullHist = root.TH1F("nctMu26nnloDimitriRelBwFullHist","Cross Section for NNLO Full ",50,110,160)
settings.setHistTitles(nctMu26nnloDimitriRelBwFullHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section [pb]")

nctMu26nnloModDimitriRelBwFullHist = root.TH1F("nctMu26nnloModDimitriRelBwFullHist","Cross Section for NNLO Full ",50,110,160)
settings.setHistTitles(nctMu26nnloModDimitriRelBwFullHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section [pb]")

# fill the histograms
for num, xsec, error in zip(range(len(nctMu26nnloFull) ), nctMu26nnloFull, errorNctMu26Full):
   # must add one because histogram bins start at 1 not 0
   binNum = num + 1

   nctMu26nnloExpoFullHist.SetBinContent(binNum, xsec)
   nctMu26nnloExpoFullHist.SetBinError(binNum, error)
   nctMu26nnloChebyshevFullHist.SetBinContent(binNum, xsec)
   nctMu26nnloChebyshevFullHist.SetBinError(binNum, error)
   nctMu26nnloBernsteinFullHist.SetBinContent(binNum, xsec)
   nctMu26nnloBernsteinFullHist.SetBinError(binNum, error)
   nctMu26nnloDimitriFullHist.SetBinContent(binNum, xsec)
   nctMu26nnloDimitriFullHist.SetBinError(binNum, error)
   nctMu26nnloBwExpoFullHist.SetBinContent(binNum, xsec)
   nctMu26nnloBwExpoFullHist.SetBinError(binNum, error)
   nctMu26nnloRelBwExpoFullHist.SetBinContent(binNum, xsec)
   nctMu26nnloRelBwExpoFullHist.SetBinError(binNum, error)
   nctMu26nnloPerExpoBwFullHist.SetBinContent(binNum, xsec)
   nctMu26nnloPerExpoBwFullHist.SetBinError(binNum, error)
   nctMu26nnloPerExpoRelBwFullHist.SetBinContent(binNum, xsec)
   nctMu26nnloPerExpoRelBwFullHist.SetBinError(binNum, error)
   nctMu26nnloDimitriRelBwFullHist.SetBinContent(binNum, xsec)
   nctMu26nnloDimitriRelBwFullHist.SetBinError(binNum, error)
   nctMu26nnloModDimitriRelBwFullHist.SetBinContent(binNum, xsec)
   nctMu26nnloModDimitriRelBwFullHist.SetBinError(binNum, error)

# adjust histogram settings
settings.setDataPoint(nctMu26nnloExpoFullHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26nnloChebyshevFullHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26nnloBernsteinFullHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26nnloDimitriFullHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26nnloBwExpoFullHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26nnloRelBwExpoFullHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26nnloPerExpoBwFullHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26nnloPerExpoRelBwFullHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26nnloDimitriRelBwFullHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26nnloModDimitriRelBwFullHist, root.kBlack, root.kFullDotLarge)

#==================================================================================
# Fit the Histograms //////////////////////////////////////////////////////////////
#==================================================================================

# initial values of fit parameters
parameters = numpy.array([0.0711, 4688, 0.0787])
#chebyshevParameters = numpy.array([2450, -18.3, 1.71, -0.159, 0.0146, -0.00129, 0.000092])
chebyshevParameters = numpy.array([2450.63, -18.2964, 1.70660, -0.158805, 0.0146300, -0.00129222, 0.0000933257, 0.00000176165, -0.00000408221, -0.00000132960, 0])
bernsteinParameters = numpy.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) #[396, -11.2, 0.0515, -0.000024, -0.0000005, 0.0000000015, -0.0000000000013]) #[62, -1.3, 0.005, -0.000006, 0.00000001, -0.00000000005, 0.00000000000007])
dimitriParameters = numpy.array([0.2968, -0.7566, -2.261, 0.6513]) #[4688, 0.01, -0.079, 0.0001])
bwExpoParameters = numpy.array([0.379, -0.0053])
relBwExpoParameters = numpy.array([0.379, -0.0053])
perExpoBwParameters = numpy.array([107, 1.94, 1.46, -0.54])
perExpoRelBwParameters = numpy.array([870000, 1.94, 2.3, -0.6])
dimitriRelBwParameters = numpy.array([965.2, 0.548, -0.37069])
modDimitriRelBwParameters = numpy.array([118, 2.5, 7, -2])

# parameter limits
perExpoBwParLimits = numpy.array([[1, 1.5, 2.5],[3, -0.6, -0.12]])
perExpoRelBwParLimits = numpy.array([[1, 1.5, 2.5],[3, -1.2, -0.12]])
dimitriRelBwParLimits = numpy.array([[2, -1.2, -0.12]])
modDimitriRelBwParLimits = numpy.array([[1, 1.5, 2.8]])#,[3, -1.2, -0.12]])
chebyshevParLimits = numpy.array([[3, -0.0001, 0.0001],[4, -0.000001, 0.000001],[5, -0.00000001, 0.00000001],[6, -0.00000000001, 0.00000000001]])

# fit with root
fitfunc = fit.fitTH1(nctMu26nnloExpoFullHist, 110, 160, parameters, pdf.expopdf, "R", root.kRed)  
fitfuncChebyshev = fit.fitTH1(nctMu26nnloChebyshevFullHist, 110, 160, chebyshevParameters, pdf.chebyshev, "S", root.kRed)
                                           #chebyshevParLimits)  
fitfuncBernstein = fit.fitTH1(nctMu26nnloBernsteinFullHist, 110, 160, bernsteinParameters, pdf.bernstein, "S", root.kRed)
fitfuncDimitri = fit.fitTH1(nctMu26nnloDimitriFullHist, 110, 160, dimitriParameters, pdf.modifiedDimitripdf, "R", root.kRed)  
fitfuncBwExpo = fit.fitTH1(nctMu26nnloBwExpoFullHist, 110, 160, bwExpoParameters, pdf.bwExpo, "R", root.kRed) 
fitfuncRelBwExpo = fit.fitTH1(nctMu26nnloRelBwExpoFullHist, 110, 160, relBwExpoParameters, pdf.relBwExpo, "R", root.kRed) 
fitfuncPerExpoBw = fit.fitTH1withParLimits(nctMu26nnloPerExpoBwFullHist, 110, 160, perExpoBwParameters, pdf.perExpoBw, "R", root.kRed, 
                                           perExpoBwParLimits)
fitfuncPerExpoRelBw = fit.fitTH1withParLimits(nctMu26nnloPerExpoRelBwFullHist, 110, 160, perExpoRelBwParameters, pdf.perExpoRelBw, 
                                              "R", root.kRed, perExpoRelBwParLimits)
fitfuncDimitriRelBw = fit.fitTH1withParLimits(nctMu26nnloDimitriRelBwFullHist, 110, 160, dimitriRelBwParameters, pdf.dimitriRelBw, 
                                              "R", root.kRed, dimitriRelBwParLimits)
fitfuncModDimitriRelBw = fit.fitTH1withParLimits(nctMu26nnloModDimitriRelBwFullHist, 110, 160, modDimitriRelBwParameters, 
                                                 pdf.modDimitriRelBw, "R", root.kRed, modDimitriRelBwParLimits)

#==================================================================================
# Draw Plots //////////////////////////////////////////////////////////////////////
#==================================================================================

# make a TCanvas and a histogram plot with residuals
residualExpoCanvas = root.TCanvas("residualCanvas", "residualCanvas")
settings.makeResidualHist(residualExpoCanvas, nctMu26nnloExpoFullHist, nctMu26nnloExpoFullHist.GetXaxis().GetTitle(), 
                          "(fewz - fit)/ fewz", 1, "PE", root.kBlue, fitfunc)

residualChebyshevCanvas = root.TCanvas("residualChebyshevCanvas", "residualChebyshevCanvas")
settings.makeResidualHist(residualChebyshevCanvas, nctMu26nnloChebyshevFullHist, nctMu26nnloChebyshevFullHist.GetXaxis().GetTitle(), 
                          "(fewz - fit)/ fewz", 1, "PE", root.kBlue, fitfuncChebyshev)

residualBernsteinCanvas = root.TCanvas("residualBernsteinCanvas", "residualBernsteinCanvas")
settings.makeResidualHist(residualBernsteinCanvas, nctMu26nnloBernsteinFullHist, nctMu26nnloBernsteinFullHist.GetXaxis().GetTitle(), 
                          "(fewz - fit)/ fewz", 1, "PE", root.kBlue, fitfuncBernstein)

residualDimitriCanvas = root.TCanvas("residualDimitriCanvas", "residualDimitriCanvas")
settings.makeResidualHist(residualDimitriCanvas, nctMu26nnloDimitriFullHist, nctMu26nnloDimitriFullHist.GetXaxis().GetTitle(), 
                          "(fewz - fit)/ fewz", 1, "PE", root.kBlue, fitfuncDimitri)

residualBwExpoCanvas = root.TCanvas("residualBwExpoCanvas", "residualBwExpoCanvas")
settings.makeResidualHist(residualBwExpoCanvas, nctMu26nnloBwExpoFullHist, nctMu26nnloBwExpoFullHist.GetXaxis().GetTitle(), 
                          "(fewz - fit)/ fewz", 1, "PE", root.kBlue, fitfuncBwExpo)

residualRelBwExpoCanvas = root.TCanvas("residualRelBwExpoCanvas", "residualRelBwExpoCanvas")
settings.makeResidualHist(residualRelBwExpoCanvas, nctMu26nnloRelBwExpoFullHist, nctMu26nnloRelBwExpoFullHist.GetXaxis().GetTitle(), 
                          "(fewz - fit)/ fewz", 1, "PE", root.kBlue, fitfuncRelBwExpo)

residualPerExpoBwCanvas = root.TCanvas("residualPerExpoBwCanvas", "residualPerExpoBwCanvas")
settings.makeResidualHist(residualPerExpoBwCanvas, nctMu26nnloPerExpoBwFullHist, nctMu26nnloPerExpoBwFullHist.GetXaxis().GetTitle(), 
                          "(fewz - fit)/ fewz", 1, "PE", root.kBlue, fitfuncPerExpoBw)

residualPerExpoRelBwCanvas = root.TCanvas("residualPerExpoRelBwCanvas", "residualPerExpoRelBwCanvas")
settings.makeResidualHist(residualPerExpoRelBwCanvas, nctMu26nnloPerExpoRelBwFullHist, 
                          nctMu26nnloPerExpoRelBwFullHist.GetXaxis().GetTitle(), 
                          "(fewz - fit)/ fewz", 1, "PE", root.kBlue, fitfuncPerExpoRelBw)

residualDimitriRelBwCanvas = root.TCanvas("residualDimitriRelBwCanvas", "residualDimitriRelBwCanvas")
settings.makeResidualHist(residualDimitriRelBwCanvas, nctMu26nnloDimitriRelBwFullHist, 
                          nctMu26nnloDimitriRelBwFullHist.GetXaxis().GetTitle(), 
                          "(fewz - fit)/ fewz", 1, "PE", root.kBlue, fitfuncDimitriRelBw)

residualModDimitriRelBwCanvas = root.TCanvas("residualModDimitriRelBwCanvas", "residualModDimitriRelBwCanvas")
settings.makeResidualHist(residualModDimitriRelBwCanvas, nctMu26nnloModDimitriRelBwFullHist, 
                          nctMu26nnloModDimitriRelBwFullHist.GetXaxis().GetTitle(), 
                          "(fewz - fit)/ fewz", 1, "PE", root.kBlue, fitfuncModDimitriRelBw)

