# Parsed dump — job 7c14c626cff0

- Source: `7c14c626cff0_9. Policy Gradient (2).pdf`
- Elements: 140


## Page 1

`[   0 · paragraph]`

> REINFORCEMENT LEARNING

`[   1 · paragraph]`

> Lecture 9 – Policy Gradient (2)

`[   2 · paragraph]`

> Gyeongsik Moon

`[   3 · paragraph]`

> Visual Computing and AI Lab
> Korea University

`[   4 · footer]`

> Lecture credit: Emma Brunskill


## Page 2

`[   5 · paragraph]`

> 1. Fix PG with Temporal Structure

`[   6 · paragraph]`

> 2. Fix PG with Baseline

`[   7 · paragraph]`

> 3. Fix PG with Bootstrapping


## Page 3

`[   8 · paragraph]`

> 1. Fix PG with Temporal Structure


## Page 4

`[   9 · paragraph]`

> Likelihood Ratio / Score Function Policy Gradient

`[  10 · paragraph]`

> • Unbiased but very noisy
> • Fixes that can make it practical

`[  11 · paragraph]`

> • Temporal structure
> • Baseline
> • Use Bootstrapping instead of Monte Carlo

`[  12 · list]`

`[  13 · list]`


## Page 5

`[  14 · paragraph]`

> Why we introduce ‘Temporal Structure’?

`[  15 · paragraph]`

> We can eliminate the "noise" from future actions that have no
> causal link to that reward.


## Page 6

`[  16 · paragraph]`

> Policy Gradient: Use Temporal Structure

`[  17 · paragraph]`

> • Previously:

`[  18 · paragraph]`

> • We can repeat the same argument to derive the gradient estimator
> for a single reward term rt ′ .

`[  19 · paragraph]`

> • Causality Constraint: Current actions cannot affect past rewards; therefore,
> ∇𝜃 log 𝜋𝜃 𝑎𝑡 𝑠𝑡 should not be scaled by 𝑟𝑡′ where 𝑡 ′ < 𝑡.

`[  20 · equation]` *(base64 17612 chars attached)*

`[  21 · list]`

`[  22 · list]`

> • Irrelevant Noise Removal: By focusing on the gradient for a single reward
> term 𝑟𝑡 ′, we can eliminate the "noise" from future actions that have no causal
> link to that reward.

`[  23 · list]`

> • For example, ignore 𝑟0 log 𝜋 𝑎100 𝑠100


## Page 7

`[  24 · paragraph]`

> Policy Gradient: Use Temporal Structure

`[  25 · paragraph]`

> • Previously:

`[  26 · equation]` *(base64 23504 chars attached)*

`[  27 · paragraph]`

> • We can repeat the same argument to derive the gradient estimator
> for a single reward term rt ′ .

`[  28 · equation]` *(base64 17528 chars attached)*

`[  29 · equation]` *(base64 48408 chars attached)*

`[  30 · paragraph]`

> • Summing this formula over t, we obtain


## Page 8

`[  31 · header]`

> Policy Gradient: Use Temporal Structure

`[  32 · equation]` *(base64 31812 chars attached)*

`[  33 · paragraph]`

> • Reward-to-go (𝐺𝑡): The sum of rewards obtained starting from time 𝑡 (not from time 0) until
> the end of the trajectory.
> • Policy Gradient with Causality: Policy parameters are updated proportional to the score
> function ∇𝜃 log 𝜋𝜃
> • Variance Reduction: Significantly reduces noise in gradient estimation by discarding
> irrelevant past rewards that the current action cannot influence.

`[  34 · equation]` *(base64 18236 chars attached)*

`[  35 · equation]` *(base64 17624 chars attached)*


## Page 9

`[  36 · header]`

> Monte-Carlo Policy Gradient (REINFORCE)

`[  37 · paragraph]`

> Leverages likelihood ratio / score function and temporal structure

`[  38 · paragraph]`

> ∆θ t = α∇ θ log πθ (st, at )Gt

`[  39 · paragraph]`

