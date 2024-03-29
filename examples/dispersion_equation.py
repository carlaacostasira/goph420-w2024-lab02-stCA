import numpy as np
import matplotlib.pyplot as plt
from goph420_lab02.root_finding import root_secant_modified
from goph420_lab02.root_finding import root_newton_raphson

ro1 = 1800 # [kg/m3] density of layer 1
ro2 = 2500 # [kg/m3] density of layer 2
beta1 = 1900 # [m/s] shear wave of layer 1
beta2 = 3200 # [m/s] shear wave of layer 2
H = 4000 # [m] thickness of layer 1

zmax = H * ((beta1**-2) - (beta2**-2))**0.5 
#print (zmax) 

f = 0.1 # [Hz] frequency of the wave

# Define the dispersion equation
def intersection(z):
    return (ro2/ro1)*np.sqrt((H**2)*((beta1**-2)-(beta2**-2))-z**2)/z - np.tan(2*np.pi*f*z)

za = []
for i in range(0, 4): # Assuming you want to iterate from 0 to 3
    z_asyntote = (0.25/f)*(2*i+1) # Asyntotic value of the mode 0
    if z_asyntote < zmax:
        za.append(z_asyntote)
        
plt.xlim((0, 2))

# Plot the dispersion equation
if len(za):
    zplt = np.linspace(0, za[0] - 1e-5, 100) # Create a range of values around the asymptotic value
    plt.plot(zplt, intersection(zplt), color='b')
    
    zplt = np.linspace(za [-1], zmax, 100) # Create a range of values around the asymptotic value
    plt.plot(zplt, intersection(zplt), color='b')
    
else:
    zplt = np.linspace(0, zmax, 100) # Create a range of values around the asymptotic value
    plt.plot(zplt, intersection(zplt), color='b')

for k in range(len(za)-1): # Iterate over the indices of za
    zplt = np.linspace(za[k] + 1e-5, za[k+1] - 1e-5, 100) # Create a range of values around the asymptotic value
    plt.plot(zplt, intersection(zplt), color='b') # Plot the dispersion equation
    plt.ylim((-20, 45))

for x in za:
    plt.axvline(x=x, color='r', linestyle='--') # Plot the asymptotic values
    
#plt.axvline(x=za[0], color='r', linestyle='--', label='Asyntote')  
plt.title(f'Dispersion Equation for a frequency of {f} Hz')
plt.xlabel('\u03B6')
plt.ylabel('g(\u03B6)')
plt.legend()
#plt.show()

frequencies = [0.2, 0.5, 0.8, 1, 2, 3, 5, 7, 9, 10] # [Hz] frequency of the wave

# Initialize an empty list to store the roots

roots_storage = []


for i, f in enumerate(frequencies):
    mode = 0 # Initialize the mode
    roots_for_frequency = [] # List to store roots for the current frequency
    def intersection(z):
        return (ro2/ro1)*np.sqrt((H**2)*((beta1**-2)-(beta2**-2))-z**2)/z - np.tan(2*np.pi*f*z)
    
    plt.figure ()
    za_mode0 = 0

    while mode < 3:
        za_mode = (0.25/f)*(2*mode+1) # Asymptotic value of the mode 0
        if za_mode < zmax:
            z0 = za_mode - 1e-5
            
            zplt = np.linspace(za_mode0 + 1e-6, za_mode - 1e-6, 100) # Create a range of values around the asymptotic value
            plt.plot(zplt, intersection(zplt), color='b')
            plt.axvline(x=za_mode, color='r', linestyle='--', label = 'Asyntote (s)' if mode == 0 else "_nolabel_") # Plot the asymptotic values
            
            za_mode0 = za_mode
                                    
        else:
            z0 = zmax - 1e-6
            if mode:
                zplt = np.linspace(za_mode + 1e-6, zmax, 100) # Create a range of values around the asymptotic value
            else:
                zplt = np.linspace(za_mode0 + 1e-6, zmax, 100)
            plt.plot(zplt, intersection(zplt), color='b')
            
            if intersection(z0) > 0:
                break 
            
        root = root_secant_modified(z0, 1e-7, intersection)[0]
        roots_for_frequency.append(root) # Store the root for the current mode
         
        
        plt.plot (z0, 0, 'xg', label= 'Initial guess' if mode == 0 else "_nolabel_")
        plt.plot (root, intersection(root),'ro', label= 'Root (s)' if mode == 0 else "_nolabel_") 
                                 
        #print(f'Initial guess (z0) for mode {mode} and frequency {f} Hz is {z0}')
        #print(f'Root for mode {mode} and frequency {f} Hz is {root}')
        
        if za_mode > zmax:
            break
        
        mode += 1
        
    roots_storage.append(roots_for_frequency) # Store the roots for the current frequency5
    plt.ylim (-10, 10)
    #plt.xlim(0, zmax)
    plt.title('Dispersion Equation for Love Waves')
    plt.xlabel('\u03B6')
    plt.ylabel('g(\u03B6)')
    plt.legend()  
    plt.savefig (f'figures/roots_frequencies_{f}.png')
    
    
print(roots_storage)

velocities = []
lambdas = []
for i in range(len(roots_storage)):
    frequency_roots = roots_storage[i]
    velocity_array = []
    lambdas_array = []
    #print(frequency_roots)
    for root in frequency_roots:
        C_L = beta1 * H /(np.sqrt(H ** 2 - root ** 2 * beta1 ** 2))
        velocity_array.append(C_L)
        lambdas_array.append (C_L/frequencies[i])
        
    
    velocities.append(velocity_array)
    lambdas.append(lambdas_array)


#Graphs by Mode
nmodes = 3
velocities_modes = [[] for _ in range (nmodes)]
root_modes = [[] for _ in range (nmodes)]
lambda_modes = [[] for _ in range (nmodes)]
frequencies_modes = [[] for _ in range (nmodes)]

for m, (rm, vm, lm, fm) in enumerate (zip (root_modes, velocities_modes, lambda_modes, frequencies_modes)):
    for k, (rf, vf, lf) in enumerate (zip (roots_storage, velocities, lambdas)):
        if len(rf) > m:
            rm.append (rf[m])
            vm.append (vf[m]) 
            lm.append (lf[m])
            fm.append (frequencies[k])
            
plt.figure()
plt.plot(frequencies_modes[0], velocities_modes[0], '-', label='Mode 0')
plt.plot(frequencies_modes[1], velocities_modes[1], '-', label='Mode 1')
plt.plot(frequencies_modes[2], velocities_modes[2], '-', label='Mode 2')
plt.xlim (0, 10)
plt.title('Velocities vs Frequency for Modes 0, 1 and 2')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Velocities [m/s]')
plt.legend()  
plt.savefig ('figures/velocity_modes.png') 

plt.figure()
plt.plot(frequencies_modes[0], lambda_modes[0], '-', label='Mode 0')
plt.plot(frequencies_modes[1], lambda_modes[1], '-', label='Mode 1')
plt.plot(frequencies_modes[2], lambda_modes[2], '-', label='Mode 2')
plt.xlim (0, 6)
plt.ylim(0, 5000)
plt.title('Wavelength vs Frequency for Modes 0, 1 and 2')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Wavelenght [m]')
plt.legend()  
plt.savefig ('figures/wavelenght_modes.png') 


