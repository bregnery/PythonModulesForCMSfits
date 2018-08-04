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
probHhist = root.TH1F("probHhist","BEST Higgs Probability",30,0,1)
settings.setHistTitles(probHhist, "Probability", "Number of Jets")

probWhist = root.TH1F("probWhist","BEST W Probability",30,0,1)
settings.setHistTitles(probWhist, "Probability", "Number of Jets")

probZhist = root.TH1F("probZhist","BEST Z Probability",30,0,1)
settings.setHistTitles(probZhist, "Probability", "Number of Jets")

probThist = root.TH1F("probThist","BEST Top Probability",30,0,1)
settings.setHistTitles(probThist, "Probability", "Number of Jets")

probQhist = root.TH1F("probQhist","BEST QCD Probability",30,0,1)
settings.setHistTitles(probQhist, "Probability", "Number of Jets")

probMatchHhist = root.TH1F("probMatchHhist","BEST Higgs Probability for Jets Matching a gen Higgs",30,0,1)
settings.setHistTitles(probMatchHhist, "Probability", "Number of Jets")

probMatchWhist = root.TH1F("probMatchWhist","BEST W Probability for Jets Matching a gen Higgs",30,0,1)
settings.setHistTitles(probMatchWhist, "Probability", "Number of Jets")

probMatchZhist = root.TH1F("probMatchZhist","BEST Z Probability for Jets Matching a gen Higgs",30,0,1)
settings.setHistTitles(probMatchZhist, "Probability", "Number of Jets")

probMatchThist = root.TH1F("probMatchThist","BEST Top Probability for Jets Matching a gen Higgs",30,0,1)
settings.setHistTitles(probMatchThist, "Probability", "Number of Jets")

probMatchQhist = root.TH1F("probMatchQhist","BEST QCD Probability for Jets Matching a gen Higgs",30,0,1)
settings.setHistTitles(probMatchQhist, "Probability", "Number of Jets")

jet1SumHist = root.TH1F("jet1SumHist","Sum of BEST Probabilities for Jet 1", 30, 0, 1)
settings.setHistTitles(jet1SumHist, "Sum of Probabilities", "Number of Events")

jet2SumHist = root.TH1F("jet2SumHist","Sum of BEST Probabilities for Jet 2", 30, 0, 1)
settings.setHistTitles(jet2SumHist, "Sum of Probabilities", "Number of Events")

jet3SumHist = root.TH1F("jet3SumHist","Sum of BEST Probabilities for Jet 3", 30, 0, 1)
settings.setHistTitles(jet3SumHist, "Sum of Probabilities", "Number of Events")

# fill the histograms
for event in range(len(jet1dnnH) ):
   jetEtaPhi = [ [jet1eta[event], jet1phi[event] ], 
                 [jet2eta[event], jet2phi[event] ], 
                 [jet3eta[event], jet3phi[event] ] ]

   jetProb = [ [jet1dnnH[event], jet1dnnW[event], jet1dnnZ[event], jet1dnnTop[event], jet1dnnQcd[event] ], 
               [jet2dnnH[event], jet2dnnW[event], jet2dnnZ[event], jet2dnnTop[event], jet2dnnQcd[event] ], 
               [jet3dnnH[event], jet3dnnW[event], jet3dnnZ[event], jet3dnnTop[event], jet3dnnQcd[event] ] ] 

   higgsEtaPhi = [ [genHiggs1eta[event], genHiggs1phi[event] ],
                   [genHiggs2eta[event], genHiggs2phi[event] ] ]

   matchJetHiggs = tools.deltaRMatch(jetEtaPhi, higgsEtaPhi, 0.1)

   for ijet in range(len(matchJetHiggs) ):
      if(matchJetHiggs[ijet][0] == True or matchJetHiggs[ijet][1] == True):
         probMatchHhist.Fill(jetProb[ijet][0]) 
         probMatchWhist.Fill(jetProb[ijet][1]) 
         probMatchZhist.Fill(jetProb[ijet][2]) 
         probMatchThist.Fill(jetProb[ijet][3]) 
         probMatchQhist.Fill(jetProb[ijet][4]) 

   if nJets[event] > 0:
      probHhist.Fill(jet1dnnH[event])
      probWhist.Fill(jet1dnnW[event])
      probZhist.Fill(jet1dnnZ[event])
      probThist.Fill(jet1dnnTop[event])
      probQhist.Fill(jet1dnnQcd[event])
      jet1Sum = jet1dnnH[event] + jet1dnnW[event] + jet1dnnZ[event] + jet1dnnTop[event] + jet1dnnQcd[event]
      jet1SumHist.Fill(jet1Sum)
     
   if nJets[event] > 1: 
      probHhist.Fill(jet2dnnH[event])
      probWhist.Fill(jet2dnnW[event])
      probZhist.Fill(jet2dnnZ[event])
      probThist.Fill(jet2dnnTop[event])
      probQhist.Fill(jet2dnnQcd[event])
      jet2Sum = jet2dnnH[event] + jet2dnnW[event] + jet2dnnZ[event] + jet2dnnTop[event] + jet2dnnQcd[event]
      jet2SumHist.Fill(jet2Sum)
     
   if nJets[event] > 2: 
      probHhist.Fill(jet3dnnH[event])
      probZhist.Fill(jet3dnnZ[event])
      probWhist.Fill(jet3dnnW[event])
      probThist.Fill(jet3dnnTop[event])
      probQhist.Fill(jet3dnnQcd[event])
      jet3Sum = jet3dnnH[event] + jet3dnnW[event] + jet3dnnZ[event] + jet3dnnTop[event] + jet3dnnQcd[event]
      jet3SumHist.Fill(jet3Sum)

