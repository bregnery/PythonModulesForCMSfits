import ROOT as root

#rootfile = root.TFile("Radion_hh_wwww_M3500_MiniAOD.root")
rootfile = root.TFile("BESToutputs.root")
rootfile.cd("run")
print rootfile.ls()
tree = rootfile.Get("run/jetTree")
tree.Print()