> REINFORCE:
> Initialize policy parameters θ arbitrarily
> for each episode {s1, a1, r2, · · · , sT − 1, aT − 1, rT } ∼ πθ
> do for t = 1 to T − 1 do
> θ ← θ + α∇ θ log πθ(st, at )Gt
> endfor
> endfor
> return θ

`[  40 · paragraph]`

> Willia ms, R . J. (1992). Simple statistical gradient-following algorithm s for connectionist reinforcement lea rni ng. Machine Learning, 8(3), 229-256.


## Page 10

`[  41 · paragraph]`

> 2. Fix PG with Baseline


## Page 11

`[  42 · header]`

> Likelihood Ratio / Score Function Policy Gradient

`[  43 · paragraph]`

> • Unbiased but very noisy
> • Fixes that can make it practical

`[  44 · paragraph]`

> • Temporal structure
> • Baseline
> • Use Bootstrapping instead of Monte Carlo

`[  45 · list]`

`[  46 · list]`


## Page 12

`[  47 · heading1]`

> Why we introduce Baseline?

`[  48 · list]`

> • Variance Reduction: The primary goal is to lower the high variance of
> the policy gradient estimator, leading to more stable and faster
> convergence.

`[  49 · paragraph]`

> • Relative Performance Assessment: Shifts the focus from absolute
> reward values to relative advantages, reinforcing actions only if they
> perform better than the average expectation.

`[  50 · heading1]`

> Objectives of Introducing a Baseline 𝑏 𝑠

`[  51 · list]`

`[  52 · list]`

> • Balanced Gradients: Prevents the "all-positive reward" problem where
> every action probability increases regardless of its relative quality, by
> centering the learning signal.


## Page 13

`[  53 · paragraph]`

> Policy Gradient: Introduce Baseline

`[  54 · paragraph]`

> • Interpretation: increase logprob of action at proportionally to how
> much returns are better than expected

`[  55 · paragraph]`

> • Reduce variance by introducing a baseline b(s)

`[  56 · paragraph]`

> • For any choice of b, gradient estimator is unbiased.

`[  57 · list]`

`[  58 · list]`

> • Near optimal choice is the expected return,

`[  59 · list]`

`[  60 · list]`


## Page 14

`[  61 · header]`

> Baseline b(s) Does Not Introduce Bias–Derivation

`[  62 · paragraph]`

> (probability: sum to 1)
> (derivative of constant is zero)

`[  63 · equation]` *(base64 142708 chars attached)*


## Page 15

`[  64 · paragraph]`

> Baseline b(s) Does Not Introduce Bias–Derivation

`[  65 · paragraph]`

> • Policy Gradient Theorem
> • ∇𝐽 ≈ 𝔼 ∇ log 𝜋 ⋅ 𝐺
> • ∇𝐽 ≈ 𝔼 ∇ log 𝜋 ⋅ 𝐺 − 𝑏 = 𝔼 ∇ log 𝜋 ⋅ 𝐺 − 𝔼 ∇ log 𝜋 ⋅ 𝑏
> Original Direction Zero (0)

`[  66 · paragraph]`

> • Same Direction: Since 𝔼 ∇ log 𝜋 ⋅ 𝑏 = 0, the overall gradient direction
> (Expectation) remains identical to the original objective.
> • Lower Magnitude: Subtracting 𝑏 centers the learning signal around
> zero, reducing the absolute magnitude of the updates.
> • Stability: Smaller, centered updates mean the policy doesn't "over-
> correct" or swing wildly, leading to much faster and more reliable
> convergence.

`[  67 · list]`


## Page 16

`[  68 · heading1]`

> ”Vanilla” Policy Gradient Algorithm

`[  69 · paragraph]`

> From Lecture 8

`[  70 · equation]` *(base64 24292 chars attached)*

`[  71 · figure]` *(base64 133168 chars attached)*

> ![image](/image/placeholder)


## Page 17

`[  72 · heading1]`

> ”Vanilla” Policy Gradient Algorithm

`[  73 · list]`

