#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# hhmcTestingPlots.py /////////////////////////////////////////////////////////////
#==================================================================================
# This program reads data from a file and makes histograms ////////////////////////
#==================================================================================

# Give interpreter a search path

# modules
import ROOT as root
import numpy
import root_numpy

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
leadJetSDmass = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","LeadAK8Jet_softdrop_mass")
leadJetPt = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","LeadAK8Jet_pt")
leadJetEta = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","LeadAK8Jet_eta")
leadJetPhi = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","LeadAK8Jet_phi")
leadJetMass = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","LeadAK8Jet_mass")

subleadJetSDmass = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","SubLeadAK8Jet_softdrop_mass")
subleadJetPt = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","SubLeadAK8Jet_pt")
subleadJetEta = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","SubLeadAK8Jet_eta")
subleadJetPhi = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","SubLeadAK8Jet_phi")
subleadJetMass = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","SubLeadAK8Jet_mass")

nJets = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","nJetsAK8")
nVertices = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","nPrimaryVertices")

print(subleadJetPt)

#==================================================================================
# Make Histograms /////////////////////////////////////////////////////////////////
#==================================================================================

# Set style options
settings.setSimpleStyle()

# Stat Box options
root.gStyle.SetOptStat(0)

# make root histogram variables
leadJetSDMassHist = root.TH1F("leadJetSDMassHist","Leading Jet SoftDrop Mass",30,0,300)
settings.setHistTitles(leadJetSDMassHist, "SoftDrop Mass [GeV/c^{2}]", "Number of Events")

leadJetPtHist = root.TH1F("leadJetPtHist","Leading Jet Pt",30,0,1800)
settings.setHistTitles(leadJetPtHist, "p_{T} [GeV/c]", "Number of Events")

leadJetEtaHist = root.TH1F("leadJetEtaHist","Leading Jet #eta",5,-0.5,4.5)
settings.setHistTitles(leadJetEtaHist, "#eta", "Number of Events")

leadJetPhiHist = root.TH1F("leadJetPhiHist","Leading Jet #phi",7,-3.5,3.5)
settings.setHistTitles(leadJetPhiHist, "#phi", "Number of Events")

leadJetMassHist = root.TH1F("leadJetMassHist","Leading Jet 4 Vector Mass",30,0,300)
settings.setHistTitles(leadJetSDMassHist, "Mass [GeV/c^{2}]", "Number of Events")

subleadJetSDMassHist = root.TH1F("subleadJetSDMassHist","Subleading Jet SoftDrop Mass",30,0,300)
settings.setHistTitles(subleadJetSDMassHist, "SoftDrop Mass [GeV/c^{2}]", "Number of Events")

subleadJetPtHist = root.TH1F("subleadJetPtHist","Subleading Jet Pt",30,0,1000)
settings.setHistTitles(subleadJetPtHist, "p_{T} [GeV/c]", "Number of Events")

subleadJetEtaHist = root.TH1F("subleadJetEtaHist","Subleading Jet #eta",5,-0.5,4.5)
settings.setHistTitles(subleadJetEtaHist, "#eta", "Number of Events")

subleadJetPhiHist = root.TH1F("subleadJetPhiHist","Subleading Jet #phi",7,-3.5,3.5)
settings.setHistTitles(subleadJetPhiHist, "#phi", "Number of Events")

subleadJetMassHist = root.TH1F("subleadJetMassHist","Subleading Jet 4 Vector Mass",30,0,300)
settings.setHistTitles(subleadJetMassHist, "Mass [GeV/c^{2}]", "Number of Events")

nJetsHist = root.TH1F("nJetsHist","Number of Jets",8,-0.5,7.5)
settings.setHistTitles(nJetsHist, "Number of Jets", "Number of Events")

nVerticesHist = root.TH1F("nVerticesHist","Number of Primary Vertices",51,-0.5,50.5)
settings.setHistTitles(nVerticesHist, "Number of Vertices", "Number of Events")

# fill the histograms
for event in range(len(leadJetSDmass) ):
   leadJetSDMassHist.Fill(leadJetSDmass[event])
   leadJetPtHist.Fill(leadJetPt[event])
   leadJetEtaHist.Fill(numpy.absolute(leadJetEta[event]))
   leadJetPhiHist.Fill(leadJetPhi[event])
   leadJetMassHist.Fill(leadJetMass[event])

   subleadJetSDMassHist.Fill(subleadJetSDmass[event])
   subleadJetPtHist.Fill(subleadJetPt[event])
   subleadJetEtaHist.Fill(numpy.absolute(subleadJetEta[event]))
   subleadJetPhiHist.Fill(subleadJetPhi[event])
   subleadJetMassHist.Fill(subleadJetMass[event])

   nJetsHist.Fill(nJets[event])
   nVerticesHist.Fill(nVertices[event])

