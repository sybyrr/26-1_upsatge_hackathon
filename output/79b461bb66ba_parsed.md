# Parsed dump — job 79b461bb66ba

- Source: `79b461bb66ba_Lec06 - Recurrent Neural Networks.pdf`
- Elements: 686


## Page 1

`[   0 · paragraph]`

> Natural Language Processing (COSE461)
> Recurrent Neural Networks

`[   1 · heading1]`

> Instructor:

`[   2 · paragraph]`

> Buru Chang, Ph.D.

`[   3 · paragraph]`

> Assistant Professor
> Dept. of Computer Science & Engineering
> Korea University, Seoul, South Korea

`[   4 · figure]` *(base64 38572 chars attached)*

> ![image](/image/placeholder)


## Page 2

`[   5 · paragraph]`

> Recurrent Neural Networks

`[   6 · paragraph]`

> Class Objective

`[   7 · paragraph]`

> Understanding recurrent neural networks (RNNs)

`[   8 · list]`

> - Recap: Neural Networks for NLP

`[   9 · list]`

> - Recurrent Neural Networks (RNNs)

`[  10 · paragraph]`

> Recommended reading textbook 9.1-9.3

`[  11 · list]`

> - RNN Variants
> Long Short-Term Memories (LSTMs)
> Gated Recurrent Unit (GRU)

`[  12 · footer]`

> Natural Language Processing (COSE461)


## Page 3

`[  13 · paragraph]`

> Recap: Neural Networks


## Page 4

`[  14 · paragraph]`

> Recurrent Neural Networks

`[  15 · heading1]`

> Neural Networks

`[  16 · heading1]`

> Feed-forward NNs

`[  17 · list]`

> - The units are connected with no cycles

`[  18 · list]`

> - The outputs from units in each layer are passed to units in the next higher layer

`[  19 · list]`

> - No outputs are passed back to lower layers

`[  20 · figure]` *(base64 128588 chars attached)*

> ![image](/image/placeholder)

`[  21 · paragraph]`

> Fully-connected (FC) layers:
> All the units from one layer are fully
> connected to every unit of the next layer

`[  22 · footer]`

> Natural Language Processing (COSE461)


## Page 5

`[  23 · header]`

> Recurrent Neural Networks

`[  24 · heading1]`

> Neural Networks

`[  25 · heading1]`

> Feed-forward NNs

`[  26 · list]`

> 1 1 1 1
> - ℎ1 = 𝑓 𝑤1,1 𝑥1 + 𝑤1,2 𝑥2 + 𝑤1,3 𝑥3
> 2 2 1 2 1 2 1 2 1 𝜎, 𝑡𝑎𝑛ℎ, or 𝑅𝑒𝐿𝑈
> - ℎ3 = 𝑓 𝑤3,1 ℎ1 + 𝑤3,2 ℎ2 + 𝑤3,3 ℎ3 + 𝑤3,4 ℎ4 non-linearity f:

`[  27 · figure]` *(base64 260828 chars attached)*

> ![image](/image/placeholder)
> 1 2
> ℎ1 ℎ1
> 𝑥1
> 1 2
> ℎ2 ℎ2
> 𝑦
> 𝑥2
> 1 2
> ℎ3 ℎ3
> 𝑥3
> 1 2
> ℎ4 ℎ4

`[  28 · footer]`

> Natural Language Processing (COSE461)


## Page 6

`[  29 · header]`

> Recurrent Neural Networks

`[  30 · paragraph]`

> Neural Networks
> Activation functions

`[  31 · chart]` *(base64 30584 chars attached)*

> ![image](/image/placeholder)
> - Chart Title: f(z) ==
> - Chart Type: bar
> |  | -6 | -4 | -2 | 0 | 2 | 4 | 6 |
> | --- | --- | --- | --- | --- | --- | --- | --- |
> | item_01 | 0.05 | 0.05 | 0.0 | 0.95 | 1.05 | 1.15 | 1.25 |

`[  32 · equation]` *(base64 17548 chars attached)*

`[  33 · chart]` *(base64 31364 chars attached)*

> ![image](/image/placeholder)
> - Chart Type: line
> |  | -3 | -2 | -1 | 0 | 1 | 2 | 3 |
> | --- | --- | --- | --- | --- | --- | --- | --- |
> | item_01 | 0.0 | 0.02 | 0.12 | 0.49 | 0.88 | 0.98 | 1.0 |
> | item_02 | 1.0 | 1.0 | 0.96 | 0.0 | 0.96 | 1.0 | 1.0 |

`[  34 · equation]` *(base64 23896 chars attached)*

`[  35 · chart]` *(base64 23964 chars attached)*

> ![image](/image/placeholder)
> - Chart Type: bar
> |  | -10 | -5 | 0 | 5 | 10 |
> | --- | --- | --- | --- | --- | --- |
> | item_01 | 0 | 0 | 0 | 6 | 8 |

`[  36 · equation]` *(base64 26212 chars attached)*

`[  37 · footer]`

> Natural Language Processing (COSE461)


## Page 7

`[  38 · paragraph]`

> Recurrent Neural Networks

`[  39 · paragraph]`

> Neural Networks

`[  40 · heading1]`

> Matrix notations

`[  41 · figure]` *(base64 143764 chars attached)*

> ![image](/image/placeholder)
> 1 2
> ℎ1 ℎ1
> 𝑥1
> 1 2
> ℎ2 ℎ2
> 𝑦
> 𝑥2
> 1 2
> ℎ3 ℎ3
> 𝑥3
> 1 2
> ℎ4 ℎ4

`[  42 · paragraph]`

> 𝑓 is applied element-wise
> 𝑓 𝑧1, 𝑧2, 𝑧3 = 𝑓 𝑧1 , 𝑓 𝑧2 , 𝑓 𝑧3
> 𝐶: number of classes
> 𝑑: input dimension, 𝑑1, 𝑑2: hidden dimensions

`[  43 · list]`

> - Input layer: 𝐱 ∈ ℝ𝑑

`[  44 · list]`

> - Hidden layer 1:
> 𝐡1 = 𝑓 𝐖 1 𝐱 + 𝐛 1 ∈ ℝ𝑑1
> 𝐖 1 ∈ ℝ𝑑1×𝑑, 𝐛 1 ∈ ℝ𝑑1

`[  45 · paragraph]`

> - Hidden layer 2:
> 𝐡2 = 𝑓 𝐖 2 𝐡1 + 𝐛 2 ∈ ℝ𝑑2
> 𝐖 2 ∈ ℝ𝑑2×𝑑1, 𝐛 2 ∈ ℝ𝑑2

`[  46 · paragraph]`

> - Output layer:
> 𝑦 = 𝐖 𝑜 𝐡2, 𝐖 𝑜 ∈ ℝ𝐶×𝑑2

`[  47 · footer]`

> Natural Language Processing (COSE461)


## Page 8

`[  48 · paragraph]`

> Recurrent Neural Networks

`[  49 · heading1]`

> Neural Networks

`[  50 · heading1]`

> Example: Feedforward NNs

`[  51 · paragraph]`

> 1
> - For 𝑥1 = 𝑥2 = 𝑥3 = 1, what is the value of ℎ1 ?

`[  52 · list]`

> (A) 0
> (B) -1
> (C) 1
> (D) 2

`[  53 · figure]` *(base64 120492 chars attached)*

> ![image](/image/placeholder)
> (Bias terms omitted in the next few slides)

`[  54 · footer]`

> Natural Language Processing (COSE461)


## Page 9

`[  55 · heading1]`

> Recurrent Neural Networks

`[  56 · paragraph]`

> Neural Networks

`[  57 · paragraph]`

> Feedforward NNs for multi-class classification

`[  58 · paragraph]`

> - 𝐲 = 𝐖 𝑜 𝐡2, 𝐖 𝑜 ∈ ℝ𝐶×𝑑2, 𝐲 = 𝑦1, 𝑦2, ⋯ , 𝑦𝐶

`[  59 · list]`

> exp 𝑦𝑘
> - ො𝐲 = 𝑠𝑜𝑓𝑡𝑚𝑎𝑥 𝐲 , 𝑠𝑜𝑓𝑡𝑚𝑎𝑥 𝐲 𝑘 = 𝐶
> σ𝑗=1 exp 𝑦𝑗

`[  60 · list]`

> - Training objective:

`[  61 · paragraph]`

> min Σ 𝐱,𝑦 ∈𝐷 log 𝐲𝑦 ො
> 𝐖 1 ,𝐖 2 ,𝐖 𝑜

`[  62 · paragraph]`

> - Training feedforward NNs:
> Stochastic gradient descent!

`[  63 · paragraph]`

> Neural networks are difficult to optimize.
> SGD can only converge to local minimum.
> Initializations and optimizers matter a lot!

`[  64 · footer]`

> Natural Language Processing (COSE461)


## Page 10

`[  65 · paragraph]`

> Recurrent Neural Networks

`[  66 · paragraph]`

> Neural Networks

`[  67 · heading1]`

> Backpropagation

`[  68 · figure]` *(base64 411172 chars attached)*

> ![image](/image/placeholder)

`[  69 · footer]`

> Natural Language Processing (COSE461)


## Page 11

`[  70 · heading1]`

> Recurrent Neural Networks

`[  71 · paragraph]`

> Neural Networks

`[  72 · paragraph]`

> Backpropagation in PyTorch

`[  73 · list]`

`[  74 · list]`

`[  75 · footer]`

> Natural Language Processing (COSE461)


## Page 12

`[  76 · paragraph]`

> Recurrent Neural Networks

`[  77 · paragraph]`

> Neural Networks

`[  78 · paragraph]`

> Comparison: Image vs text inputs

`[  79 · paragraph]`

> - Images: fixed-size input, continuous values

`[  80 · list]`

`[  81 · list]`

> - Text: variable-length input, discrete words
> Need to convert into vectors – word embeddings!

`[  82 · figure]` *(base64 219584 chars attached)*

