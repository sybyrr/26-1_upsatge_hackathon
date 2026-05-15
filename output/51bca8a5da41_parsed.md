# Parsed dump — job 51bca8a5da41

- Source: `51bca8a5da41_8. Policy Gradient.pdf`
- Elements: 182


## Page 1

`[   0 · paragraph]`

> REINFORCEMENT LEARNING
> Lecture 8 – Policy Gradient

`[   1 · paragraph]`

> Gyeongsik Moon

`[   2 · paragraph]`

> Visual Computing and AI Lab
> Korea University

`[   3 · footer]`

> Lecture credit: Emma Brunskill


## Page 2

`[   4 · paragraph]`

> Evolution from Value-Based to Policy-Based RL

`[   5 · list]`

> 1. Why did we start with Value-Based (DQN)?
> • Mathematical Foundation: Rooted in the Bellman Equation, it provides a recursive structure that is
> easy for computers to optimize.
> • Explicit Goal: By learning the "worth" (Q-value) of each action, the agent simply picks the one with
> the highest score (Greedy Policy).
> • Efficiency in Discrete Space: Highly effective for environments with a limited number of actions,
> like Atari games.

`[   6 · list]`

> 2. Why the Shift to Policy-Based (PG)?Despite the success of DQN, it faces critical limitations in
> complex, real-world scenarios:

`[   7 · list]`

> • Continuous Action Spaces: DQN must compute max_{a} Q(s, a), which is nearly impossible when
> actions are continuous (e.g., precise robot joint angles). PG avoids this by directly learning the
> action probability.
> • Stochastic Policies: Value-based methods are inherently deterministic. However, in games like
> Rock-Paper-Scissors or Aliased Environments, an optimal strategy must be stochastic to avoid
> being trapped.
> • Better Convergence: Q-values can change drastically with small parameter updates, leading to
> oscillations (The Deadly Triad). PG changes the policy smoothly, offering more stable convergence.


## Page 3

`[   8 · paragraph]`

> Policy-Based Reinforcement Learning

`[   9 · paragraph]`

> In the last lecture we approximated the value or action-value function
> using parameters w,

`[  10 · paragraph]`

> Vw (s) ≈ V π (s)
> Qw (s, a) ≈ Qπ (s, a)

`[  11 · paragraph]`

> A policy was generated directly from the value function

`[  12 · paragraph]`

> • e.g. using ϵ-greedy

`[  13 · paragraph]`

> In this lecture we will directly parametrize the policy, and will typically
> use θ to show parameterization:

`[  14 · paragraph]`

> πθ (s, a) = P[a|s;θ]

`[  15 · paragraph]`

> Goal is to find a policy π with the highest value function V π
> We will focus again on model-free reinforcement learning


## Page 4

`[  16 · heading1]`

> Value, Q-Value, Policy

`[  17 · heading1]`

> • Value function (State-Value) 𝑉𝜋 𝑠

`[  18 · list]`

> • The expected total reward an agent can accumulate starting from state s and following policy
> 𝜋 thereafter.
> • It represents "how good" it is for the agent to be in a particular state.

`[  19 · paragraph]`

> • Q-Value Function (Action-Value) 𝑄𝜋 𝑠, 𝑎

`[  20 · list]`

> • The expected total reward starting from state s, taking a specific action a, and then following
> policy 𝜋.
> • It captures the specific "worth" of an action in a given state.
> • In Value-Based RL (like DQN), we pick the action that maximizes this value: a = argmax_a Q(s,
> a).

`[  21 · list]`

`[  22 · paragraph]`

> • Policy 𝜋𝜃 𝑎 𝑠

`[  23 · list]`

`[  24 · list]`

> • A mapping from states to a probability distribution over actions.
> • In Policy-Based RL, we directly parameterize this mapping with 𝜃 (e.g., neural network weights).
> • The goal is to directly optimize the parameters 𝜃 to maximize the overall value 𝑉(𝜃).


## Page 5

`[  25 · heading1]`

> Value-Based and Policy-Based RL

`[  26 · heading1]`

> Value Based

`[  27 · paragraph]`

> • Learned Value Function
> • Implicit policy (e.g. ϵ-greedy)

`[  28 · list]`

`[  29 · paragraph]`

> Policy Based

`[  30 · list]`

> • No Value Function
> • Learned Policy

`[  31 · paragraph]`

> Actor-Critic

`[  32 · list]`

> • Learned Value Function
> • Learned Policy

`[  33 · figure]` *(base64 18860 chars attached)*

> ![image](/image/placeholder)


## Page 6

`[  34 · paragraph]`

> Types of Policies to Search Over

`[  35 · paragraph]`

