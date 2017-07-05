# BlackbodyFit

This algorithm fits a blackbody curve to a given dataset. If the data contains instrumental flux, the function **blackbody_flux_fit** will cross-reference wavelength and corresponding intensity for the given spectral class of the source. If the spectral class is unknown, intensity data for an F0 star is selected. If no data is available for the specific spectral class selected, the algorithm will pick the closest spectral class available. As of now, the algorithm can only take in wavelength measurements ranging from 351.0 nm to 742.72 nm. Intensity measurements are from SPECLIB (JACOBY, HUNTER, AND CHRISTIAN 1984). See: http://adsabs.harvard.edu/abs/1984ApJS...56..257J

**_IMPORTANT_:** The algorithm performs best when the correct spectral class is selected, as it yields a more accurate correction factor to convert the instrumental flux to intensity. 

If input data is already in intensity, use the function **blackbody_fit**. This function is not limited to the wavelength range as **blackbody_flux_fit** is. 