> ![image](/image/placeholder)

`[  83 · footer]`

> Natural Language Processing (COSE461)


## Page 13

`[  84 · header]`

> Recurrent Neural Networks

`[  85 · heading1]`

> Neural Networks

`[  86 · heading1]`

> Neural networks for text classification

`[  87 · paragraph]`

> - Input: 𝑤1, 𝑤2, ⋯ , 𝑤𝑛 ∈ 𝑉
> ex) “dessert was great”

`[  88 · heading1]`

> - Output: 𝑦 ∈ 𝐶

`[  89 · paragraph]`

> ex) positive, 𝐶 = positive, negative, neutral

`[  90 · paragraph]`

> - Solution #1: You can construct a feature vector 𝐱 from the input and simply feed the vector to
> a neural network, instead of a logistic regression classifier

`[  91 · chart]` *(base64 107548 chars attached)*

> ![image](/image/placeholder)
> - Chart Type: line
> |  | dessert | wordcount | positive lexicon words | x | count of "no" |
> | --- | --- | --- | --- | --- | --- |
> | item_01 | 3 | 1 | 2 | 1 | 0 |

`[  92 · list]`

`[  93 · footer]`

> Natural Language Processing (COSE461)


## Page 14

`[  94 · header]`

> Recurrent Neural Networks

`[  95 · heading1]`

> Neural Networks

`[  96 · heading1]`

> Neural networks for text classification

`[  97 · paragraph]`

> - How can we feed a variable-length input to a neural network classifier?
> 𝑤1, 𝑤2, … , 𝑤𝑛 ∈ 𝑉

`[  98 · paragraph]`

> - Solution #2: Let’s take the all the word embeddings of these words and aggregate
> them into a vector through some pooling function!

`[  99 · figure]` *(base64 125924 chars attached)*

> ![image](/image/placeholder)
> 𝑛
> 1
> 𝐱𝑚𝑒𝑎𝑛 = ෍ 𝑒 𝑤𝑖
> 𝑛
> 𝑖 =1

`[ 100 · paragraph]`

> pooling: sum, mean or max

`[ 101 · list]`

`[ 102 · footer]`

> Natural Language Processing (COSE461)


## Page 15

`[ 103 · paragraph]`

> Recurrent Neural Networks

`[ 104 · paragraph]`

> Neural Networks

`[ 105 · paragraph]`

> How to train this model?

`[ 106 · list]`

> - Training data: 𝑑 1 , 𝑦 1 , ⋯ , 𝑑 𝑚 , 𝑦 𝑚

`[ 107 · list]`

> - Parameters: 𝐖, 𝐛, 𝐔

`[ 108 · list]`

> - Optimize these parameters using gradient descent

`[ 109 · list]`

> - Word embeddings can be treated as trainable parameters too
> 𝐄 ∈ ℝ 𝑉 ×𝑑

`[ 110 · figure]` *(base64 39776 chars attached)*

> ![image](/image/placeholder)

`[ 111 · footer]`

> Natural Language Processing (COSE461)


## Page 16

`[ 112 · heading1]`

> Recurrent Neural Networks

`[ 113 · paragraph]`

> Neural Networks

`[ 114 · paragraph]`

> How to train this model?

`[ 115 · paragraph]`

> - Common practice: initialize 𝐄 using word
> embeddings (e.g. word2vec), and optimize them
> using SGD!

`[ 116 · paragraph]`

> - When the training data is small, don’t treat 𝐄 as
> parameters!

`[ 117 · paragraph]`

> - When the training data is very large (e.g., language
> modeling), initialization doesn’t matter much either
> (= can use random initialization)

`[ 118 · footer]`

> Natural Language Processing (COSE461)


## Page 17

`[ 119 · paragraph]`

> Recurrent Neural Networks

`[ 120 · heading1]`

> Neural Networks
> How to train this model?

`[ 121 · figure]` *(base64 339688 chars attached)*

> ![image](/image/placeholder)
> - Common practice: initialize 𝐄 using word
> embeddings (e.g. word2vec), and optimize them
> using SGD!
> - When the training data is small, don’t treat 𝐄 as
> parameters!
> - When the training data is very large (e.g., language
> modeling), initialization doesn’t matter much either
> (= can use random initialization)

`[ 122 · footer]`

> Natural Language Processing (COSE461)


## Page 18

`[ 123 · heading1]`

> Recurrent Neural Networks

`[ 124 · paragraph]`

> Neural Networks

`[ 125 · paragraph]`

> How to train this model?

`[ 126 · paragraph]`

> - Common practice: initialize 𝐄 using word
> embeddings (e.g. word2vec), and optimize them
> using SGD!

`[ 127 · paragraph]`

> - When the training data is small, don’t treat 𝐄 as
> parameters!

`[ 128 · paragraph]`

> - When the training data is very large (e.g., language
> modeling), initialization doesn’t matter much either
> (= can use random initialization)

`[ 129 · footer]`

> Natural Language Processing (COSE461)


## Page 19

`[ 130 · paragraph]`

> Recurrent Neural Networks

`[ 131 · heading1]`

> Neural Networks

`[ 132 · heading1]`

> Deep Averaging Networks (DAN)

`[ 133 · heading1]`

> - Iyyer et al., ACL 2015

`[ 134 · chart]` *(base64 91988 chars attached)*

> ![image](/image/placeholder)
> - Chart Type: bar
> |  | Predator | C | C2 | C3 | C4 |
> | --- | --- | --- | --- | --- | --- |
> | item_01 | 1 | 1 | 2 | 3 | 2 |

`[ 135 · figure]` *(base64 91988 chars attached)*

> ![image](/image/placeholder)

`[ 136 · footer]`

> Natural Language Processing (COSE461)


## Page 20

`[ 137 · paragraph]`

> Recurrent Neural Networks

`[ 138 · heading1]`

> Neural Networks

`[ 139 · paragraph]`

> Neural networks for text classification

`[ 140 · list]`

> (+): This provides a simple and flexible way to handle variable-length input
> (+): It learns feature representations automatically from the data
> (+): It can generalize to similar inputs through word embeddings
> (-): The model throws away any sequential information of the text

`[ 141 · footer]`

> Natural Language Processing (COSE461)


## Page 21

`[ 142 · heading1]`

> Recurrent Neural Networks

`[ 143 · heading1]`

> Neural Networks

`[ 144 · paragraph]`

> N-gram vs neural language models

`[ 145 · paragraph]`

> - Language models: Given , the goal is to model:

`[ 146 · paragraph]`

> 𝑛 𝑃 𝑥𝑖 𝑥1, ⋯ , 𝑥𝑖−1
> 𝑃 𝑥1, 𝑥2, … , 𝑥𝑛 = Π𝑖=1

`[ 147 · list]`

> 𝑛 𝑃 𝑥𝑖 𝑥𝑖−1
> - Bigram: Trigram: 𝑃 𝑥1, 𝑥2, … , 𝑥𝑛 = Π𝑖=1

`[ 148 · list]`

> 𝑛 𝑃 𝑥𝑖 𝑥𝑖−2, 𝑥𝑖−1
> - Trigram: Trigram: 𝑃 𝑥1, 𝑥2, … , 𝑥𝑛 = Π𝑖=1

`[ 149 · list]`

> - Limitations: Can’t handle long histories

`[ 150 · paragraph]`

> As the proctor started the clock, the students opened their

`[ 151 · paragraph]`

> The keys to the cabinet is/are

`[ 152 · paragraph]`

> ______

`[ 153 · footer]`

> Natural Language Processing (COSE461)


## Page 22

`[ 154 · heading1]`

> Recurrent Neural Networks

`[ 155 · heading1]`

> Neural Networks

`[ 156 · heading1]`

> N-gram vs neural language models

`[ 157 · paragraph]`

> - If we use a 4-gram, 5-gram, 6-gram language model, it will become too sparse to
> estimate the probabilities:

`[ 158 · paragraph]`

> 𝑐𝑜𝑢𝑛𝑡(𝑠𝑡𝑢𝑑𝑒𝑛𝑡𝑠 𝑜𝑝𝑒𝑛𝑒𝑑 𝑡ℎ𝑒𝑖𝑟 𝑤)
> 𝑃 𝑤 𝑠𝑡𝑢𝑑𝑒𝑛𝑡𝑠 𝑜𝑝𝑒𝑛𝑒𝑑 𝑡ℎ𝑒𝑖𝑟 =
> 𝑐𝑜𝑢𝑛𝑡(𝑠𝑡𝑢𝑑𝑒𝑛𝑡 𝑜𝑝𝑒𝑛𝑒𝑑 𝑡ℎ𝑒𝑖𝑟)

`[ 159 · heading1]`

> - Dilemma:

`[ 160 · paragraph]`

> We need to model bigger context
> The # of probabilities that we need to estimate grow exponentially with widow size

`[ 161 · paragraph]`

> - A lot of contexts are similar and simply counting them won’t generalize

`[ 162 · paragraph]`

> I am a good _____ count (I am a good 𝑤)
> I am a great _____ count (I am a great 𝑤)

`[ 163 · paragraph]`

> e(good) ≈ e(great)

`[ 164 · footer]`

> Natural Language Processing (COSE461)


## Page 23

`[ 165 · header]`

> Recurrent Neural Networks

`[ 166 · heading1]`

> Neural Networks

`[ 167 · paragraph]`

> Feedforward neural language models

`[ 168 · figure]` *(base64 40880 chars attached)*

> ![image](/image/placeholder)

`[ 169 · footer]`

> Natural Language Processing (COSE461)


## Page 24

`[ 170 · paragraph]`

> Recurrent Neural Networks

`[ 171 · heading1]`

> Neural Networks

`[ 172 · heading1]`

> Feedforward neural language models

`[ 173 · figure]` *(base64 41540 chars attached)*

> ![image](/image/placeholder)

`[ 174 · paragraph]`

