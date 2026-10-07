import matplotlib.pyplot as plt
import numpy as np

from KdV_solver_function import solve_kdv

# using numpy function arange to generate lists from ranges that 
# can include floating point values
test_x = np.arange(0,1.00,0.02) # 50 values
test_t = np.arange(0,0.202,0.002) # 101 values up to t=0.2
test_delta = 0.03

# construct initial shape of the wave using the analytic solution to the equation
a = 0.05 # larger 'a' variable gives a greater peak width
A = 12*test_delta**2 / (a**2)
x_0 = 0.5
test_u_init = A*(np.cosh((test_x-x_0)/a))**(-2)

# plot the output function for time t=0.200 (can be changed by adjusting the index
# of the output in plt.plot)
output = solve_kdv(test_u_init, test_x, test_t, test_delta)
heights = output[-1, :]

plt.plot(test_x, heights)
plt.ylabel('u [actual height of wave * nonlinear coef]')
plt.xlabel('x [(r - ct)]')
plt.title(r'u against x for soliton solution of KdV equation, $\Delta t = 0.002, t=0.200$')
# note c would be the speed of the wave had there been no non-linear/dispersive terms in the
# original differential equation

# finding the x coordinate of the peak for a given t plot (done here with t=0.200)
max_x_pos = test_x[np.argmax(heights)]
plt.axvline(max_x_pos, color = 'b')

#adding tick mark of location of peak onto axis
max_position = test_x[np.argmax(heights)]

# look at nearby tick marks to see if they are too close to the new one

ticks = plt.gca().get_xticks()

for tick in ticks:
    if np.abs(max_position - tick) < 0.05: # threshold is if the ticks are within 0.03 of eachother
        ticks = ticks[ticks != tick] # remove the overlapping tick

addtick = np.append(ticks, max_position)
plt.gca().set_xticks(addtick)

plt.show()
