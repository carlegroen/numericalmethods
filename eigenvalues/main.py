from __future__ import division
from jacobidiag import *
import numpy as np
import sys
from numpy import linalg as LA

A    = np.array([[2.0,12.0,6.0],[12.0,8.0,-10.0],[6.0,-10.0,12.0]])
Aorg = np.copy(A)
print "Un-changed matrix A:"
print A

EigenvalA,EigenvecA,sweeps = jacobidiag(A)
npEigenval,npEigenvec = LA.eig(Aorg)
print "Eigenvalues of A:"
print EigenvalA
print "Eigenvectors of A:"
print EigenvecA
print "Number of sweeps:"
print sweeps
print "----------------------------------"
print "Eigenvalues and eigenvectors found with numpy.linalg:"
print "Eigenvalues:"
print npEigenval
print "Eigenvectors:"
print npEigenvec
print "----------------------------------"
print "Orthogonality of the eigenvectors:"
V1=EigenvecA[:,0]
V2=EigenvecA[:,1]
V3=EigenvecA[:,2]
print "v1 * v2"
check1=0
n=len(V1)
for i in range(n):
	check1+=V1[i]*V2[i]
print check1
print "v1 * v3"
check2=0
for i in range(n):
	check2+=V1[i]*V3[i]
print check2
print "v2 * v3"
check3=0
for i in range(n):
	check3+=V2[i]*V3[i]
print check3
print "----------------------------------"
print "Check normalization"
check1=0
print "v1"
for i in range(n):
	check1+=V1[i]*V1[i]
print np.sqrt(check1)
check2=0
print "v2"
for i in range(n):
	check2+=V2[i]*V2[i]
print np.sqrt(check2)
check3=0
print "v3"
for i in range(n):
	check3+=V3[i]*V3[i]
print np.sqrt(check3)
print "Checking eigenvectors:"
print "A * v1 = lamb1 * v1"
print "A * v1"
print np.dot(Aorg,V1)
print "lamb1 * v1"
print EigenvalA[0]*V1
print "A * v2 = lamb2 * v2"
print "A * v2"
print np.dot(Aorg,V2)
print "lamb2 * v2"
print EigenvalA[1]*V2
print "A * v3 = lamb3 * v3"
print "A * v3"
print np.dot(Aorg,V3)
print "lamb3 * v3"
print EigenvalA[2]*V3
