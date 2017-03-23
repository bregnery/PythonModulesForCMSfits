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
# Modified Dimitri's PDF //////////////////////////////////////////////////////////
#----------------------------------------------------------------------------------
# x is the independent variable and p are the parameters //////////////////////////
#----------------------------------------------------------------------------------

def modifiedDimitripdf(x, p):
   pdf = p[0]*root.TMath.Power((x[0]-100)/70, p[1])*root.TMath.Exp(p[2]*(x[0]-100)/70 + p[3]*root.TMath.Power((x[0]-100)/70, 2) ) # ** is exponent
   return pdf

#==================================================================================
# Exponential PDF /////////////////////////////////////////////////////////////////
#----------------------------------------------------------------------------------
# x is the independent variable and p are the parameters //////////////////////////
#----------------------------------------------------------------------------------

def expopdf(x, p):
   pdf = p[0] + p[1]*root.TMath.Exp(-1*p[2]*x[0]) # ** is exponent
   return pdf

#==================================================================================
# Chebyshev Polynomials with NumPy ////////////////////////////////////////////////
#----------------------------------------------------------------------------------
# x is the independent variable and p are the coefficients ////////////////////////
# the order of the the polynomials is determined by the  //////////////////////////
# length of the vector p //////////////////////////////////////////////////////////
#----------------------------------------------------------------------------------

def chebyshevNumPy(x, p):
   chebyshev = numpy.polynomial.chebyshev.chebval(x[0], p)
   return chebyshev

#==================================================================================
# Chebyshev Polynomials ///////////////////////////////////////////////////////////
#----------------------------------------------------------------------------------
# x is the independent variable and p are the coefficients ////////////////////////
# the order of the the polynomials is determined by the  //////////////////////////
# length of the vector p //////////////////////////////////////////////////////////
#----------------------------------------------------------------------------------

def chebyshev(x, p):
   FirstKind = numpy.zeros(len(p) )
   FirstKindValue = numpy.zeros(len(p) )
   FirstKind[0] = 1
   FirstKind[1] = x[0]
   for i in range(2, len(p) ):
      FirstKind[i] = 2*x[0]*FirstKind[i-1] - FirstKind[i-2]
   for i in range(len(p) ):
      FirstKindValue[i] = p[i] * FirstKind[i]
   chebyshev = numpy.sum(FirstKindValue)
   return chebyshev

#==================================================================================
# Bernstein Polynomials ///////////////////////////////////////////////////////////
#----------------------------------------------------------------------------------
# x is the independent variable and p are the coefficients ////////////////////////
# the order of the the polynomials is determined by the  //////////////////////////
# length of the vector p //////////////////////////////////////////////////////////
#----------------------------------------------------------------------------------

def bernstein(x, p):
   breakpoints = [110, 310] #160] # breakpoints need to be changed to region of interest
   bPolynomial = numpy.zeros(len(p))
   polyValue = numpy.zeros(len(p))
   bPolynomial[0] = (breakpoints[1] - x[0]) / (breakpoints[1] - breakpoints[0])
   bPolynomial[1] = (x[0] - breakpoints[0]) / (breakpoints[1] - breakpoints[0])
   for i in range(2, len(p)):
      bPolynomial[i] = (x[0] - breakpoints[0]) * bPolynomial[i-1] / (breakpoints[1] - breakpoints[0])
      for j in range(i - 1, 0, -1):
         bPolynomial[j] = ((breakpoints[1] - x[0]) * bPolynomial[j] + (x[0] - breakpoints[0]) * bPolynomial[j-1] ) / (breakpoints[1] - breakpoints[0])
      bPolynomial[0] = (breakpoints[1] - x[0]) * bPolynomial[0] / (breakpoints[1] - breakpoints[0])
   for i in range(len(p) ):
      polyValue[i] = p[i] * bPolynomial[i]
   bernstein = numpy.sum(polyValue)
   return bernstein

#==================================================================================
# exponential x gaussian //////////////////////////////////////////////////////////
#----------------------------------------------------------------------------------
# x is the independent variable and p are the parameters //////////////////////////
#----------------------------------------------------------------------------------

def expoGaus(x, p):
   expoGaus = p[0]*root.TMath.Exp(-p[1]*x[0])*root.TMath.Exp( root.TMath.Power((x[0]-p[2]), 2) / (2*root.TMath.Power(p[3], 2) ) )
   return expoGaus

