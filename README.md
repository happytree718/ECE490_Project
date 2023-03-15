# Simulated Annealing Algorithms Python Implementation

Self python implementation of simulated annealing algorithms analyzed in [SIMULATED ANNEALING: A REVIEW AND A NEW SCHEME](https://ieeexplore.ieee.org/document/9513782) by Thomas Guilmeau, Emilie Chouzenoux, and Víctor Elvira. Including the following algorithms:

* Simulated Annealing (SA)
* Fast Simulated Annealing (FSA)
* Sequential Monte Carlo Simulated Annealing (SMC-SA)
* Curious Simulated Annealing (CSA)

## Installation

To download the source code of the project, you need to clone this git repo.

```bash
git clone https://github.com/happytree718/ECE490_Project.git
```

Then, if you don't have the [NumPy](https://numpy.org/doc/stable/index.html) library installed on your machine, you need to install it as well.

```bash
pip install numpy
```

## Usage


**Configurations**

$N$ - Number of iterations to perform

$func$ - Target function to apply the simulated annealing algorithms

$algo$ - Algorithm applied to optimize on the target function

$initial \_ x$ - Initial value assigned to start the iterations.

The program is designed to run $N$ iterations of the applied algorithms on the target function to calculate its average best value and standard deviation as a direct conparison for different variations of the simulated annealing algorithm.

**Execution**

To run the script, run the following command in the terminal.

```bash
python result.py
```

The program will output two numbers, which are the average best value and its corresponding standard deviation of $N$ runs of the algorithm.

## Results

The results can be found in the report, with more details on the analysis of the different algorithms.

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