> • So far have focused on deterministic policies or ϵ-greedy policies
> • Now we are thinking about direct policy search in RL, will focus
> heavily on stochastic policies

`[  36 · list]`


## Page 7

`[  37 · header]`

> Example: Aliased Gridworld

`[  38 · figure]` *(base64 14176 chars attached)*

> ![image](/image/placeholder)

`[  39 · list]`

> • The agent cannot differentiate the grey states
> • Consider features of the following form (for all N, E, S, W)

`[  40 · figure]` *(base64 7876 chars attached)*

> ![image](/image/placeholder)
> ϕ(s, a) = 1(wall to N, a = move E)

`[  41 · paragraph]`

> • Compare value-based RL, using an approximate value function

`[  42 · list]`

`[  43 · paragraph]`

> Qθ(s, a) = f (ϕ(s, a);θ)

`[  44 · paragraph]`

> • To policy-based RL, using a parametrized policy
> πθ (s, a) = g(ϕ(s, a);θ)

`[  45 · list]`


## Page 8

`[  46 · header]`

> Example: Aliased Gridworld

`[  47 · paragraph]`

> • Either way, it can get stuck and never reach the money Value-based RL learns
> a near-deterministic policy

`[  48 · list]`

`[  49 · figure]` *(base64 16676 chars attached)*

> ![image](/image/placeholder)

`[  50 · paragraph]`

> • Under aliasing, an optimal deterministic policy will either

`[  51 · figure]` *(base64 14928 chars attached)*

> ![image](/image/placeholder)

`[  52 · list]`

> • move W in both grey states (shown by red arrows)
> • move E in both grey states

`[  53 · list]`

> • e.g. greedy or ϵ-greedy

`[  54 · list]`

> • So it will traverse the corridor for a long time


## Page 9

`[  55 · paragraph]`

> Example: Aliased Gridworld

`[  56 · figure]` *(base64 18024 chars attached)*

> ![image](/image/placeholder)

`[  57 · figure]` *(base64 17184 chars attached)*

> ![image](/image/placeholder)
> An optimal stochastic policy will randomly move E or W in grey states

`[  58 · paragraph]`

> πθ(wall to N and S, move E) = 0.5

`[  59 · paragraph]`

> πθ(wall to N and S, move W) = 0.5
> It will reach the goal state in a few steps with high probability
> Policy-based RL can learn the optimal stochastic policy


## Page 10

`[  60 · heading1]`

> Policy optimization

`[  61 · paragraph]`

> • Policy based reinforcement learning is an optimization problem
> • Find policy parameters θ that maximize V (s0, θ)
> • Can use gradient free optimization
> • Greater efficiency often possible using gradient

`[  62 · list]`

`[  63 · list]`

> • Gradient descent
> • Conjugate gradient
> • Quasi-newton

`[  64 · list]`

> • We focus on gradient descent, many extensions possible
> • And on methods that exploit sequential structure


## Page 11

`[  65 · heading1]`

> Policy Gradient

`[  66 · list]`

> • Define V πθ = V (s0, θ) to make explicit the dependence of the value on the policy parameters
> • Assume episodic MDPs
> • Policy gradient algorithms search for a local maximum in V (s0, θ) by ascending the gradient of
> the policy, w.r.t parameters θ

`[  67 · paragraph]`

> • Where ∇ θ V (s0, θ) is the policy gradient

`[  68 · equation]` *(base64 20020 chars attached)*

`[  69 · equation]` *(base64 7448 chars attached)*

`[  70 · list]`

`[  71 · paragraph]`

> • and α is a step-size parameter

`[  72 · list]`


## Page 12

`[  73 · paragraph]`

> Policy Gradient

`[  74 · paragraph]`

> • ∇ θ V (s0, θ) is the policy gradient

`[  75 · figure]` *(base64 8876 chars attached)*

> ![image](/image/placeholder)

`[  76 · heading1]`

> • What is the relationship between ∇ θ V (s0, θ) and ∇θπθ (s, a)?

`[  77 · paragraph]`

> • Max imi zin g v alue s w ith ∇ θ V (s0, θ) is our goal
> • What we can compute is ∇θπθ (s, a) as we do not have learnable value function
> • How to derive ∇ θ V (s0, θ) from ∇θπθ (s, a) so that we can maximize value function
> during the training of the policy function?

`[  78 · list]`


## Page 13

`[  79 · header]`

> Value of a Parameterized Policy

`[  80 · paragraph]`

> • Assume policy πθ is differentiable whenever it is non-zero and we
> can compute the gradient ∇θπθ (s, a)

`[  81 · list]`

`[  82 · list]`

> • Recall policy value is where
> the expectation is taken over the states & actions visited by πθ

`[  83 · list]`

> • We can re-express this in multiple ways

