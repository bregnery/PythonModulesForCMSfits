#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# fitwithroot.py //////////////////////////////////////////////////////////////////
#==================================================================================
# This module contains functions that complete fits with root /////////////////////
#==================================================================================

# modules
import ROOT as root
import numpy
import rootpdfs

#==================================================================================
# Fit a TH1 ///////////////////////////////////////////////////////////////////////
#----------------------------------------------------------------------------------
# This function fit a histogram and returns the fitted TF1. ///////////////////////
# p is the vector of parameters, make sure that it is the correct size //////////// 
# for the pdf that is being fitted. pdf is the pdf defined in rootpdfs ////////////
# that the histogram is being fitted to. xmin and xmax are the range   ////////////
# of the fit. fittype is the of fit being performed. ////////////////////////////// 
#----------------------------------------------------------------------------------

def fitTH1(hist, xmin, xmax, p, pdf, fittype, color):
   root.gStyle.SetOptFit(1111) # shows the chi 2
   fitfunc = root.TF1("fitfunc", pdf, xmin, xmax, len(p))
   for position, value in zip(range(0,p.size), p):
      fitfunc.SetParameter(position, value)
   fitfunc.SetLineColor(color)
   hist.Fit("fitfunc") #, fittype)
   print "Chi Squared value: ", fitfunc.GetChisquare()
   return fitfunc