> • Two-Network Architecture: Modern policy gradient methods
> typically maintain two separate functional approximators
> (often two distinct neural networks).
> • Policy Network (𝜋𝜃): Learns the best action strategy to
> maximize returns.
> • Value Network (𝑉𝜙 or 𝑏): Learns to estimate the expected
> return of the current state, serving as a stable baseline.
> • The Birth of Actor-Critic: This structure is the fundamental
> precursor to Actor-Critic methods, where the "Critic"
> (Baseline) evaluates the "Actor" (Policy).


## Page 18

`[  74 · header]`

> Choosing the Baseline: Value Functions

`[  75 · paragraph]`

> • Recall Q-function / state-action-value function:

`[  76 · paragraph]`

> • State-value function can serve as a great baseline


## Page 19

`[  77 · paragraph]`

> 3. Fix PG with Bootstrapping


## Page 20

`[  78 · header]`

> Likelihood Ratio / Score Function Policy Gradient

`[  79 · heading1]`

> • Policy gradient:

`[  80 · paragraph]`

> • Fixes that improve simplest estimator

`[  81 · paragraph]`

> • Temporal structure (shown in above equation)
> • Baseline (shown in above equation)
> • Use Bootstrapping instead of Monte Carlo

`[  82 · list]`


## Page 21

`[  83 · heading1]`

> Monte Carlo (MC) Sampling

`[  84 · list]`

> • Definition: A broad class of
> computational algorithms that rely on
> repeated random sampling to obtain
> numerical results.
> • Core Principle: It uses randomness to
> solve problems that might be
> deterministic in principle or too complex
> to solve analytically.
> • Law of Large Numbers: As the number
> of random samples increases, the
> average of the results converges to the
> true expected value.

`[  85 · chart]` *(base64 141864 chars attached)*

> ![image](/image/placeholder)
> - Chart Title: Monte Carlo Simulation for n
> - X-Axis: x
> - Y-Axis: y
> - Chart Type: line
> |  | -1.00 | -0.75 | -0.50 | -0.25 | 0.00 | 0.25 | 0.50 | 0.75 | 1.00 |
> | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
> | item_01 | 0.75No units specified | 0.25No units specified | 0.25No units specified | 0.25No units specified | 0.25No units specified | 0.25No units specified | 0.25No units specified | 0.25No units specified | 0.75No units specified |


## Page 22

`[  86 · heading1]`

> MC vs. TD

`[  87 · list]`

> • A method of estimating values by averaging the actual returns (𝐺𝑡) from
> multiple completed trajectories.
> • Learning occurs only after reaching the terminal state (𝑇).
> • Relies strictly on real experience, but suffers from High Variance due to
> cumulative noise.

`[  88 · paragraph]`

> • Temporal Difference (TD)

`[  89 · list]`

> • A method that updates value estimates based on other learned estimates,
> without waiting for the final outcome (Bootstrapping).
> • Learning occurs online at every single time step (𝑡) using 𝑟𝑡 + 𝛾𝑉 𝑠𝑡+1
> • Much more stable and efficient, though it introduces Bias during early
> learning phases.

`[  90 · heading1]`

> • Monte Carlo (MC)

`[  91 · list]`


## Page 23

`[  92 · paragraph]`

> Choosing the Target

`[  93 · paragraph]`

> • The Dilemma: We must choose between a noisy but truthful target
> (𝐺𝑡) and a stable but potentially "lying" target (Bootstrapping).
> • Monte Carlo (MC): High Variance, Zero Bias. Safe but painfully slow
> to converge.

`[  94 · list]`

`[  95 · paragraph]`

> • Summation of true rewards from states timesteps.
> • MC Target: 𝐺𝑡 = 𝑟𝑡 + 𝑟𝑡+1 + 𝑟𝑡+2 + ⋯

`[  96 · paragraph]`

> • Bootstrapping (TD): Low Variance, High Bias. Fast and stable, but
> risks converging to a wrong solution if the approximation is poor.

`[  97 · paragraph]`

> • Summation of true reward of a single timestep and function
> approximation
> • TD Target: 𝑟𝑡 + 𝛾𝑉 𝑠𝑡+1

`[  98 · list]`

`[  99 · list]`

`[ 100 · list]`

