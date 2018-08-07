#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# hhmc2jetsTestingPlots.py ////////////////////////////////////////////////////////
#==================================================================================
# This program reads data from a file and makes histograms ////////////////////////
#==================================================================================

# Give interpreter a search path

# modules
import sys
import ROOT as root
import numpy
import root_numpy

# import modules from other directories
sys.path.append('../')
import style.histogramsettings as settings
import fitting.rootpdfs as pdf
import fitting.fitwithroot as fit

# enter batch mode in root (so python can access displays)
root.gROOT.SetBatch(True)

# delta phi function
def deltaPhi(phi0,phi1):
    result = phi0-phi1
    while result>root.TMath.Pi():
        result -= 2*root.TMath.Pi()
    while result<=-root.TMath.Pi():
        result += 2*root.TMath.Pi()
    return result

# create a deltaR function
def deltaR(eta0,phi0,eta1,phi1):
    deta = eta0-eta1
    dphi = deltaPhi(phi0,phi1)
    return root.TMath.Sqrt(deta**2+dphi**2)

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

genHiggs1pt = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","GenHiggs1_pt")
genHiggs1phi = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","GenHiggs1_phi")
genHiggs1eta = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","GenHiggs1_eta")

genHiggs2pt = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","GenHiggs2_pt")
genHiggs2phi = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","GenHiggs2_phi")
genHiggs2eta = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","GenHiggs2_eta")

nGenHiggs = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","nGenHiggs")
nJets = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","nJetsAK8")
nJetsAK4 = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","nJets")
nVertices = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","nPrimaryVertices")

#==================================================================================
# Make Histograms /////////////////////////////////////////////////////////////////
#==================================================================================

# Set style options
settings.setSimpleStyle()

# Stat Box options
root.gStyle.SetOptStat(0)

# make root histogram variables
diHiggsDeltaRHist = root.TH1F("diHiggsDeltaRHist","#Delta R Between the Higgs",30,0,6)
settings.setHistTitles(diHiggsDeltaRHist, "#Delta R", "Number of Events")

nHiggsHist = root.TH1F("nHiggsHist","Number of Generator Higgs",5, -0.5, 4.5)
settings.setHistTitles(nHiggsHist, "Number of Generator Higgs", "Number of Events")

nJetsHist = root.TH1F("nJetsHist","Number of AK8 Jets",8,-0.5,7.5)
settings.setHistTitles(nJetsHist, "Number of AK8 Jets", "Number of Events")

nJetsAK4Hist = root.TH1F("nJetsAK4Hist","Number of AK4 Jets",22,-0.5,21.5)
settings.setHistTitles(nJetsAK4Hist, "Number of AK4 Jets", "Number of Events")

nVerticesHist = root.TH1F("nVerticesHist","Number of Primary Vertices",51,-0.5,50.5)
settings.setHistTitles(nVerticesHist, "Number of Vertices", "Number of Events")

# When there are two jets
leadTwoJetSDMassHist = root.TH1F("leadTwoJetSDMassHist","(nJets = 2) Leading AK8 Jet SoftDrop Mass",30,0,300)
settings.setHistTitles(leadTwoJetSDMassHist, "SoftDrop Mass [GeV/c^{2}]", "Number of Events")

leadTwoJetPtHist = root.TH1F("leadTwoJetPtHist","(nJets = 2) Leading AK8 Jet Pt",30,0,2500)
settings.setHistTitles(leadTwoJetPtHist, "p_{T} [GeV/c]", "Number of Events")

leadTwoJetEtaHist = root.TH1F("leadTwoJetEtaHist","(nJets = 2) Leading AK8 Jet |#eta|",20,0,5)
settings.setHistTitles(leadTwoJetEtaHist, "|#eta|", "Number of Events")

leadTwoJetPhiHist = root.TH1F("leadTwoJetPhiHist","(nJets = 2) Leading AK8 Jet #phi",15,-3.5,3.5)
settings.setHistTitles(leadTwoJetPhiHist, "#phi", "Number of Events")

leadTwoJetMassHist = root.TH1F("leadTwoJetMassHist","(nJets = 2) Leading AK8 Jet 4 Vector Mass",30,0,300)
settings.setHistTitles(leadTwoJetMassHist, "Mass [GeV/c^{2}]", "Number of Events")

