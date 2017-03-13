#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# rootpdfs.py /////////////////////////////////////////////////////////////////////
#==================================================================================
# This module contains pdfs for fits with the root functionTH1::Fit() /////////////
#==================================================================================

# modules
import ROOT as root
import numpy
import array

# it is incredibly important to always specify an array position

#==================================================================================
# Dimitri's PDF ///////////////////////////////////////////////////////////////////
#----------------------------------------------------------------------------------
# x is the independent variable and p are the parameters //////////////////////////
#----------------------------------------------------------------------------------

def dimitripdf(x, p):
   pdf = p[0]*root.TMath.Power(x[0], p[1])*root.TMath.Exp(p[2]*x[0] + p[3]*root.TMath.Power(x[0], 2) ) # ** is exponent
   return pdf

#==================================================================================
# Exponential PDF /////////////////////////////////////////////////////////////////
#----------------------------------------------------------------------------------
# x is the independent variable and p are the parameters //////////////////////////
#----------------------------------------------------------------------------------

def expopdf(x, p):
   pdf = p[0] + p[1]*root.TMath.Exp(-1*p[2]*x[0] ) # ** is exponent
   return pdf

#==================================================================================
# Chebyshev Polynomials ///////////////////////////////////////////////////////////
#----------------------------------------------------------------------------------
# x is the independent variable and p are the parameters //////////////////////////
# the order of the the polynomials is determined by the  //////////////////////////
# length of the vector p //////////////////////////////////////////////////////////
#----------------------------------------------------------------------------------

def chebyshev(x, p):
   chebyshev = numpy.polynomial.chebyshev.chebval(x[0], p)
   return chebyshev

#==================================================================================
# exponential x gaussian //////////////////////////////////////////////////////////
#----------------------------------------------------------------------------------
# x is the independent variable and p are the parameters //////////////////////////
#----------------------------------------------------------------------------------

def expoGaus(x, p):
   expoGaus = p[0]*root.TMath.Exp(-p[1]*x[0])*root.TMath.Exp( root.TMath.Power((x[0]-p[2]), 2) / (2*root.TMath.Power(p[3], 2) ) )
   return expoGaus

#==================================================================================
# breit weigner mixture scaled by falling exp /////////////////////////////////////
#----------------------------------------------------------------------------------
# x is the independent variable and p are the parameters //////////////////////////
#----------------------------------------------------------------------------------

def bwExpo(x, p):
   bwExpo = (p[0]*root.TMath.Exp(p[1]*x[0]) )/(root.TMath.Power((x[0]-91.2), 2) + root.TMath.Power((2.5/2), 2) ) + (1-p[0])*(root.TMath.Exp(p[1]*x[0]))/(root.TMath.Power(x[0], 2) )
   return bwExpo

#==================================================================================
# perturbed exponential times breit weigner ///////////////////////////////////////
#----------------------------------------------------------------------------------
# x is the independent variable and p are the parameters //////////////////////////
#----------------------------------------------------------------------------------

def perExpoBw(x, p):
   perExpoBw = p[0]*root.TMath.Exp(p[2]*(x[0]/100) + p[3]*root.TMath.Power((x[0]/100), 2) )/(root.TMath.Power((x[0]-91.2), p[1]) + root.TMath.Power((2.5/2), p[1]) )
   return perExpoBw

