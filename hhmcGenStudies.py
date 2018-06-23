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

jet3Mass = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","Jet3AK8_mass")

genHiggs1pt = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","GenHiggs1_pt")
genHiggs1px = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","GenHiggs1_px")
genHiggs1py = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","GenHiggs1_py")
genHiggs1pz = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","GenHiggs1_pz")
genHiggs1phi = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","GenHiggs1_phi")
genHiggs1eta = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","GenHiggs1_eta")
genHiggs1energy = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","GenHiggs1_energy")

genHiggs2pt = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","GenHiggs2_pt")
genHiggs2px = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","GenHiggs2_px")
genHiggs2py = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","GenHiggs2_py")
genHiggs2pz = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","GenHiggs2_pz")
genHiggs2phi = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","GenHiggs2_phi")
genHiggs2eta = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","GenHiggs2_eta")
genHiggs2energy = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","GenHiggs2_energy")

genW1pt = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","GenW1_pt")
genW1px = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","GenW1_px")
genW1py = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","GenW1_py")
genW1pz = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","GenW1_pz")
genW1phi = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","GenW1_phi")
genW1eta = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","GenW1_eta")
genW1mass = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","GenW1_mass")
genW1energy = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","GenW1_energy")

genW2pt = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","GenW2_pt")
genW2px = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","GenW2_px")
genW2py = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","GenW2_py")
genW2pz = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","GenW2_pz")
genW2phi = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","GenW2_phi")
genW2eta = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","GenW2_eta")
genW2mass = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","GenW2_mass")
genW2energy = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","GenW2_energy")

genW3pt = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","GenW3_pt")
genW3px = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","GenW3_px")
genW3py = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","GenW3_py")
genW3pz = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","GenW3_pz")
genW3phi = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","GenW3_phi")
genW3eta = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","GenW3_eta")
genW3mass = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","GenW3_mass")
genW3energy = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","GenW3_energy")

genW4pt = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","GenW4_pt")
genW4px = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","GenW4_px")
genW4py = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","GenW4_py")
genW4pz = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","GenW4_pz")
genW4phi = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","GenW4_phi")
genW4eta = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","GenW4_eta")
genW4mass = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","GenW4_mass")
genW4energy = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","GenW4_energy")

virW1mass = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","virGenW1_mass")
virW1pt = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","virGenW1_pt")
virW1px = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","virGenW1_px")
virW1py = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","virGenW1_py")
virW1pz = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","virGenW1_pz")
virW1phi = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","virGenW1_phi")
virW1eta = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","virGenW1_eta")
virW1energy = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","virGenW1_energy")

virW2mass = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","virGenW2_mass")
virW2pt = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","virGenW2_pt")
virW2px = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","virGenW2_px")
virW2py = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","virGenW2_py")
virW2pz = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","virGenW2_pz")
virW2phi = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","virGenW2_phi")
virW2eta = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","virGenW2_eta")
virW2energy = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","virGenW2_energy")

nGenHiggs = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","nGenHiggs")
nGenWs = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","nGenWs")
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

leadJetMassHist = root.TH1F("leadJetMassHist","Leading AK8 Jet 4 Vector Mass",30,0,300)
settings.setHistTitles(leadJetMassHist, "Mass [GeV/c^{2}]", "Number of Events")

subleadJetSDMassHist = root.TH1F("subleadJetSDMassHist","Subleading AK8 Jet SoftDrop Mass",30,0,300)
settings.setHistTitles(subleadJetSDMassHist, "SoftDrop Mass [GeV/c^{2}]", "Number of Events")

subleadJetMassHist = root.TH1F("subleadJetMassHist","Subleading AK8 Jet 4 Vector Mass",30,0,300)
settings.setHistTitles(subleadJetMassHist, "Mass [GeV/c^{2}]", "Number of Events")

jet3MassHist = root.TH1F("jet3MassHist","The Mass of the AK8 Jet with the 3^{rd} largest p_{T}",30,0,300)
settings.setHistTitles(jet3MassHist, "Mass [GeV]", "Number of Events")

# Gen Particle Histograms
genWPtHist = root.TH1F("genWPtHist","p_{T} of the Generator W Bosons",30, 0, 2000)
settings.setHistTitles(genWPtHist, "p_{T} [GeV/c]", "Number of Events")

