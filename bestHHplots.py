#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ExamplePlots.py /////////////////////////////////////////////////////////////////
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
import tools.usefulFunctions as tools

# enter batch mode in root (so python can access displays)
root.gROOT.SetBatch(True)

#==================================================================================
# Load Data ///////////////////////////////////////////////////////////////////////
#==================================================================================

# read data from file into a numpy array
jet1particleType = root_numpy.root2array("best_HH_results.root","run/bestTree","jet1_particleType")
jet1dnnW = root_numpy.root2array("best_HH_results.root","run/bestTree","jet1_dnn_w")
jet1dnnZ = root_numpy.root2array("best_HH_results.root","run/bestTree","jet1_dnn_z")
jet1dnnH = root_numpy.root2array("best_HH_results.root","run/bestTree","jet1_dnn_h")
jet1dnnTop = root_numpy.root2array("best_HH_results.root","run/bestTree","jet1_dnn_top")
jet1dnnQcd = root_numpy.root2array("best_HH_results.root","run/bestTree","jet1_dnn_qcd")

jet2particleType = root_numpy.root2array("best_HH_results.root","run/bestTree","jet2_particleType")
jet2dnnW = root_numpy.root2array("best_HH_results.root","run/bestTree","jet2_dnn_w")
jet2dnnZ = root_numpy.root2array("best_HH_results.root","run/bestTree","jet2_dnn_z")
jet2dnnH = root_numpy.root2array("best_HH_results.root","run/bestTree","jet2_dnn_h")
jet2dnnTop = root_numpy.root2array("best_HH_results.root","run/bestTree","jet2_dnn_top")
jet2dnnQcd = root_numpy.root2array("best_HH_results.root","run/bestTree","jet2_dnn_qcd")

jet3particleType = root_numpy.root2array("best_HH_results.root","run/bestTree","jet3_particleType")
jet3dnnW = root_numpy.root2array("best_HH_results.root","run/bestTree","jet3_dnn_w")
jet3dnnZ = root_numpy.root2array("best_HH_results.root","run/bestTree","jet3_dnn_z")
jet3dnnH = root_numpy.root2array("best_HH_results.root","run/bestTree","jet3_dnn_h")
jet3dnnTop = root_numpy.root2array("best_HH_results.root","run/bestTree","jet3_dnn_top")
jet3dnnQcd = root_numpy.root2array("best_HH_results.root","run/bestTree","jet3_dnn_qcd")

nJets = root_numpy.root2array("best_HH_results.root","run/bestTree","nJets")

jet1phi = root_numpy.root2array("best_HH_results.root","run/bestTree","jet1AK8_phi")
jet1eta = root_numpy.root2array("best_HH_results.root","run/bestTree","jet1AK8_eta")

jet2phi = root_numpy.root2array("best_HH_results.root","run/bestTree","jet2AK8_phi")
jet2eta = root_numpy.root2array("best_HH_results.root","run/bestTree","jet2AK8_eta")

jet3phi = root_numpy.root2array("best_HH_results.root","run/bestTree","jet3AK8_phi")
jet3eta = root_numpy.root2array("best_HH_results.root","run/bestTree","jet3AK8_eta")

genHiggs1phi = root_numpy.root2array("best_HH_results.root","run/bestTree","genHiggs1_phi")
genHiggs1eta = root_numpy.root2array("best_HH_results.root","run/bestTree","genHiggs1_eta")

genHiggs2phi = root_numpy.root2array("best_HH_results.root","run/bestTree","genHiggs2_phi")
genHiggs2eta = root_numpy.root2array("best_HH_results.root","run/bestTree","genHiggs2_eta")

#==================================================================================
# Make Histograms /////////////////////////////////////////////////////////////////
#==================================================================================

# Set style options
settings.setSimpleStyle()

# Stat Box options
root.gStyle.SetOptStat(0)

# make root histogram variables
probHHist = root.TH1F("probHHist","BEST Higgs Probability",30,0,1)
settings.setHistTitles(probHHist, "Probability", "Number of Jets")