> - Key idea: Instead of estimating raw probabilities, let’s use a neural network to fit the
> probabilistic distribution of language!
> 𝑃 𝑤 𝐼 𝑎𝑚 𝑎 𝑔𝑜𝑜𝑑 ≅ 𝑃(𝑤|𝐼 𝑎𝑚 𝑎 𝑔𝑟𝑒𝑎𝑡)

`[ 175 · paragraph]`

> - Key ingredient: word embeddings 𝑒 𝑔𝑜𝑜𝑑 ≅ 𝑒(𝑔𝑟𝑒𝑎𝑡)
> Hope: this would give us similar distributions for similar contexts!

`[ 176 · footer]`

> Natural Language Processing (COSE461)


## Page 25

`[ 177 · heading1]`

> Recurrent Neural Networks

`[ 178 · paragraph]`

> Neural Networks

`[ 179 · heading1]`

> Feedforward neural language models

`[ 180 · paragraph]`

> - Feedforward neural language models approximate the probability based
> on the previous 𝑚 (e.g., 5) words - 𝑚 is a hyper-parameter!

`[ 181 · paragraph]`

> 𝑛

`[ 182 · paragraph]`

> 𝑖=1

`[ 183 · paragraph]`

> - 𝑃 𝑚𝑎𝑡 𝑡ℎ𝑒 𝑐𝑎𝑡 𝑠𝑎𝑡 𝑜𝑛 𝑡ℎ𝑒) = ?

`[ 184 · paragraph]`

> 𝑑: word embedding size
> ℎ: hidden size
> It is a |𝑉|-way classification problem

`[ 185 · paragraph]`

> 𝑃 𝑥1, 𝑥2, ⋯ , 𝑥𝑛 ≅ ෑ

`[ 186 · paragraph]`

> 𝑃 𝑥𝑖 𝑥𝑖−𝑚+1, ⋯ , 𝑥𝑖−1

`[ 187 · chart]` *(base64 70180 chars attached)*

> ![image](/image/placeholder)
> - Chart Type: line
> |  | Green | Red | Blue | Yellow |
> | --- | --- | --- | --- | --- |
> | item_01 | 1 | 2 | 3 | 4 |

`[ 188 · footer]`

> Natural Language Processing (COSE461)


## Page 26

`[ 189 · paragraph]`

> Recurrent Neural Networks

`[ 190 · paragraph]`

> Neural Networks

`[ 191 · heading1]`

> Feedforward neural language models

`[ 192 · paragraph]`

> - Input layer (𝑚 = 5):

`[ 193 · paragraph]`

> 𝐱 = 𝑒 𝑡ℎ𝑒 ; 𝑒 𝑐𝑎𝑡 ; 𝑒 𝑠𝑎𝑡 ; 𝑒 𝑜𝑛 ; 𝑒 𝑡ℎ𝑒 ∈ ℝ𝑚𝑑

`[ 194 · paragraph]`

> - Hidden layer:

`[ 195 · paragraph]`

> 𝐡 = tanh 𝐖𝐱 + 𝐛 ∈ ℝℎ

`[ 196 · paragraph]`

> - Output layer:

`[ 197 · paragraph]`

> 𝐳 = 𝐔𝐡 ∈ ℝ 𝑉

`[ 198 · paragraph]`

> - Probability:

`[ 199 · paragraph]`

> 𝑒 𝑧𝑖
> 𝑃 𝑤 = 𝑖 𝑡ℎ𝑒 𝑐𝑎𝑡 𝑠𝑎𝑡 𝑜𝑛 𝑡ℎ𝑒 = 𝑠𝑜𝑓𝑡𝑚𝑎𝑥 𝑧 𝑖 =
> σ𝑘 𝑒𝑧𝑘

`[ 200 · chart]` *(base64 90024 chars attached)*

> ![image](/image/placeholder)
> - Chart Type: line
> |  | Green | Red | Blue | Yellow |
> | --- | --- | --- | --- | --- |
> | item_01 | 1 | 1 | 1 | 1 |

`[ 201 · footer]`

> Natural Language Processing (COSE461)


## Page 27

`[ 202 · paragraph]`

> Recurrent Neural Networks

`[ 203 · paragraph]`

> Neural Networks

`[ 204 · paragraph]`

> Feedforward neural language models

`[ 205 · paragraph]`

> - What are the dimensions of 𝐖 and 𝐔?

`[ 206 · paragraph]`

> (A) 𝐖 ∈ ℝℎ×𝑑, 𝐔 ∈ ℝ 𝑉 ×ℎ

`[ 207 · list]`

> (B) 𝐖 ∈ ℝℎ×5𝑑, 𝐔 ∈ ℝ 𝑉 ×ℎ

`[ 208 · list]`

> (C) 𝐖 ∈ ℝℎ×5𝑑, 𝐔 ∈ ℝ 𝑉 ×𝑑

`[ 209 · list]`

> (D) 𝐖 ∈ ℝℎ×𝑑, 𝐔 ∈ ℝ𝑑×ℎ

`[ 210 · figure]` *(base64 126316 chars attached)*

> ![image](/image/placeholder)
> - Input layer (𝑚 = 5):
> 𝐱 = 𝑒 𝑡ℎ𝑒 ; 𝑒 𝑐𝑎𝑡 ; 𝑒 𝑠𝑎𝑡 ; 𝑒 𝑜𝑛 ; 𝑒 𝑡ℎ𝑒 ∈ ℝ𝑚𝑑
> - Hidden layer:
> 𝐡 = tanh 𝐖𝐱 + 𝐛 ∈ ℝℎ
> - Output layer:
> 𝐳 = 𝐔𝐡 ∈ ℝ 𝑉
> - Probability:
> 𝑒 𝑧𝑖
> 𝑃 𝑤 = 𝑖 𝑡ℎ𝑒 𝑐𝑎𝑡 𝑠𝑎𝑡 𝑜𝑛 𝑡ℎ𝑒 = 𝑠𝑜𝑓𝑡𝑚𝑎𝑥 𝑧 𝑖 =
> σ𝑘 𝑒𝑧𝑘

`[ 211 · footer]`

> Natural Language Processing (COSE461)


## Page 28

`[ 212 · paragraph]`

> Recurrent Neural Networks

`[ 213 · paragraph]`

> Neural Networks

`[ 214 · paragraph]`

> Feedforward neural language models

`[ 215 · paragraph]`

> - How to train this model? A: Use a lot of raw text to create training examples and run
> gradient-descent optimization!

`[ 216 · paragraph]`

> The Fat Cat Sat on the Mat is a 1996 children's
> book by Nurit Karlin. Published by Harper Collins as
> part of the reading readiness program, the book
> stresses the ability to read words of specific
> structure, such as -at.

`[ 217 · paragraph]`

> the fat cat sat on → the
> fat cat sat on the → mat
> cat sat on the mat → is
> sat on the mat is → a

`[ 218 · paragraph]`

> - Limitations:

`[ 219 · paragraph]`

> 𝐖 linearly scales with the context size 𝑚

`[ 220 · paragraph]`

> The models learn separate patterns for different positions

`[ 221 · paragraph]`

> the fat cat sat on → the
> fat cat sat on the → mat
> cat sat on the mat → is

`[ 222 · paragraph]`

> - Better solutions
> Recurrent NNs, Transformers, ..

`[ 223 · paragraph]`

> “sat on” corresponds to
> different parameters in 𝑊

`[ 224 · footer]`

> Natural Language Processing (COSE461)


## Page 29

`[ 225 · paragraph]`

> Recurrent Neural Networks


## Page 30

`[ 226 · header]`

> Recurrent Neural Networks

`[ 227 · heading1]`

> Recurrent Neural Networks (RNNs)

`[ 228 · paragraph]`

> Motivation

`[ 229 · paragraph]`

> - How can we model sequences using neural networks?

`[ 230 · figure]` *(base64 123076 chars attached)*

> ![image](/image/placeholder)

`[ 231 · paragraph]`

> - Recurrent neural networks = A class of neural networks used to model sequences, allowing
> to handle variable length inputs

`[ 232 · paragraph]`

> - Very crucial in NLP problems (different from images) because sentences/paragraphs are
> variable-length, sequential inputs

`[ 233 · footer]`

> Natural Language Processing (COSE461)


## Page 31

`[ 234 · heading1]`

> Recurrent Neural Networks

`[ 235 · paragraph]`

> Recurrent Neural Networks (RNNs)

`[ 236 · paragraph]`

> Motivation: n-gram vs neural language models

`[ 237 · paragraph]`

> - Language models: given 𝑥1, 𝑥2, ⋯ , 𝑥𝑛 ∈ 𝒱, the goal is to model
> 𝑛 𝑃 𝑥𝑖 𝑥1, ⋯ , 𝑥𝑖−1
> 𝑃 𝑥1, 𝑥2, ⋯ , 𝑥𝑛 = Π𝑖=1

`[ 238 · paragraph]`

> - N-gram models:

`[ 239 · paragraph]`

> 𝑐𝑜𝑢𝑛𝑡(the cat sat)
> 𝑃 sat the cat =
> 𝑐𝑜𝑢𝑛𝑡(the cat)

`[ 240 · heading1]`

> - Dilemma:

`[ 241 · paragraph]`

> We need to model bigger context
> The # of probabilities that we need to estimate grow exponentially with window size

`[ 242 · footer]`

> As the proctor started the clock, the students opened their

`[ 243 · paragraph]`

> ______

`[ 244 · footer]`

> Natural Language Processing (COSE461)


## Page 32

`[ 245 · header]`

> Recurrent Neural Networks

`[ 246 · heading1]`

> Recurrent Neural Networks (RNNs)

`[ 247 · paragraph]`

> Introduction

`[ 248 · paragraph]`

> - A family of neural networks that can handle variable length inputs

`[ 249 · figure]` *(base64 82896 chars attached)*

> ![image](/image/placeholder)

`[ 250 · paragraph]`

