# MujocoUnity

![MujocoUnity](images/MujocoUnityBanner.gif)

Mujoco is a high end physics simulator used for bleeding edge research into robotics and reinforcement learning. Many of the standard benchmarks are implemented in Mujoco. 

MujocoUnity enables the reproduction of these benchmarks within Unity ml-agents using Unity’s native physics simulator, PhysX. Mujoco Unity maybe useful for:
* Video Game researchers interested in apply bleeding edge robotics research into the domain of locomotion and AI for video games.
* Traditional academic researchers looking to leverage the strengths of Unity and ml-agents along with the body of existing research and benchmarks in Mujoco.
* Benchmarking current and future algorithms within Unity ml-agents. For example, comparing the performance of ml-agents PPO implementation with OpenAI.Baselines implementation of PPO.

References: 
* OpenAI Baselines / Gym / Roboschool
* DeepMind 
* Some other algos

Important: 
* PhysX makes many tradeoffs in terms of accuracy when compared with Mujoco. It may not be the best choice for your research project.
* MujocoUnity environments are running at 300-500 physics simulations per second. This is significantly higher that Unity’s defaults setting of 50 physics simulations per second.
* Currently, MujocoUnity does not properly simulate how Mujoco handles joint observations - as such, it maybe difficult to do transfer learning (from simulation to real world robots)
* A good primer on the differences between physics engines is ['Physics simulation engines have traditional made tradeoffs between performance’](https://homes.cs.washington.edu/~todorov/papers/ErezICRA15.pdf) and it’s accompanying [video](https://homes.cs.washington.edu/~todorov/media/ErezICRA15.mp4)


## Humanoid


| **DeepMindHumanoid** | **OpenAIHumanoid** |
| --- | --- |
| ![DeepMindHumanoid](images/DeepMindHumanoid102-2m.gif) | ![OpenAIHumanoid](images/OpenAIHumanoid164-2m.gif) |


* Set-up: Simple (OpenAI) and complex (DeepMind) Humanoid agents. 
* Goal: The agents must move its body toward the goal as quickly as possible without falling.
* Agents: The environment contains 16 independent agents linked to a single brain.
* Agent Reward Function: 
  * Reference OpenAI.Roboschool and / or DeepMind
    * -joints at limit penality
    * -effort penality (ignors hip_y and knee)
    * +velocity
    * -height penality if below 1.2m
  * Inspired by Deliberate Practice (currently, only does legs)
    * +facing upright bonus for shoulders, waist, pelvis
    * +facing target bonus for shoulders, waist, pelvis
    * -non straight thigh penality
    * +leg phase bonus (for height of knees)
    * +0.01 times body direction alignment with goal direction.
    * -0.01 times head velocity difference from body velocity.
* Brains: One brain with the following observation/action space.
    * Vector Observation space: (Continuous) 74 (Simple Humanoid), 88 (Complex Humanoid) variables
    * Vector Action space: (Continuous) Size of 17 (Simple Humanoid), 21 (Complex Humanoid) corresponding to target rotations applicable to the joints. 
    * Visual Observations: None.
* Reset Parameters: None.
* Benchmark Mean Reward: **TODO show vs OpenAI PPO**

## TODO - other models


## Structure
* TODO List Files



| DeepMindHumanoid | DeepMindHopper | DeepMindWalker | |
|:--------------:|:--------------:|:--------------:|:--------------:|
| ![DeepMindHumanoid](images/DeepMindHumanoid102-2m.gif) | ![DeepMindHopper](images/DeepMindHopper101-1m.gif) | ![DeepMindWalker](images/DeepMindWalker108-1m.gif) |
| **OpenAIAnt** ![OpenAIAnt](images/OpenAIAnt102-1m.gif) | **OpenAIHopper** ![OpenAIHopper](images/OpenAIHopper102-300k.gif) | **OpenAIWalker** ![OpenAIWalker](images/OpenAIWalker106-300k.gif) | **OpenAIHumanoid** ![OpenAIHumanoid](images/OpenAIHumanoid164-2m.gif) |
