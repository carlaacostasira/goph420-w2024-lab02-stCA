import numpy as np
import matplotlib.pyplot as plt

def root_newton_raphson(x0, f, dfdx): 
    # """
    # Compute root finding using Newton-Raphson method.

    # Inputs
    # ------
    # x0 : float
    #     Initial guess for the root.
    # f : callable function
    #     Function to find the root of.
    # dfdx : callable function 
    #     Derivative of the function.
    #
    # Returns
    # -------
    #   root estimate : float 
    #   number of iterations to convergence : int
    #   approximate relative error at each iteration : numpy.ndarray
    #
    # Raises
    # ------
    # ValueError
    #     If x0 is not a float
    #     If f and dfdx are not a callable functions
    # """

    if not isinstance(x0, float):
        raise ValueError(f"x0 must be a float, not {type(x0)}")
    if not callable(f):
        raise ValueError("f must be callable function")
    if not callable(dfdx):
        raise ValueError("dfdx must be callable functions")

    x = x0
    error = np.array([])
    while True:
        x_new = x - f(x)/dfdx(x)
        error = np.append(error, abs((x_new - x)/x_new))
        if abs((x_new - x)/x_new) < 1e-6:
            break
        x = x_new
    return x_new, len(error), error
    

def root_secant_modified(x0, dx, f): 
# """
# Compute root finding using modified secant method.

#     Inputs
#     ------
#     x0 : float
#         Initial guess for the root.
#     dx : numpy.ndarray
#         Step size for derivative estimation.
#     f : callable function
#         Function to find the root of. 
#                
#     Returns
#     -------
#     root estimate : float 
#     number of iterations to convergence : int
#     approximate relative error at each iteration : numpy.ndarray
#
#     Raises
#     ------
#     ValueError
#         If x0 is not a float
#         If dx is not an int
#         If f is not an array_like
#     """

    if not isinstance(x0, float):
        raise ValueError(f"x0 must be a float, not {type(x0)}")
    if not callable(f):
        raise ValueError("f must be callable function")
    
    x = x0
    error = np.array([])
    while True:
        x_new = x - f(x)*dx/(f(x + dx) - f(x))
        error = np.append(error, abs((x_new - x)/x_new))
        if abs((x_new - x)/x_new) < 1e-6:
            break
        x = x_new
    return x_new, len(error), error