> - A function: 𝐲 = 𝑅𝑁𝑁 𝐱1, 𝐱2, … , 𝐱𝑛 ∈ ℝℎ where 𝐱1, 𝐱2, ⋯ , 𝐱𝑛 ∈ ℝ𝑑

`[ 251 · heading1]`

> Core idea: apply the same weights repeatedly at different positions

`[ 252 · footer]`

> Natural Language Processing (COSE461)


## Page 33

`[ 253 · header]`

> Recurrent Neural Networks

`[ 254 · heading1]`

> Recurrent Neural Networks (RNNs)

`[ 255 · paragraph]`

> Introduction

`[ 256 · paragraph]`

> - Highly effective approach for language modeling, sequence tagging, text
> classification

`[ 257 · heading1]`

> Language modeling

`[ 258 · figure]` *(base64 80992 chars attached)*

> ![image](/image/placeholder)

`[ 259 · paragraph]`

> Sequence tagging

`[ 260 · figure]` *(base64 58680 chars attached)*

> ![image](/image/placeholder)

`[ 261 · paragraph]`

> Text classification

`[ 262 · figure]` *(base64 28000 chars attached)*

> ![image](/image/placeholder)

`[ 263 · footer]`

> Natural Language Processing (COSE461)


## Page 34

`[ 264 · header]`

> Recurrent Neural Networks

`[ 265 · paragraph]`

> Recurrent Neural Networks (RNNs)

`[ 266 · paragraph]`

> Sequent-to-sequence models

`[ 267 · paragraph]`

> - Form the basis for the modern approaches to machine translation, question
> answering and dialogue systems:

`[ 268 · figure]` *(base64 47612 chars attached)*

> ![image](/image/placeholder)

`[ 269 · paragraph]`

> Sutskever et al., Sequence to Sequence Learning with Neural Networks (2014)

`[ 270 · footer]`

> Natural Language Processing (COSE461)


## Page 35

`[ 271 · heading1]`

> Recurrent Neural Networks

`[ 272 · heading1]`

> Recurrent Neural Networks (RNNs)

`[ 273 · paragraph]`

> Simple recurrent neural networks

`[ 274 · paragraph]`

> - A function: 𝐲 = 𝑅𝑁𝑁 𝐱1, 𝐱2, ⋯ , 𝐱𝑛 ∈ ℝℎ where 𝐱1, ⋯ , 𝐱𝑛 ∈ ℝ𝑑

`[ 275 · list]`

> 𝐡0 ∈ ℝℎ is an initial state
> 𝐡𝑡: hidden states which store information from 𝐱1 to 𝐱𝑡

`[ 276 · paragraph]`

> 𝐡𝑡 = 𝑓 𝐡𝑡−1, 𝐱𝑡 ∈ ℝℎ

`[ 277 · paragraph]`

> - Simple RNNs:

`[ 278 · paragraph]`

> 𝑔: nonlinearity (e.g., tanh, ReLU)

`[ 279 · paragraph]`

> 𝐖 ∈ ℝℎ×ℎ, 𝐔 ∈ ℝℎ×𝑑, 𝐛 ∈ ℝℎ
> 𝐡𝑡 = 𝑔 𝐖𝐡𝑡−1 + 𝐔𝐱𝑡 + 𝐛 ∈ ℝℎ

`[ 280 · footer]`

> Natural Language Processing (COSE461)


## Page 36

`[ 281 · header]`

> Recurrent Neural Networks

`[ 282 · paragraph]`

> Recurrent Neural Networks (RNNs)

`[ 283 · paragraph]`

> Simple recurrent neural networks

`[ 284 · paragraph]`

> - Key idea: apply the same weights 𝐖, 𝐔, 𝐛 repeatedly

`[ 285 · paragraph]`

> 𝐡𝑡 = 𝑔 𝐖𝐡𝑡−1 + 𝐔𝐱𝑡 + 𝐛 ∈ ℝℎ

`[ 286 · figure]` *(base64 108152 chars attached)*

> ![image](/image/placeholder)

`[ 287 · footer]`

> Natural Language Processing (COSE461)


## Page 37

`[ 288 · header]`

> Recurrent Neural Networks

`[ 289 · paragraph]`

> Recurrent Neural Networks (RNNs)

`[ 290 · heading1]`

> Feedforward NNs vs RNNs

`[ 291 · figure]` *(base64 47956 chars attached)*

> ![image](/image/placeholder)

`[ 292 · paragraph]`

> 𝐡1 = 𝑔 𝐖 1 𝐱 + 𝐛 1 ∈ ℝℎ1
> 𝐡2 = 𝑔 𝐖 2 𝐡1 + 𝐛 2 ∈ ℝℎ2

`[ 293 · figure]` *(base64 67828 chars attached)*

> ![image](/image/placeholder)

`[ 294 · paragraph]`

> 𝐡𝑡 = 𝑔 𝐖𝐡𝑡−1 + 𝐔𝐱𝑡 + 𝐛 ∈ ℝℎ

`[ 295 · footer]`

> Natural Language Processing (COSE461)


## Page 38

`[ 296 · paragraph]`

> Recurrent Neural Language Models (RNNLMs)


## Page 39

`[ 297 · header]`

> Recurrent Neural Networks

`[ 298 · heading1]`

> Recurrent Neural Language Models (RNNLMs)

`[ 299 · paragraph]`

> Formulation

`[ 300 · heading1]`

> - 𝑃 𝑤1, 𝑤2, ⋯ , 𝑤𝑛

`[ 301 · list]`

> = 𝑃 𝑤1 × 𝑃 𝑤2 𝑤1 × 𝑃 𝑤3 𝑤1, 𝑤2 × ⋯ × 𝑃 𝑤𝑛 𝑤1, 𝑤2, ⋯ , 𝑤𝑛−1
> = 𝑃 𝑤1 𝐡0 × 𝑃 𝑤2 𝐡1 × ⋯ 𝑃 𝑤𝑛 𝐡𝑛−1 No Markov assumption here

`[ 302 · figure]` *(base64 109980 chars attached)*

> ![image](/image/placeholder)

`[ 303 · paragraph]`

> Denote ො𝑦𝑡 = 𝑠𝑜𝑓𝑡𝑚𝑎𝑥 𝐖𝑜𝐡𝑡 , 𝐖𝑜 ∈ ℝ 𝒱 ×ℎ

`[ 304 · paragraph]`

> The probability of 𝑤2: ො𝑦1 𝑤2

`[ 305 · footer]`

> Natural Language Processing (COSE461)


## Page 40

`[ 306 · header]`

> Recurrent Neural Networks

`[ 307 · heading1]`

> Recurrent Neural Language Models (RNNLMs)

`[ 308 · paragraph]`

> Formulation

`[ 309 · paragraph]`

> - 𝑃 𝑤1, 𝑤2, ⋯ , 𝑤𝑛

`[ 310 · list]`

> = 𝑃 𝑤1 × 𝑃 𝑤2 𝑤1 × 𝑃 𝑤3 𝑤1, 𝑤2 × ⋯ × 𝑃 𝑤𝑛 𝑤1, 𝑤2, ⋯ , 𝑤𝑛−1
> = 𝑃 𝑤1 𝐡0 × 𝑃 𝑤2 𝐡1 × ⋯ 𝑃 𝑤𝑛 𝐡𝑛−1 No Markov assumption here

`[ 311 · figure]` *(base64 111928 chars attached)*

> ![image](/image/placeholder)

`[ 312 · paragraph]`

> 𝐡𝑡 = 𝑔 𝐖𝐡𝑡−1 + 𝐔𝐱𝑡 + 𝐛 ∈ ℝℎ
> ො = 𝑠𝑜𝑓𝑡𝑚𝑎𝑥 𝐖𝑜𝐡𝑡
> 𝑦𝑡

`[ 313 · list]`

`[ 314 · paragraph]`

> Training loss:

`[ 315 · figure]` *(base64 21364 chars attached)*

> ![image](/image/placeholder)
> 𝑛
> 1
> 𝐿 𝜃 = − ෍ log ො𝑦𝑡−1 𝑤𝑡
> 𝑛
> 𝑡 =1

`[ 316 · paragraph]`

> Trainable parameters:
> 𝜃 = 𝐖, 𝐔, 𝐛, 𝐖𝑜, 𝐄

`[ 317 · footer]`

> Natural Language Processing (COSE461)


## Page 41

`[ 318 · header]`

> Recurrent Neural Networks

`[ 319 · paragraph]`

> Recurrent Neural Language Models (RNNLMs)
> Weight tying

`[ 320 · paragraph]`

> - It works better empirically and becomes a common practice

`[ 321 · figure]` *(base64 114360 chars attached)*

> ![image](/image/placeholder)

`[ 322 · paragraph]`

> Word embeddings (= input embeddings)
> 𝐄 ∈ ℝ 𝒱 ×𝑑

`[ 323 · heading1]`

> Output layer

`[ 324 · paragraph]`

> 𝐖𝑜 ∈ ℝ 𝒱 ×ℎ

`[ 325 · paragraph]`

> If 𝑑 = ℎ, we can just merge 𝐸 and 𝑊𝑜:
> 𝑦𝑡 = 𝑠𝑜𝑓𝑡𝑚𝑎𝑥 𝐖𝑜𝐡𝑡 → 𝑠𝑜𝑓𝑡𝑚𝑎𝑥(𝐄𝑇𝐡𝑡)
> ො

`[ 326 · paragraph]`

> Trainable parameters:
> 𝜃 = 𝐖, 𝐔, 𝐛, 𝐄

`[ 327 · footer]`

> Natural Language Processing (COSE461)


## Page 42

`[ 328 · header]`

> Recurrent Neural Networks

`[ 329 · paragraph]`

> Recurrent Neural Language Models (RNNLMs)

`[ 330 · paragraph]`

> Progress on language models

`[ 331 · paragraph]`

> - On the Penn Treebank (PTB) dataset

