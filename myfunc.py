# Create a DOCUMENTED function with an explicit name and variables
def Ingredients4Pancakes(pan, out=dict):
    # The """  """ syntax encloses the function documentation
    # It is automatically returnes by the ? syntax in the console
    """ Return the ingredients to make pan pancakes 
    
    When fed a number of pancakes (pan), return the ingredients necessary
    The output can be a tuple of all variables or a dict
    
    Parameters
    ----------
    pan :   float
        The number of pancakes to be made
        
    Return
    ------
    out :   dict / tuple
        The output, formatted as required 
    """
    # Use explicit variable names whenver possible
    eggs, eg_u = pan/2+1, 'eggs'
    milk, mlk_u = 2*pan, 'L'
    toads, td_u = 10*pan, 'kg'
    
    # ------ optional 
    # A good practice, if your function returns several arguments
    # That may not be clear and it needs to be used by others
    # Is to return a dict with explicit keys
    if out is dict:
        out = {'eggs':{'val':eggs,'units':eg_u},
               'milk':{'val':milk,'units':mlk_u},
               'toads':{'val':toads,'units':td_u}}
    else:
        out = (eggs, eg_u, milk, mlk_u, toads, td_u)
    return out

def f2():
    print("Fast-and-dirty coding")
    