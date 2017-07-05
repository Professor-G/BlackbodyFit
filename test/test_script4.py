# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 17:55:39 2017

@author: danielgodinez
"""

import sys
sys.path.append('../')
import numpy as np
import blackbody_curve as bc

data = np.loadtxt('BeStar.txt')
pixel = data[:,0]
flux = data[:,1]

# This is the lamp data used to convert pixel to wavelength
# THIS IS INSTRUMENT DEPENDENT!

lamp_pix = [316.0, 322.0, 392.0, 649.0, 722.0]
lamp_wave = [579.1, 577.0, 546.1, 435.8, 404.7]

m, b = np.polyfit(lamp_pix, lamp_wave, 1)

wave = [(m*i + b) for i in pixel]

wavelength = np.array(wave)
flux = np.array(flux)

bc.blackbody_flux_fit(wavelength, flux, 'B2')