# adjust histogram settings
settings.setFillOptions(leadJetSDMassHist, root.kBlue, 1, 2, 1)
settings.setFillOptions(leadJetPtHist, root.kBlue, 1, 2, 1)
settings.setFillOptions(leadJetEtaHist, root.kBlue, 1, 2, 1)
settings.setFillOptions(leadJetPhiHist, root.kBlue, 1, 2, 1)
settings.setFillOptions(leadJetMassHist, root.kBlue, 1, 2, 1)

settings.setFillOptions(subleadJetSDMassHist, root.kBlue, 1, 2, 1)
settings.setFillOptions(subleadJetPtHist, root.kBlue, 1, 2, 1)
settings.setFillOptions(subleadJetEtaHist, root.kBlue, 1, 2, 1)
settings.setFillOptions(subleadJetPhiHist, root.kBlue, 1, 2, 1)
settings.setFillOptions(subleadJetMassHist, root.kBlue, 1, 2, 1)

settings.setFillOptions(nJetsHist, root.kBlue, 1, 2, 1)
settings.setFillOptions(nVerticesHist, root.kBlue, 1, 2, 1)

#==================================================================================
# Fit the Histograms //////////////////////////////////////////////////////////////
#==================================================================================

# specify number of fit parameters
#parameters = numpy.array([0.3, -1, -2, 0.5])
#parameters = numpy.array([1, 110, 0.01])

# fit with root
#fit.fitTH1(nctPhotonFullHist, 110, 160, parameters, pdf.dimitripdf, "R", root.kRed)  
#fitfunc = fit.fitTH1(nctPhotonFullHist, 110, 160, parameters, pdf.expopdf, "R", root.kRed)  

#==================================================================================
# Draw Plots //////////////////////////////////////////////////////////////////////
#==================================================================================

# make a TCanvas and draw the histograms
canvas = root.TCanvas()
leadJetSDMassHist.Draw("hist")

leadJetPtCanvas = root.TCanvas()
leadJetPtHist.Draw("hist")

leadJetEtaCanvas = root.TCanvas()
leadJetEtaHist.Draw("hist")

leadJetPhiCanvas = root.TCanvas()
leadJetPhiHist.Draw("hist")

leadJetMassCanvas = root.TCanvas()
leadJetMassHist.Draw("hist")

subleadJetSDMassCanvas = root.TCanvas()
subleadJetSDMassHist.Draw("hist")

subleadJetPtCanvas = root.TCanvas()
subleadJetPtHist.Draw("hist")

subleadJetEtaCanvas = root.TCanvas()
subleadJetEtaHist.Draw("hist")

subleadJetPhiCanvas = root.TCanvas()
subleadJetPhiHist.Draw("hist")

subleadJetMassCanvas = root.TCanvas()
subleadJetMassHist.Draw("hist")

nJetsCanvas = root.TCanvas()
nJetsHist.Draw("hist")

nVerticesCanvas = root.TCanvas()
nVerticesHist.Draw("hist")

# make a TCanvas and a histogram plot with residuals
#residualCanvas = root.TCanvas("residualCanvas", "residualCanvas")
#settings.makeResidualHist(residualCanvas, nctPhotonFullHist, nctPhotonFullHist.GetXaxis().GetTitle(), 
#                          "data - fit", 0, "P", root.kBlue, fitfunc)

# Save the Plots
canvas.SaveAs("Hist_LeadJetSDmass.png")
leadJetPtCanvas.SaveAs("Hist_LeadJetPt.png")
leadJetEtaCanvas.SaveAs("Hist_LeadJetEta.png")
leadJetPhiCanvas.SaveAs("Hist_LeadJetPhi.png")
leadJetMassCanvas.SaveAs("Hist_LeadJetMass.png")

subleadJetSDMassCanvas.SaveAs("Hist_SubLeadJetSDmass.png")
subleadJetPtCanvas.SaveAs("Hist_SubLeadJetPt.png")
subleadJetEtaCanvas.SaveAs("Hist_SubLeadJetEta.png")
subleadJetPhiCanvas.SaveAs("Hist_SubLeadJetPhi.png")
subleadJetMassCanvas.SaveAs("Hist_SubLeadJetMass.png")

nJetsCanvas.SaveAs("Hist_nJets.png")
nVerticesCanvas.SaveAs("Hist_nVertices.png")
	
