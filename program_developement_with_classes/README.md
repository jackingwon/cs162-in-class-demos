# Program Development with Classes

## Predator-Prey Problem

In this demo we will create a simulation of a natural habitat which is home to predators and their prey and model their interactions for various population sizes.

Both groups will have fixed birthrates; prey generally procreate faster than their predators. However, as the population of prey increases, the habitat can support a higher number of predators. This is turn leads to an increasing predator population and, after some time, a decreasing prey population. As the predator population grows it will reach a critical point where there are not enough prey animals to support it, thus it will begin to shrink. Fewer predators lead to more prey and the cycle repeats.

### The Rules

These are the rules for our simulation:

- The habitat updates itself in units of time called _ticks_. During one tick of our clock, every animal in the habitat gets an opportunity to do something.
- All animals are given an opportunity to move into an adjacent space, if an empty adjacent space can be found. One move per clock tick is allowed.
- Both the predators and the prey can reproduce. Each animal is assigned a fixed _breed time_. If the animal is still alive after breed-time ticks of the clock, it will reproduce. The animal does so by finding an unoccupied adjacent space and fills that space with its offspring. The animal's breed time is then reset to zero. An animal can breed at most once in a clock tick.
- The predators must eat. They have a fixed _starve time_. If they cannot find a prey animal to eat before starve-time clicks of the clock, they die.
- When a predator eats, it moves into an adjacent space that is occupied by prey (its meal). The prey is removed and the predator's start time is reset to zero. Eating counts as the predator's move during that clock tick.
- At the end of every clock tick, each animal's breed- or starve-time are decremented.


### Simulation Using OOP

Simulation is perfectly suited for OOP. In a simulation we need to identify the objects and their interactions.

For our program we will need:

- Island Class
- Prey Class
- Predator Class

We now need to identify for each class:

- _What_ we need to have represented in each class instance
- _How_ these instances can be manipulated, that is, what methods are needed

## Classes

### Island Class

`island.py`

### Predator and Prey, Kinds of Animals

#### Animal Object

The animal object will store properties that are common to all animals.
