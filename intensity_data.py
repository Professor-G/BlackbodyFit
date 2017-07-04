# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 21:31:30 2017

@author: danielgodinez
"""

import numpy as np

def select_data(spect_class):
    
    intensity_data = np.loadtxt('all_spectra.txt')
    
    if spect_class == 'O' or spect_class == 'O5' or spect_class == 'O4' or spect_class == 'O3' or spect_class == 'O2' or spect_class == 'O1':
        data = intensity_data[:,1]
        print 'Intensity data for star O5 V HD 242908 selected'
        
    elif spect_class == 'O6':
        data = intensity_data[:,3]
        print 'Intensity data for star O6.5 V HD 12993 selected'
        
    elif spect_class == 'O7':
        data = intensity_data[:,4]
        print 'Intensity data for star O7 V HD 35619 selected'
        
    elif spect_class == 'O8':
        data = intensity_data[:,6]
        print 'Intensity data for star O8 V HD 242935 selected'
        
    elif spect_class == 'O9':
        data = intensity_data[:,8]
        print 'Intensity data for star O9 V HD 17520 selected'
        
    elif spect_class == 'B' or spect_class == 'B4':
        data = intensity_data[:,15]
        print 'Intensity data for star B4 V FEIGE 40 selected'
        
    elif spect_class == 'B0':
        data = intensity_data[:,11]
        print 'Intensity data for star B0 V HD 158659 selected'     
        
    elif spect_class == 'B1' or spect_class == 'B2':
        data = intensity_data[:,13]
        print 'Intensity data for star  B1.5  V HD  35215 selected'
        
    elif spect_class == 'B3' or spect_class == 'B4':
        data = intensity_data[:,14]
        print 'Intensity data for star   B3    V HD  37767 selected'
        
    elif spect_class == 'B5' or spect_class == 'B6':
        data = intensity_data[:,17]
        print 'Intensity data for star   B6    V HD  30584 selected'
        
    elif spect_class == 'B7' or spect_class == 'B8' or spect_class == 'B9':
        data = intensity_data[:,18]
        print 'Intensity data for star    B8    V O    1015 selected'
        
    elif spect_class == 'A0' or spect_class == 'A1':
        data = intensity_data[:,19]
        print 'Intensity data for star   A1    V HD 116608 selected'
        
    elif spect_class == 'A2':
        data = intensity_data[:,21]
        print 'Intensity data for star    A2    V HD 124320 selected'
        
    elif spect_class == 'A3':
        data = intensity_data[:,24]
        print 'Intensity data for star    A3    V HD 221741 selected'
        
    elif spect_class == 'A4' or spect_class == 'A5' or spect_class == 'A':
        data = intensity_data[:,25]
        print 'Intensity data for star   A5    V HD   9547 selected'
        
    elif spect_class == 'A6':
        data = intensity_data[:,26]
        print 'Intensity data for star   A6    V HD  21619 selected'
        
    elif spect_class == 'A7':
        data = intensity_data[:,27]
        print 'Intensity data for star  A7    V HD  23863 selected'
        
    elif spect_class == 'A8':
        data = intensity_data[:,29]
        print 'Intensity data for star  A8    V HD   9972 selected'
        
    elif spect_class == 'A9':
        data = intensity_data[:,30]
        print 'Intensity data for star  A9    V HD  23733 selected'
        
    elif spect_class == 'F0' or spect_class == 'F1':
        data = intensity_data[:,31]
        print 'Intensity data for star   F0    V HD  10032 selected'
        
    elif spect_class == 'F2' or spect_class == 'F3':
        data = intensity_data[:,32]
        print 'Intensity data for star   F3    V HZ    948 selected'
        
    elif spect_class == 'F4':
        data = intensity_data[:,33]
        print 'Intensity data for star  F4    V HD  23511 selected'
        
    elif spect_class == 'F5' or spect_class == 'F':
        data = intensity_data[:,34]
        print 'Intensity data for star   F5    V HZ    227 selected'
        
    elif spect_class == 'F6':
        data = intensity_data[:,35]
        print 'Intensity data for star   F6    V SAO 57199 selected'
        
    elif spect_class == 'F7':
        data = intensity_data[:,37]
        print 'Intensity data for star  F7    V HD   5702 selected'
        
    elif spect_class == 'F8':
        data = intensity_data[:,40]
        print 'Intensity data for star   F8    V HD   6111 selected'
        
    elif spect_class == 'F9':
        data = intensity_data[:,41]
        print 'Intensity data for star    F9    V HD  31084 selected'
        
    elif spect_class == 'F9':
        data = intensity_data[:,41]
        print 'Intensity data for star    F9    V HD  31084 selected'
        
    elif spect_class == 'G0':
        data = intensity_data[:,43]
        print 'Intensity data for star    G0    V HD  28099 selected'
        
    elif spect_class == 'G1':
        data = intensity_data[:,44]
        print 'Intensity data for star     G1    V HD  17647 selected'
        
    elif spect_class == 'G2':
        data = intensity_data[:,45]
        print 'Intensity data for star   G2    V HD  66171  selected'
        
    elif spect_class == 'G3':
        data = intensity_data[:,46]
        print 'Intensity data for star    G3    V BD+581199 selected'
        
    elif spect_class == 'G4':
        data = intensity_data[:,47]
        print 'Intensity data for star   G4    V TR A   14 selected'
        
    elif spect_class == 'G5' or spect_class == 'G6' or spect_class == 'G':
        data = intensity_data[:,48]
        print 'Intensity data for star  G6    V HD  22193 selected'
        
    elif spect_class == 'G7':
        data = intensity_data[:,49]
        print 'Intensity data for star  G7    V HD  27685 selected'
        
    elif spect_class == 'G8' or spect_class == 'G9':
        data = intensity_data[:,50]
        print 'Intensity data for star   G9    V HD  33278 selected'
        
    elif spect_class == 'K0' or spect_class == 'K1' or spect_class == 'K2':
        data = intensity_data[:,52]
        print 'Intensity data for star  K0    V HD  23524 selected'
        
    elif spect_class == 'K3' or spect_class == 'K4':
        data = intensity_data[:,53]
        print 'Intensity data for star  K4    V HD   5351 selected'
        
    elif spect_class == 'K' or spect_class == 'K5' or spect_class == 'K6' or spect_class == 'K7' or spect_class == 'K8' or spect_class == 'K9':
        data = intensity_data[:,54]
        print 'Intensity data for star  K5    V SAO 76803 selected'
        
    elif spect_class == 'M0':
        data = intensity_data[:,55]
        print 'Intensity data for star   M0    V HD 260655 selected'
        
    elif spect_class == 'M1' or spect_class == 'M2' or spect_class == 'M3':
        data = intensity_data[:,56]
        print 'Intensity data for star  M1    V BD+63 137 selected'
        
    elif spect_class == 'M' or spect_class == 'M4' or spect_class == 'M5' or spect_class == 'M6' or spect_class == 'M7' or spect_class == 'M8' or spect_class == 'M9':
        data = intensity_data[:,57]
        print 'Intensity data for star   M5    V YALE 1755 selected'
        
    else:
        data = intensity_data[:,31]
        print 'Spectral class not identified. Intensity data for star   F0    V HD  10032 selected'
        
    return data
        