`[ 101 · paragraph]`

> • Function Approximation: Using a neural network to estimate values
> naturally introduces bias but is essential for handling large state
> spaces.

`[ 102 · list]`


## Page 24

`[ 103 · paragraph]`

> Actor-critic Methods

`[ 104 · paragraph]`

> • Estimate of V /Q is done by a critic

`[ 105 · list]`

> • Actor-critic methods maintain an explicit representation of policy and
> the value function, and update both

`[ 106 · list]`

> • A3C (Mnih et al. ICML 2016) is a very popular actor-critic method

`[ 107 · list]`


## Page 25

`[ 108 · heading1]`

> Policy Gradient Formulas with Value Functions

`[ 109 · paragraph]`

> • Recall:

`[ 110 · equation]` *(base64 46296 chars attached)*

`[ 111 · paragraph]`

> • Letting the baseline be an estimate of the value V , we can represent the
> gradient in terms of the state-action advantage function

`[ 112 · equation]` *(base64 26688 chars attached)*

`[ 113 · paragraph]`

> where the advantage function Aπ(s, a) = Qπ(s, a) − V π(s)


## Page 26

`[ 114 · paragraph]`

> Policy Gradient Formulas with Value Functions

`[ 115 · paragraph]`

> • From Returns to Estimates: Transitioning from empirical returns (𝐺𝑡)
> to learned value functions (𝑄 and 𝑉).
> • Actor-Critic Foundation: By replacing the raw return with a learned
> 𝑄-function, we move into the Actor-Critic framework.
> • Generalized Advantage: Expressing the gradient in terms of ෢𝐴𝜋 𝑠, 𝑎
> allows for more flexible and stable updates using Bootstrapping.

`[ 116 · list]`


## Page 27

`[ 117 · heading1]`

> Choosing the Target: N-step estimators

`[ 118 · paragraph]`

> Note that critic can select any blend between TD and MC estimators
> for the target to substitute for the true state-action value function.

`[ 119 · paragraph]`

> tRˆ(1) = rt + γV (st+1)
> tRˆ(2) = rt + γrt+ 1 + γ2V (st+2)
> tRˆ(inf) = rt + γrt + 1 + γ2rt+ 2 + · · ·

`[ 120 · paragraph]`

> · · ·

`[ 121 · paragraph]`

> If subtract baselines from the above, get advantage estimators

`[ 122 · paragraph]`

> tAˆ(1) = rt + γV (st+1)−V (st )
> tAˆ(inf) = rt + γrt+ 1 + γ2rt+ 1 + · · · − V (st)

`[ 123 · equation]` *(base64 14012 chars attached)*


## Page 28

`[ 124 · header]`

> Check Your Understanding: Blended Advantage Estimators

`[ 125 · paragraph]`

> If subtract baselines from the above, get advantage estimators

`[ 126 · paragraph]`

> tAˆ(1) = rt + γV (st+1)−V (st )
> tAˆ(inf) = rt + γrt+ 1 + γ2rt+ 1 + · · · − V (st)

`[ 127 · equation]` *(base64 13996 chars attached)*

`[ 128 · paragraph]`

> Emma Brunskill (CS234 Reinforcement Lear


## Page 29

`[ 129 · heading1]`

> ”Vanilla” Policy Gradient Algorithm

`[ 130 · figure]` *(base64 93808 chars attached)*

> ![image](/image/placeholder)

`[ 131 · paragraph]`

> Note, we can choose which blended estimator Aˆ n to use


## Page 30

`[ 132 · header]`

> Current Summary of Benefits of Policy-Based RL

`[ 133 · paragraph]`

> Advantages:

`[ 134 · paragraph]`

> • Better convergence properties
> • Effective in high-dimensional or continuous action spaces
> • Can learn stochastic policies

`[ 135 · list]`

`[ 136 · paragraph]`

> Disadvantages:

`[ 137 · list]`

`[ 138 · paragraph]`

> • Typically converge to a local rather than global optimum
> • Evaluating a policy can be inefficient and high variance
> (though baseline and temporal structure helps)

`[ 139 · list]`
