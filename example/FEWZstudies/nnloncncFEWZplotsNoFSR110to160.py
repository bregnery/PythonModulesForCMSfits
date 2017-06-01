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
fewzdata = numpy.loadtxt("LeadMu26-NNLO-xs", usecols=range(0,11) )

# extract necessary information
mass = fewzdata[:,0]
nctMu26nnloncnc = fewzdata[:,5]
errorNctMu26ncnc = fewzdata[:,6]

#==================================================================================
# Make Histograms /////////////////////////////////////////////////////////////////
#==================================================================================

# Set style options
settings.setSimpleStyle()

# Stat Box options
root.gStyle.SetOptStat(0)

# make root histogram variables
nctMu26nnloExponcncHist = root.TH1F("nctMu26nnloExponcncHist","Cross Section for NNLO ncnc",50,110,160)
settings.setHistTitles(nctMu26nnloExponcncHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section")

nctMu26nnloChebyshevncncHist = root.TH1F("nctMu26nnloChebyshevncncHist","Cross Section for NNLO ncnc",50,110,160)
settings.setHistTitles(nctMu26nnloChebyshevncncHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section")

nctMu26nnloDimitrincncHist = root.TH1F("nctMu26nnloDimitrincncHist","Cross Section for NNLO ncnc",50,110,160)
settings.setHistTitles(nctMu26nnloDimitrincncHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section")

nctMu26nnloBwExponcncHist = root.TH1F("nctMu26nnloBwExponcncHist","Cross Section for NNLO ncnc",50,110,160)
settings.setHistTitles(nctMu26nnloBwExponcncHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section")

nctMu26nnloRelBwExponcncHist = root.TH1F("nctMu26nnloRelBwExponcncHist","Cross Section for NNLO ncnc",50,110,160)
settings.setHistTitles(nctMu26nnloRelBwExponcncHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section")

nctMu26nnloPerExpoBwncncHist = root.TH1F("nctMu26nnloPerExpoBwncncHist","Cross Section for NNLO ncnc",50,110,160)
settings.setHistTitles(nctMu26nnloPerExpoBwncncHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section")

nctMu26nnloPerExpoRelBwncncHist = root.TH1F("nctMu26nnloPerExpoRelBwncncHist","Cross Section for NNLO ncnc",50,110,160)
settings.setHistTitles(nctMu26nnloPerExpoRelBwncncHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section")

nctMu26nnloDimitriRelBwncncHist = root.TH1F("nctMu26nnloDimitriRelBwncncHist","Cross Section for NNLO ncnc",50,110,160)
settings.setHistTitles(nctMu26nnloDimitriRelBwncncHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section")

nctMu26nnloModDimitriRelBwncncHist = root.TH1F("nctMu26nnloModDimitriRelBwncncHist","Cross Section for NNLO ncnc",50,110,160)
settings.setHistTitles(nctMu26nnloModDimitriRelBwncncHist, "Dimuon Mass [GeV/c^{2}]", "Cross Section")

# fill the histograms
for num, xsec, error in zip(range(len(nctMu26nnloncnc) ), nctMu26nnloncnc, errorNctMu26ncnc):
   # must add one because histogram bins start at 1 not 0
   binNum = num + 1

   nctMu26nnloExponcncHist.SetBinContent(binNum, xsec)
   nctMu26nnloExponcncHist.SetBinError(binNum, error)
   nctMu26nnloChebyshevncncHist.SetBinContent(binNum, xsec)
   nctMu26nnloChebyshevncncHist.SetBinError(binNum, error)
   nctMu26nnloDimitrincncHist.SetBinContent(binNum, xsec)
   nctMu26nnloDimitrincncHist.SetBinError(binNum, error)
   nctMu26nnloBwExponcncHist.SetBinContent(binNum, xsec)
   nctMu26nnloBwExponcncHist.SetBinError(binNum, error)
   nctMu26nnloRelBwExponcncHist.SetBinContent(binNum, xsec)
   nctMu26nnloRelBwExponcncHist.SetBinError(binNum, error)
   nctMu26nnloPerExpoBwncncHist.SetBinContent(binNum, xsec)
   nctMu26nnloPerExpoBwncncHist.SetBinError(binNum, error)
   nctMu26nnloPerExpoRelBwncncHist.SetBinContent(binNum, xsec)
   nctMu26nnloPerExpoRelBwncncHist.SetBinError(binNum, error)
   nctMu26nnloDimitriRelBwncncHist.SetBinContent(binNum, xsec)
   nctMu26nnloDimitriRelBwncncHist.SetBinError(binNum, error)
   nctMu26nnloModDimitriRelBwncncHist.SetBinContent(binNum, xsec)
   nctMu26nnloModDimitriRelBwncncHist.SetBinError(binNum, error)

# adjust histogram settings
settings.setDataPoint(nctMu26nnloExponcncHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26nnloChebyshevncncHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26nnloDimitrincncHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26nnloBwExponcncHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26nnloRelBwExponcncHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26nnloPerExpoBwncncHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26nnloPerExpoRelBwncncHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26nnloDimitriRelBwncncHist, root.kBlack, root.kFullDotLarge)
settings.setDataPoint(nctMu26nnloModDimitriRelBwncncHist, root.kBlack, root.kFullDotLarge)

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
modDimitriRelBwParameters = numpy.array([118, 2.5, 7, -2])

# parameter limits
perExpoBwParLimits = numpy.array([[1, 1.5, 2.5],[3, -1.2, -0.12]])
perExpoRelBwParLimits = numpy.array([[1, 1.5, 2.5],[3, -1.2, -0.12]])
dimitriRelBwParLimits = numpy.array([[2, -1.2, -0.12]])
modDimitriRelBwParLimits = numpy.array([[1, 1.5, 2.8]]) #,[3, -1.2, -0.12]])
chebyshevParLimits = numpy.array([[3, -0.0001, 0],[4, -0.000001, 0],[5, 0, 0.00000001],[6, -0.00000000001, 0]])

# fit with root
fitfunc = fit.fitTH1(nctMu26nnloExponcncHist, 110, 160, parameters, pdf.expopdf, "R", root.kRed)  
fitfuncChebyshev = fit.fitTH1withParLimits(nctMu26nnloChebyshevncncHist, 110, 160, chebyshevParameters, pdf.chebyshev, "R", root.kRed,
                                           chebyshevParLimits)  
fitfuncDimitri = fit.fitTH1(nctMu26nnloDimitrincncHist, 110, 160, dimitriParameters, pdf.modifiedDimitripdf, "R", root.kRed)  
fitfuncBwExpo = fit.fitTH1(nctMu26nnloBwExponcncHist, 110, 160, bwExpoParameters, pdf.bwExpo, "R", root.kRed) 
fitfuncRelBwExpo = fit.fitTH1(nctMu26nnloRelBwExponcncHist, 110, 160, relBwExpoParameters, pdf.relBwExpo, "R", root.kRed) 
fitfuncPerExpoBw = fit.fitTH1withParLimits(nctMu26nnloPerExpoBwncncHist, 110, 160, perExpoBwParameters, pdf.perExpoBw, "R", root.kRed, 
                                           perExpoBwParLimits)
fitfuncPerExpoRelBw = fit.fitTH1withParLimits(nctMu26nnloPerExpoRelBwncncHist, 110, 160, perExpoRelBwParameters, pdf.perExpoRelBw, 
                                              "R", root.kRed, perExpoRelBwParLimits)
fitfuncDimitriRelBw = fit.fitTH1withParLimits(nctMu26nnloDimitriRelBwncncHist, 110, 160, dimitriRelBwParameters, pdf.dimitriRelBw, 
                                              "R", root.kRed, dimitriRelBwParLimits)
fitfuncModDimitriRelBw = fit.fitTH1withParLimits(nctMu26nnloModDimitriRelBwncncHist, 110, 160, modDimitriRelBwParameters, 
                                                 pdf.modDimitriRelBw, "R", root.kRed, modDimitriRelBwParLimits)

#==================================================================================
# Draw Plots //////////////////////////////////////////////////////////////////////
#==================================================================================

# make a TCanvas and a histogram plot with residuals
residualExpoCanvas = root.TCanvas("residualCanvas", "residualCanvas")
settings.makeResidualHist(residualExpoCanvas, nctMu26nnloExponcncHist, nctMu26nnloExponcncHist.GetXaxis().GetTitle(), 
                          "(fewz - fit)/ fewz", 1, "PE", root.kBlue, fitfunc)

residualChebyshevCanvas = root.TCanvas("residualChebyshevCanvas", "residualChebyshevCanvas")
settings.makeResidualHist(residualChebyshevCanvas, nctMu26nnloChebyshevncncHist, nctMu26nnloChebyshevncncHist.GetXaxis().GetTitle(), 
                          "(fewz - fit)/ fewz", 1, "PE", root.kBlue, fitfuncChebyshev)

residualDimitriCanvas = root.TCanvas("residualDimitriCanvas", "residualDimitriCanvas")
settings.makeResidualHist(residualDimitriCanvas, nctMu26nnloDimitrincncHist, nctMu26nnloDimitrincncHist.GetXaxis().GetTitle(), 
                          "(fewz - fit)/ fewz", 1, "PE", root.kBlue, fitfuncDimitri)

residualBwExpoCanvas = root.TCanvas("residualBwExpoCanvas", "residualBwExpoCanvas")
settings.makeResidualHist(residualBwExpoCanvas, nctMu26nnloBwExponcncHist, nctMu26nnloBwExponcncHist.GetXaxis().GetTitle(), 
                          "(fewz - fit)/ fewz", 1, "PE", root.kBlue, fitfuncBwExpo)

residualRelBwExpoCanvas = root.TCanvas("residualRelBwExpoCanvas", "residualRelBwExpoCanvas")
settings.makeResidualHist(residualRelBwExpoCanvas, nctMu26nnloRelBwExponcncHist, nctMu26nnloRelBwExponcncHist.GetXaxis().GetTitle(), 
                          "(fewz - fit)/ fewz", 1, "PE", root.kBlue, fitfuncRelBwExpo)

residualPerExpoBwCanvas = root.TCanvas("residualPerExpoBwCanvas", "residualPerExpoBwCanvas")
settings.makeResidualHist(residualPerExpoBwCanvas, nctMu26nnloPerExpoBwncncHist, nctMu26nnloPerExpoBwncncHist.GetXaxis().GetTitle(), 
                          "(fewz - fit)/ fewz", 1, "PE", root.kBlue, fitfuncPerExpoBw)

residualPerExpoRelBwCanvas = root.TCanvas("residualPerExpoRelBwCanvas", "residualPerExpoRelBwCanvas")
settings.makeResidualHist(residualPerExpoRelBwCanvas, nctMu26nnloPerExpoRelBwncncHist, 
                          nctMu26nnloPerExpoRelBwncncHist.GetXaxis().GetTitle(), 
                          "(fewz - fit)/ fewz", 1, "PE", root.kBlue, fitfuncPerExpoRelBw)

residualDimitriRelBwCanvas = root.TCanvas("residualDimitriRelBwCanvas", "residualDimitriRelBwCanvas")
settings.makeResidualHist(residualDimitriRelBwCanvas, nctMu26nnloDimitriRelBwncncHist, 
                          nctMu26nnloDimitriRelBwncncHist.GetXaxis().GetTitle(), 
                          "(fewz - fit)/ fewz", 1, "PE", root.kBlue, fitfuncDimitriRelBw)

residualModDimitriRelBwCanvas = root.TCanvas("residualModDimitriRelBwCanvas", "residualModDimitriRelBwCanvas")
settings.makeResidualHist(residualModDimitriRelBwCanvas, nctMu26nnloModDimitriRelBwncncHist, 
                          nctMu26nnloModDimitriRelBwncncHist.GetXaxis().GetTitle(), 
                          "(fewz - fit)/ fewz", 1, "PE", root.kBlue, fitfuncModDimitriRelBw)