`[ 332 · paragraph]`

> - Metric: perplexity

`[ 333 · paragraph]`

> Mikolov and Zweig,
> Context dependent recurrent neural network language model (2012)

`[ 334 · paragraph]`

> Yang et al.,
> Breaking the Softmax Bottleneck: A High-Rank RNN Language Model (2018)

`[ 335 · footer]`

> Natural Language Processing (COSE461)


## Page 43

`[ 336 · header]`

> Recurrent Neural Networks

`[ 337 · heading1]`

> Recurrent Neural Language Models (RNNLMs)

`[ 338 · paragraph]`

> Pros and cons

`[ 339 · paragraph]`

> - Advantages:

`[ 340 · paragraph]`

> Can process any length input
> Computation for step 𝑡 can (in theory) use information from many steps back
> Model size doesn’t increase for longer input context

`[ 341 · paragraph]`

> - Disadvantages:

`[ 342 · paragraph]`

> Recurrent computation is slow (can’t parallelize) Transformers
> In practice, difficult to access information from many steps back (optimization issue)

`[ 343 · paragraph]`

> We will see some advanced RNNs
> (e.g., LSTMs, GRUs)

`[ 344 · footer]`

> Natural Language Processing (COSE461)


## Page 44

`[ 345 · header]`

> Recurrent Neural Networks

`[ 346 · paragraph]`

> Recurrent Neural Language Models (RNNLMs)
> Training RNNLMs

`[ 347 · paragraph]`

> - Forward pass + backward pass (compute gradients)

`[ 348 · paragraph]`

> - Forward pass:

`[ 349 · paragraph]`

> 𝐿 = 0, 𝐡0 = 0
> for 𝑡 = 1,2, ⋯ , 𝑛

`[ 350 · paragraph]`

> 𝑦 = − log 𝑠𝑜𝑓𝑡𝑚𝑎𝑥 𝐖𝑜𝐡𝑡−1 𝑤𝑡
> 𝐱𝑡 = 𝑒 𝑤𝑡
> 𝐡𝑡 = 𝑔 𝐖𝐡𝑡−1 + 𝐔𝐱𝑡 + 𝐛
> 1
> 𝐿 = 𝐿 + 𝑦
> 𝑛

`[ 351 · footer]`

> accumulate loss

`[ 352 · footer]`

> Natural Language Processing (COSE461)


## Page 45

`[ 353 · header]`

> Recurrent Neural Networks

`[ 354 · paragraph]`

> Recurrent Neural Language Models (RNNLMs)
> What is the running time of a forward pass?

`[ 355 · paragraph]`

> - What is the running time of a forward pass?

`[ 356 · list]`

> (A) 𝑂 ℎ × 𝑑 + ℎ + 𝒱
> (B) 𝑂 𝑛 × ℎ × 𝑑 + ℎ + 𝒱
> (C) 𝑂 𝑛 × 𝑑 + ℎ + 𝒱
> (D) 𝑂 𝑛 × ℎ × 𝑑 + ℎ

`[ 357 · paragraph]`

> 𝐿 = 0, 𝐡0 = 0
> for 𝑡 = 1,2, ⋯ , 𝑛

`[ 358 · paragraph]`

> 𝑦 = − log 𝑠𝑜𝑓𝑡𝑚𝑎𝑥 𝐖𝑜𝐡𝑡−1 𝑤𝑡

`[ 359 · paragraph]`

> 𝐱𝑡 = 𝑒 𝑤𝑡

`[ 360 · paragraph]`

> 1

`[ 361 · paragraph]`

> 𝐿 = 𝐿 + 𝑦

`[ 362 · paragraph]`

> 𝑛

`[ 363 · paragraph]`

> 𝐡𝑡 = 𝑔 𝐖𝐡𝑡−1 + 𝐔𝐱𝑡 + 𝐛

`[ 364 · paragraph]`

> 𝑛=number of time steps
> ℎ=hidden dimension
> 𝑑=word vector dimension
> 𝒱=output vocabulary

`[ 365 · footer]`

> Natural Language Processing (COSE461)


## Page 46

`[ 366 · header]`

> Recurrent Neural Networks

`[ 367 · paragraph]`

> Recurrent Neural Language Models (RNNLMs)
> Training RNNLMs

`[ 368 · paragraph]`

> - Backward pass:
> Backpropagation? Yes, but not that simple

`[ 369 · figure]` *(base64 173736 chars attached)*

> ![image](/image/placeholder)

`[ 370 · paragraph]`

> - The algorithm is called Backpropagation Through Time (BPTT)

`[ 371 · footer]`

> Natural Language Processing (COSE461)


## Page 47

`[ 372 · header]`

> Recurrent Neural Networks

`[ 373 · paragraph]`

> Recurrent Neural Language Models (RNNLMs)
> Backpropagation through time

`[ 374 · paragraph]`

> - 𝐡1 = 𝑔 𝐖𝐡0 + 𝐔𝐱1 + 𝐛 , 𝐡2 = 𝑔 𝐖𝐡1 + 𝐔𝐱2 + 𝐛 , 𝐡3 = 𝑔 𝐖𝐡2 + 𝐔𝐱3 + 𝐛
> 𝑦3 = 𝑠𝑜𝑓𝑡𝑚𝑎𝑥 𝐖𝑜𝐡3 → 𝐿3 = − log ො𝐲3 𝑤4
> ො

`[ 375 · paragraph]`

> 𝜕𝐿3
> - First, compute gradient with respect to hidden vector of last time step:
> 𝜕𝐡3

`[ 376 · table]` *(base64 45956 chars attached)*

> | 𝜕𝐿3 = | 𝜕𝐿3 𝜕𝐡3 | 𝜕𝐿3 𝜕𝐡3 𝜕𝐡2 + + | 𝜕𝐿3 𝜕𝐡3 𝜕𝐡2 𝜕𝐡1 |
> | --- | --- | --- | --- |
> | 𝜕𝐖 | 𝜕𝐡3 𝜕𝐖 | 𝜕𝐡3 𝜕𝐡2 𝜕𝐖 | 𝜕𝐡3 𝜕𝐡2 𝜕𝐡1 𝜕𝐖 |

`[ 377 · footer]`

> Natural Language Processing (COSE461)


## Page 48

`[ 378 · header]`

> Recurrent Neural Networks

`[ 379 · paragraph]`

> Recurrent Neural Language Models (RNNLMs)
> Backpropagation through time

`[ 380 · paragraph]`

> - More generally,

`[ 381 · table]` *(base64 39528 chars attached)*

> | 𝜕𝐿 | 𝑛 𝑡 1 𝜕𝐿𝑡 𝑡 𝜕𝐡𝑗 𝜕𝐡𝑘 = − ෍ ෍ Π𝑗=𝑘+1 |
> | --- | --- |
> | 𝜕𝐖 | 𝑛 𝜕𝐡𝑡 𝜕𝐡𝑗−1 𝜕𝐖 𝑡 =1 𝑘 =1 |

`[ 382 · paragraph]`

> - If 𝑘 and 𝑡 are far wary, the gradients can grow/shrink exponentially (called the
> gradient exploding or gradient vanishing problem)

`[ 383 · footer]`

> Natural Language Processing (COSE461)


## Page 49

`[ 384 · header]`

> Recurrent Neural Networks

`[ 385 · paragraph]`

> Recurrent Neural Language Models (RNNLMs)
> What if gradients become too large or small?

`[ 386 · paragraph]`

> - What if gradients become too large or small?

`[ 387 · list]`

> (A) If too large, the model will become difficult to converge
> (B) If too small, the model can’t capture long-term dependencies
> (C) If too small, the model may capture a wrong recent dependency
> (D) All of the above

`[ 388 · footer]`

> Natural Language Processing (COSE461)


## Page 50

`[ 389 · paragraph]`

> Recurrent Neural Networks

`[ 390 · paragraph]`

> Recurrent Neural Language Models (RNNLMs)

`[ 391 · paragraph]`

> Backpropagation through time

`[ 392 · paragraph]`

> - One solution for gradient exploding is called gradient clipping
> If the norm of the gradient is greater than some threshold, scale it down before applying
> SGD update.

`[ 393 · paragraph]`

> Algorithm 1 Pseudo-code for norm clipping
> 𝜕𝜀
> ො ←
> 𝐠
> 𝜕𝜃
> if 𝐠 ො ≥ 𝑡ℎ𝑟𝑒𝑠ℎ𝑜𝑙𝑑 then
> 𝑡ℎ𝑟𝑒𝑠ℎ𝑜𝑙𝑑
> ො ← 𝐠 ො
> 𝐠
> ||ො𝐠||
> end if

`[ 394 · paragraph]`

> Intuition: take a step in the same direction but a smaller step!

`[ 395 · paragraph]`

> - Gradient vanishing is a harder problem to solve

`[ 396 · footer]`

> Natural Language Processing (COSE461)


## Page 51

`[ 397 · header]`

> Recurrent Neural Networks

`[ 398 · paragraph]`

> Recurrent Neural Language Models (RNNLMs)

`[ 399 · paragraph]`

> Truncated backpropagation through time

`[ 400 · paragraph]`

> - Backpropagation is very expensive if you handle long sequences

`[ 401 · figure]` *(base64 104060 chars attached)*

> ![image](/image/placeholder)

`[ 402 · paragraph]`

> - Run forward and backward through chunks of the sequence instead of whole sequence

`[ 403 · paragraph]`

> - Carry hidden states forward in time forever, but only back-propagate for some smaller
> number of steps

`[ 404 · footer]`

> Natural Language Processing (COSE461)


## Page 52

`[ 405 · paragraph]`

> Application and Variants


## Page 53

`[ 406 · heading1]`

> Recurrent Neural Networks

`[ 407 · paragraph]`

> Applications and Variants

`[ 408 · paragraph]`

> Application: Text generation

`[ 409 · paragraph]`

> - You can generate text by repeated sampling

