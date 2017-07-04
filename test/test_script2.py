# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 16:27:10 2017

@author: danielgodinez
"""

import sys
sys.path.append('../')
import numpy as np
import blackbody_curve as bc

intensity = np.loadtxt('O7_star.txt')
wavelength = np.loadtxt('all_spectra.txt')[:,0]
wavelength = wavelength*1e-1 #convert angstroms to nm

bc.blackbody_fit(wavelength, intensity)