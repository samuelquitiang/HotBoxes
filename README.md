### Monte Carlo Simulation of Particle Distribution in Potential Wells with Thermal Reservoir
In this work, we study the scenario of an array of infinite potential wells in contact with a thermal reservoir, each containing one electron. It is well known that in certain physical systems, the likelihood of being in a particular state is determined by the Boltzmann distribution, which is a function of the energy and temperature.


# $P(n_i) = \frac{e^{-E_i/k_b T}}{Z}$

The objective of this project is to delve into the distribution of particles within the energy levels of the system upon reaching equilibrium. Additionally, it aims to explore how the system's behavior varies concerning different parameters, such as the length of the wells. To achieve this, we will use the Monte Carlo approach with the Metropolis algorithm in which we make the system evolve according to a certain probabilities. We aim to explore how temperature affects the final distribution of particles on energy levels, the stability of the system, and the convergence of simulation results.

![Potenciales](https://github.com/samuelquitiang/HotBoxes/assets/53834570/66a53846-9845-46b1-90f9-aaeea9430fb4)

In this case, the initial state of the system can be expressed as:
$n_0 = (4, 3, 2, ..., 4)$

The code will make evolve the system from a state $n_i$ to a state $n_j$ by doing a "random walk" in which the probability of accept a transition to a higher level of energy is given by:

$W=P\left(n_i \rightarrow n_j\right)=\frac{p\left(E_{n_j}\right)}{p\left(E_{n_i}\right)}=\frac{e^{-\beta E_{n_j}} / Z}{e^{-\beta E_{n_i} / Z}}=e^{\beta\left(E_{n_j}-E_{n_i}\right)}$

And after taking into account the probability of moving to a lower energy state due to the system's tendency to reach its ground state. The transition conditions are compute by generating a random number and the following test:

*    $r: random.uniform()<0.5$: Downward transition
*    if $r>0.5$ $and$ $r': random.uniform() < W$ : Upward transition

The code has the function:

Potential_reservoir(Ta, N, l, nmax, plot=False, live=False)

    Perform a simulation to compute the total energy of an array of N potential wells when the system reach the equilibrium with a thermal reservoir at a temperature T. The functions make use of the function Pot_energy(T, N, l, nmax, plot, live).

    Parameters:
        Ta (float, list, np.ndarray): Temperature or array of temperatures.
        N (int): Number of potential wells in the system.
        l (float, list, np.ndarray): Length of the wells or array of lengths in nm.
        nmax (int): Maximum level of occupancy for a well.
        plot (bool): Whether to generate a plot of the simulation results. Total energy vs epoch and a histogram of the occupation distribution of the energy states. Default: False
        live (bool): Whether to generate an animation of the distribution of energy states. Default: False

    Returns:
        Tuple: A tuple containing arrays or integers representing the average energy and heat capacity. The format of the tuple varies depending on the type of the Ta parameter: if Ta is an integer, both average energy and heat capacity are single values; if Ta is a list, each element of the tuple corresponds to an array of values, and similarly for the l parameter.
    

This is the main function for the user, from it the user can obtain how is the behaviour of the system energy respect to the different parameters.
