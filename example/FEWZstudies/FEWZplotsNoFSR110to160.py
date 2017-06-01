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
fewzdata = numpy.loadtxt("LeadMu26-PhotonRecomb-13tev-xs", usecols=range(0,14) )

# extract necessary information
mass = fewzdata[:,0]
nctMu26Full = fewzdata[:,5]
errorNctMu26Full = fewzdata[:,6]

#==================================================================================
# Make Histograms /////////////////////////////////////////////////////////////////
#==================================================================================

# Set style options
settings.setSimpleStyle()

# Stat Box options
root.gStyle.SetOptStat(0)

# make root histogram variables
nctMu26ExpoFullHist = root.TH1F("nctMu26ExpoFullHist","Cross Section for NLO CT Full ",50,110,160)
settings.setHistTitles(nctMu26ExpoFullHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section [pb]")

nctMu26ChebyshevFullHist = root.TH1F("nctMu26ChebyshevFullHist","Cross Section for NLO CT Full ",50,110,160)
settings.setHistTitles(nctMu26ChebyshevFullHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section [pb]")

nctMu26BernsteinFullHist = root.TH1F("nctMu26BernsteinFullHist","Cross Section for NLO CT Full ",50,110,160)
settings.setHistTitles(nctMu26BernsteinFullHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section [pb]")

nctMu26DimitriFullHist = root.TH1F("nctMu26DimitriFullHist","Cross Section for NLO CT Full ",50,110,160)
settings.setHistTitles(nctMu26DimitriFullHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section [pb]")

nctMu26BwExpoFullHist = root.TH1F("nctMu26BwExpoFullHist","Cross Section for NLO CT Full ",50,110,160)
settings.setHistTitles(nctMu26BwExpoFullHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section [pb]")

nctMu26RelBwExpoFullHist = root.TH1F("nctMu26RelBwExpoFullHist","Cross Section for NLO CT Full ",50,110,160)
settings.setHistTitles(nctMu26RelBwExpoFullHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section [pb]")

nctMu26PerExpoBwFullHist = root.TH1F("nctMu26PerExpoBwFullHist","Cross Section for NLO CT Full ",50,110,160)
settings.setHistTitles(nctMu26PerExpoBwFullHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section [pb]")

nctMu26PerExpoRelBwFullHist = root.TH1F("nctMu26PerExpoRelBwFullHist","Cross Section for NLO CT Full ",50,110,160)
settings.setHistTitles(nctMu26PerExpoRelBwFullHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section [pb]")

nctMu26DimitriRelBwFullHist = root.TH1F("nctMu26DimitriRelBwFullHist","Cross Section for NLO CT Full ",50,110,160)
settings.setHistTitles(nctMu26DimitriRelBwFullHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section [pb]")

nctMu26ModDimitriRelBwFullHist = root.TH1F("nctMu26ModDimitriRelBwFullHist","Cross Section for NLO CT Full ",50,110,160)
settings.setHistTitles(nctMu26ModDimitriRelBwFullHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section [pb]")

# fill the histograms
for num, xsec, error in zip(range(len(nctMu26Full) ), nctMu26Full, errorNctMu26Full):
   # must add one because histogram bins start at 1 not 0
   binNum = num + 1

   nctMu26ExpoFullHist.SetBinContent(binNum, xsec)
   nctMu26ExpoFullHist.SetBinError(binNum, error)
   nctMu26ChebyshevFullHist.SetBinContent(binNum, xsec)
   nctMu26ChebyshevFullHist.SetBinError(binNum, error)
   nctMu26BernsteinFullHist.SetBinContent(binNum, xsec)
   nctMu26BernsteinFullHist.SetBinError(binNum, error)
   nctMu26DimitriFullHist.SetBinContent(binNum, xsec)
   nctMu26DimitriFullHist.SetBinError(binNum, error)
   nctMu26BwExpoFullHist.SetBinContent(binNum, xsec)
   nctMu26BwExpoFullHist.SetBinError(binNum, error)
   nctMu26RelBwExpoFullHist.SetBinContent(binNum, xsec)
   nctMu26RelBwExpoFullHist.SetBinError(binNum, error)
   nctMu26PerExpoBwFullHist.SetBinContent(binNum, xsec)
   nctMu26PerExpoBwFullHist.SetBinError(binNum, error)
   nctMu26PerExpoRelBwFullHist.SetBinContent(binNum, xsec)
   nctMu26PerExpoRelBwFullHist.SetBinError(binNum, error)
   nctMu26DimitriRelBwFullHist.SetBinContent(binNum, xsec)
   nctMu26DimitriRelBwFullHist.SetBinError(binNum, error)
   nctMu26ModDimitriRelBwFullHist.SetBinContent(binNum, xsec)
   nctMu26ModDimitriRelBwFullHist.SetBinError(binNum, error)

# adjust histogram settings
settings.setDataPoint(nctMu26ExpoFullHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26ChebyshevFullHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26BernsteinFullHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26DimitriFullHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26BwExpoFullHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26RelBwExpoFullHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26PerExpoBwFullHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26PerExpoRelBwFullHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26DimitriRelBwFullHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26ModDimitriRelBwFullHist, root.kBlack, root.kFullDotLarge)

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
modDimitriRelBwParameters = numpy.array([709, 1.94, 0.2, -0.29])

# parameter limits
perExpoBwParLimits = numpy.array([[1, 1.5, 2.5],[3, -0.6, -0.12]])
perExpoRelBwParLimits = numpy.array([[1, 1.5, 2.5],[3, -1.2, -0.12]])
dimitriRelBwParLimits = numpy.array([[2, -1.2, -0.12]])
modDimitriRelBwParLimits = numpy.array([[1, 1.5, 2.5],[3, -1.2, -0.12]])
chebyshevParLimits = numpy.array([[3, -0.0001, 0.0001],[4, -0.000001, 0.000001],[5, -0.00000001, 0.00000001],[6, -0.00000000001, 0.00000000001]])

# fit with root
fitfunc = fit.fitTH1(nctMu26ExpoFullHist, 110, 160, parameters, pdf.expopdf, "R", root.kRed)  
fitfuncChebyshev = fit.fitTH1(nctMu26ChebyshevFullHist, 110, 160, chebyshevParameters, pdf.chebyshev, "S", root.kRed)
                                           #chebyshevParLimits)  
fitfuncBernstein = fit.fitTH1(nctMu26BernsteinFullHist, 110, 160, bernsteinParameters, pdf.bernstein, "S", root.kRed)
fitfuncDimitri = fit.fitTH1(nctMu26DimitriFullHist, 110, 160, dimitriParameters, pdf.modifiedDimitripdf, "R", root.kRed)  
fitfuncBwExpo = fit.fitTH1(nctMu26BwExpoFullHist, 110, 160, bwExpoParameters, pdf.bwExpo, "R", root.kRed) 
fitfuncRelBwExpo = fit.fitTH1(nctMu26RelBwExpoFullHist, 110, 160, relBwExpoParameters, pdf.relBwExpo, "R", root.kRed) 
fitfuncPerExpoBw = fit.fitTH1withParLimits(nctMu26PerExpoBwFullHist, 110, 160, perExpoBwParameters, pdf.perExpoBw, "R", root.kRed, 
                                           perExpoBwParLimits)
fitfuncPerExpoRelBw = fit.fitTH1withParLimits(nctMu26PerExpoRelBwFullHist, 110, 160, perExpoRelBwParameters, pdf.perExpoRelBw, 
                                              "R", root.kRed, perExpoRelBwParLimits)
fitfuncDimitriRelBw = fit.fitTH1withParLimits(nctMu26DimitriRelBwFullHist, 110, 160, dimitriRelBwParameters, pdf.dimitriRelBw, 
                                              "R", root.kRed, dimitriRelBwParLimits)
fitfuncModDimitriRelBw = fit.fitTH1withParLimits(nctMu26ModDimitriRelBwFullHist, 110, 160, modDimitriRelBwParameters, 
                                                 pdf.modDimitriRelBw, "R", root.kRed, modDimitriRelBwParLimits)

#==================================================================================
# Draw Plots //////////////////////////////////////////////////////////////////////
#==================================================================================

# make a TCanvas and a histogram plot with residuals
residualExpoCanvas = root.TCanvas("residualCanvas", "residualCanvas")
settings.makeResidualHist(residualExpoCanvas, nctMu26ExpoFullHist, nctMu26ExpoFullHist.GetXaxis().GetTitle(), 
                          "(fewz - fit)/ fewz", 1, "PE", root.kBlue, fitfunc)

residualChebyshevCanvas = root.TCanvas("residualChebyshevCanvas", "residualChebyshevCanvas")
settings.makeResidualHist(residualChebyshevCanvas, nctMu26ChebyshevFullHist, nctMu26ChebyshevFullHist.GetXaxis().GetTitle(), 
                          "(fewz - fit)/ fewz", 1, "PE", root.kBlue, fitfuncChebyshev)

residualBernsteinCanvas = root.TCanvas("residualBernsteinCanvas", "residualBernsteinCanvas")
settings.makeResidualHist(residualBernsteinCanvas, nctMu26BernsteinFullHist, nctMu26BernsteinFullHist.GetXaxis().GetTitle(), 
                          "(fewz - fit)/ fewz", 1, "PE", root.kBlue, fitfuncBernstein)

residualDimitriCanvas = root.TCanvas("residualDimitriCanvas", "residualDimitriCanvas")
settings.makeResidualHist(residualDimitriCanvas, nctMu26DimitriFullHist, nctMu26DimitriFullHist.GetXaxis().GetTitle(), 
                          "(fewz - fit)/ fewz", 1, "PE", root.kBlue, fitfuncDimitri)

residualBwExpoCanvas = root.TCanvas("residualBwExpoCanvas", "residualBwExpoCanvas")
settings.makeResidualHist(residualBwExpoCanvas, nctMu26BwExpoFullHist, nctMu26BwExpoFullHist.GetXaxis().GetTitle(), 
                          "(fewz - fit)/ fewz", 1, "PE", root.kBlue, fitfuncBwExpo)

residualRelBwExpoCanvas = root.TCanvas("residualRelBwExpoCanvas", "residualRelBwExpoCanvas")
settings.makeResidualHist(residualRelBwExpoCanvas, nctMu26RelBwExpoFullHist, nctMu26RelBwExpoFullHist.GetXaxis().GetTitle(), 
                          "(fewz - fit)/ fewz", 1, "PE", root.kBlue, fitfuncRelBwExpo)

residualPerExpoBwCanvas = root.TCanvas("residualPerExpoBwCanvas", "residualPerExpoBwCanvas")
settings.makeResidualHist(residualPerExpoBwCanvas, nctMu26PerExpoBwFullHist, nctMu26PerExpoBwFullHist.GetXaxis().GetTitle(), 
                          "(fewz - fit)/ fewz", 1, "PE", root.kBlue, fitfuncPerExpoBw)

residualPerExpoRelBwCanvas = root.TCanvas("residualPerExpoRelBwCanvas", "residualPerExpoRelBwCanvas")
settings.makeResidualHist(residualPerExpoRelBwCanvas, nctMu26PerExpoRelBwFullHist, 
                          nctMu26PerExpoRelBwFullHist.GetXaxis().GetTitle(), 
                          "(fewz - fit)/ fewz", 1, "PE", root.kBlue, fitfuncPerExpoRelBw)

residualDimitriRelBwCanvas = root.TCanvas("residualDimitriRelBwCanvas", "residualDimitriRelBwCanvas")
settings.makeResidualHist(residualDimitriRelBwCanvas, nctMu26DimitriRelBwFullHist, 
                          nctMu26DimitriRelBwFullHist.GetXaxis().GetTitle(), 
                          "(fewz - fit)/ fewz", 1, "PE", root.kBlue, fitfuncDimitriRelBw)

residualModDimitriRelBwCanvas = root.TCanvas("residualModDimitriRelBwCanvas", "residualModDimitriRelBwCanvas")
settings.makeResidualHist(residualModDimitriRelBwCanvas, nctMu26ModDimitriRelBwFullHist, 
                          nctMu26ModDimitriRelBwFullHist.GetXaxis().GetTitle(), 
                          "(fewz - fit)/ fewz", 1, "PE", root.kBlue, fitfuncModDimitriRelBw)

