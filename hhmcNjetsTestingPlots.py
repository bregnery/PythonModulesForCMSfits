#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# hhmcNjetsTestingPlots.py ////////////////////////////////////////////////////////
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
leadJetSDMassHist = root.TH1F("leadJetSDMassHist","Leading AK8 Jet SoftDrop Mass",30,0,300)
settings.setHistTitles(leadJetSDMassHist, "SoftDrop Mass [GeV/c^{2}]", "Number of Events")

leadJetPtHist = root.TH1F("leadJetPtHist","Leading AK8 Jet Pt",30,0,2500)
settings.setHistTitles(leadJetPtHist, "p_{T} [GeV/c]", "Number of Events")

leadJetEtaHist = root.TH1F("leadJetEtaHist","Leading AK8 Jet |#eta|",20,0,5)
settings.setHistTitles(leadJetEtaHist, "|#eta|", "Number of Events")

leadJetPhiHist = root.TH1F("leadJetPhiHist","Leading AK8 Jet #phi",15,-3.5,3.5)
settings.setHistTitles(leadJetPhiHist, "#phi", "Number of Events")

leadJetMassHist = root.TH1F("leadJetMassHist","Leading AK8 Jet 4 Vector Mass",30,0,300)
settings.setHistTitles(leadJetMassHist, "Mass [GeV/c^{2}]", "Number of Events")

subleadJetSDMassHist = root.TH1F("subleadJetSDMassHist","Subleading AK8 Jet SoftDrop Mass",30,0,300)
settings.setHistTitles(subleadJetSDMassHist, "SoftDrop Mass [GeV/c^{2}]", "Number of Events")

subleadJetSDMassZoomHist = root.TH1F("subleadJetSDMassZoomHist","Subleading AK8 Jet SoftDrop Mass",30,0,10)
settings.setHistTitles(subleadJetSDMassZoomHist, "SoftDrop Mass [GeV/c^{2}]", "Number of Events")

subleadJetPtHist = root.TH1F("subleadJetPtHist","Subleading AK8 Jet Pt",30,0,2000)
settings.setHistTitles(subleadJetPtHist, "p_{T} [GeV/c]", "Number of Events")

subleadJetEtaHist = root.TH1F("subleadJetEtaHist","Subleading AK8 Jet |#eta|",20,0,5)
settings.setHistTitles(subleadJetEtaHist, "|#eta|", "Number of Events")

subleadJetPhiHist = root.TH1F("subleadJetPhiHist","Subleading AK8 Jet #phi",15,-3.5,3.5)
settings.setHistTitles(subleadJetPhiHist, "#phi", "Number of Events")

subleadJetMassHist = root.TH1F("subleadJetMassHist","Subleading AK8 Jet 4 Vector Mass",30,0,300)
settings.setHistTitles(subleadJetMassHist, "Mass [GeV/c^{2}]", "Number of Events")

# Matching Histograms
matchedLeadHiggsDeltaRHist = root.TH1F("matchedLeadHiggsDeltaRHist","#Delta R Between a Matched Leading Jet and the Higgs",20,0,0.1)
settings.setHistTitles(matchedLeadHiggsDeltaRHist, "#Delta R", "Number of Events")

unmatchedLeadHiggsDeltaRHist = root.TH1F("unmatchedLeadHiggsDeltaRHist","#Delta R Between a Unmatched Leading Jet and the Higgs",30,0,6)
settings.setHistTitles(unmatchedLeadHiggsDeltaRHist, "#Delta R", "Number of Events")

matchedSubleadHiggsDeltaRHist = root.TH1F("matchedSubleadHiggsDeltaRHist","#Delta R Between a Matched Subleading Jet and the Higgs",20,0,0.1)
settings.setHistTitles(matchedSubleadHiggsDeltaRHist, "#Delta R", "Number of Events")

unmatchedSubleadHiggsDeltaRHist = root.TH1F("unmatchedSubleadHiggsDeltaRHist","#Delta R Between a Unmatched Subleading Jet and the Higgs",30,0,6)
settings.setHistTitles(unmatchedSubleadHiggsDeltaRHist, "#Delta R", "Number of Events")

# Validation Histograms
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