genWMassHist = root.TH1F("genWMassHist","Mass of the On Shell W Bosons",61, 0, 100)
settings.setHistTitles(genWMassHist, "Mass [GeV/c^{2}]", "Number of Events")

virWMassHist = root.TH1F("virWMassHist","Mass of the Off Shell W Bosons",61,0,100)
settings.setHistTitles(virWMassHist, "Mass [GeV]", "Number of Events")

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

nWsHist = root.TH1F("nWsHist","Number of Generator W Bosons",7, -0.5, 6.5)
settings.setHistTitles(nWsHist, "Number of Generator W Bosons", "Number of Events")

nJetsHist = root.TH1F("nJetsHist","Number of AK8 Jets",8,-0.5,7.5)
settings.setHistTitles(nJetsHist, "Number of AK8 Jets", "Number of Events")

nJetsAK4Hist = root.TH1F("nJetsAK4Hist","Number of AK4 Jets",22,-0.5,21.5)
settings.setHistTitles(nJetsAK4Hist, "Number of AK4 Jets", "Number of Events")

# Higgs Rest Frame
w1HiggsFramePHist = root.TH1F("w1HiggsFramePHist","Momentum of W1 in the Higgs Rest Frame",30,0,100)
settings.setHistTitles(w1HiggsFramePHist, "|P| [GeV]", "Number of Events")

w2HiggsFramePHist = root.TH1F("w2HiggsFramePHist","Momentum of W2 in the Higgs Rest Frame",30,0,100)
settings.setHistTitles(w2HiggsFramePHist, "|P| [GeV]", "Number of Events")

unmatchedWpairsHist = root.TH1F("unmatchedWpairsHist", "Number of Leading and Subleading Jets with no W pair match", 2,0.5,2.5)
settings.setHistTitles(unmatchedWpairsHist,"1 for leading Jet, 2 for subleading jet","Number of Unmatched Jets")

# 2D Histograms
w1w2massHist = root.TH2F("w1w2massHist","Mass of Daughter W Bosons",15,40,120,15,0,80)
settings.setHistTitles(w1w2massHist, "Mass of W1 [GeV]", "Mass of W2 [GeV]")

