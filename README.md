# BlackbodyFit
![](http://imgur.com/TZgZym0 )

# Curve Fitting

This algorithm fits a blackbody curve to a given dataset. If the data contains instrumental flux, the function **blackbody_flux_fit** will cross-reference wavelength and corresponding intensity for the given spectral class of the source. If the spectral class is unknown, intensity data for an F0 star is selected. If no data is available for the specific spectral class selected, the algorithm will pick the closest spectral class available. As of now, the algorithm can only take in wavelength measurements ranging from 351.0 nm to 742.72 nm. Intensity measurements are from SPECLIB (JACOBY, HUNTER, AND CHRISTIAN 1984). See: http://adsabs.harvard.edu/abs/1984ApJS...56..257J

**_IMPORTANT_:** The algorithm performs best when the correct spectral class is selected, as it yields a more accurate correction factor to convert the instrumental flux to intensity. 

If input data is already in intensity, use the function **blackbody_fit**. This function is not limited to the wavelength range as **blackbody_flux_fit** is. 

# Installation

Clone the repository or download to a local system as a ZIP file.

It's best to work off the same directory in which the package is saved, so that the modules can be called directly, such as:

from **blackbody_curve** import **blackbody_fit**

# Required libraries

This code utilizes three common python packages:

* numpy
* scipy
* matplotlib

These three packages are bundled with anaconda. If you have anaconda installed all these packages are installed in your machine already.

# Test Scripts

To make sure that the algorithm is working, you can run the three test scripts available in the **test** folder. 

**test_script1**: Fits data for F4 star HD  23511.
**test_script2**: Fits data for O7 star HD 35619
**test_script3** Fits data for A0 star, Vega. Data contains instrumental flux as measured by the 16-inch telescope at Mt. Wilson. This is the only test script that makes use of the **blackbody_flux_fit** function. 

You can run any of these test scripts by typing, for example, *python test_script1.py* in a terminal.

# How to Contribute?

Want to contribute? Bug detections? Comments? Please email me : dg7541@bard.edu


