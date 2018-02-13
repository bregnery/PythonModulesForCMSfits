import ROOT as root

rootfile = root.TFile("Radion_hh_wwww_M3500_MiniAOD.root")
tree = rootfile.Get("Events")
tree.Print()