# fill the histograms
for event in range(len(leadJetSDmass) ):
   nJetsHist.Fill(nJets[event])
   if nGenHiggs[event] > 1:
      diHiggsDeltaR = deltaR(genHiggs1eta[event], genHiggs1phi[event], genHiggs2eta[event], genHiggs2phi[event] )
      diHiggsDeltaRHist.Fill(diHiggsDeltaR)  

   if nJets[event] > 1 :
      leadJetSDMassHist.Fill(leadJetSDmass[event])
      leadJetMassHist.Fill(leadJetMass[event])
   
      subleadJetSDMassHist.Fill(subleadJetSDmass[event])
      subleadJetMassHist.Fill(subleadJetMass[event])

      nWsHist.Fill(nGenWs[event]) 
      nJetsAK4Hist.Fill(nJetsAK4[event])

      # Gen W bosons
      genWPtHist.Fill(genW1pt[event])
      genWPtHist.Fill(genW2pt[event])
      genWPtHist.Fill(genW3pt[event])
      genWPtHist.Fill(genW4pt[event])

      if genW1mass[event] != 0:
          genWMassHist.Fill(genW1mass[event])
      if genW2mass[event] != 0:
          genWMassHist.Fill(genW2mass[event])
      if genW3mass[event] != 0:
          genWMassHist.Fill(genW3mass[event])
      if genW4mass[event] != 0:
          genWMassHist.Fill(genW4mass[event])

      if virW1mass[event] != 0:
          virWMassHist.Fill(virW1mass[event])
      if virW2mass[event] != 0:
          virWMassHist.Fill(virW2mass[event])

      # match Higgs to Jets
      leadJetHMatch = [False, False]
      subleadJetHMatch = [False, False]
      leadJetHiggs1DeltaR = deltaR(genHiggs1eta[event], genHiggs1phi[event], leadJetEta[event], leadJetPhi[event] )
      leadJetHiggs2DeltaR = deltaR(genHiggs2eta[event], genHiggs2phi[event], leadJetEta[event], leadJetPhi[event] )
      subleadJetHiggs1DeltaR = deltaR(genHiggs1eta[event], genHiggs1phi[event], subleadJetEta[event], subleadJetPhi[event] )
      subleadJetHiggs2DeltaR = deltaR(genHiggs2eta[event], genHiggs2phi[event], subleadJetEta[event], subleadJetPhi[event] )
     
      if leadJetHiggs1DeltaR <= 0.1 or leadJetHiggs2DeltaR <= 0.1 :
         if leadJetHiggs1DeltaR > leadJetHiggs2DeltaR :
            matchedLeadHiggsDeltaRHist.Fill(leadJetHiggs2DeltaR)
            leadJetHMatch[1] = True
         else :
            matchedLeadHiggsDeltaRHist.Fill(leadJetHiggs1DeltaR)
            leadJetHMatch[0] = True
      elif leadJetHiggs1DeltaR > 0.1 and leadJetHiggs2DeltaR > 0.1 :
         if leadJetHiggs1DeltaR > leadJetHiggs2DeltaR :
            unmatchedLeadHiggsDeltaRHist.Fill(leadJetHiggs2DeltaR)
         else :
            unmatchedLeadHiggsDeltaRHist.Fill(leadJetHiggs1DeltaR)
      if subleadJetHiggs1DeltaR <= 0.1 or subleadJetHiggs2DeltaR <= 0.1 :
         if subleadJetHiggs1DeltaR > subleadJetHiggs2DeltaR :
            matchedSubleadHiggsDeltaRHist.Fill(subleadJetHiggs2DeltaR)
            subleadJetHMatch[1] = True
         else :
            matchedSubleadHiggsDeltaRHist.Fill(subleadJetHiggs1DeltaR)
            subleadJetHMatch[0] = True
      elif subleadJetHiggs1DeltaR > 0.1 and subleadJetHiggs2DeltaR > 0.1 :
         if subleadJetHiggs1DeltaR > subleadJetHiggs2DeltaR :
            unmatchedSubleadHiggsDeltaRHist.Fill(subleadJetHiggs2DeltaR)
         else :
            unmatchedSubleadHiggsDeltaRHist.Fill(subleadJetHiggs1DeltaR)

      # match W bosons to Jets
      leadJetWMatch = [False, False, False, False]
      subleadJetWMatch = [False, False, False, False]
      wMassList = [genW1mass[event], genW2mass[event], genW3mass[event], genW4mass[event] ]
      if genW1mass[event] != 0:
         w1jet1DeltaR = deltaR(genW1eta[event], genW1phi[event], leadJetEta[event], leadJetPhi[event])
         w1jet2DeltaR = deltaR(genW1eta[event], genW1phi[event], subleadJetEta[event], subleadJetPhi[event])
         if w1jet1DeltaR < 1.0:
            leadJetWMatch[0] = True
         if w1jet2DeltaR < 1.0:
            subleadJetWMatch[0] = True
      if genW2mass[event] != 0:
         w2jet1DeltaR = deltaR(genW2eta[event], genW2phi[event], leadJetEta[event], leadJetPhi[event])
         w2jet2DeltaR = deltaR(genW2eta[event], genW2phi[event], subleadJetEta[event], subleadJetPhi[event])
         if w2jet1DeltaR < 1.0:
            leadJetWMatch[1] = True
         if w2jet2DeltaR < 1.0:
            subleadJetWMatch[1] = True
      if genW3mass[event] != 0:
         w3jet1DeltaR = deltaR(genW3eta[event], genW3phi[event], leadJetEta[event], leadJetPhi[event])
         w3jet2DeltaR = deltaR(genW3eta[event], genW3phi[event], subleadJetEta[event], subleadJetPhi[event])
         if w3jet1DeltaR < 1.0:
            leadJetWMatch[2] = True
         if w3jet2DeltaR < 1.0:
            subleadJetWMatch[2] = True
      if genW4mass[event] != 0:
         w4jet1DeltaR = deltaR(genW4eta[event], genW4phi[event], leadJetEta[event], leadJetPhi[event])
         w4jet2DeltaR = deltaR(genW4eta[event], genW4phi[event], subleadJetEta[event], subleadJetPhi[event])
         if w4jet1DeltaR < 1.0:
            leadJetWMatch[3] = True
         if w4jet2DeltaR < 1.0:
            subleadJetWMatch[3] = True

      # match offshell Ws to Jets
      leadJetVirWMatch = [False, False]
      subleadJetVirWMatch = [False, False]
      virWmassList = [virW1mass[event], virW2mass[event] ]
      if virW1mass[event] != 0:
         vW1jet1DeltaR = deltaR(virW1eta[event], virW1phi[event], leadJetEta[event], leadJetPhi[event])
         vW1jet2DeltaR = deltaR(virW1eta[event], virW1phi[event], subleadJetEta[event], subleadJetPhi[event])
         if vW1jet1DeltaR < 1.0: 
            leadJetVirWMatch[0] = True
         if vW1jet2DeltaR < 1.0:
            subleadJetVirWMatch[0] = True
      if virW2mass[event] != 0:
         vW2jet1DeltaR = deltaR(virW2eta[event], virW2phi[event], leadJetEta[event], leadJetPhi[event])
         vW2jet2DeltaR = deltaR(virW2eta[event], virW2phi[event], subleadJetEta[event], subleadJetPhi[event])
         if vW2jet1DeltaR < 1.0: 
            subleadJetVirWMatch[1] = True
         if vW2jet2DeltaR < 1.0:
            subleadJetVirWMatch[1] = True

      # Make four vectors
      Higgs1 = root.TLorentzVector(genHiggs1px[event], genHiggs1py[event], genHiggs1pz[event], genHiggs1energy[event])
      Higgs2 = root.TLorentzVector(genHiggs2px[event], genHiggs2py[event], genHiggs2pz[event], genHiggs2energy[event])
      Higgs = [Higgs1, Higgs2]

      genW1 = root.TLorentzVector(genW1px[event], genW1py[event], genW1pz[event], genW1energy[event])
      genW2 = root.TLorentzVector(genW2px[event], genW2py[event], genW2pz[event], genW2energy[event])
      genW3 = root.TLorentzVector(genW3px[event], genW3py[event], genW3pz[event], genW3energy[event])
      genW4 = root.TLorentzVector(genW4px[event], genW4py[event], genW4pz[event], genW4energy[event])
      genW = [genW1, genW2, genW3, genW4]

      virW1 = root.TLorentzVector(virW1px[event], virW1py[event], virW1pz[event], virW1energy[event])
      virW2 = root.TLorentzVector(virW2px[event], virW2py[event], virW2pz[event], virW2energy[event])
      virW = [virW1, virW2]

      # W1 vs W2
      for i in range(len(leadJetWMatch) ):
         twoWmatches = False
         if leadJetWMatch[i] == True:
            for j in range(len(leadJetWMatch) ):
               if i != j and leadJetWMatch[j] == True:
                  if wMassList[i] > wMassList[j]:
                     w1w2massHist.Fill(wMassList[i], wMassList[j])
                  if wMassList[i] < wMassList[j]:
                     w1w2massHist.Fill(wMassList[j], wMassList[i])
                  twoWmatches == True
                  # Boost into H frame
                  for l in range(len(leadJetHMatch) ):
                     if leadJetHMatch[l] == True:
                        genW[i].Boost( -Higgs[l].BoostVector() )
                        genW[j].Boost( -Higgs[l].BoostVector() )
                        if wMassList[i] > wMassList[j]:
                           w1HiggsFramePHist.Fill(genW[i].P() )
                           w2HiggsFramePHist.Fill(genW[j].P() )
                        if wMassList[i] < wMassList[j]:
                           w1HiggsFramePHist.Fill(genW[j].P() )
                           w2HiggsFramePHist.Fill(genW[i].P() )
            if twoWmatches == False:
               for k in range(len(leadJetVirWMatch) ):
                  if leadJetVirWMatch[k] == True:
                    w1w2massHist.Fill(wMassList[i], virWmassList[k])
                    twoWmatches == True
                    # Boost into H frame
                    for l in range(len(leadJetHMatch) ):
                       if leadJetHMatch[l] == True:
                          genW[i].Boost( -Higgs[l].BoostVector() )
                          virW[k].Boost( -Higgs[l].BoostVector() )
                          w1HiggsFramePHist.Fill(genW[i].P() )
                          w2HiggsFramePHist.Fill(virW[k].P() )
         if twoWmatches == True: break
      if twoWmatches == False: unmatchedWpairsHist.Fill(1)
                          
      for i in range(len(subleadJetWMatch) ):
         twoWmatches = False
         if subleadJetWMatch[i] == True:
            for j in range(len(subleadJetWMatch) ):
               if i != j and subleadJetWMatch[j] == True:
                  if wMassList[i] > wMassList[j]:
                     w1w2massHist.Fill(wMassList[i], wMassList[j])
                  if wMassList[j] > wMassList[i]:
                     w1w2massHist.Fill(wMassList[j], wMassList[i])
                  twoWmatches == True
                  # Boost into H frame
                  for l in range(len(subleadJetHMatch) ):
                     if subleadJetHMatch[l] == True:
                        genW[i].Boost( -Higgs[l].BoostVector() )
                        genW[j].Boost( -Higgs[l].BoostVector() )
                        if wMassList[i] > wMassList[j]:
                           w1HiggsFramePHist.Fill(genW[i].P() )
                           w2HiggsFramePHist.Fill(genW[j].P() )
                        if wMassList[i] < wMassList[j]:
                           w1HiggsFramePHist.Fill(genW[j].P() )
                           w2HiggsFramePHist.Fill(genW[i].P() )
            if twoWmatches == False:
               for k in range(len(subleadJetVirWMatch) ):
                  if subleadJetVirWMatch[k] == True:
                    w1w2massHist.Fill(wMassList[i], virWmassList[k])
                    twoWmatches == True
                    # Boost into H frame
                    for l in range(len(subleadJetHMatch) ):
                       if subleadJetHMatch[l] == True:
                          genW[i].Boost( -Higgs[l].BoostVector() )
                          virW[k].Boost( -Higgs[l].BoostVector() )
                          w1HiggsFramePHist.Fill(genW[i].P() )
                          w2HiggsFramePHist.Fill(virW[k].P() )
         if twoWmatches == True: break
      if twoWmatches == False: unmatchedWpairsHist.Fill(2)
         


   if nJets[event] > 2:
      jet3MassHist.Fill(jet3Mass[event])
   
