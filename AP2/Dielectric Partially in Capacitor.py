kappa = 5 
K = kappa

#Algorithmic variables

length_of_plates = 10 
L = length_of_plates

x_K = [2, 5, 6, 8] # values of amount of dielectric in capacitor x_K = np.array(x_K)

x_ratio = (1/L) * x_K 
x = x_ratio

def calc_capacitance(area_plates, plate_separation, x_values): 
  A = area_plates 
  d = plate_separation 
  C_o = epsil_o * A / d 
  C_coeff = np.array([]) 
  for n in x_values:
    np.append(C_coeff, (1-n)+(K*n)) 
  New_capacitance = C_o * C_coeff 
  return New_capacitance

calc_capacitance(50, 5, x)

plt.plot(x, New_capacitance, label="Portion of Capacitor Occupied by Dielectric (K = 5) vs. Resulting Capacitance") 
plt.show()
