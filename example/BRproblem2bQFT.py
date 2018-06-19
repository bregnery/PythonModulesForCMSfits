#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# BRproblem2bQFT.py //////////////////////////////////////////////
#=================================================================
# This program calculates the matrix for problem 2b //////////////
#=================================================================

#================================
# Import Modules ////////////////
#================================

import numpy

#================================
# Calculate Matricies ///////////
#================================

matrix = numpy.zeros((11,11) )

idmatrix = numpy.zeros((11,11) )

for n in range(len(matrix[0]) ):
   for m in range(len(matrix[0]) ):
      if m == n:
         idmatrix[n,m] = 1
      if m == n or m == n+2 or n == m+2:
         matrix[n,m] = 1
      if m == n+4 or n == m+4:
         matrix[n,m] = 0.25

print idmatrix
print matrix

hamMatrix = idmatrix + 0.2*matrix

print numpy.linalg.eig(hamMatrix)

#================================
# Calculate 20 x 20 Matricies ///
#================================

matrix20 = numpy.zeros((20,20) )

idmatrix20 = numpy.zeros((20,20) )

for n in range(len(matrix20[0]) ):
   for m in range(len(matrix20[0]) ):
      if m == n:
         idmatrix20[n,m] = 1
      if m == n or m == n+2 or n == m+2:
         matrix20[n,m] = 1
      if m == n+4 or n == m+4:
         matrix20[n,m] = 0.25


hamMatrix20 = idmatrix20 + 0.2*matrix20

print numpy.linalg.eig(hamMatrix20)


