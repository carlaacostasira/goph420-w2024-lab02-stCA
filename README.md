# goph420-w2024-lab02-stCA
Repository for lab 02 Root Finding in the GOPH 420 Course


# GOPH 420 - Inversion and Parameter Estimation for Geophysicists
*Semester:* W2024
*Instructor:* B. Karchewski
*Author:* <Carla Acosta>
*Topic:* Root Finding - Newton Raphson and Secant Method

This repository contains the following functions:

# root_newton_raphson 
This function computes root finding using Newton-Raphson method

Input
 ------
x0 : float
    Initial guess for the root.
f : callable function
    Function to find the root of.
dfdx : callable function 
    Derivative of the function.

Returns
-------
root estimate : float 
number of iterations to convergence : int
approximate relative error at each iteration : numpy.ndarray

# root_secant_modified
This function computes root finding using modified secant method

Inputs 
------
x0 : float
    Initial guess for the root.
dx : numpy.ndarray
    Step size for derivative estimation.
f : callable function
    Function to find the root of. 
            
Returns
-------
root estimate : float 
number of iterations to convergence : int
approximate relative error at each iteration : numpy.ndarray
