import numpy as np

def solve_kdv(u_init, x, t, delta):
    # Author: Callum Newman , Date: 05/02/2026
    # Solving KdV equation using the iterative algorithm given in the script.
    # Input:
    # ∗ u_init: (1 x N) array that contains the initial values of u at time t0
    # ∗ x: vector of N elements that contains the grid points of x
    # ∗ t: vector of M elements that contains the time points of the simulations
    # ∗ delta: the delta in the KdV equation
    #
    # Output:
    # ∗ u_hist: (M x N) array that contains the values of u at every grid point of x
    #   and every time step
    #
    # Constraints:
    # ∗ Periodic boundary condition is assumed in the x-grid
    #
    # Example use:
    #   x = arange(0,1.02,0.02)
    #   t = arange(0,0.202,0.02)
    #   delta = 0.03
    #   u_init = exp(-(test_x-0.5)**2/(2*0.1**2))
    #   u_hist = solve_kdv(u_init, x, t, delta)
    #   plt.plot(x, u_hist(M,:)) # plot the last u
    #   
    # Note: this function assumes that we have numpy imported as np, and matplotlib.pyplot
    #       imported as plt
    # Physically, the plot gives the 

    # assume we are given constant time and space steps
    dt = t[2] - t[1]
    dx = x[2] - x[1]
    N = x.size
    M = t.size

    # set up periodic boundary conditions so that the formula can be used
    # on the edges of the spatial grid
    u_hist = np.zeros((M,N))
    u_per = np.concatenate((u_init[-2:], u_init, u_init[:2]))
    
    # set first row of u_hist to give initial condition:
    u_hist[0,:] = u_init

    # create rows holding the values for u at three adjacent times - u_t0 and u_t1 
    u_t0 = u_per
    u_t1 = np.zeros(N+4)
    u_t2 = np.zeros(N+4)

    # use the recurrence relation for the first iteration from initial values to get the
    # first set of values at t = dt
    for i in range(2,N+2):
         u_t1[i] = u_per[i] - (dt/(6*dx)) * (u_per[i+1] + u_per[i] + u_per[i-1]) * \
            (u_per[i+1] - u_per[i-1]) - delta**2 * (dt/(2*dx**3)) * (u_per[i+2] - 2* \
            u_per[i+1] + 2 * u_per[i-1] - u_per[i-2])
    u_t1[N+2:] = u_t1[2:4]
    u_t1[:2] = u_t1[N:N+2]
    u_hist[1,:] = u_t1[2:N+2]

    # loop over all remaining time values to fill out output matrix
    for j in range(2,M):
        for i in range(2,N+2):
            u_t2[i] = u_t0[i] - dt/(3*dx) * (u_t1[i+1] + u_t1[i] + u_t1[i-1]) * (u_t1[i+1] \
                - u_t1[i-1]) - delta**2 * dt/(dx**3) * (u_t1[i+2] - 2 * u_t1[i+1] + 2 * u_t1[i-1] \
                - u_t1[i-2])
        u_t2[N+2:] = u_t2[2:4]
        u_t2[:2] = u_t2[N:N+2]

        # fill out result into output array
        u_hist[j,:] = u_t2[2:N+2]

        #cycle the rows of u values at different times for the next iteration
        u_t0 = u_t1.copy()
        u_t1 = u_t2.copy()
         
    
    return u_hist