import numpy as np 

def km2miles(km):
    '''
    This function converts value give in KM to 
    Miles. 

    Args:
    km (int or float): Value in km to convert to miles.

    Returns;
    miles (float): Calculated value in miles. 
    '''
    ## rate at which km is converted to miles
    conversion_ratio = 0.621371  
    
    ## calculate miles 
    # miles = km * conversion_ratio
    miles = np.multiply(km,  conversion_ratio)

    return miles  