`[ 410 · paragraph]`

> - Sampled output is next step’s input

`[ 411 · figure]` *(base64 125880 chars attached)*

> ![image](/image/placeholder)

`[ 412 · footer]`

> Natural Language Processing (COSE461)


## Page 54

`[ 413 · header]`

> Recurrent Neural Networks

`[ 414 · paragraph]`

> Applications and Variants

`[ 415 · paragraph]`

> Application: Text generation

`[ 416 · paragraph]`

> - You can train an RNN-LM on any kind of text, then generate text in that style

`[ 417 · paragraph]`

> Latex text

`[ 418 · footer]`

> Natural Language Processing (COSE461)


## Page 55

`[ 419 · header]`

> Recurrent Neural Networks

`[ 420 · paragraph]`

> Applications and Variants

`[ 421 · heading1]`

> Application: Text generation

`[ 422 · paragraph]`

> - You can train an RNN-LM on any kind of text, then generate text in that style

`[ 423 · figure]` *(base64 58456 chars attached)*

> ![image](/image/placeholder)

`[ 424 · footer]`

> Natural Language Processing (COSE461)

`[ 425 · footer]`

> President speech


## Page 56

`[ 426 · paragraph]`

> Recurrent Neural Networks

`[ 427 · paragraph]`

> Applications and Variants

`[ 428 · paragraph]`

> Application: Sequence tagging

`[ 429 · paragraph]`

> - Input: a sentence of 𝑛 words: 𝑥1, ⋯ , 𝑥𝑛

`[ 430 · figure]` *(base64 139928 chars attached)*

> ![image](/image/placeholder)

`[ 431 · paragraph]`

> 1 𝑛 log 𝑃 𝑦𝑖 = 𝑘
> - 𝑃 𝑦𝑖 = 𝑘 = 𝑠𝑜𝑓𝑡𝑚𝑎𝑥𝑘 𝐖𝑜𝐡𝑖 𝐖𝑜 ∈ ℝ𝐶×ℎ 𝐿 = − σ𝑖=1
> 𝑛

`[ 432 · footer]`

> Natural Language Processing (COSE461)


## Page 57

`[ 433 · paragraph]`

> Recurrent Neural Networks

`[ 434 · paragraph]`

> Applications and Variants

`[ 435 · paragraph]`

> Application: Text classification

`[ 436 · list]`

> - Input: a sentence of 𝑛 words: 𝑥1, ⋯ , 𝑥𝑛
> - Output: 𝑦 ∈ 1,2, ⋯ , 𝐶

`[ 437 · figure]` *(base64 86092 chars attached)*

> ![image](/image/placeholder)

`[ 438 · paragraph]`

> - 𝑃 𝑦 = 𝑘 = 𝑠𝑜𝑓𝑡𝑚𝑎𝑥𝑘 𝐖𝑜𝐡𝑛 𝐖𝑜 ∈ ℝ𝐶×ℎ 𝐿 = − log 𝑃 𝑦 = 𝑐

`[ 439 · footer]`

> Natural Language Processing (COSE461)


## Page 58

`[ 440 · heading1]`

> Recurrent Neural Networks

`[ 441 · paragraph]`

> Applications and Variants

`[ 442 · heading1]`

> Multi-layer RNNs

`[ 443 · paragraph]`

> - RNNs are already “deep” on one dimension (unroll over time steps)

`[ 444 · paragraph]`

> - We can also make them “deep” in another dimension by applying multiple RNNs

`[ 445 · paragraph]`

> - Multi-layer RNNs are also called stacked RNNs

`[ 446 · footer]`

> Natural Language Processing (COSE461)

`[ 447 · list]`

`[ 448 · list]`


## Page 59

`[ 449 · paragraph]`

> Recurrent Neural Networks

`[ 450 · heading1]`

> Applications and Variants

`[ 451 · paragraph]`

> Multi-layer RNNs

`[ 452 · paragraph]`

> - The hidden states from RNN layer 𝑖 are inputs to RNN layer 𝑖 + 1

`[ 453 · figure]` *(base64 112516 chars attached)*

> ![image](/image/placeholder)

`[ 454 · list]`

> - In practice, using 2 to 4 layers is common (usually better than 1 layer)
> - Transformer networks can be up to 24 layers with lots of skip-connections

`[ 455 · footer]`

> Natural Language Processing (COSE461)


## Page 60

`[ 456 · header]`

> Recurrent Neural Networks

`[ 457 · paragraph]`

> Applications and Variants

`[ 458 · heading1]`

> Bidirectional RNNs

`[ 459 · paragraph]`

> - Bidirectionality is important in language representations:

`[ 460 · figure]` *(base64 71288 chars attached)*

> ![image](/image/placeholder)

`[ 461 · paragraph]`

> “terribly”:

`[ 462 · list]`

> - left context “the movie was”
> - right context “exciting !”

`[ 463 · footer]`

> Natural Language Processing (COSE461)


## Page 61

`[ 464 · header]`

> Recurrent Neural Networks

`[ 465 · paragraph]`

> Applications and Variants

`[ 466 · heading1]`

> Bidirectional RNNs

`[ 467 · paragraph]`

> - Bidirectionality is important in language representations:

`[ 468 · figure]` *(base64 141540 chars attached)*

> ![image](/image/placeholder)

`[ 469 · heading1]`

> 𝐡𝑡 = 𝑓 𝐡𝑡−1, 𝐱𝑡 ∈ ℝℎ

`[ 470 · paragraph]`

> Ԧ 𝑥𝑡 , 𝑡 = 1,2, ⋯ , 𝑛
> Ԧ 𝐡𝑡 = 𝑓1 𝐡𝑡−1,
> ശ 𝐡𝑡 = 𝑓2 𝐡𝑡−1, 𝑥𝑡 , 𝑡 = 𝑛, 𝑛 − 1, ⋯ , 1
> ശ
> 𝐡𝑡 = Ԧ𝐡𝑡; ശ𝐡𝑡 ∈ ℝ2ℎ

`[ 471 · equation]` *(base64 33000 chars attached)*

`[ 472 · footer]`

> Natural Language Processing (COSE461)


## Page 62

`[ 473 · heading1]`

> Recurrent Neural Networks

`[ 474 · heading1]`

> Applications and Variants

`[ 475 · heading1]`

> When can we use bidirectional RNNs?

`[ 476 · paragraph]`

> - Can we use bidirectional RNNs in the following tasks?

`[ 477 · paragraph]`

> (1) text classification, (2) sequence tagging, (3) text generation?

`[ 478 · list]`

`[ 479 · list]`

> (A) Yes, Yes, Yes
> (B) Yes, No, Yes
> (C) Yes, Yes, No
> (D) No, Yes, No

`[ 480 · footer]`

> Natural Language Processing (COSE461)


## Page 63

`[ 481 · header]`

> Recurrent Neural Networks

`[ 482 · paragraph]`

> Applications and Variants

`[ 483 · paragraph]`

> When can we use bidirectional RNNs?

`[ 484 · paragraph]`

> - Can we use bidirectional RNNs in the following tasks?

`[ 485 · paragraph]`

> Sequence tagging: Yes (especially, important)

`[ 486 · figure]` *(base64 104180 chars attached)*

> ![image](/image/placeholder)

`[ 487 · footer]`

> Natural Language Processing (COSE461)


## Page 64

`[ 488 · paragraph]`

> Recurrent Neural Networks

`[ 489 · paragraph]`

> Applications and Variants

`[ 490 · paragraph]`

> When can we use bidirectional RNNs?

`[ 491 · paragraph]`

> - Can we use bidirectional RNNs in the following tasks?

`[ 492 · paragraph]`

> Text classification: Yes

`[ 493 · paragraph]`

> Common practice: concatenate the last hidden vectors in two directions or take the
> mean/max over all the hidden vectors

`[ 494 · figure]` *(base64 136624 chars attached)*

> ![image](/image/placeholder)

`[ 495 · paragraph]`

> Text generation: No. Because we can’t see the future to predict next word

`[ 496 · footer]`

> Natural Language Processing (COSE461)


## Page 65

`[ 497 · heading1]`

> Recurrent Neural Networks

`[ 498 · paragraph]`

> Applications and Variants

`[ 499 · heading1]`

> A note on terminology

`[ 500 · paragraph]`

> - Simple RNNs are also called vanilla RNNs

`[ 501 · figure]` *(base64 5756 chars attached)*

> ![image](/image/placeholder)

`[ 502 · paragraph]`

> - Sometimes vanilla RNNs don’t work that well, so we need to use some advanced
> RNN variants such as LSTM or GRUs

`[ 503 · figure]` *(base64 10612 chars attached)*

> ![image](/image/placeholder)

`[ 504 · paragraph]`

> - In practice, we generally use multi-layer RNNs

`[ 505 · figure]` *(base64 17308 chars attached)*

> ![image](/image/placeholder)

`[ 506 · paragraph]`

> - Together with fancy ingredients such as residual connections with self-attention,

`[ 507 · paragraph]`

> variational dropout, …

`[ 508 · figure]` *(base64 41396 chars attached)*

> ![image](/image/placeholder)

`[ 509 · footer]`

> Natural Language Processing (COSE461)


## Page 66

`[ 510 · paragraph]`

> Long Short-Term Memory RNNs (LSTMs)


## Page 67

`[ 511 · header]`

> Recurrent Neural Networks

`[ 512 · paragraph]`

> Long Short-Term Memory RNNs (LSTMs)

`[ 513 · paragraph]`

> Introduction

`[ 514 · paragraph]`

> - A type of RNN proposed by Hochreiter and Schmidhuber in 1997 as a solution to the
> vanishing gradients problem

`[ 515 · paragraph]`

> Everyone cites that paper but really a crucial part of the modern LSTM is from Gers et al.
> (2000)

`[ 516 · footer]`

> Natural Language Processing (COSE461)


## Page 68

`[ 517 · header]`

> Recurrent Neural Networks