subleadTwoJetSDMassHist = root.TH1F("subleadTwoJetSDMassHist","(nJets = 2) Subleading AK8 Jet SoftDrop Mass",30,0,300)
settings.setHistTitles(subleadTwoJetSDMassHist, "SoftDrop Mass [GeV/c^{2}]", "Number of Events")

subleadTwoJetSDMassZoomHist = root.TH1F("subleadTwoJetSDMassZoomHist","(nJets = 2) Subleading AK8 Jet SoftDrop Mass",30,0,10)
settings.setHistTitles(subleadTwoJetSDMassZoomHist, "SoftDrop Mass [GeV/c^{2}]", "Number of Events")

subleadTwoJetPtHist = root.TH1F("subleadTwoJetPtHist","(nJets = 2) Subleading AK8 Jet Pt",30,0,2000)
settings.setHistTitles(subleadTwoJetPtHist, "p_{T} [GeV/c]", "Number of Events")

subleadTwoJetEtaHist = root.TH1F("subleadTwoJetEtaHist","(nJets = 2) Subleading AK8 Jet |#eta|",20,0,5)
settings.setHistTitles(subleadTwoJetEtaHist, "|#eta|", "Number of Events")

subleadTwoJetPhiHist = root.TH1F("subleadTwoJetPhiHist","(nJets = 2) Subleading AK8 Jet #phi",15,-3.5,3.5)
settings.setHistTitles(subleadTwoJetPhiHist, "#phi", "Number of Events")

subleadTwoJetMassHist = root.TH1F("subleadTwoJetMassHist","(nJets = 2) Subleading AK8 Jet 4 Vector Mass",30,0,300)
settings.setHistTitles(subleadTwoJetMassHist, "Mass [GeV/c^{2}]", "Number of Events")


# fill the histograms
for event in range(len(leadJetSDmass) ):
   if nGenHiggs[event] > 1:
      diHiggsDeltaR = deltaR(genHiggs1eta[event], genHiggs1phi[event], genHiggs2eta[event], genHiggs2phi[event] )
      diHiggsDeltaRHist.Fill(diHiggsDeltaR)  

   if nJets[event] > 0 :
      nHiggsHist.Fill(nGenHiggs[event]) 
      nJetsHist.Fill(nJets[event])
      nJetsAK4Hist.Fill(nJetsAK4[event])
      nVerticesHist.Fill(nVertices[event])
   
   if nJets[event] == 2 :
      leadTwoJetSDMassHist.Fill(leadJetSDmass[event])
      leadTwoJetPtHist.Fill(leadJetPt[event])
      leadTwoJetEtaHist.Fill(numpy.absolute(leadJetEta[event]))
      leadTwoJetPhiHist.Fill(leadJetPhi[event])
      leadTwoJetMassHist.Fill(leadJetMass[event])
   
      subleadTwoJetSDMassHist.Fill(subleadJetSDmass[event])
      subleadTwoJetSDMassZoomHist.Fill(subleadJetSDmass[event])
      subleadTwoJetPtHist.Fill(subleadJetPt[event])
      subleadTwoJetEtaHist.Fill(numpy.absolute(subleadJetEta[event]))
      subleadTwoJetPhiHist.Fill(subleadJetPhi[event])
      subleadTwoJetMassHist.Fill(subleadJetMass[event])

#   if nJets[event] == 3 :
#   if nJets[event] == 4 :

# adjust histogram settings
settings.setFillOptions(diHiggsDeltaRHist, root.kBlue, 1, 2, 1)

settings.setFillOptions(nHiggsHist, root.kBlue, 1, 2, 1)
settings.setFillOptions(nJetsHist, root.kBlue, 1, 2, 1)
settings.setFillOptions(nJetsAK4Hist, root.kBlue, 1, 2, 1)
settings.setFillOptions(nVerticesHist, root.kBlue, 1, 2, 1)

# when there are two jets in an event
settings.setFillOptions(leadTwoJetSDMassHist, root.kBlue, 1, 2, 1)
settings.setFillOptions(leadTwoJetPtHist, root.kBlue, 1, 2, 1)
settings.setFillOptions(leadTwoJetEtaHist, root.kBlue, 1, 2, 1)
settings.setFillOptions(leadTwoJetPhiHist, root.kBlue, 1, 2, 1)
settings.setFillOptions(leadTwoJetMassHist, root.kBlue, 1, 2, 1)