#   if nJets[event] == 3 :
#   if nJets[event] == 4 :

# adjust histogram settings
settings.setFillOptions(leadJetSDMassHist, root.kBlue, 1, 2, 1)
settings.setFillOptions(leadJetMassHist, root.kBlue, 1, 2, 1)

settings.setFillOptions(subleadJetSDMassHist, root.kBlue, 1, 2, 1)
settings.setFillOptions(subleadJetMassHist, root.kBlue, 1, 2, 1)

settings.setFillOptions(jet3MassHist, root.kBlue, 1, 2, 1)

settings.setFillOptions(genWPtHist, root.kBlue, 1, 2, 1)
settings.setFillOptions(genWMassHist, root.kBlue, 1, 2, 1)
settings.setFillOptions(virWMassHist, root.kOrange, 1, 2, 1)

settings.setFillOptions(diHiggsDeltaRHist, root.kBlue, 1, 2, 1)

settings.setFillOptions(nWsHist, root.kBlue, 1, 2, 1)
settings.setFillOptions(nJetsHist, root.kBlue, 1, 2, 1)
settings.setFillOptions(nJetsAK4Hist, root.kBlue, 1, 2, 1)

settings.setFillOptions(w1HiggsFramePHist, root.kBlue, 1, 2, 1)
settings.setFillOptions(w2HiggsFramePHist, root.kBlue, 1, 2, 1)
settings.setFillOptions(unmatchedWpairsHist, root.kBlue, 1, 2, 1)

