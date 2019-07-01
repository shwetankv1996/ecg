import numpy as np
import scipy.signal as signal
import pylab as pl

# Calculate the coefficients for a pure fixed point
# integer filter

# sampling rate
fs = 1000

# cutoffs
f1 = 45
f2 = 55

# scaling factor in bits
q = 14
# scaling factor as facor...
scaling_factor = 2**q

# let's generate a sequence of 2nd order IIR filters
sos = signal.butter(2,[f1/fs*2,f2/fs*2],'stop',output='sos')
print(sos)
sos = np.round(sos * scaling_factor)

# print coefficients
for biquad in sos:
    for coeff in biquad:
        print(int(coeff),",",sep="",end="")
    print(q)

