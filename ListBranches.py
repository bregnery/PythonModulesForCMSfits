import ROOT as root

#rootfile = root.TFile("Radion_hh_wwww_M3500_MiniAOD.root")
rootfile = root.TFile("best_HH_results.root")
tree = rootfile.Get("Events")
tree.Print()
