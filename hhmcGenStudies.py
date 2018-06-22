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
genHiggs1phi = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","GenHiggs1_phi")
genHiggs1eta = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","GenHiggs1_eta")

genHiggs2pt = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","GenHiggs2_pt")
genHiggs2phi = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","GenHiggs2_phi")
genHiggs2eta = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","GenHiggs2_eta")

genW1pt = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","GenW1_pt")
genW1phi = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","GenW1_phi")
genW1eta = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","GenW1_eta")
genW1mass = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","GenW1_mass")

genW2pt = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","GenW2_pt")
genW2phi = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","GenW2_phi")
genW2eta = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","GenW2_eta")
genW2mass = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","GenW2_mass")

genW3pt = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","GenW3_pt")
genW3phi = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","GenW3_phi")
genW3eta = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","GenW3_eta")
genW3mass = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","GenW3_mass")

genW4pt = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","GenW4_pt")
genW4phi = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","GenW4_phi")
genW4eta = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","GenW4_eta")
genW4mass = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","GenW4_mass")

virW1mass = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","virGenW1_mass")
virW1pt = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","virGenW1_pt")
virW1phi = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","virGenW1_phi")
virW1eta = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","virGenW1_eta")

virW2mass = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","virGenW2_mass")
virW2pt = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","virGenW2_pt")
virW2phi = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","virGenW2_phi")
virW2eta = root_numpy.root2array("Radion_HH_wwww_FWLite.root","AnalysisTree","virGenW2_eta")

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

genWMassHist = root.TH1F("genWMassHist","Mass of the On Shell W Bosons",30, 0, 100)
settings.setHistTitles(genWMassHist, "Mass [GeV/c^{2}]", "Number of Events")

virWMassHist = root.TH1F("virWMassHist","Mass of the Off Shell W Bosons",30,0,100)
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
      leadJetHiggs1DeltaR = deltaR(genHiggs1eta[event], genHiggs1phi[event], leadJetEta[event], leadJetPhi[event] )
      leadJetHiggs2DeltaR = deltaR(genHiggs2eta[event], genHiggs2phi[event], leadJetEta[event], leadJetPhi[event] )
      subleadJetHiggs1DeltaR = deltaR(genHiggs1eta[event], genHiggs1phi[event], subleadJetEta[event], subleadJetPhi[event] )
      subleadJetHiggs2DeltaR = deltaR(genHiggs2eta[event], genHiggs2phi[event], subleadJetEta[event], subleadJetPhi[event] )
     
      if leadJetHiggs1DeltaR <= 0.1 or leadJetHiggs2DeltaR <= 0.1 :
         if leadJetHiggs1DeltaR > leadJetHiggs2DeltaR :
            matchedLeadHiggsDeltaRHist.Fill(leadJetHiggs2DeltaR)
         else :
            matchedLeadHiggsDeltaRHist.Fill(leadJetHiggs1DeltaR)
      elif leadJetHiggs1DeltaR > 0.1 and leadJetHiggs2DeltaR > 0.1 :
         if leadJetHiggs1DeltaR > leadJetHiggs2DeltaR :
            unmatchedLeadHiggsDeltaRHist.Fill(leadJetHiggs2DeltaR)
         else :
            unmatchedLeadHiggsDeltaRHist.Fill(leadJetHiggs1DeltaR)
      if subleadJetHiggs1DeltaR <= 0.1 or subleadJetHiggs2DeltaR <= 0.1 :
         if subleadJetHiggs1DeltaR > subleadJetHiggs2DeltaR :
            matchedSubleadHiggsDeltaRHist.Fill(subleadJetHiggs2DeltaR)
         else :
            matchedSubleadHiggsDeltaRHist.Fill(subleadJetHiggs1DeltaR)
      elif subleadJetHiggs1DeltaR > 0.1 and subleadJetHiggs2DeltaR > 0.1 :
         if subleadJetHiggs1DeltaR > subleadJetHiggs2DeltaR :
            unmatchedSubleadHiggsDeltaRHist.Fill(subleadJetHiggs2DeltaR)
         else :
            unmatchedSubleadHiggsDeltaRHist.Fill(subleadJetHiggs1DeltaR)

      # match W bosons to Jets
      leadJetWMatch = [False, False, False, False]
      subleadJetWMatch = [False, False, False, False]
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
            subleadJetVirWMatch[0] = True
         if vW2jet2DeltaR < 1.0:
            subleadJetVirWMatch[0] = True

      # W1 vs W2 
      for i in range(len(leadJetWMatch) ):
         twoWmatches = False
         if leadJetWMatch[i] == True:
            for j in range(len(leadJetWMatch) ):
               if i != j and leadJetWMatch[j] == True:
                  #Fill
                  twoWmatches == True
            if twoWmatches == False:
               for k in range(len(leadJetVirWMatch) ):
                  if leadJetVirWMatch[k] == True:
                    #Fill
                    twoWmatches == True
         if twoWmatches == True: break
      for i in range(len(subleadJetWMatch) ):
         twoWmatches = False
         if subleadJetWMatch[i] == True:
            for j in range(len(subleadJetWMatch) ):
               if i != j and subleadJetWMatch[j] == True:
                  #Fill
                  twoWmatches == True
            if twoWmatches == False:
               for k in range(len(subleadJetVirWMatch) ):
                  if subleadJetVirWMatch[k] == True:
                    #Fill
                    twoWmatches == True
         if twoWmatches == True: break
          


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

# make a TCanvas and a histogram plot with residuals
#residualCanvas = root.TCanvas("residualCanvas", "residualCanvas")
#settings.makeResidualHist(residualCanvas, nctPhotonFullHist, nctPhotonFullHist.GetXaxis().GetTitle(), 
#                          "data - fit", 0, "P", root.kBlue, fitfunc)

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
