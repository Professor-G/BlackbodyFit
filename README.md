# BlackbodyFit
<img src="https://user-images.githubusercontent.com/19847448/135402464-0e8ada6a-db1a-4e8c-8608-2d88bb1b633d.png">

# Curve Fitting

This is an open source algorithm that fits a blackbody curve to a given dataset to predict the temperature of the source. If the data contains instrumental flux, the function **blackbody_flux_fit** will cross-reference wavelength and corresponding intensity for the given spectral class of the source. If the spectral class is unknown, intensity data for an F0 star is selected. If no data is available for the specific spectral class selected, the algorithm will pick the closest spectral class available. As of now, the algorithm can only take in wavelength measurements ranging from 351.0 nm to 742.72 nm. Intensity measurements are from SPECLIB (JACOBY, HUNTER, AND CHRISTIAN 1984). See: http://adsabs.harvard.edu/abs/1984ApJS...56..257J

**_IMPORTANT_:** The algorithm performs best when the correct spectral class is selected, as it yields a more accurate correction factor to convert the instrumental flux to intensity. 

If input data is already in intensity, use the function **blackbody_fit**. This function is not limited to the wavelength range as **blackbody_flux_fit** is. 

Note that the algorithm scales the theoretial Planck curve by a scale ratio, defined by the integral of the data points divided by the integral of the theoretical planck curve. This scales the theoretical curve accordingly so that it can be plotted with the same scale as your data. 

# Example

An astrophysical source is measured to have magnitude 12 in the L photometric band (centered at 3.5&mu;), and 20 in the H band (centered at 1.65&mu;). Assume that the source is emitting like a blackbody, plot the blackbody curve that best fits the data. What is the temperature of the source?

```python
import numpy as np
from blackbody_curve import blackbody_fit

wavelength = np.array([3500, 1650]) #convert to nanometers
magnitudes = np.array([12, 20])

intensity = 10**(magnitudes/2.5) #convert magnitudes to intensity

blackbody_fit(wavelength, intensity)
```
<img src="https://user-images.githubusercontent.com/19847448/135399228-415d72c3-f7ba-4b88-a692-897bb1415674.png">

If instead you wish to fit data you collected, you can do so by calling the **blackbody_flux_fit** function and entering your flux measurements, and if known, the stellar spectral class.

```python
from blackbody_curve import blackbody_flux_fit

blackbody_flux_fit(wavelength, flux, spect_class = 'G7')
```
# Installation

Clone the repository or download to a local system as a ZIP file.

It's best to work off the same directory in which the package is saved, so that the modules can be called directly, such as:

from **blackbody_curve** import **blackbody_fit**

# Required libraries

This code utilizes three common python packages:

* numpy
* scipy
* matplotlib

# Test Scripts

To make sure that the algorithm is working, you can run the four test scripts available in the **test** folder. 

* **test_script1**: Fits data for F4 star HD  23511.
* **test_script2**: Fits data for O7 star HD 35619
* **test_script3** Fits data for A0 star, Vega. Data contains instrumental flux as measured by the 16-inch telescope at Mt. Wilson. This script makes use of the **blackbody_flux_fit** function. 
* **test_script4** Fits data for Be star GSC 3984:1357. Data contains instrumental flux as measured by the 16-inch telescope at Mt. Wilson. This script makes use of the **blackbody_flux_fit** function. 

You can run any of these test scripts by typing, for example, *python test_script1.py* in a terminal.

# How to Contribute?

Want to contribute? Bug detections? Comments? Please email me : danielgodinez123@gmail.com

# Acknowledgements

The author would like to thank the CUREA program at Mt. Wilson for the motivation and guidance necessary for the development of this program. Please see: http://physics.kenyon.edu/people/turner/cureaweb/CUREA.htm