settings.setFillOptions(matchedLeadHiggsDeltaRHist, root.kBlue, 1, 2, 1)
settings.setFillOptions(unmatchedLeadHiggsDeltaRHist, root.kBlue, 1, 2, 1)
settings.setFillOptions(matchedSubleadHiggsDeltaRHist, root.kBlue, 1, 2, 1)
settings.setFillOptions(unmatchedSubleadHiggsDeltaRHist, root.kBlue, 1, 2, 1)


#==================================================================================
# Make Stacked Histograms /////////////////////////////////////////////////////////
#==================================================================================

# Make Histogram List
wMassHistList = []
wMassHistList.append(genWMassHist)
wMassHistList.append(virWMassHist)

# Make Stacked Histogram
stackWMassCanvas = root.TCanvas()
wMassStackHist = settings.makeStackHist(stackWMassCanvas, wMassHistList, "Mass of Generator W Bosons", "Mass [GeV]", "Events", "hist", 1)

#==================================================================================
# Draw Plots //////////////////////////////////////////////////////////////////////
#==================================================================================

# make a TCanvas and draw the histograms
canvas = root.TCanvas()
leadJetSDMassHist.Draw("hist")

leadJetMassCanvas = root.TCanvas()
leadJetMassHist.Draw("hist")

subleadJetSDMassCanvas = root.TCanvas()
subleadJetSDMassHist.Draw("hist")