# fill the histograms
for event in range(len(leadJetSDmass) ):
   if nGenHiggs[event] > 1:
      diHiggsDeltaR = deltaR(genHiggs1eta[event], genHiggs1phi[event], genHiggs2eta[event], genHiggs2phi[event] )
      diHiggsDeltaRHist.Fill(diHiggsDeltaR)  

   if nJets[event] > 1 :
      leadJetSDMassHist.Fill(leadJetSDmass[event])
      leadJetPtHist.Fill(leadJetPt[event])
      leadJetEtaHist.Fill(numpy.absolute(leadJetEta[event]))
      leadJetPhiHist.Fill(leadJetPhi[event])
      leadJetMassHist.Fill(leadJetMass[event])
   
      subleadJetSDMassHist.Fill(subleadJetSDmass[event])
      subleadJetSDMassZoomHist.Fill(subleadJetSDmass[event])
      subleadJetPtHist.Fill(subleadJetPt[event])
      subleadJetEtaHist.Fill(numpy.absolute(subleadJetEta[event]))
      subleadJetPhiHist.Fill(subleadJetPhi[event])
      subleadJetMassHist.Fill(subleadJetMass[event])

      nHiggsHist.Fill(nGenHiggs[event]) 
      nJetsHist.Fill(nJets[event])
      nJetsAK4Hist.Fill(nJetsAK4[event])
      nVerticesHist.Fill(nVertices[event])

      # match Higgs to Jets
      leadJetHiggs1DeltaR = deltaR(genHiggs1eta[event], genHiggs1phi[event], leadJetEta[event], leadJetPhi[event] )
      leadJetHiggs2DeltaR = deltaR(genHiggs2eta[event], genHiggs2phi[event], leadJetEta[event], leadJetPhi[event] )
      subleadJetHiggs1DeltaR = deltaR(genHiggs1eta[event], genHiggs1phi[event], subleadJetEta[event], subleadJetPhi[event] )
      subleadJetHiggs2DeltaR = deltaR(genHiggs2eta[event], genHiggs2phi[event], subleadJetEta[event], subleadJetPhi[event] )
     
      if leadJetHiggs1DeltaR <= 0.1 or leadJetHiggs2DeltaR <= 0.1 :
         if leadJetHiggs1DeltaR > leadJetHiggs2DeltaR :
            matchedLeadHiggsDeltaRHist.Fill(leadJetHiggs2DeltaR)
         else :
            matchedLeadHiggsDeltaRHist.Fill(leadJetHiggs1DeltaR)
      elif leadJetHiggs1DeltaR > 0.1 and leadJetHiggs1DeltaR > 0.1 :
         if leadJetHiggs1DeltaR > leadJetHiggs2DeltaR :
            unmatchedLeadHiggsDeltaRHist.Fill(leadJetHiggs2DeltaR)
         else :
            unmatchedLeadHiggsDeltaRHist.Fill(leadJetHiggs1DeltaR)
      if subleadJetHiggs1DeltaR <= 0.1 or subleadJetHiggs2DeltaR <= 0.1 :
         if subleadJetHiggs1DeltaR > subleadJetHiggs2DeltaR :
            matchedSubleadHiggsDeltaRHist.Fill(subleadJetHiggs2DeltaR)
         else :
            matchedSubleadHiggsDeltaRHist.Fill(subleadJetHiggs1DeltaR)
      elif subleadJetHiggs1DeltaR > 0.1 and subleadJetHiggs1DeltaR > 0.1 :
         if subleadJetHiggs1DeltaR > subleadJetHiggs2DeltaR :
            unmatchedSubleadHiggsDeltaRHist.Fill(subleadJetHiggs2DeltaR)
         else :
            unmatchedSubleadHiggsDeltaRHist.Fill(subleadJetHiggs1DeltaR)

   
#   if nJets[event] == 3 :
#   if nJets[event] == 4 :

# adjust histogram settings
settings.setFillOptions(leadJetSDMassHist, root.kBlue, 1, 2, 1)
settings.setFillOptions(leadJetPtHist, root.kBlue, 1, 2, 1)
settings.setFillOptions(leadJetEtaHist, root.kBlue, 1, 2, 1)
settings.setFillOptions(leadJetPhiHist, root.kBlue, 1, 2, 1)
settings.setFillOptions(leadJetMassHist, root.kBlue, 1, 2, 1)