#==================================================================================
# breit wigner mixture scaled by falling exp /////////////////////////////////////
#----------------------------------------------------------------------------------
# x is the independent variable and p are the parameters //////////////////////////
#----------------------------------------------------------------------------------

def bwExpo(x, p):
   bwExpo = (p[0]*root.TMath.Exp(p[1]*x[0]) )/(root.TMath.Power((x[0]-91.2), 2) + root.TMath.Power((2.5/2), 2) ) + (1-p[0])*(root.TMath.Exp(p[1]*x[0]))/(root.TMath.Power(x[0], 2) )
   return bwExpo

#==================================================================================
# relativistic breit wigner mixture scaled by falling exp /////////////////////////
#----------------------------------------------------------------------------------
# x is the independent variable and p are the parameters //////////////////////////
#----------------------------------------------------------------------------------

def relBwExpo(x, p):
   xsqr = root.TMath.Power(x[0], 2)
   Msqr = root.TMath.Power(91.2, 2)
   relBwExpo = (p[0]*root.TMath.Exp(p[1]*x[0]) )/(root.TMath.Power((xsqr-Msqr), 2) + root.TMath.Power(91.2*2.5, 2) ) + (1-p[0])*(root.TMath.Exp(p[1]*x[0]))/(root.TMath.Power(x[0], 2) )
   return relBwExpo

#==================================================================================
# perturbed exponential times breit wigner ///////////////////////////////////////
#----------------------------------------------------------------------------------
# x is the independent variable and p are the parameters //////////////////////////
#----------------------------------------------------------------------------------

def perExpoBw(x, p):
   perExpoBw = p[0]*root.TMath.Exp(p[2]*(x[0]/100) + p[3]*root.TMath.Power((x[0]/100), 2) )/(root.TMath.Power((x[0]-91.2), p[1]) + root.TMath.Power((2.5/2), p[1]) )
   return perExpoBw

#==================================================================================
# perturbed exponential times relativistic breit wigner ///////////////////////////
#----------------------------------------------------------------------------------
# x is the independent variable and p are the parameters //////////////////////////
#----------------------------------------------------------------------------------

def perExpoRelBw(x, p):
   xsqr = root.TMath.Power(x[0], 2)
   Msqr = root.TMath.Power(91.2, 2)
   perExpoRelBw = p[0]*root.TMath.Exp(p[2]*(x[0]/100) + p[3]*root.TMath.Power((x[0]/100), 2) )/(root.TMath.Power((xsqr-Msqr), p[1]) + root.TMath.Power(91.2*2.5, p[1]) )
   return perExpoRelBw

#==================================================================================
# Dimitri's relativistic breit wigner /////////////////////////////////////////////
#----------------------------------------------------------------------------------
# x is the independent variable and p are the parameters //////////////////////////
#----------------------------------------------------------------------------------

def dimitriRelBw(x, p):
   xsqr = root.TMath.Power(x[0], 2)
   Msqr = root.TMath.Power(91.2, 2)
   relBw = (xsqr*xsqr)/(root.TMath.Power(xsqr-Msqr, 2)+root.TMath.Power(xsqr, 2)*root.TMath.Power(2.5, 2)/Msqr )
   dimitriRelBw = (p[0]/xsqr)*relBw*root.TMath.Exp(p[1]*(x[0]/100) + p[2]*root.TMath.Power((x[0]/100), 2) )
   return dimitriRelBw

#==================================================================================
# modified version of Dimitri's relativistic breit wigner /////////////////////////
#----------------------------------------------------------------------------------
# x is the independent variable and p are the parameters //////////////////////////
#----------------------------------------------------------------------------------

def modDimitriRelBw(x, p):
   xsqr = root.TMath.Power(x[0], 2)
   Msqr = root.TMath.Power(91.2, 2)
   relBw = (xsqr*xsqr)/(root.TMath.Power(xsqr-Msqr, p[1])+root.TMath.Power(xsqr, p[1])*root.TMath.Power(2.5/(91.2), p[1]) )
   modDimitriRelBw = (p[0]/xsqr)*relBw*root.TMath.Exp(p[2]*(x[0]/100) + p[3]*root.TMath.Power((x[0]/100), 2) )
   return modDimitriRelBw