`[  84 · list]`

`[  85 · paragraph]`

> • where τ = (s0, a0, r0, ..., sT− 1, aT − 1, rT − 1, sT ) is a state-action
> trajectory,
> • P(τ;θ) is used to denote the probability over trajectories when

`[  86 · list]`

`[  87 · paragraph]`

> executing policy π(θ) starting in state s0, and
> the sum of rewards for a trajectory τ

`[  88 · list]`

> • To start will focus on this latter definition.


## Page 14

`[  89 · header]`

> Likelihood Ratio Policies

`[  90 · paragraph]`

> • Denote a state-action trajectory as
> τ = (s0, a0, r0, ..., sT − 1 , aT − 1 , rT − 1 , sT )
> • Use to be the sum of rewards for a trajectory τ
> • Policy value is

`[  91 · equation]` *(base64 19872 chars attached)*

`[  92 · list]`

> where P(τ;θ) is used to denote the probability over trajectories when
> executing policy π(θ)

`[  93 · list]`

`[  94 · paragraph]`

> • In this new notation, our goal is to find the policy parameters θ:

`[  95 · list]`

`[  96 · equation]` *(base64 13784 chars attached)*


## Page 15

`[  97 · header]`

> Likelihood Ratio Policy Gradient

`[  98 · paragraph]`

> Goal is to find the policy parameters θ:

`[  99 · paragraph]`

> Take the gradient with respect to θ:

`[ 100 · equation]` *(base64 78776 chars attached)*


## Page 16

`[ 101 · paragraph]`

> Likelihood Ratio Policy Gradient

`[ 102 · paragraph]`

> • Goal is to find the policy parameters θ:

`[ 103 · equation]` *(base64 16344 chars attached)*

`[ 104 · paragraph]`

> • Take the gradient with respect to θ:

`[ 105 · paragraph]`

> • Approximate using m sample trajectories under policy πθ:

`[ 106 · equation]` *(base64 26376 chars attached)*


## Page 17

`[ 107 · header]`

> Decomposing the Trajectories Into States and Actions

`[ 108 · equation]` *(base64 18740 chars attached)*

`[ 109 · equation]` *(base64 78572 chars attached)*

`[ 110 · paragraph]`

> • Approximate using m sample paths under policy πθ:


## Page 18

`[ 111 · header]`

> Policy Gradient

`[ 112 · header]`

> From slide 12

`[ 113 · equation]` *(base64 18916 chars attached)*

`[ 114 · paragraph]`

> • ∇ θ V (s0, θ) is the policy gradient

`[ 115 · figure]` *(base64 8900 chars attached)*

> ![image](/image/placeholder)

`[ 116 · heading1]`

> • What is the relationship between ∇ θ V (s0, θ) and ∇θπθ (s, a)?

`[ 117 · list]`

> • Max imi zin g v alue s w ith ∇ θ V (s0, θ) is our goal
> • What we can compute is ∇θπθ (s, a) as we do not have learnable value function
> • How to derive ∇ θ V (s0, θ) from ∇θπθ (s, a) so that we can maximize value function
> during the training of the policy function?


## Page 19

`[ 118 · header]`

> Decomposing the Trajectories Into States and Actions

`[ 119 · equation]` *(base64 18740 chars attached)*

`[ 120 · equation]` *(base64 83808 chars attached)*

> Same mathematica l form as tha t in di ffusion m odels

`[ 121 · heading1]`

> • Approximate using m sample paths under policy πθ:


## Page 20

`[ 122 · header]`

> Score Function

`[ 123 · paragraph]`

> • A score function is the derivative of the log of a parameterized
> probability / likelihood
> • Example: let π(s; θ) be the probability of state s under parameter θ
> • Then the score function would be

`[ 124 · list]`

`[ 125 · paragraph]`

> • For many policy classes, it is not hard to compute the score function

`[ 126 · list]`


## Page 21

`[ 127 · header]`

> Softmax Policy

`[ 128 · paragraph]`

> • Weight actions using linear combination of features ϕ(s, a)T θ
> • Probability of action is proportional to exponentiated weight

`[ 129 · list]`

`[ 130 · equation]` *(base64 14252 chars attached)*

`[ 131 · list]`

> • The score function is

`[ 132 · equation]` *(base64 16628 chars attached)*

`[ 133 · equation]` *(base64 1720 chars attached)*

`[ 134 · equation]` *(base64 12852 chars attached)*

`[ 135 · equation]` *(base64 1844 chars attached)*

`[ 136 · equation]` *(base64 12616 chars attached)*

`[ 137 · equation]` *(base64 1740 chars attached)*

`[ 138 · equation]` *(base64 14488 chars attached)*

