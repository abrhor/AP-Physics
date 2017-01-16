import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

"""
----------------------------------
Ohmic Resistance - Metallic Coils
----------------------------------
"""

# Raw Data
voltage1 = np.array([0, .3, .5, .8, 1., 1.2, 1.5, 1.8])
current1 = np.array([0, .1, .12, .14, .18, .2, .24, .28])

def linfunct(x, m, b):
  return m * x + b
  
ws, cov = curve_fit(linfunct, voltage1, current1)
print(ws)


"""
----------------------------------------------------------------------------------
Risk Metric Functions
(1) Squared Error
(2) Percent Squared Error, which is the return value of (1) divided by the variance
----------------------------------------------------------------------------------
"""

def err(actual, predicted):
  try:
    distance = np.square(actual - predicted)
    error = np.sum(distance) / len(actual)
    return error
  except ValueError:
    print("Error: Different Dimensions of Actual and Predicted")
 
def percenterr(squarederror, actual):
  numerator = squarederror * 100.
  denominator = np.nanvar(actual)
  return numerator / denominator
  
modelcurrent1 = linfunct(voltage1, ws[0], ws[1])
errorlin = err(current1, predcurrent)
linerrpercent = percenterr(errorlin, current1)

# Figure 1: Scatter and Best Fit of Voltage vs. Current in Case of Ohmic Resistance
plt.scatter(voltage1, current1, color='g')
plt.plot(voltage1, predcurrent)
plt.xlabel('Voltage')
plt.ylabel('Current')
plt.legend(loc='upper left')
plt.suptitle('Voltage vs. Current with Best Fit Line (Ohmic)')
plt.show()

"""
----------------------------------
Non-Ohmic Resistance - Light Bulbs
----------------------------------
"""
# Raw Data
voltage2 = np.array([0., .1, .2, .5, .8, 1., 1.3])
current2 = np.array([0., .14, .16, .2, .24, .26, .3])

def lnfunct(x, m, h, k):
  return m * np.log(x + h) + k

ws2, cov2 = curve_fit(lnfunct, voltage2[1:], current2[1:])
 
# error metrics for non-ohmic

modelcurrent2 = lnfunct(voltage2[1:], ws2[0], ws2[1], ws2[2])

lnerr = err(current2[1:], modelcurrentln)
lnpercenterr = percenterr(lnerr, current2[1:])
print(lnerr, lnpercenterr)

# For plotting purposes
trendxs = np.linspace(-0.2, 1.5, 500) 
trendys = lnfunct(trendxs, ws2[0], ws2[1], ws2[2]) 

# Figure 2: Scatter and Logarithmic Best Fit of Voltage vs. Current in Case of Non-Ohmic Resistance
plt.scatter(voltage2, current2, label='Raw Data for Current', color='g')
plt.plot(trendxs, trendys, label='Best Fit', color='b')
plt.xlabel('Voltage')
plt.ylabel('Current')
plt.suptitle('Voltage vs. Current with Best Fit Natural Logarithmic Curve (Non-Ohmic)')
plt.show()

"""

g(x) = f**-1 (x). gprimeprime is the second derivative of g(x). 
Since f'' would have been the ROC of 1 / resistance with respect voltage,
g'' is the ROC of R with respect to V

"""

def gprimeprime(x):
  return 3.56*np.exp((100. / 53.) * x + (51. / 53.))

gprimeprimeys = gprimeprime(trendxs)

# Figure 3: ROC of the Non-Ohmic Resistance with Respect to Voltage
plt.plot(trendxs, gprimeprimeys, c='r')
plt.xlabel('Voltage')
plt.ylabel('Rate of Change in Resistance')
plt.suptitle('Rate of Change of Resistance with Respect to Voltage')
plt.show()
