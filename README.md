# BlackbodyFit

This algorithm fits a blackbody curve to a given dataset. If the data contains instrumental flux, the function **blackbody_flux_fit** will cross-reference wavelength and corresponding intensity for the given spectral class of the source. If the spectral class is unknown, intensity data for an F0 star is selected. 

**_IMPORTANT_:** The algorithm performs best when the correct spectral class is selected, as it yields a more accurate correction factor to convert the instrumental flux to intensity. 

3510 7427
