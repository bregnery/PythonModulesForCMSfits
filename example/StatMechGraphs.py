#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ExamplePlots.py /////////////////////////////////////////////////////////////////
#==================================================================================
# This program reads data from a file and makes histograms ////////////////////////
#==================================================================================

# Give interpreter a search path

# modules
import ROOT as root
import numpy

# import modules from other directories
import style.histogramsettings as settings
import fitting.rootpdfs as pdf
import fitting.fitwithroot as fit

# enter batch mode in root (so python can access displays)
root.gROOT.SetBatch(True)

#==================================================================================
# Make Data ///////////////////////////////////////////////////////////////////////
#==================================================================================

T = numpy.zeros(2000)
U = numpy.zeros(2000)
C = numpy.zeros(2000)
n = numpy.zeros(2000)
evenC = numpy.zeros(2000)
oddC = numpy.zeros(2000)
hydroC = numpy.zeros(2000)
noneqhydroC = numpy.zeros(2000)
T[0] = 0.01

for m in range(len(T) ): 
   if m < 1999:
      T[m+1] = T[m] + 0.01

   top   = 0.0
   utop  = 0.0
   denom = 0.0
   cterm = 0.0
   ortho = 0.0
   para  = 0.0

   eventop   = 0.0
   evenutop  = 0.0
   evendenom = 0.0
   evencterm = 0.0

   oddtop   = 0.0
   oddutop  = 0.0
   odddenom = 0.0
   oddcterm = 0.0

   for l in range(0,100):
      power = -l*(l+1.0)*(1.0/T[m]) 
      expo = numpy.exp(power)
      utop = utop + (2*l+1)*l*(l+1)*expo
      top = top + (2*l+1)*l*(l+1)*(1/T[m])*expo
      denom = denom + (2*l+1)*expo
      cterm = cterm + (2*l+1)*l*l*(l+1)*(l+1)*(1/T[m])*(1/T[m])*expo

      ortho = ortho + (4*l+1)*numpy.exp(-2*l*(2*l+1)*(1/T[m]) )
      para = para + (4*l+2)*numpy.exp(-(2*l+1)*(2*l+2)*(1/T[m]) )
     
      k = 2*l 
      evenpower = -k*(k+1.0)*(1.0/T[m]) 
      evenexpo = numpy.exp(evenpower)
      evenutop = evenutop + (2*k+1)*k*(k+1)*evenexpo
      eventop = eventop + (2*k+1)*k*(k+1)*(1/T[m])*evenexpo
      evendenom = evendenom + (2*k+1)*evenexpo
      evencterm = evencterm + (2*k+1)*k*k*(k+1)*(k+1)*(1/T[m])*(1/T[m])*evenexpo

      r = 2*l+1 
      oddpower = -r*(r+1.0)*(1.0/T[m]) 
      oddexpo = numpy.exp(oddpower)
      oddutop = oddutop + (2*r+1)*r*(r+1)*oddexpo
      oddtop = oddtop + (2*r+1)*r*(r+1)*(1/T[m])*oddexpo
      odddenom = odddenom + (2*r+1)*oddexpo
      oddcterm = oddcterm + (2*r+1)*r*r*(r+1)*(r+1)*(1/T[m])*(1/T[m])*oddexpo

   U[m] = 6.022*1.38*(utop/denom)

   C[m] = 6.022*1.38*(denom*cterm-top*top)/(denom*denom)

   if T[m] > 0.1:
      n[m] = (3/2)*(ortho/para)

   evenC[m] = 6.022*1.38*(evendenom*evencterm-eventop*eventop)/(evendenom*evendenom)
   oddC[m] = 6.022*1.38*(odddenom*oddcterm-oddtop*oddtop)/(odddenom*odddenom)
   hydroC[m] = 0.25*evenC[m] + 0.75*oddC[m]
   noneqhydroC[m] = 0.0625*evenC[m] + 0.5625*oddC[m]
   print(n[m])
   print(evenC[m])
   print(hydroC[m])
   print(noneqhydroC[m])

#==================================================================================
# Make Graphs /////////////////////////////////////////////////////////////////////
#==================================================================================

# Set style options
settings.setSimpleStyle()

# Stat Box options
root.gStyle.SetOptStat(0)

# make root graph variables
uGraph = root.TGraph(len(T),T,U)
uGraph.SetTitle("Graph of U vs T/#theta_{r}")
uGraph.GetXaxis().SetTitle("T/#theta_{r}")
uGraph.GetYaxis().SetTitle("U")
cGraph = root.TGraph(len(T),T,C)
cGraph.SetTitle("Graph of C vs T/#theta_{r}")
uGraph.GetXaxis().SetTitle("T/#theta_{r}")
uGraph.GetYaxis().SetTitle("C")

nGraph = root.TGraph(len(T),T,n)
nGraph.SetTitle("Graph of n vs T/#theta_{r}")
nGraph.GetXaxis().SetTitle("T/#theta_{r}")
nGraph.GetYaxis().SetTitle("n")

hydrocGraph = root.TGraph(len(T),T,hydroC)
hydrocGraph.SetTitle("Graph of C vs T/#theta_{r}")
hydrocGraph.GetXaxis().SetTitle("T/#theta_{r}")
hydrocGraph.GetYaxis().SetTitle("C")

noneqGraph = root.TGraph(len(T),T,noneqhydroC)
noneqGraph.SetTitle("Graph of C vs T/#theta_{r}")
noneqGraph.GetXaxis().SetTitle("T/#theta_{r}")
noneqGraph.GetYaxis().SetTitle("C")

# adjust histogram settings
#settings.setDataPoint(nctPhotonFullHist, root.kBlack, root.kFullDotLarge)

#==================================================================================
# Draw Plots //////////////////////////////////////////////////////////////////////
#==================================================================================

# make a TCanvas and draw the histograms
uCanvas = root.TCanvas("c1","Graph of U vs T/#theta_{r}")
uCanvas.SetLogx()
uGraph.Draw()

cCanvas = root.TCanvas("c2","Graph of C vs T/#theta_{r}")
cCanvas.SetLogx()
cGraph.Draw()

nCanvas = root.TCanvas("c3")
nGraph.Draw()

hydroCanvas = root.TCanvas("c4")
hydrocGraph.Draw("alp")
noneqGraph.Draw("lp same")

# Save the Plots
uCanvas.SaveAs("Graph_U.png")
cCanvas.SaveAs("Graph_C.png")
nCanvas.SaveAs("Graph_n.png")
hydroCanvas.SaveAs("Graph_hydro.png")