subleadJetMassCanvas = root.TCanvas()
subleadJetMassHist.Draw("hist")

jet3MassCanvas = root.TCanvas()
jet3MassHist.Draw("hist")

# Generator Particles
genWPtCanvas = root.TCanvas()
genWPtHist.Draw("hist")

genWMassCanvas = root.TCanvas()
genWMassHist.Draw("hist")

virWMassCanvas = root.TCanvas()
virWMassHist.Draw("hist")

diHiggsDeltaRCanvas = root.TCanvas()
diHiggsDeltaRHist.Draw("hist")

# Gen Studies
nWsCanvas = root.TCanvas()
nWsHist.Draw("hist")

nJetsCanvas = root.TCanvas()
nJetsHist.Draw("hist")

nJetsAK4Canvas = root.TCanvas()
nJetsAK4Hist.Draw("hist")

matchedLeadHiggsDeltaRCanvas = root.TCanvas()
matchedLeadHiggsDeltaRHist.Draw("hist")

unmatchedLeadHiggsDeltaRCanvas = root.TCanvas()
unmatchedLeadHiggsDeltaRHist.Draw("hist")

matchedSubleadHiggsDeltaRCanvas = root.TCanvas()
matchedSubleadHiggsDeltaRHist.Draw("hist")

unmatchedSubleadHiggsDeltaRCanvas = root.TCanvas()
unmatchedSubleadHiggsDeltaRHist.Draw("hist")

w1HiggsFramePCanvas = root.TCanvas()
w1HiggsFramePHist.Draw("hist")

w2HiggsFramePCanvas = root.TCanvas()
w2HiggsFramePHist.Draw("hist")

unmatchedWpairsCanvas = root.TCanvas()
unmatchedWpairsHist.Draw("hist")

# 2D Histograms
root.gStyle.SetPadRightMargin(0.2)
w1w2massCanvas = root.TCanvas()
w1w2massHist.Draw("colz")

# Save the Plots
canvas.SaveAs("Hist_LeadJetSDmass.png")
leadJetMassCanvas.SaveAs("Hist_LeadJetMass.png")

subleadJetSDMassCanvas.SaveAs("Hist_SubLeadJetSDmass.png")
subleadJetMassCanvas.SaveAs("Hist_SubLeadJetMass.png")

jet3MassCanvas.SaveAs("Hist_Jet3Mass.png")

genWPtCanvas.SaveAs("Hist_GenWPt.png")
genWMassCanvas.SaveAs("Hist_GenWMass.png")
virWMassCanvas.SaveAs("Hist_VirWMass.png")

diHiggsDeltaRCanvas.SaveAs("Hist_diHiggsDeltaR.png")

nWsCanvas.SaveAs("Hist_nWs.png")
nJetsCanvas.SaveAs("Hist_nJets.png")
nJetsAK4Canvas.SaveAs("Hist_nJetsAK4.png")

matchedLeadHiggsDeltaRCanvas.SaveAs("Hist_MatchedLeadHiggsDeltaR.png")
unmatchedLeadHiggsDeltaRCanvas.SaveAs("Hist_UnmatchedLeadHiggsDeltaR.png")
matchedSubleadHiggsDeltaRCanvas.SaveAs("Hist_MatchedSubLeadHiggsDeltaR.png")
unmatchedSubleadHiggsDeltaRCanvas.SaveAs("Hist_UnmatchedSubLeadHiggsDeltaR.png")

w1HiggsFramePCanvas.SaveAs("Hist_W1HiggsFrameP.png")
w2HiggsFramePCanvas.SaveAs("Hist_W2HiggsFrameP.png")
unmatchedWpairsCanvas.SaveAs("Hist_UnmatchedWPairs.png")

w1w2massCanvas.SaveAs("Hist_W1W2mass.png")