probWHist = root.TH1F("probWHist","BEST W Probability",30,0,1)
settings.setHistTitles(probWHist, "Probability", "Number of Jets")

probZHist = root.TH1F("probZHist","BEST Z Probability",30,0,1)
settings.setHistTitles(probZHist, "Probability", "Number of Jets")

probTHist = root.TH1F("probTHist","BEST Top Probability",30,0,1)
settings.setHistTitles(probTHist, "Probability", "Number of Jets")

probQHist = root.TH1F("probQHist","BEST QCD Probability",30,0,1)
settings.setHistTitles(probQHist, "Probability", "Number of Jets")

probMatchHHist = root.TH1F("probMatchHHist","BEST Higgs Probability for Jets Matching a gen Higgs",30,0,1)
settings.setHistTitles(probMatchHHist, "Probability", "Number of Jets")

probMatchWHist = root.TH1F("probMatchWHist","BEST W Probability for Jets Matching a gen Higgs",30,0,1)
settings.setHistTitles(probMatchWHist, "Probability", "Number of Jets")

probMatchZHist = root.TH1F("probMatchZHist","BEST Z Probability for Jets Matching a gen Higgs",30,0,1)
settings.setHistTitles(probMatchZHist, "Probability", "Number of Jets")

probMatchTHist = root.TH1F("probMatchTHist","BEST Top Probability for Jets Matching a gen Higgs",30,0,1)
settings.setHistTitles(probMatchTHist, "Probability", "Number of Jets")

probMatchQHist = root.TH1F("probMatchQHist","BEST QCD Probability for Jets Matching a gen Higgs",30,0,1)
settings.setHistTitles(probMatchQHist, "Probability", "Number of Jets")

jet1SumHist = root.TH1F("jet1SumHist","Sum of BEST Probabilities for Jet 1", 30, 0, 1)
settings.setHistTitles(jet1SumHist, "Sum of Probabilities", "Number of Events")

jet2SumHist = root.TH1F("jet2SumHist","Sum of BEST Probabilities for Jet 2", 30, 0, 1)
settings.setHistTitles(jet2SumHist, "Sum of Probabilities", "Number of Events")

jet3SumHist = root.TH1F("jet3SumHist","Sum of BEST Probabilities for Jet 3", 30, 0, 1)
settings.setHistTitles(jet3SumHist, "Sum of Probabilities", "Number of Events")

hMatchHist = root.TH1F("hMatchHist","Number of Matched and Unmatched Higgs", 2, 0, 2)
settings.setHistTitles(hMatchHist, "Matched (0.5) or Unmatched (1.5) Higgs", "Number of Events")

unmatchedHEtaHist = root.TH1F("unmatchedHEtaHist","#eta of Generator Higgs with no matching Jet", 30, 0, 4)
settings.setHistTitles(unmatchedHEtaHist, "#eta", "Number of Events")