`[ 518 · paragraph]`

> Long Short-Term Memory RNNs (LSTMs)

`[ 519 · paragraph]`

> Motivation: Vanishing gradient problem

`[ 520 · paragraph]`

> - 𝐡1 = 𝑔 𝐖𝐡0 + 𝐔𝐱1 + 𝐛 , 𝐡2 = 𝑔 𝐖𝐡1 + 𝐔𝐱2 + 𝐛 , 𝐡3 = 𝑔 𝐖𝐡2 + 𝐔𝐱3 + 𝐛
> ො = 𝑠𝑜𝑓𝑡𝑚𝑎𝑥 𝐖𝑜𝐡3 → 𝐿3 = − log ො𝐲3 𝑤4
> 𝑦3

`[ 521 · paragraph]`

> 𝜕𝐿3
> - First, compute gradient with respect to hidden vector of last time step:
> 𝜕𝐡3

`[ 522 · figure]` *(base64 152152 chars attached)*

> ![image](/image/placeholder)
> 𝜕𝐿3 𝜕𝐿3 𝜕𝐡3 𝜕𝐿3 𝜕𝐡3 𝜕𝐡2 𝜕𝐿3 𝜕𝐡3 𝜕𝐡2 𝜕𝐡1
> = + +
> 𝜕𝐖 𝜕𝐡3 𝜕𝐖 𝜕𝐡3 𝜕𝐡2 𝜕𝐖 𝜕𝐡3 𝜕𝐡2 𝜕𝐡1 𝜕𝐖
> Vanishing gradient problem:
> when these are small, the gradient signal
> gets smaller and smaller as it
> backpropagates further

`[ 523 · footer]`

> Natural Language Processing (COSE461)


## Page 69

`[ 524 · header]`

> Recurrent Neural Networks

`[ 525 · paragraph]`

> Long Short-Term Memory RNNs (LSTMs)

`[ 526 · paragraph]`

> Motivation: Vanishing gradient problem

`[ 527 · figure]` *(base64 70812 chars attached)*

> ![image](/image/placeholder)

`[ 528 · paragraph]`

> - Gradient signal from far away is lost because it’s much small than gradient signal

`[ 529 · heading1]`

> from close-by

`[ 530 · paragraph]`

> - So, model weights are basically updated only with respect to near effects, not

`[ 531 · heading1]`

> long-term effects

`[ 532 · footer]`

> Natural Language Processing (COSE461)


## Page 70

`[ 533 · header]`

> Recurrent Neural Networks

`[ 534 · heading1]`

> Long Short-Term Memory RNNs (LSTMs)

`[ 535 · paragraph]`

> Introduction

`[ 536 · paragraph]`

> - Key idea: turning multiplication into addition and using “gates” to control how
> much information to add/erase

`[ 537 · paragraph]`

> - At each time step, instead of re-writing the hidden state 𝐡𝑡 = 𝑔 𝐖𝐡𝑡−1 + 𝐔𝐱𝑡 + 𝐛 ,
> there is also a cell state 𝐜𝑡 ∈ ℝℎ which stores long-term information

`[ 538 · paragraph]`

> We write to/erase information from 𝐜𝑡 after each step
> We read 𝐡𝑡 from 𝐜𝑡

`[ 539 · figure]` *(base64 55344 chars attached)*

> ![image](/image/placeholder)
> Natural Language Processing (COSE461)

`[ 540 · chart]` *(base64 55344 chars attached)*

> ![image](/image/placeholder)
> - X-Axis: x_t
> - Chart Type: line
> |  | c_t-1 | h_t-1 | stack | t_t |
> | --- | --- | --- | --- | --- |
> | item_01 | 1Not specified | 1Not specified | 9Not specified | 1Not specified |


## Page 71

`[ 541 · header]`

> Recurrent Neural Networks

`[ 542 · paragraph]`

> Long Short-Term Memory RNNs (LSTMs)

`[ 543 · paragraph]`

> Formulation

`[ 544 · paragraph]`

> - Input gate (how much to write)

`[ 545 · paragraph]`

> 𝐢𝑡 = 𝜎 𝐖𝑖𝐡𝑡−1 + 𝐔𝑖𝐱𝑡 + 𝐛𝑖 ∈ ℝℎ

`[ 546 · paragraph]`

> - Forget gate (how much to erase)

`[ 547 · paragraph]`

> 𝐟𝑡 = 𝜎 𝐖𝑓𝐡𝑡−1 + 𝐔𝑓𝐱𝑡 + 𝐛𝑓 ∈ ℝℎ

`[ 548 · paragraph]`

> - Output gate (how much to reveal)

`[ 549 · paragraph]`

> 𝐨𝑡 = 𝜎 𝐖𝑜𝐡𝑡−1 + 𝐔𝑜𝐱𝑡 + 𝐛𝑜 ∈ ℝℎ

`[ 550 · paragraph]`

> - New memory cell (what to write)

`[ 551 · paragraph]`

> 𝐠𝑡 = tanh 𝐖𝑔𝐡𝑡−1 + 𝐔𝐠𝐱𝑡 + 𝐛𝐠 ∈ ℝℎ

`[ 552 · paragraph]`

> - Final memory cell

`[ 553 · paragraph]`

> 𝐜𝑡 = 𝐜𝑡−1 ⊙ 𝐟𝑡 + 𝐠𝑡 ⊙ 𝐢𝑡

`[ 554 · paragraph]`

> - Final hidden cell

`[ 555 · paragraph]`

> 𝐡𝑡 = tanh 𝐜𝑡 ⊙ 𝐨𝑡

`[ 556 · figure]` *(base64 65744 chars attached)*

> ![image](/image/placeholder)

`[ 557 · paragraph]`

> 𝐡0, 𝐜0 ∈ ℝℎ are initial states (usually set to 0)

`[ 558 · paragraph]`

> element-wise product

`[ 559 · footer]`

> Natural Language Processing (COSE461)


## Page 72

`[ 560 · header]`

> Recurrent Neural Networks

`[ 561 · paragraph]`

> Long Short-Term Memory RNNs (LSTMs)

`[ 562 · paragraph]`

> Formulation

`[ 563 · paragraph]`

> - LSTMs has 4x parameters compared to simple RNNs:

`[ 564 · paragraph]`

> 𝐡𝑡 = 𝑔 𝐖𝐡𝑡−1 + 𝐔𝐱𝑡 + 𝐛 ∈ ℝℎ

`[ 565 · figure]` *(base64 47480 chars attached)*

> ![image](/image/placeholder)
> 𝐖 ∈ ℝℎ×ℎ, 𝐔 ∈ ℝℎ×𝑑, 𝐛 ∈ ℝℎ
> 𝐖𝑖, 𝐖𝑓, 𝐖𝑔, 𝐖𝑜 ∈ ℝℎ×ℎ
> 𝐔𝑖, 𝐔𝑓, 𝐔𝑔, 𝐔𝑜 ∈ ℝℎ×𝑑
> 𝐛𝑖, 𝐛𝑓, 𝐛𝑔, 𝐛𝑜 ∈ ℝℎ

`[ 566 · figure]` *(base64 25476 chars attached)*

> ![image](/image/placeholder)

`[ 567 · figure]` *(base64 51480 chars attached)*

> ![image](/image/placeholder)

`[ 568 · footer]`

> Natural Language Processing (COSE461)


## Page 73

`[ 569 · header]`

> Recurrent Neural Networks

`[ 570 · heading1]`

> Long Short-Term Memory RNNs (LSTMs)

`[ 571 · heading1]`

> What is the range of values?

`[ 572 · paragraph]`

> - What is the range of values for each element in the hidden representations 𝐡𝑡?

`[ 573 · list]`

> (A) 0 𝑡𝑜 ∞
> (B) 0 𝑡𝑜 1
> (C) −1 𝑡𝑜 1
> (D) −∞ 𝑡𝑜 ∞

`[ 574 · figure]` *(base64 33524 chars attached)*

> ![image](/image/placeholder)

`[ 575 · footer]`

> Natural Language Processing (COSE461)


## Page 74

`[ 576 · header]`

> Recurrent Neural Networks

`[ 577 · heading1]`

> Long Short-Term Memory RNNs (LSTMs)

`[ 578 · heading1]`

> What is the range of values?

`[ 579 · paragraph]`

> - What is the range of values for each element in the hidden representations 𝐡𝑡?

`[ 580 · list]`

> (A) 0 𝑡𝑜 ∞
> (B) 0 𝑡𝑜 1
> (C) −1 𝑡𝑜 1
> (D) −∞ 𝑡𝑜 ∞

`[ 581 · figure]` *(base64 33524 chars attached)*

> ![image](/image/placeholder)

`[ 582 · footer]`

> Natural Language Processing (COSE461)


## Page 75

`[ 583 · header]`

> Recurrent Neural Networks

`[ 584 · paragraph]`

> Long Short-Term Memory RNNs (LSTMs)

`[ 585 · heading1]`

> LSTMs: the formulation

`[ 586 · figure]` *(base64 165008 chars attached)*

> ![image](/image/placeholder)

`[ 587 · paragraph]`

> - LSTM doesn’t guarantee that there is no vanishing/exploding gradient, but it does
> provide an easier way for the model to learn long-distance dependencies

`[ 588 · paragraph]`

> - LSTMs were invented in 1997 but finally got working from 2013-2015

`[ 589 · footer]`

> Natural Language Processing (COSE461)


## Page 76

`[ 590 · header]`

> Recurrent Neural Networks

`[ 591 · paragraph]`

> Long Short-Term Memory RNNs (LSTMs)

`[ 592 · heading1]`

> Visualization of LSTMs

`[ 593 · figure]` *(base64 110088 chars attached)*

> ![image](/image/placeholder)

`[ 594 · footer]`

> Natural Language Processing (COSE461)


## Page 77

`[ 595 · header]`

> Recurrent Neural Networks

`[ 596 · paragraph]`

