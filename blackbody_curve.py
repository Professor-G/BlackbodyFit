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


def blackbody(wavelength, T):
        return 2*h*c**2 / (wavelength**5 * (np.e**(h*c / (wavelength*k*T)) - 1))
        
def blackbody_flux_fit(wavelength, flux, spect_class = None):
    """This function converts instrumental flux measurements to intensity
    by assigning a correction factor by cross referencing wavelength and
    intensity for known stars. Intensity measurements are from SPECLIB (JACOBY, HUNTER, AND CHRISTIAN 1984).
    See: http://adsabs.harvard.edu/abs/1984ApJS...56..257J
    
    After converting flux to intensity, the function fits a black body curve
    using the least squares method. 
    
    :param wavelength: Wavelength measurements. MUST BE IN NANOMETERS!
    :param flux: Instrumental flux from your instrument.
    :param spect_Class: Spectral class. Must be a string. Ex) 'A5'
    
    :rtype: Plot of data with fit, along with predicted temperature. 
    """
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
        blackbody_intensity = blackbody(wave, T)

        flux_integral = np.abs(np.trapz(intensity, wave))
        planck_integral = np.abs(quad(blackbody, np.min(wave), np.max(wave), args = T ))[0]
        scale_factor = flux_integral / planck_integral

        return scale_factor*blackbody_intensity

    def residuals(T, y, lam):
        return y - blackbody_intensity(wavelength, intensity, T)
    
    t0 = np.array([3000]) #the initial temperature guess for the optimization
    T = leastsq(residuals, t0, args = (intensity, wavelength))[0].astype('float32')        
    bbody_fit = blackbody(wavelength, T)
    
    intsrumental_integral = np.abs(np.trapz(intensity, wavelength))
    planck_integral = np.abs(quad(blackbody, np.min(wavelength), np.max(wavelength), args = T))[0]
    scale_factor = intsrumental_integral / planck_integral
    y = scale_factor*bbody_fit
    
    fig = plt.figure()
    ax = fig.add_subplot(111)    
    plt.plot(wavelength, intensity, 'yo', label = "DATA")
    plt.plot(wavelength, y, 'r-', linewidth =3, label = "FIT")
    plt.title("Planck Curve With Predicted Fit")
    plt.xlabel("$\lambda$ (m)")
    plt.ylabel("Intensity")
    ax.text(0.65, 0.01, "T (K): %s" % T[0],
        verticalalignment='bottom', horizontalalignment='right',
        transform=ax.transAxes,
        color='black', fontsize=20)
    plt.legend(loc = 1)
    plt.show()
    
    print("The best fit temperature in Kelvins is: " +str(T[0]))

    
def blackbody_fit(wavelength, intensity):
    """This function fits a black body curve to the input data using
    the least squares method. 
    
    :param wavelength: Wavelength measurements. MUST BE IN NANOMETERS!
    :param intensity: Intensity measurements.
    
    :rtype: Plot of data with fit, along with predicted temperature. 
    """
    wavelength = wavelength*1e-9 #convert to meters for SI consistency
  
    def blackbody_intensity(wave, intensity, T):
        blackbody_intensity = blackbody(wave, T)

        flux_integral = np.abs(np.trapz(intensity, wave))
        planck_integral = np.abs(quad(blackbody, np.min(wave), np.max(wave), args = T ))[0]
        scale_factor = flux_integral / planck_integral

        return scale_factor*blackbody_intensity
        
    def residuals(T, y, lam):
        return y - blackbody_intensity(wavelength, intensity, T)

    t0 = np.array([3000]) #the initial temperature guess for the optimization
    T = leastsq(residuals, t0, args = (intensity, wavelength))[0].astype('float32')        
    bbody_fit = blackbody(wavelength, T)
    
    intsrumental_integral = np.abs(np.trapz(intensity, wavelength))
    planck_integral = np.abs(quad(blackbody, np.min(wavelength), np.max(wavelength), args = T))[0]
    scale_factor = intsrumental_integral / planck_integral
    y = scale_factor*bbody_fit
      
    fig = plt.figure()
    ax = fig.add_subplot(111)    
    plt.plot(wavelength, intensity, 'yo', label = "DATA")
    plt.plot(wavelength, y, 'r-', linewidth =3, label = "FIT")
    plt.title("Planck Curve With Predicted Fit")
    plt.xlabel("$\lambda$ (m)")
    plt.ylabel("Intensity")
    ax.text(0.65, 0.01, "T (K): %s" % T[0],
        verticalalignment='bottom', horizontalalignment='right',
        transform=ax.transAxes,
        color='black', fontsize=20)
    plt.legend(loc = 1)
    plt.show()
    
    print("The best fit temperature in Kelvins is: " +str(T[0]))
        

