#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# histogramsettings.py ////////////////////////////////////////////////////////////
#==================================================================================
# This module contains settings for histograms ////////////////////////////////////
#==================================================================================

# modules
import ROOT as root

#==================================================================================
# Set the histogram axis titles ///////////////////////////////////////////////////
#----------------------------------------------------------------------------------
# Axis titles are strings /////////////////////////////////////////////////////////
#----------------------------------------------------------------------------------

def setHistTitles(hist, xtitle, ytitle):
   hist.GetXaxis().SetTitle(xtitle)
   hist.GetYaxis().SetTitle(ytitle)

#==================================================================================
# Set the data point style and color //////////////////////////////////////////////
#----------------------------------------------------------------------------------
# Color options are: kColor ///////////////////////////////////////////////////////
# marker options are: kMarker /////////////////////////////////////////////////////
#----------------------------------------------------------------------------------

def setDataPoint(hist, color, marker):
   hist.SetMarkerStyle(marker)
   hist.SetMarkerColor(color)

#==================================================================================
# Set the line color, line style, line width, fill color and fill style ///////////
#----------------------------------------------------------------------------------
# Color options are: kColor ///////////////////////////////////////////////////////
# Line style options are integers 1-10 ////////////////////////////////////////////
# Line Width options are integers 1-10 ////////////////////////////////////////////
# Fill style options are: https://root.cern.ch/doc/master/classTAttFill.html //////
#----------------------------------------------------------------------------------

def setFillOptions(hist, color, lstyle, lwidth, fstyle):
   hist.SetFillColor(color-1)
   hist.SetLineColor(color+1)
   hist.SetLineStyle(lstyle)
   hist.SetLineWidth(lwidth)
   hist.SetFillStyle(fstyle)

#==================================================================================
# Set the style to a simple clean look ////////////////////////////////////////////
#----------------------------------------------------------------------------------

def setSimpleStyle():
   root.gStyle.SetCanvasColor(0)
   root.gStyle.SetCanvasBorderSize(10)
   root.gStyle.SetCanvasBorderMode(0)
   root.gStyle.SetCanvasDefH(700)
   root.gStyle.SetCanvasDefW(700)
 
   root.gStyle.SetPadColor       (0)
   root.gStyle.SetPadBorderSize  (10)
   root.gStyle.SetPadBorderMode  (0)
   root.gStyle.SetPadBottomMargin(0.13)
   root.gStyle.SetPadTopMargin   (0.08)
   root.gStyle.SetPadLeftMargin  (0.15)
   root.gStyle.SetPadRightMargin (0.05)
   root.gStyle.SetPadGridX       (0)
   root.gStyle.SetPadGridY       (0)
   root.gStyle.SetPadTickX       (1)
   root.gStyle.SetPadTickY       (1)
 
   root.gStyle.SetFrameFillStyle ( 0)
   root.gStyle.SetFrameFillColor ( 0)
   root.gStyle.SetFrameLineColor ( 1)
   root.gStyle.SetFrameLineStyle ( 0)
   root.gStyle.SetFrameLineWidth ( 1)
   root.gStyle.SetFrameBorderSize(10)
   root.gStyle.SetFrameBorderMode( 0)
 
   root.gStyle.SetNdivisions(505)
 
   root.gStyle.SetLineWidth(2)
   root.gStyle.SetHistLineWidth(2)
   root.gStyle.SetFrameLineWidth(2)
   root.gStyle.SetLegendFillColor(root.kWhite)
   root.gStyle.SetLegendFont(42)
   root.gStyle.SetMarkerSize(1.2)
   root.gStyle.SetMarkerStyle(20)
  
   root.gStyle.SetLabelSize(0.040,"X")
   root.gStyle.SetLabelSize(0.040,"Y")
 
   root.gStyle.SetLabelOffset(0.010,"X")
   root.gStyle.SetLabelOffset(0.010,"Y")
  
   root.gStyle.SetLabelFont(42,"X")
   root.gStyle.SetLabelFont(42,"Y")
  
   root.gStyle.SetTitleBorderSize(0)
   root.gStyle.SetTitleFont(42)
   root.gStyle.SetTitleFont(42,"X")
   root.gStyle.SetTitleFont(42,"Y")
 
   root.gStyle.SetTitleSize(0.045,"X")
   root.gStyle.SetTitleSize(0.045,"Y")
  
   root.gStyle.SetTitleOffset(1.4,"X")
   root.gStyle.SetTitleOffset(1.4,"Y")
  
   root.gStyle.SetTextSize(0.055)
   root.gStyle.SetTextFont(42)
