from __future__ import division
import numpy as np
import search
np.seterr(divide='ignore', invalid='ignore')

def bilinear(x,y,F,px,py):
    i = search.bin(x,px)
    j = search.bin(y,py)
    a1 = F[i][j]
    a2 = F[i + 1][j] - F[i][j]
    a3 = F[i][j+i] - F[i][j]
    a4 = F[i][j] - F[i + 1][j] - F[i][j + 1] + F[i + 1][j + 1]
    p = a1 + a2 * (px - x[i]) + a3 * (py - y[j]) + a4 * (px - x[i]) * (py - y[j])
    return p
