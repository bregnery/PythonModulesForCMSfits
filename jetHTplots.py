#=========================================================================================
# jetHTplots.py --------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------
# Author(s): Brendan Regnery -------------------------------------------------------------
#-----------------------------------------------------------------------------------------

# modules
import ROOT as root
import numpy as np
import matplotlib
matplotlib.use('Agg') #prevents opening displays (fast), must use before pyplot
import matplotlib.pyplot as plt
import mplhep as hep
import uproot
#import uproot_methods
#import awkward

# import modules from other directories
import style.histogramsettings as settings
import fitting.rootpdfs as pdf
import fitting.fitwithroot as fit

# enter batch mode in root (so python can access displays)
root.gROOT.SetBatch(True)

#=========================================================================================
# Load Data ------------------------------------------------------------------------------
#=========================================================================================

upTree = uproot.open("BESToutputs.root")["run/jetTree"]
jetDF = upTree.pandas.df(["jetAK8*"])

#=========================================================================================
# Make Plots -----------------------------------------------------------------------------
#=========================================================================================

# use the CMS plot style
plt.style.use(hep.style.ROOT)

# plot jet pT
plt.figure(1)
plt.hist(jetDF["jetAK8_pt"], bins=30)
plt.ylabel('Events/GeV')
plt.xlabel(r'Jet $p_{T}$ [GeV]')
hep.cms.cmslabel(data=True, paper=False, year='2017')
plt.savefig('plots/hist_jetAK8_pt.png')




