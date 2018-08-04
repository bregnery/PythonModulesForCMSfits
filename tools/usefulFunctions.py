#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# usefulFunctions.py //////////////////////////////////////////////////////////////
#==================================================================================
# This module contains useful functions for CMS Analyses //////////////////////////
#==================================================================================

# modules
import ROOT as root

#==================================================================================
# Calculate delta Phi /////////////////////////////////////////////////////////////
#----------------------------------------------------------------------------------
# phi1 and phi2 are azimuthal angles in the detector ------------------------------
#----------------------------------------------------------------------------------

def deltaPhi(phi1, phi2):
   delPhi = phi1-phi2
   while delPhi > root.TMath.Pi():
      delPhi -= 2*root.TMath.Pi()
   while delPhi <= -root.TMath.Pi():
      delPhi += 2*root.TMath.Pi()
   return delPhi

#==================================================================================
# Calculate delta R ///////////////////////////////////////////////////////////////
#----------------------------------------------------------------------------------
# phi is the azimuthal angle in the detector --------------------------------------
# eta is psuedorapidity -----------------------------------------------------------
#----------------------------------------------------------------------------------

def deltaR(eta1, phi1, eta2, phi2):
   delEta = eta1 - eta2
   delPhi = deltaPhi(phi1, phi2)
   delR = root.TMath.Sqrt(delEta**2 + delPhi**2)
   return delR

#==================================================================================
# Match using delta R cone ////////////////////////////////////////////////////////
#----------------------------------------------------------------------------------
# etaPhi is a 2D array of eta phi values ( [ [eta1, phi1], [eta2, phi2], ...] ) ---
# limR is the upper bound of delta R for matching ---------------------------------
# returns an array where true means matched ---------------------------------------
#----------------------------------------------------------------------------------

def deltaRMatch(etaPhi1, etaPhi2, limR):
   matchList = []
   for i in range(len(etaPhi1) ):
      nestedMatchList = []
      for j in range(len(etaPhi2) ):
         delR = deltaR(etaPhi1[i][0], etaPhi1[i][1], etaPhi2[j][0], etaPhi2[j][1])
         if delR < limR: match = True
         if delR > limR: match = False
         nestedMatchList.append(match)
      matchList.append(nestedMatchList)
   return matchList        