> Long Short-Term Memory RNNs (LSTMs)

`[ 597 · heading1]`

> Visualization of LSTMs

`[ 598 · figure]` *(base64 192580 chars attached)*

> ![image](/image/placeholder)

`[ 599 · footer]`

> Natural Language Processing (COSE461)


## Page 78

`[ 600 · header]`

> Recurrent Neural Networks

`[ 601 · paragraph]`

> Long Short-Term Memory RNNs (LSTMs)
> Visualization of LSTMs

`[ 602 · figure]` *(base64 52364 chars attached)*

> ![image](/image/placeholder)

`[ 603 · paragraph]`

> - Cell state = a conveyor belt

`[ 604 · paragraph]`

> - It allows adding or removing information carefully regulated by gates

`[ 605 · footer]`

> Natural Language Processing (COSE461)


## Page 79

`[ 606 · header]`

> Recurrent Neural Networks

`[ 607 · paragraph]`

> Long Short-Term Memory RNNs (LSTMs)

`[ 608 · heading1]`

> Visualization of LSTMs

`[ 609 · figure]` *(base64 51784 chars attached)*

> ![image](/image/placeholder)

`[ 610 · footer]`

> Natural Language Processing (COSE461)


## Page 80

`[ 611 · header]`

> Recurrent Neural Networks

`[ 612 · paragraph]`

> Long Short-Term Memory RNNs (LSTMs)

`[ 613 · heading1]`

> Visualization of LSTMs

`[ 614 · figure]` *(base64 65156 chars attached)*

> ![image](/image/placeholder)

`[ 615 · footer]`

> Natural Language Processing (COSE461)


## Page 81

`[ 616 · header]`

> Recurrent Neural Networks

`[ 617 · paragraph]`

> Long Short-Term Memory RNNs (LSTMs)

`[ 618 · heading1]`

> Visualization of LSTMs

`[ 619 · figure]` *(base64 71660 chars attached)*

> ![image](/image/placeholder)

`[ 620 · footer]`

> Natural Language Processing (COSE461)


## Page 82

`[ 621 · heading1]`

> Recurrent Neural Networks

`[ 622 · paragraph]`

> Long Short-Term Memory RNNs (LSTMs)

`[ 623 · heading1]`

> Visualization of LSTMs

`[ 624 · figure]` *(base64 74340 chars attached)*

> ![image](/image/placeholder)

`[ 625 · footer]`

> Natural Language Processing (COSE461)


## Page 83

`[ 626 · paragraph]`

> Gated Recurrent Units (GRUs)


## Page 84

`[ 627 · paragraph]`

> Recurrent Neural Networks

`[ 628 · paragraph]`

> Gated Recurrent Units (GRUs)

`[ 629 · paragraph]`

> Introduction

`[ 630 · paragraph]`

> - Learning Phrase Representations using RNN Encoder-Decoder for Statistical Machine
> Translation, Cho et al., EMNLP 2014

`[ 631 · paragraph]`

> - Introduced by Kyunghyun Cho et al. in 2014

`[ 632 · paragraph]`

> - Simplified 3 gates to 2 gates: reset gate and update gate, without an explicit cell state

`[ 633 · footer]`

> Natural Language Processing (COSE461)


## Page 85

`[ 634 · heading1]`

> Recurrent Neural Networks

`[ 635 · paragraph]`

> Gated Recurrent Units (GRUs)

`[ 636 · heading1]`

> Formulation

`[ 637 · paragraph]`

> - Reset gate:

`[ 638 · paragraph]`

> 𝐫𝑡 = 𝜎 𝐖𝑟𝐡𝑡−1 + 𝐔𝑟𝐱𝑡 + 𝐛𝑟

`[ 639 · paragraph]`

> - Update gate:

`[ 640 · paragraph]`

> 𝐳𝑡 = 𝜎 𝐖𝑧𝐡𝑡−1 + 𝐔𝑧𝐱𝑡 + 𝐛𝑧

`[ 641 · paragraph]`

> - New hidden state:

`[ 642 · paragraph]`

> ሚ = tanh 𝐖 𝐫𝑡 ⊙ 𝐡𝑡−1 + 𝐔𝐱𝑡 + 𝐛

`[ 643 · paragraph]`

> 𝐡𝑡

`[ 644 · figure]` *(base64 84192 chars attached)*

> ![image](/image/placeholder)

`[ 645 · paragraph]`

> Q: What is the range of the hidden representations 𝐡𝑡?

`[ 646 · paragraph]`

> 𝐡𝑡 = 1 − 𝐳𝑡 ⊙ 𝐡𝑡−1 + 𝐳𝑡 ⊙ ሚ𝐡𝑡

`[ 647 · paragraph]`

> merge input and forget gates

`[ 648 · paragraph]`

> Q: How many parameters are there compared to simple RNNs?

`[ 649 · footer]`

> LSTMs: 𝐜𝑡 = 𝐜𝑡−1 ⊙ 𝐟𝑡 + 𝐠𝑡 ⊙ 𝐢𝑡, 𝐡𝑡 = tanh 𝐜𝑡 ⊙ 𝐨𝑡

`[ 650 · footer]`

> Natural Language Processing (COSE461)


## Page 86

`[ 651 · heading1]`

> Recurrent Neural Networks

`[ 652 · paragraph]`

> Gated Recurrent Units (GRUs)

`[ 653 · heading1]`

> Comparison of LSTMs and GRUs

`[ 654 · figure]` *(base64 80164 chars attached)*

> ![image](/image/placeholder)

`[ 655 · paragraph]`

> 𝐢𝑡 = 𝜎 𝐖𝑖𝐡𝑡−1 + 𝐔𝑖𝐱𝑡 + 𝐛𝑖
> 𝐟𝑡 = 𝜎 𝐖𝑓𝐡𝑡−1 + 𝐔𝑓𝐱𝑡 + 𝐛𝑓
> 𝐨𝑡 = 𝜎 𝐖𝑜𝐡𝑡−1 + 𝐔𝑜𝐱𝑡 + 𝐛𝑜
> 𝐠𝑡 = 𝑡𝑎𝑛ℎ 𝐖𝑔𝐡𝑡−1 + 𝐔𝐠𝐱𝑡 + 𝐛𝐠
> 𝐜𝑡 = 𝐜𝑡−1 ⊙ 𝐟𝑡 + 𝐠𝑡 ⊙ 𝐢𝑡
> 𝐡𝑡 = tanh 𝐜𝑡 ⊙ 𝐨𝑡

`[ 656 · paragraph]`

> 𝐡𝑡 = 𝑓 𝐡𝑡−1, 𝐱𝑡 ∈ ℝℎ

`[ 657 · paragraph]`

> 𝐡𝑡 = 𝑡𝑎𝑛ℎ 𝐖𝐡𝑡−1 + 𝐔𝐱𝑡 + 𝐛 ∈ ℝℎ

`[ 658 · paragraph]`

> 𝐫𝑡 = 𝜎 𝐖𝑟𝐡𝑡−1 + 𝐔𝑟𝐱𝑡 + 𝐛𝑟
> 𝐳𝑡 = 𝜎 𝐖𝑧𝐡𝑡−1 + 𝐔𝑧𝐱𝑡 + 𝐛𝑧
> ሚ = 𝑡𝑎𝑛ℎ 𝐖 𝐫𝑡 ⊙ 𝐡𝑡−1 + 𝐔𝐱𝑡 + 𝐛
> 𝐡𝑡
> 𝐡𝑡 = 1 − 𝐳𝑡 ⊙ 𝐡𝑡−1 + 𝐳𝑡 ⊙ ሚ𝐡𝑡

`[ 659 · footer]`

> LSTMs

`[ 660 · paragraph]`

> GRUs

`[ 661 · footer]`

> Natural Language Processing (COSE461)


## Page 87

`[ 662 · paragraph]`

> Recurrent Neural Networks

`[ 663 · paragraph]`

> Gated Recurrent Units (GRUs)

`[ 664 · paragraph]`

> Comparison of LSTMs and GRUs

`[ 665 · paragraph]`

> - Let’s compare LSTMs and GRUs

`[ 666 · paragraph]`

> - Which of the following statements is correct?

`[ 667 · list]`

> (A) GRUs can be trained faster
> (B) In theory LSTMs can capture long-term dependencies better
> (C) LSTMs have a controlled exposure of memory content while GRUs don’t
> (D) All of the above

`[ 668 · footer]`

> Natural Language Processing (COSE461)


## Page 88

`[ 669 · header]`

> Recurrent Neural Networks

`[ 670 · paragraph]`

> Gated Recurrent Units (GRUs)

`[ 671 · paragraph]`

> Comparison: FFNNs vs Simple RNNs vs LSTMs vs GRUs

`[ 672 · figure]` *(base64 28352 chars attached)*

> ![image](/image/placeholder)

`[ 673 · figure]` *(base64 32628 chars attached)*

> ![image](/image/placeholder)

`[ 674 · figure]` *(base64 30864 chars attached)*

> ![image](/image/placeholder)

`[ 675 · figure]` *(base64 23468 chars attached)*

> ![image](/image/placeholder)

`[ 676 · footer]`

> Natural Language Processing (COSE461)


## Page 89

`[ 677 · heading1]`

> Recurrent Neural Networks

`[ 678 · paragraph]`

> Gated Recurrent Units (GRUs)

`[ 679 · paragraph]`

> Practical takeaways

`[ 680 · figure]` *(base64 36168 chars attached)*

> ![image](/image/placeholder)

`[ 681 · figure]` *(base64 28192 chars attached)*

> ![image](/image/placeholder)

`[ 682 · figure]` *(base64 45660 chars attached)*

> ![image](/image/placeholder)

`[ 683 · figure]` *(base64 45788 chars attached)*

> ![image](/image/placeholder)

`[ 684 · footer]`

> Natural Language Processing (COSE461)


## Page 90

`[ 685 · paragraph]`

> E.O.D
