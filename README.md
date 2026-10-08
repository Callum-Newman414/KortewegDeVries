# KortewegDeVries
In this project, I use leapfrog time stepping and central spatial difference stepping to form a recurrence relation which evolves a given solution to the Korteweg-De Vries PDE in time. 

The Korteweg-De Vries equation (KdV) is a non-linear partial differential equation that can be used to describe waves in shallow water. As it is integrable, it has an exact, simple solution in the form of a soliton, a wave that moves at constant speed and keeps its shape in time. I have used this exact solution as an initial condition, from which the code can evolve in time.
The equation itself is of the following form:

$$\frac{\partial \eta}{\partial t} + c\frac{\partial \eta}{\partial r} + \alpha \eta \frac{\partial \eta}{\partial r} + \delta^2 \frac{\partial^3 \eta}{\partial r^3} = 0$$

where $\eta$ is the height of the disturbance of the water, $r$ is the 1-dimensional spatial coordinate of the water, and $\alpha$ and $\delta$ represent the non-linearity and dispersion of the medium, respectively.
This equation can (as in [2], section 2) be recast into the form:

$$
\frac{\partial u}{\partial t}
+ u\frac{\partial u}{\partial x}
+ \delta^2\frac{\partial^3 u}{\partial x^3}
= 0
$$

This equation is the KdV that the function that I have written is attempting
to solve. Here, the changes of variables are $x = r - ct$ and
$u = \alpha\eta$. These variables represent a change of basis such that the
frame now being considered is moving at speed $c$, which would