`[ 139 · equation]` *(base64 1772 chars attached)*

`[ 140 · equation]` *(base64 7168 chars attached)*

`[ 141 · equation]` *(base64 1892 chars attached)*


## Page 22

`[ 142 · header]`

> Softmax Policy

`[ 143 · paragraph]`

> • Weight actions using linear combination of features ϕ(s, a)T θ
> • Probability of action is proportional to exponentiated weight

`[ 144 · list]`

`[ 145 · equation]` *(base64 18580 chars attached)*

`[ 146 · equation]` *(base64 16940 chars attached)*

`[ 147 · paragraph]`

> • The score function is

`[ 148 · list]`


## Page 23

`[ 149 · paragraph]`

> Gaussian Policy

`[ 150 · paragraph]`

> • In continuous action spaces, a Gaussian policy is natural
> • Mean is a linear combination of state features µ(s) = ϕ(s)T θ
> • Variance may be fixed σ2, or can also parameterized
> • Policy is Gaussian a ∼ N(µ(s), σ2)
> • The score function is

`[ 151 · list]`

`[ 152 · paragraph]`

> • Deep neural networks (and other models where can compute
> the gradient) can also be used to represent the policy

`[ 153 · list]`


## Page 24

`[ 154 · paragraph]`

> Likelihood Ratio / Score Function Policy Gradient

`[ 155 · list]`

> • Putting this together
> • Goal is to find the policy parameters θ:

`[ 156 · paragraph]`

> • Approximate with empirical estimate for m sample paths under policy
> πθ using score function:

`[ 157 · equation]` *(base64 17536 chars attached)*

`[ 158 · list]`

`[ 159 · equation]` *(base64 49640 chars attached)*

`[ 160 · paragraph]`

> • Do not need to know dynamics model

`[ 161 · paragraph]`

> Emma Brunskill (CS234 Reinforcement Lear


## Page 25

`[ 162 · heading1]`

> Check Your Understanding: Score functions

`[ 163 · paragraph]`

> The likelihood ratio / score function policy gradient (select one):

`[ 164 · paragraph]`

> (a) requires reward functions that are differentiable
> (b) can only be used with Markov decision processes
> (c) Is useful mostly for infinite horizon tasks


## Page 26

`[ 165 · heading1]`

> Score Function Gradient Estimator: Intuition

`[ 166 · paragraph]`

> • Consider generic form of R(τ(i ))∇θ log P(τ(i ); θ): gˆi = f (xi )∇θ log p(xi |θ)
> • f (x) measures how good the sample x is.
> • Moving in the direction gˆi pushes up the logprob of the sample, in proportion to
> how good it is
> • Valid even if f (x) is discontinuous, and unknown, or sample space (containing x)
> is a discrete set

`[ 167 · list]`


## Page 27

`[ 168 · heading1]`

> Policy Gradient Theorem

`[ 169 · paragraph]`

> • Generalization: Provides a unified gradient form for various objective functions J, such as episodic
> reward or average reward.
> • Key Identity: Expresses the gradient of the overall performance as the expectation of the policy's
> score function weighted by the action-value Q.
> • Model-Free Advantage: Allows for policy optimization without requiring a transition dynamics model
> of the environment.
> • Intuition: Suggests adjusting policy parameters 𝜃 to increase the probability of actions that yield
> higher-than-average returns.

`[ 170 · list]`


## Page 28

`[ 171 · paragraph]`

> Why Policy Gradient is Noisy (High Variance)

`[ 172 · paragraph]`

> • Sample Dependency: Since the gradient is estimated using a limited number of sampled
> trajectories (m), the estimate ො𝑔 can deviate significantly from the true gradient ∇𝜃𝑉 𝜃 .

`[ 173 · paragraph]`

> • Full Trajectory Cumulative Reward: The update rule uses the total return 𝑅 𝜏 , which is a
> sum of many random rewards along a long path. Any small random variation in early
> transitions can lead to massive swings in the final cumulative reward.

`[ 174 · list]`

`[ 175 · list]`

`[ 176 · paragraph]`

> • Credit Assignment Problem: Every action in a trajectory is scaled by the same total reward
> 𝑅 𝜏 . This makes it hard to distinguish which specific action was actually responsible for a
> good or bad outcome.

`[ 177 · list]`

`[ 178 · list]`

> • Lack of Absolute Scale: Policy Gradient only cares about the relative increase in probabilities.
> Without a baseline, even a "bad" action that happened to get a slightly positive reward will
> have its probability increased, leading to erratic updates.


## Page 29

`[ 179 · paragraph]`

> How to Fix Noisy Policy Gradient?

`[ 180 · paragraph]`

> • Temporal structure (REINFORCE)
> • Baseline

`[ 181 · list]`
