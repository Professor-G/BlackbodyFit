# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 21:23:06 2017

@author: danielgodinez
"""

import numpy as np
import matplotlib.pyplot as plt
from intensity_data import select_data
from scipy.interpolate import interp1d
from scipy.constants import h,k,c
from scipy.integrate import quad
from scipy.optimize import leastsq


#wavelength must be in nm

def blackbody_flux_fit(wavelength, flux, spect_class = None):
    
    if spect_class == None:
        spect_class == 'F0'
    
    wave = np.array(wavelength)
    flux = np.array(flux)


    wave_data = np.loadtxt('all_spectra.txt')
    wave_check = wave_data[:,0]

    spect_data = select_data(spect_class)

    wave = wave*10 #convert to angstroms for cross checking

    #check where wave matches closest to wave_check, and that index is applied
    #to spect_data to give the corresponding intensity. Interpolation between the
    #two closest intensity values is applied for increased accuracy


    intensity_list = []

    for i in wave:
        list1 = np.abs(wave_check - i)

        index1 = np.argpartition(list1, 0)[0]
        index2 = np.argpartition(list1, 1)[1]
    
        if index2 < index1:
    
            max_val = wave_check[index1]    
            min_val = wave_check[index2]
            y = [spect_data[index2], spect_data[index1]]
        
        elif index2 > index1:
        
            max_val = wave_check[index2]
            min_val = wave_check[index1]
            y = [spect_data[index1], spect_data[index2]]
    
        x = [1, 2]

        f = interp1d(x, y, kind = 'linear')
    
        a = np.abs(max_val - min_val)
        b = np.abs(max_val - i)
        ratio = b/a
    
        x_new = 2 - ratio
        intensity = f(x_new)
        intensity_list.append(intensity)

    
    correction = intensity_list/flux
    intensity = [q*w for q,w in zip(flux, correction)]
    
    wavelength = wave*1e-10 #convert to meters for SI consistency

    def blackbody_intensity(wave, intensity, T):
        
        blackbody_intensity = 2*h*c**2 / (wave**5 * (np.e**(h*c / (wave*k*T)) - 1))
        flux_integral = np.abs(np.trapz(intensity, wave))
        planck_integral = np.abs(quad(blackbody, np.min(wave), np.max(wave), args = T ))[0]
        
        scale_factor = flux_integral / planck_integral
        return scale_factor*blackbody_intensity
        
    t0 = np.array([5000])

    def residuals(T, y, lam):
        return y - blackbody_intensity(wavelength, intensity, T)
    
    T = leastsq(residuals, t0, args = (intensity, wavelength))[0]        
    bbody_fit = blackbody(wavelength, T)
    
    intsrumental_integral = np.abs(np.trapz(intensity, wavelength))
    planck_integral = np.abs(quad(blackbody, np.min(wavelength), np.max(wavelength), args = T ))[0]

    scale_factor = intsrumental_integral / planck_integral

    y = scale_factor*bbody_fit
    T = np.float(T)
    
    fig = plt.figure()
    ax = fig.add_subplot(111)    
    plt.plot(wavelength, intensity, 'yo', label = "DATA")
    plt.plot(wavelength, y, 'r-', linewidth =3, label = "FIT")
    plt.title("Planck Curve With Predicted Fit")
    plt.xlabel("$\lambda$")
    plt.ylabel("Intensity")
    ax.text(0.65, 0.01, "T (K): %s" % T,
        verticalalignment='bottom', horizontalalignment='right',
        transform=ax.transAxes,
        color='black', fontsize=20)
    plt.legend(loc = 1)
    plt.show()
    
    return "The best fit temperature in Kelvins is:", T
    
def blackbody_fit(wavelength, intensity):
    #wavelength must be in nm
    wavelength = wavelength*1e-9 #convert to meters for SI consistency


    def blackbody_intensity(wave, intensity, T):
        blackbody_intensity = 2*h*c**2 / (wave**5 * (np.e**(h*c / (wave*k*T)) - 1))
        flux_integral = np.abs(np.trapz(intensity, wave))
        planck_integral = np.abs(quad(blackbody, np.min(wave), np.max(wave), args = T ))[0]
        scale_factor = flux_integral / planck_integral
        return scale_factor*blackbody_intensity
        
    t0 = np.array([5000])

    def residuals(T, y, lam):
        return y - blackbody_intensity(wavelength, intensity, T)
    
    T = leastsq(residuals, t0, args = (intensity, wavelength))[0]        
    bbody_fit = blackbody(wavelength, T)
    
    intsrumental_integral = np.abs(np.trapz(intensity, wavelength))
    planck_integral = np.abs(quad(blackbody, np.min(wavelength), np.max(wavelength), args = T ))[0]

    scale_factor = intsrumental_integral / planck_integral

    y = scale_factor*bbody_fit
    T = np.float(T)
      
    fig = plt.figure()
    ax = fig.add_subplot(111)    
    plt.plot(wavelength, intensity, 'yo', label = "DATA")
    plt.plot(wavelength, y, 'r-', linewidth =3, label = "FIT")
    plt.title("Planck Curve With Predicted Fit")
    plt.xlabel("$\lambda$")
    plt.ylabel("Intensity")
    ax.text(0.65, 0.01, "T (K): %s" % T,
        verticalalignment='bottom', horizontalalignment='right',
        transform=ax.transAxes,
        color='black', fontsize=20)
    plt.legend(loc = 1)
    plt.show()
    
    return "The best fit temperature in Kelvins is:", T
        
def blackbody(lam, T):
        return 2*h*c**2 / (lam**5 * (np.e**(h*c / (lam*k*T)) - 1))
        