# adjust histogram settings
settings.setFillOptions(probHhist, root.kBlue, 1, 2, 1)
settings.setFillOptions(probWhist, root.kBlue, 1, 2, 1)
settings.setFillOptions(probZhist, root.kBlue, 1, 2, 1)
settings.setFillOptions(probThist, root.kBlue, 1, 2, 1)
settings.setFillOptions(probQhist, root.kBlue, 1, 2, 1)
settings.setFillOptions(probMatchHhist, root.kBlue, 1, 2, 1)
settings.setFillOptions(probMatchWhist, root.kBlue, 1, 2, 1)
settings.setFillOptions(probMatchZhist, root.kBlue, 1, 2, 1)
settings.setFillOptions(probMatchThist, root.kBlue, 1, 2, 1)
settings.setFillOptions(probMatchQhist, root.kBlue, 1, 2, 1)
settings.setFillOptions(jet1SumHist, root.kBlue, 1, 2, 1)
settings.setFillOptions(jet2SumHist, root.kBlue, 1, 2, 1)
settings.setFillOptions(jet3SumHist, root.kBlue, 1, 2, 1)

#==================================================================================
# Draw Plots //////////////////////////////////////////////////////////////////////
#==================================================================================

# make a TCanvas and draw the histograms
probHcanvas = root.TCanvas()
probHhist.Draw("hist")

probWcanvas = root.TCanvas()
probWhist.Draw("hist")

probZcanvas = root.TCanvas()
probZhist.Draw("hist")

probTcanvas = root.TCanvas()
probThist.Draw("hist")

probQcanvas = root.TCanvas()
probQhist.Draw("hist")

probMatchHcanvas = root.TCanvas()
probMatchHhist.Draw("hist")

probMatchWcanvas = root.TCanvas()
probMatchWhist.Draw("hist")

probMatchZcanvas = root.TCanvas()
probMatchZhist.Draw("hist")

probMatchTcanvas = root.TCanvas()
probMatchThist.Draw("hist")

probMatchQcanvas = root.TCanvas()
probMatchQhist.Draw("hist")

jet1SumCanvas = root.TCanvas()
jet1SumHist.Draw("hist")

jet2SumCanvas = root.TCanvas()
jet2SumHist.Draw("hist")

jet3SumCanvas = root.TCanvas()
jet3SumHist.Draw("hist")

# Save the Plots
probHcanvas.SaveAs("Hist_probH.png")
probWcanvas.SaveAs("Hist_probW.png")
probZcanvas.SaveAs("Hist_probZ.png")
probTcanvas.SaveAs("Hist_probTop.png")
probQcanvas.SaveAs("Hist_probQCD.png")
probMatchHcanvas.SaveAs("Hist_probMatchH.png")
probMatchWcanvas.SaveAs("Hist_probMatchW.png")
probMatchZcanvas.SaveAs("Hist_probMatchZ.png")
probMatchTcanvas.SaveAs("Hist_probMatchTop.png")
probMatchQcanvas.SaveAs("Hist_probMatchQCD.png")
jet1SumCanvas.SaveAs("Hist_probSumJet1.png")
jet2SumCanvas.SaveAs("Hist_probSumJet2.png")
jet3SumCanvas.SaveAs("Hist_probSumJet3.png")
