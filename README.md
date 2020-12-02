# MehtaKnights

## Learning Objectives
### Overall Objectives
- Teach students the basic terminology of reinforcement learning (i.e. policy, reward, state, action, etc.)
- Introduce students to policy updates and policy gradients as means to optimize policies to solve tasks
- Provide students with a mathematical understanding of how to optimize policies using these methods
- Expose students to state-of-the-art reinforcement learning models and how they work

### Problem 1 Objectives
1) Introduce students to basic terminology in reinforcement learning (i.e. Markov Decision Processes, Rewards, Policies)
2) Explain how to solve markov decision processes to arrive at good policies
3) Introduce basic reinforcement learning algorithms that use policy updates (i.e. Direct Evaluation, Temporal Difference Learning, Q-learning)

### Problem 2 Objectives
1) Help students understand cases in which policy update methods from problem 1 do not solve the task well
2) Introduce policy gradients to optimize a policy via gradient ascent
3) Characterize a policy as a neural network, thus providing exposure to deep reinforcement learning
4) Allow students to tie their new skills to old problems, namely the Segway problem from EECS 16AB

### Problem 3 Objectives
1) Understand how state-of-the-art deep RL algorithms work via an introduction to a3c

### Problem 4 Objectives
1) Extra problem to help students solidify their understanding of reinforcement learning

## How to Navigate the Repository

### Documentation
<b> Slide Deck</b> – Named slides.pdf in the main directory

<b> Note</b> – Named note.pdf in the main directory

<b> Quiz</b> – Named quiz.pdf in the main directory, with solutions named quiz_sol.pdf in the main directory

### Coding Assignment
<b> Problem 1 </b> – Located in the prob1 folder in the main directory
- prob1.ipynb contains the coding assignment
- prob1_sol.ipynb contains the solution to the coding assignment
- gym-note4-mdp is a folder that contains files and code to build a chain world environment that we developed for students to visualize how agents affect the state of the world in reinforcement learning problems

<b> Problem 2 </b> – Located in the prob2 folder in the main directory
- prob2.ipynb contains the coding assignment
- prob2_sol.ipynb contains the solution to the coding assignment
- vpg.py contains code that implements Vanilla Policy Gradient, a reinforcement learning algorithm that the students will use in their coding assignment to test their code
- core.py and the utils folder contain helper python functions for vpg.py
- images folder contains the images that are used in the coding assignment notebook to help students learn
- environment.yaml, setup.py, and spinup.egg-info are files needed for students to set up the development environment with the proper packages and dependencies
- All other files are caches and are not important to the project

<b> Problem 3 </b> – Located in the prob3 folder in the main directory
- prob3.ipynb contains the coding assignment
- prob3_sol.ipynb contains the solution to the coding assignment

<b> Problem 4 </b> – Located in the prob4 folder in the main directory
- prob4.pdf contains a famous "Bloom's Taxonomy" problem