# fill the histograms
for event in range(len(jet1dnnH) ):

   # Eta and Phi values of the AK8 jets
   jetEtaPhi = [ [jet1eta[event], jet1phi[event] ], 
                 [jet2eta[event], jet2phi[event] ], 
                 [jet3eta[event], jet3phi[event] ] ]

   # vector of BEST probabilities for 3 highest pT jets
   jetProb = [ [jet1dnnH[event], jet1dnnW[event], jet1dnnZ[event], jet1dnnTop[event], jet1dnnQcd[event] ], 
               [jet2dnnH[event], jet2dnnW[event], jet2dnnZ[event], jet2dnnTop[event], jet2dnnQcd[event] ], 
               [jet3dnnH[event], jet3dnnW[event], jet3dnnZ[event], jet3dnnTop[event], jet3dnnQcd[event] ] ] 

   # Eta and Phi values of the generator Higgs
   higgsEtaPhi = [ [genHiggs1eta[event], genHiggs1phi[event] ],
                   [genHiggs2eta[event], genHiggs2phi[event] ] ]

   # delta R match AK8 jets to Higgs
   matchJetHiggs = tools.deltaRMatch(jetEtaPhi, higgsEtaPhi, 0.1)

   # 1.5 = False, 0.5 = True
   higgs1match = 1.5
   higgs2match = 1.5

   # look at jets with matching generator Higgs
   for ijet in range(len(matchJetHiggs) ):
      if(matchJetHiggs[ijet][0] == True or matchJetHiggs[ijet][1] == True):
         probMatchHHist.Fill(jetProb[ijet][0]) 
         probMatchWHist.Fill(jetProb[ijet][1]) 
         probMatchZHist.Fill(jetProb[ijet][2]) 
         probMatchTHist.Fill(jetProb[ijet][3]) 
         probMatchQHist.Fill(jetProb[ijet][4]) 

      if(matchJetHiggs[ijet][0] == True): higgs1match = 0.5
      if(matchJetHiggs[ijet][1] == True): higgs2match = 0.5

   hMatchHist.Fill(higgs1match)
   hMatchHist.Fill(higgs2match)

   if(higgs1match == 1.5): unmatchedHEtaHist.Fill(higgsEtaPhi[0][0])
   if(higgs2match == 1.5): unmatchedHEtaHist.Fill(higgsEtaPhi[1][0])

   # get BEST probabilities for various numbers of jets
   if nJets[event] > 0:
      probHHist.Fill(jet1dnnH[event])
      probWHist.Fill(jet1dnnW[event])
      probZHist.Fill(jet1dnnZ[event])
      probTHist.Fill(jet1dnnTop[event])
      probQHist.Fill(jet1dnnQcd[event])
      jet1Sum = jet1dnnH[event] + jet1dnnW[event] + jet1dnnZ[event] + jet1dnnTop[event] + jet1dnnQcd[event]
      jet1SumHist.Fill(jet1Sum)
     
   if nJets[event] > 1: 
      probHHist.Fill(jet2dnnH[event])
      probWHist.Fill(jet2dnnW[event])
      probZHist.Fill(jet2dnnZ[event])
      probTHist.Fill(jet2dnnTop[event])
      probQHist.Fill(jet2dnnQcd[event])
      jet2Sum = jet2dnnH[event] + jet2dnnW[event] + jet2dnnZ[event] + jet2dnnTop[event] + jet2dnnQcd[event]
      jet2SumHist.Fill(jet2Sum)
     
   if nJets[event] > 2: 
      probHHist.Fill(jet3dnnH[event])
      probZHist.Fill(jet3dnnZ[event])
      probWHist.Fill(jet3dnnW[event])
      probTHist.Fill(jet3dnnTop[event])
      probQHist.Fill(jet3dnnQcd[event])
      jet3Sum = jet3dnnH[event] + jet3dnnW[event] + jet3dnnZ[event] + jet3dnnTop[event] + jet3dnnQcd[event]
      jet3SumHist.Fill(jet3Sum)

#==================================================================================
# Draw Plots //////////////////////////////////////////////////////////////////////
#==================================================================================

# put the histograms into a vector
histVec = []
histVec.append([probHHist, "hist"])
histVec.append([probWHist, "hist"])
histVec.append([probZHist, "hist"])
histVec.append([probTHist, "hist"])
histVec.append([probQHist, "hist"])

histVec.append([probMatchHHist, "hist"])
histVec.append([probMatchWHist, "hist"])
histVec.append([probMatchZHist, "hist"])
histVec.append([probMatchTHist, "hist"])
histVec.append([probMatchQHist, "hist"])

histVec.append([jet1SumHist, "hist"])
histVec.append([jet2SumHist, "hist"])
histVec.append([jet3SumHist, "hist"])

histVec.append([hMatchHist, "hist"])
histVec.append([unmatchedHEtaHist, "hist"])

# adjust histogram settings
for ihist in range(len(histVec) ):
   settings.setFillOptions(histVec[ihist][0], root.kBlue, 1, 2, 1)

# draw and save the histograms
settings.drawHist(histVec, True, False)