settings.setFillOptions(subleadTwoJetSDMassHist, root.kBlue, 1, 2, 1)
settings.setFillOptions(subleadTwoJetSDMassZoomHist, root.kBlue, 1, 2, 1)
settings.setFillOptions(subleadTwoJetPtHist, root.kBlue, 1, 2, 1)
settings.setFillOptions(subleadTwoJetEtaHist, root.kBlue, 1, 2, 1)
settings.setFillOptions(subleadTwoJetPhiHist, root.kBlue, 1, 2, 1)
settings.setFillOptions(subleadTwoJetMassHist, root.kBlue, 1, 2, 1)


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
diHiggsDeltaRCanvas = root.TCanvas()
diHiggsDeltaRHist.Draw("hist")

nHiggsCanvas = root.TCanvas()
nHiggsHist.Draw("hist")

nJetsCanvas = root.TCanvas()
nJetsHist.Draw("hist")

nJetsAK4Canvas = root.TCanvas()
nJetsAK4Hist.Draw("hist")

nVerticesCanvas = root.TCanvas()
nVerticesHist.Draw("hist")

# when there are two jets in an event
leadTwoJetSDMassCanvas = root.TCanvas()
leadTwoJetSDMassHist.Draw("hist")

leadTwoJetPtCanvas = root.TCanvas()
leadTwoJetPtHist.Draw("hist")

leadTwoJetEtaCanvas = root.TCanvas()
leadTwoJetEtaHist.Draw("hist")

leadTwoJetPhiCanvas = root.TCanvas()
leadTwoJetPhiHist.Draw("hist")

leadTwoJetMassCanvas = root.TCanvas()
leadTwoJetMassHist.Draw("hist")

subleadTwoJetSDMassCanvas = root.TCanvas()
subleadTwoJetSDMassHist.Draw("hist")

subleadTwoJetSDMassZoomCanvas = root.TCanvas()
subleadTwoJetSDMassZoomHist.Draw("hist")

subleadTwoJetPtCanvas = root.TCanvas()
subleadTwoJetPtHist.Draw("hist")

subleadTwoJetEtaCanvas = root.TCanvas()
subleadTwoJetEtaHist.Draw("hist")

subleadTwoJetPhiCanvas = root.TCanvas()
subleadTwoJetPhiHist.Draw("hist")

subleadTwoJetMassCanvas = root.TCanvas()
subleadTwoJetMassHist.Draw("hist")


# make a TCanvas and a histogram plot with residuals
#residualCanvas = root.TCanvas("residualCanvas", "residualCanvas")
#settings.makeResidualHist(residualCanvas, nctPhotonFullHist, nctPhotonFullHist.GetXaxis().GetTitle(), 
#                          "data - fit", 0, "P", root.kBlue, fitfunc)

# Save the Plots
diHiggsDeltaRCanvas.SaveAs("Hist_diHiggsDeltaR.png")

nHiggsCanvas.SaveAs("Hist_nHiggs.png")
nJetsCanvas.SaveAs("Hist_nJets.png")
nJetsAK4Canvas.SaveAs("Hist_nJetsAK4.png")
nVerticesCanvas.SaveAs("Hist_nVertices.png")

# When there are two jets in an event	
leadTwoJetSDMassCanvas.SaveAs("Hist_LeadTwoJetSDmass.png")
leadTwoJetPtCanvas.SaveAs("Hist_LeadTwoJetPt.png")
leadTwoJetEtaCanvas.SaveAs("Hist_LeadTwoJetEta.png")
leadTwoJetPhiCanvas.SaveAs("Hist_LeadTwoJetPhi.png")
leadTwoJetMassCanvas.SaveAs("Hist_LeadTwoJetMass.png")

subleadTwoJetSDMassCanvas.SaveAs("Hist_SubLeadTwoJetSDmass.png")
subleadTwoJetSDMassZoomCanvas.SaveAs("Hist_SubLeadTwoJetSDmassZoom.png")
subleadTwoJetPtCanvas.SaveAs("Hist_SubLeadTwoJetPt.png")
subleadTwoJetEtaCanvas.SaveAs("Hist_SubLeadTwoJetEta.png")
subleadTwoJetPhiCanvas.SaveAs("Hist_SubLeadTwoJetPhi.png")
subleadTwoJetMassCanvas.SaveAs("Hist_SubLeadTwoJetMass.png")