settings.setFillOptions(subleadJetSDMassHist, root.kBlue, 1, 2, 1)
settings.setFillOptions(subleadJetSDMassZoomHist, root.kBlue, 1, 2, 1)
settings.setFillOptions(subleadJetPtHist, root.kBlue, 1, 2, 1)
settings.setFillOptions(subleadJetEtaHist, root.kBlue, 1, 2, 1)
settings.setFillOptions(subleadJetPhiHist, root.kBlue, 1, 2, 1)
settings.setFillOptions(subleadJetMassHist, root.kBlue, 1, 2, 1)

settings.setFillOptions(diHiggsDeltaRHist, root.kBlue, 1, 2, 1)

settings.setFillOptions(nHiggsHist, root.kBlue, 1, 2, 1)
settings.setFillOptions(nJetsHist, root.kBlue, 1, 2, 1)
settings.setFillOptions(nJetsAK4Hist, root.kBlue, 1, 2, 1)
settings.setFillOptions(nVerticesHist, root.kBlue, 1, 2, 1)

settings.setFillOptions(matchedLeadHiggsDeltaRHist, root.kBlue, 1, 2, 1)
settings.setFillOptions(unmatchedLeadHiggsDeltaRHist, root.kBlue, 1, 2, 1)
settings.setFillOptions(matchedSubleadHiggsDeltaRHist, root.kBlue, 1, 2, 1)
settings.setFillOptions(unmatchedSubleadHiggsDeltaRHist, root.kBlue, 1, 2, 1)


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

subleadJetSDMassZoomCanvas = root.TCanvas()
subleadJetSDMassZoomHist.Draw("hist")

subleadJetPtCanvas = root.TCanvas()
subleadJetPtHist.Draw("hist")

subleadJetEtaCanvas = root.TCanvas()
subleadJetEtaHist.Draw("hist")

subleadJetPhiCanvas = root.TCanvas()
subleadJetPhiHist.Draw("hist")

subleadJetMassCanvas = root.TCanvas()
subleadJetMassHist.Draw("hist")

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

matchedLeadHiggsDeltaRCanvas = root.TCanvas()
matchedLeadHiggsDeltaRHist.Draw("hist")

unmatchedLeadHiggsDeltaRCanvas = root.TCanvas()
unmatchedLeadHiggsDeltaRHist.Draw("hist")

matchedSubleadHiggsDeltaRCanvas = root.TCanvas()
matchedSubleadHiggsDeltaRHist.Draw("hist")

unmatchedSubleadHiggsDeltaRCanvas = root.TCanvas()
unmatchedSubleadHiggsDeltaRHist.Draw("hist")

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
subleadJetSDMassZoomCanvas.SaveAs("Hist_SubLeadJetSDmassZoom.png")
subleadJetPtCanvas.SaveAs("Hist_SubLeadJetPt.png")
subleadJetEtaCanvas.SaveAs("Hist_SubLeadJetEta.png")
subleadJetPhiCanvas.SaveAs("Hist_SubLeadJetPhi.png")
subleadJetMassCanvas.SaveAs("Hist_SubLeadJetMass.png")

diHiggsDeltaRCanvas.SaveAs("Hist_diHiggsDeltaR.png")

nHiggsCanvas.SaveAs("Hist_nHiggs.png")
nJetsCanvas.SaveAs("Hist_nJets.png")
nJetsAK4Canvas.SaveAs("Hist_nJetsAK4.png")
nVerticesCanvas.SaveAs("Hist_nVertices.png")

matchedLeadHiggsDeltaRCanvas.SaveAs("Hist_MatchedLeadHiggsDeltaR.png")
unmatchedLeadHiggsDeltaRCanvas.SaveAs("Hist_UnmatchedLeadHiggsDeltaR.png")
matchedSubleadHiggsDeltaRCanvas.SaveAs("Hist_MatchedSubLeadHiggsDeltaR.png")
unmatchedSubleadHiggsDeltaRCanvas.SaveAs("Hist_UnmatchedSubLeadHiggsDeltaR.png")
