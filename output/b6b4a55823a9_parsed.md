# Parsed dump — job b6b4a55823a9

- Source: `b6b4a55823a9_Lec07 - Sequence-to-Sequence.pdf`
- Elements: 379


## Page 1

`[   0 · heading1]`

> Natural Language Processing (COSE461)

`[   1 · paragraph]`

> Sequence-to-Sequence

`[   2 · paragraph]`

> Instructor:

`[   3 · paragraph]`

> Buru Chang, Ph.D.

`[   4 · paragraph]`

> Assistant Professor
> Dept. of Computer Science & Engineering
> Korea University, Seoul, South Korea

`[   5 · figure]` *(base64 38572 chars attached)*

> ![image](/image/placeholder)


## Page 2

`[   6 · paragraph]`

> Sequence-to-Sequence

`[   7 · paragraph]`

> Class Objective

`[   8 · paragraph]`

> Understanding sequence-to-sequence

`[   9 · list]`

> - Machine translation

`[  10 · list]`

> - Sequence-to-Sequence (Seq2Seq) architecture

`[  11 · list]`

> - Attention mechanism

`[  12 · footer]`

> Natural Language Processing (COSE461)


## Page 3

`[  13 · paragraph]`

> Machine Translation


## Page 4

`[  14 · paragraph]`

> Sequence-to-Sequence

`[  15 · paragraph]`

> Machine Translation

`[  16 · heading1]`

> Introduction

`[  17 · figure]` *(base64 72704 chars attached)*

> ![image](/image/placeholder)

`[  18 · figure]` *(base64 108280 chars attached)*

> ![image](/image/placeholder)

`[  19 · list]`

> - One of the “holy grail” problems in artificial intelligence
> - Practical use case: facilitate communication between people in the world
> - Extremely challenging (especially for low-resource languages)

`[  20 · footer]`

> Natural Language Processing (COSE461)


## Page 5

`[  21 · paragraph]`

> Sequence-to-Sequence

`[  22 · paragraph]`

> Machine Translation

`[  23 · paragraph]`

> Some translations

`[  24 · paragraph]`

> - Easy:

`[  25 · paragraph]`

> I like apples <-> ich mag Ä pfel (German)

`[  26 · paragraph]`

> - Not so easy:

`[  27 · paragraph]`

> I like apples <-> J'aime les pommes (French)
> I like red apples <-> J'aime les pommes rouges (French)
> les <-> the
> les pommes <-> apples

`[  28 · footer]`

> Natural Language Processing (COSE461)


## Page 6

`[  29 · heading1]`

> Sequence-to-Sequence

`[  30 · paragraph]`

> Machine Translation

`[  31 · paragraph]`

> Basics of machine translation

`[  32 · heading1]`

> - Goal:

`[  33 · paragraph]`

> Translate a sentence 𝐰(𝑠) in a source language (input) to a sentence in the target language (output)

`[  34 · paragraph]`

> - Can be formulated as an optimization problem:

`[  35 · paragraph]`

> Most likely translation, ෝ𝐰𝑡 = arg max (𝜓(𝐰(𝑠), 𝐰 𝑡 ) where 𝜓 is a scoring function over source and target
> 𝐰 t
> sentences

`[  36 · heading1]`

> - Requires two components:

`[  37 · paragraph]`

> Learning algorithm to compute parameters of scoring function 𝜓
> Decoding algorithm for computing the best translation ෝ𝐰 𝑡

`[  38 · footer]`

> Natural Language Processing (COSE461)


## Page 7

`[  39 · heading1]`

> Sequence-to-Sequence

`[  40 · paragraph]`

> Machine Translation

`[  41 · paragraph]`

> Why is MT challenging?

`[  42 · paragraph]`

> - Single words may be replaced with multi-word phrases
> I like apples <-> J'aime les pommes

`[  43 · paragraph]`

> - Reordering of phrases

`[  44 · paragraph]`

> I like red apples <-> J'aime les pommes rouges

`[  45 · paragraph]`

> - Contextual dependence

`[  46 · paragraph]`

> les <-> the

`[  47 · paragraph]`

> les pommes <-> apples

`[  48 · footer]`

> Natural Language Processing (COSE461)


## Page 8

`[  49 · paragraph]`

> Sequence-to-Sequence

`[  50 · heading1]`

> Machine Translation

`[  51 · heading1]`

> Evaluating machine translation

`[  52 · heading1]`

> - Two main criteria:

`[  53 · paragraph]`

> Adequacy: Translation 𝐰 𝑡 𝐰 𝑠
> should adequately reflect the linguistic content of
> should be fluent text in the target language
> Fluency: Translation 𝐰 𝑡

`[  54 · paragraph]`

> Ground truth: 나나 나나나나 나나나나나 나나나

`[  55 · table]` *(base64 71540 chars attached)*

> | 나나나나나 나나나 나나 나나나 |
> | --- |
> | 나 나나나나 나나나 <table><thead></thead><tbody><tr><td>Adequate?</td><td>Fluent?</td></tr><tr><td>Adequate?</td><td>Fluent?</td></tr><tr><td>Adequate?</td><td>Fluent?</td></tr></tbody></table> |
> | 나나나나 나나 나나나나나 나나나 |

`[  56 · footer]`

> Natural Language Processing (COSE461)


## Page 9

`[  57 · heading1]`

> Sequence-to-Sequence

`[  58 · paragraph]`

> Machine Translation

`[  59 · heading1]`

> Evaluation metrics

`[  60 · paragraph]`

> - Manual evaluation: ask a native speaker to verify the translation
> Most accurate, but expensive

`[  61 · paragraph]`

> - Automated evaluation metrics:

`[  62 · paragraph]`

> Compare system hypothesis with reference translations

`[  63 · paragraph]`

> Bi-Lingual Evaluation Understudy (BLEU) (Papineni et al., 2002):

`[  64 · paragraph]`

> Modified n-gram precision

`[  65 · paragraph]`

> reference translation

`[  66 · paragraph]`

> number of 𝑛−grams appearing in both reference and hypothesis translations
> 𝑝𝑛 =
> number of 𝑛−grams appearing in the hypothesis translation

`[  67 · paragraph]`

> system prediction

`[  68 · footer]`

> 𝑁
> 1
> BLEU = exp ෍ 𝑝𝑛
> 𝑁
> 𝑛 =1

`[  69 · footer]`

> Natural Language Processing (COSE461)


## Page 10

`[  70 · paragraph]`

> Sequence-to-Sequence

`[  71 · heading1]`

> Machine Translation

`[  72 · heading1]`

> Evaluation metrics

`[  73 · paragraph]`

> - To avoid log 0 , all precisions are smoothed

`[  74 · paragraph]`

> - Each 𝑛-gram in reference can be used at most once
> e.g., Hypothesis: “to to to to to” vs Reference: “to be or not to be” should not get a unigram
> precision of 1
> BLEU-k: average of BLEU scores computed using 1-gram through k-gram

`[  75 · paragraph]`

> - Problem: Precision-based metrics favor short translations
> Solution: Multiply score with a brevity penalty for translations shorter than reference, 𝑒1−𝑟/ℎ

`[  76 · footer]`

> Natural Language Processing (COSE461)


## Page 11

`[  77 · header]`

> Sequence-to-Sequence

`[  78 · paragraph]`

> Machine Translation

`[  79 · heading1]`

> BLEU scores

`[  80 · paragraph]`

> BLEU is useful (and
> widely used) but far
> from perfect

`[  81 · paragraph]`

> A good translation
> can get a poor BLEU
> score because it has
> low n-gram overlap
> with human
> translation

`[  82 · paragraph]`

> - Alternatives have been proposed:

`[  83 · paragraph]`

> METEOR: weighted F-measure
> Translation Error Rate (TER): Edit distance between hypothesis and reference

`[  84 · footer]`

> Natural Language Processing (COSE461)


## Page 12

`[  85 · header]`

> Sequence-to-Sequence

`[  86 · paragraph]`

> Machine Translation

`[  87 · paragraph]`

> Data: parallel corpora

`[  88 · paragraph]`

> - Statistical MT relies requires parallel corpora (bilingual)

`[  89 · paragraph]`

> - Not easily available for many low-resource languages in the world

`[  90 · footer]`

> Natural Language Processing (COSE461)


## Page 13

`[  91 · heading1]`

> Sequence-to-Sequence

`[  92 · paragraph]`

> Machine Translation

`[  93 · heading1]`

> Machine translation: Data

`[  94 · paragraph]`

> - 21 European languages: Romanic (French, Italian, Spanish, Portuguese, Romanian),
> Germanic (English, Dutch, German, Danish, Swedish), Slavik (Bulgarian, Czech, Polish,
> Slovak, Slovene), Finni-Ugric (Finnish, Hungarian, Estonian), Baltic (Latvian,

`[  95 · heading1]`

> Lithuanian), and Greek

`[  96 · footer]`

> Natural Language Processing (COSE461)


## Page 14

`[  97 · paragraph]`

> Sequence-to-Sequence

`[  98 · paragraph]`

> Machine Translation

`[  99 · paragraph]`

> Statistical machine translation (SMT)

`[ 100 · paragraph]`

> - Core idea: Learn a probabilistic model from data

`[ 101 · list]`

`[ 102 · paragraph]`

> - Suppose we are translating French → English

`[ 103 · list]`

`[ 104 · paragraph]`

> - We want to find best target sentence 𝐰(𝑡), given source sentence 𝐰(𝑠)

`[ 105 · list]`

`[ 106 · paragraph]`

> arg max 𝑃 𝐰(𝑡) 𝐰(𝑠) )
> 𝐰 𝑡

`[ 107 · paragraph]`

> - According to Bayes’ rule, we can break this down into two components:

`[ 108 · paragraph]`

> arg max 𝑃 𝐰 𝑠 𝐰 𝑡 )𝑃 𝐰 𝑡
> 𝐰 𝑡

`[ 109 · footer]`

> Natural Language Processing (COSE461)


## Page 15

`[ 110 · paragraph]`

> Sequence-to-Sequence

`[ 111 · paragraph]`

> Machine Translation

`[ 112 · heading1]`

> Statistical machine translation (SMT)

`[ 113 · paragraph]`

> arg max 𝑃 𝐰 𝑠 𝐰 𝑡 )𝑃 𝐰 𝑡
> 𝐰 𝑡

`[ 114 · paragraph]`

> Translation model: models whether the
> target sentence reflects the linguistic
> content of the source language
> (adequacy) Learned from parallel data

`[ 115 · paragraph]`

> Language model: models how fluent the
> target sentence is (fluency)
> Can be learned from monolingual data

`[ 116 · paragraph]`

> - How should we align words in source to words in target?

`[ 117 · chart]` *(base64 34876 chars attached)*

> ![image](/image/placeholder)
> - Chart Type: bar
> |  | Vinary | Likes | Python |
> | --- | --- | --- | --- |
> | item_01 | 4 | 2 | 0 |

`[ 118 · footer]`

> Natural Language Processing (COSE461)


## Page 16

`[ 119 · heading1]`

> Sequence-to-Sequence

`[ 120 · heading1]`

> Machine Translation

`[ 121 · heading1]`

> Statistical machine translation (SMT)

`[ 122 · paragraph]`

> - SMT was a huge field (1990s-2010s) - The best systems were extremely complex

`[ 123 · paragraph]`

> - Systems had many separately-designed subcomponents
> Need to design features to capture particular language phenomena
> Required compiling and maintaining extra resources
> Lots of human effort to maintain - repeated effort for each language pair!

`[ 124 · footer]`

> Natural Language Processing (COSE461)


## Page 17

`[ 125 · paragraph]`

> Sequence-to-Sequence

`[ 126 · paragraph]`

> Machine Translation

`[ 127 · paragraph]`

> SMT → NMT

`[ 128 · footer]`

> Natural Language Processing (COSE461)


## Page 18

`[ 129 · heading1]`

> Sequence-to-Sequence

`[ 130 · heading1]`

> Machine Translation

`[ 131 · heading1]`

> Neural machine translation (NMT)

`[ 132 · paragraph]`

> - Neural Machine Translation (NMT) is a way to do machine translation with a single
> end-to-end neural network

`[ 133 · list]`

`[ 134 · paragraph]`

> - The neural network architecture is called a sequence-to-sequence model (aka
> seq2seq) and it involves two RNNs

`[ 135 · paragraph]`

> cited by 28K ↑

`[ 136 · figure]` *(base64 47292 chars attached)*

> ![image](/image/placeholder)

`[ 137 · footer]`

> Natural Language Processing (COSE461)


## Page 19

`[ 138 · paragraph]`

> Sequence-to-Sequence


## Page 20

`[ 139 · header]`

> Sequence-to-Sequence

`[ 140 · paragraph]`

> Sequence-to-Sequence (seq2seq)

`[ 141 · figure]` *(base64 199204 chars attached)*

> ![image](/image/placeholder)
> Introduction Encoding of
> source sentence
> = initial hidden state
> for decoder RNN
> A special symbol <bos>
> before generating
> the first word

`[ 142 · paragraph]`

> - It is called an encoder-decoder architecture

`[ 143 · paragraph]`

> The encoder is an RNN to read the input sentence (source language)
> The decoder is another RNN to generate output word by word (target language)

`[ 144 · footer]`

> Natural Language Processing (COSE461)


## Page 21

`[ 145 · header]`

> Sequence-to-Sequence

`[ 146 · paragraph]`

> Sequence-to-Sequence (seq2seq)

`[ 147 · paragraph]`

> Seq2seq: encoder

`[ 148 · figure]` *(base64 87868 chars attached)*

> ![image](/image/placeholder)

`[ 149 · footer]`

> Natural Language Processing (COSE461)


## Page 22

`[ 150 · header]`

> Sequence-to-Sequence

`[ 151 · paragraph]`

> Sequence-to-Sequence (seq2seq)

`[ 152 · paragraph]`

> Seq2seq: decoder

`[ 153 · paragraph]`

> - A conditional language model

`[ 154 · figure]` *(base64 164948 chars attached)*

> ![image](/image/placeholder)

`[ 155 · footer]`

> Natural Language Processing (COSE461)


## Page 23

`[ 156 · paragraph]`

> Sequence-to-Sequence

`[ 157 · paragraph]`

> Sequence-to-Sequence (seq2seq)

`[ 158 · paragraph]`

> Seq2seq: decoder

`[ 159 · paragraph]`

> - A conditional language model

`[ 160 · paragraph]`

> It is a language model because the decoder is predicting the next word of the target
> sentence
> Conditional because the predictions are also conditioned on the source sentence through
> ℎ𝑒𝑛𝑐

`[ 161 · paragraph]`

> - NMT (neural machine translation) directly calculates 𝑃 𝐰 𝑡 𝐰 𝑠
> Denote 𝐰 𝑡 = 𝑦1, ⋯ , 𝑦𝑇
> 𝑃 𝐰 𝑡 𝐰 𝑠 = 𝑃 𝑦1 𝐰 𝑠 𝑃 𝑦2 𝑦1, 𝐰 𝑠 𝑃 𝑦3 𝑦1, 𝑦2, 𝐰 𝑠 ⋯ 𝑃 𝑦𝑇 𝑦1, ⋯ , 𝑦𝑇−1, 𝐰 𝑠
> 𝐲𝑡 = softmax 𝐖𝑜𝐡𝑡 𝑝 𝑦𝑡+1 𝑦1, ⋯ , 𝑦𝑡, 𝐰 𝑠 ) = ො𝐲𝑡(𝑦𝑡+1)

`[ 162 · footer]`

> Natural Language Processing (COSE461)


## Page 24

`[ 163 · header]`

> Sequence-to-Sequence

`[ 164 · paragraph]`

> Sequence-to-Sequence (seq2seq)

`[ 165 · paragraph]`

> Understanding seq2seq

`[ 166 · figure]` *(base64 75368 chars attached)*

> ![image](/image/placeholder)

`[ 167 · heading1]`

> - Which of the following is correct?

`[ 168 · paragraph]`

> (a) We can use bidirectional RNNs for both encoder and decoder
> (b) The decoder has more parameters because of the output matrix 𝐖𝑜
> (c) The encoder and decoder have separate word embeddings
> (d) The encoder and decoder’s parameters are optimized together

`[ 169 · list]`

`[ 170 · footer]`

> Natural Language Processing (COSE461)


## Page 25

`[ 171 · header]`

> Sequence-to-Sequence

`[ 172 · paragraph]`

> Sequence-to-Sequence (seq2seq)

`[ 173 · heading1]`

> Understanding seq2seq

`[ 174 · figure]` *(base64 76284 chars attached)*

> ![image](/image/placeholder)

`[ 175 · heading1]`

> - Encoder RNN:

`[ 176 · paragraph]`

> for source language
> Word embeddings 𝐄 𝑠
> RNN parameters, e.g., {𝐖, 𝐔, 𝐛} for simple RNNs and 4x parameters for LSTMs
> Encoder RNN can be bidirectional

`[ 177 · footer]`

> Natural Language Processing (COSE461)


## Page 26

`[ 178 · header]`

> Sequence-to-Sequence

`[ 179 · paragraph]`

> Sequence-to-Sequence (seq2seq)

`[ 180 · heading1]`

> Understanding seq2seq

`[ 181 · figure]` *(base64 76096 chars attached)*

> ![image](/image/placeholder)

`[ 182 · heading1]`

> - Decoder RNN:

`[ 183 · paragraph]`

> Word embeddings 𝐄 𝑡
> for target language
> RNN parameters, e.g., {𝐖, 𝐔, 𝐛} for simple RNNs and 4x parameters for LSTMs
> Output embedding matrix 𝐖𝑜 -> can be tied with 𝐄 𝑡
> Decoder RNN has to be unidirectional (left to right)

`[ 184 · footer]`

> Natural Language Processing (COSE461)


## Page 27

`[ 185 · header]`

> Sequence-to-Sequence

`[ 186 · paragraph]`

> Sequence-to-Sequence (seq2seq)

`[ 187 · paragraph]`

> Training seq2seq models

`[ 188 · paragraph]`

> 𝑠 𝑡
> - Training data: parallel corpus 𝐰𝑖 , 𝐰𝑖

`[ 189 · figure]` *(base64 63992 chars attached)*

> ![image](/image/placeholder)

`[ 190 · paragraph]`

> - Minimize cross-entropy loss:

`[ 191 · equation]` *(base64 21324 chars attached)*

> 𝑇
>  ෍ − log 𝑃 𝑦𝑡 𝑦1 ⋯ , 𝑦𝑡−1, 𝐰 𝑠 , 𝐰 𝑡 = 𝑦1, ⋯ , 𝑦𝑇
>  𝑡 =1

`[ 192 · paragraph]`

> - Back-propagate gradients through both encoder and decoder

`[ 193 · footer]`

> Natural Language Processing (COSE461)


## Page 28

`[ 194 · header]`

> Sequence-to-Sequence

`[ 195 · paragraph]`

> Sequence-to-Sequence (seq2seq)

`[ 196 · heading1]`

> Training seq2seq models

`[ 197 · figure]` *(base64 211948 chars attached)*

> ![image](/image/placeholder)

`[ 198 · footer]`

> Natural Language Processing (COSE461)


## Page 29

`[ 199 · paragraph]`

> Sequence-to-Sequence

`[ 200 · heading1]`

> Sequence-to-Sequence (seq2seq)

`[ 201 · paragraph]`

> Decoding seq2seq models

`[ 202 · paragraph]`

> - Greedy decoding

`[ 203 · paragraph]`

> Compute argmax at every step of decoder to generate word

`[ 204 · figure]` *(base64 108368 chars attached)*

> ![image](/image/placeholder)

`[ 205 · paragraph]`

> - Exhaustive search is very expensive: arg max 𝑃 𝑦1, ⋯ , 𝑦𝑇 𝐰 𝑠
> 𝑦1,⋯,𝑦𝑇
> We even don’t know what T is

`[ 206 · footer]`

> Natural Language Processing (COSE461)


## Page 30

`[ 207 · header]`

> Sequence-to-Sequence

`[ 208 · paragraph]`

> Sequence-to-Sequence (seq2seq)

`[ 209 · paragraph]`

> Decoding with beam search

`[ 210 · list]`

> - At every step, keep track of the 𝑘 most probable partial translations (hypotheses)

`[ 211 · list]`

> - Score of each hypothesis = log probability of sequence so far

`[ 212 · equation]` *(base64 17512 chars attached)*

> 𝑗
>  ෍ log 𝑃 𝑦𝑡 𝑦1, ⋯ , 𝑦𝑡−1, 𝐰 𝑠
>  𝑡 =1

`[ 213 · paragraph]`

> - Not guaranteed to be optimal

`[ 214 · paragraph]`

> - More efficient than exhaustive search

`[ 215 · footer]`

> Natural Language Processing (COSE461)


## Page 31

`[ 216 · header]`

> Sequence-to-Sequence

`[ 217 · paragraph]`

> Sequence-to-Sequence (seq2seq)

`[ 218 · heading1]`

> Decoding with beam search

`[ 219 · figure]` *(base64 164048 chars attached)*

> ![image](/image/placeholder)

`[ 220 · footer]`

> Natural Language Processing (COSE461)


## Page 32

`[ 221 · header]`

> Sequence-to-Sequence

`[ 222 · paragraph]`

> Sequence-to-Sequence (seq2seq)

`[ 223 · heading1]`

> Decoding with beam search

`[ 224 · figure]` *(base64 188048 chars attached)*

> ![image](/image/placeholder)

`[ 225 · footer]`

> Natural Language Processing (COSE461)


## Page 33

`[ 226 · heading1]`

> Sequence-to-Sequence

`[ 227 · paragraph]`

> Sequence-to-Sequence (seq2seq)

`[ 228 · paragraph]`

> Beam search: details

`[ 229 · paragraph]`

> - Different hypotheses may produce <eos> token at different time steps
> When a hypothesis produces <eos>, stop expanding it and place it aside

`[ 230 · paragraph]`

> - Continue beam search until:

`[ 231 · paragraph]`

> All 𝑘 hypotheses produce <eos> or hit max decoding limit T

`[ 232 · paragraph]`

> - Select top hypotheses using the normalized likelihood score

`[ 233 · equation]` *(base64 16408 chars attached)*

> 𝑇
>  1
>  ෍ log 𝑃 𝑦𝑡 𝑦1, ⋯ , 𝑦𝑡−1, 𝐰 𝑠
>  𝑇
>  𝑡 =1

`[ 234 · paragraph]`

> - Otherwise. shorter hypotheses have higher scores

`[ 235 · footer]`

> Natural Language Processing (COSE461)


## Page 34

`[ 236 · header]`

> Sequence-to-Sequence

`[ 237 · paragraph]`

> Sequence-to-Sequence (seq2seq)

`[ 238 · paragraph]`

> NMT vs SMT

`[ 239 · paragraph]`

> - Pros

`[ 240 · paragraph]`

> Better performance (more fluent, better use of context, better use of phrase similarities)
> A single neural network to be optimized end-to-end (no individual subcomponents) Less
> human engineering effort - same method for all language pairs

`[ 241 · paragraph]`

> - Cons

`[ 242 · paragraph]`

> NMT is less interpretable
> NMT is difficult to control

`[ 243 · footer]`

> Natural Language Processing (COSE461)


## Page 35

`[ 244 · header]`

> Sequence-to-Sequence

`[ 245 · paragraph]`

> Sequence-to-Sequence (seq2seq)

`[ 246 · paragraph]`

> Sequence-to-sequence is versatile

`[ 247 · paragraph]`

> - Sequence-to-sequence is useful for more than just MT

`[ 248 · paragraph]`

> - Many NLP tasks can be phrased as sequence-to-sequence
> Summarization (long text short text)
> Dialogue (previous utterances next utterance)
> Parsing (input text output parse as sequence)
> Code generation (natural language Python code)

`[ 249 · footer]`

> Natural Language Processing (COSE461)


## Page 36

`[ 250 · header]`

> Sequence-to-Sequence

`[ 251 · paragraph]`

> Sequence-to-Sequence (seq2seq)

`[ 252 · paragraph]`

> Sequence-to-sequence is versatile: summarization

`[ 253 · figure]` *(base64 114604 chars attached)*

> ![image](/image/placeholder)

`[ 254 · footer]`

> Natural Language Processing (COSE461)


## Page 37

`[ 255 · header]`

> Sequence-to-Sequence

`[ 256 · paragraph]`

> Sequence-to-Sequence (seq2seq)

`[ 257 · paragraph]`

> Sequence-to-sequence is versatile: dialogue

`[ 258 · figure]` *(base64 55080 chars attached)*

> ![image](/image/placeholder)

`[ 259 · figure]` *(base64 216900 chars attached)*

> ![image](/image/placeholder)

`[ 260 · footer]`

> Natural Language Processing (COSE461)


## Page 38

`[ 261 · header]`

> Sequence-to-Sequence

`[ 262 · paragraph]`

> Sequence-to-Sequence (seq2seq)

`[ 263 · paragraph]`

> Sequence-to-sequence is versatile: parsing

`[ 264 · figure]` *(base64 21960 chars attached)*

> ![image](/image/placeholder)

`[ 265 · figure]` *(base64 82036 chars attached)*

> ![image](/image/placeholder)

`[ 266 · footer]`

> Natural Language Processing (COSE461)


## Page 39

`[ 267 · header]`

> Sequence-to-Sequence

`[ 268 · paragraph]`

> Sequence-to-Sequence (seq2seq)

`[ 269 · paragraph]`

> Sequence-to-sequence is versatile: code generation

`[ 270 · figure]` *(base64 73756 chars attached)*

> ![image](/image/placeholder)

`[ 271 · figure]` *(base64 84028 chars attached)*

> ![image](/image/placeholder)

`[ 272 · footer]`

> Natural Language Processing (COSE461)


## Page 40

`[ 273 · paragraph]`

> Attention Mechanism


## Page 41

`[ 274 · paragraph]`

> Sequence-to-Sequence

`[ 275 · paragraph]`

> Attention Mechanism

`[ 276 · paragraph]`

> bottleneck

`[ 277 · paragraph]`

> Sequence-to-sequence: the bottleneck

`[ 278 · figure]` *(base64 91624 chars attached)*

> ![image](/image/placeholder)

`[ 279 · chart]` *(base64 91624 chars attached)*

> ![image](/image/placeholder)
> - Chart Title: Encoder
> - Chart Type: bar
> |  | hello | world | heidden | state | bonjour | le | monde | lef | monder | esos |
> | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
> | item_01 | 1Not explicitly stated | 1Not explicitly stated | 1Not explicitly stated | 1Not explicitly stated | 1Not explicitly stated | 1Not explicitly stated | 1Not explicitly stated | 1Not explicitly stated | 1Not explicitly stated | 1Not explicitly stated |

`[ 280 · paragraph]`

> - A single encoding vector, 𝐡𝑒𝑛𝑐, needs to capture all the information about source
> sentence

`[ 281 · paragraph]`

> - Longer sequences can lead to vanishing gradients

`[ 282 · footer]`

> Natural Language Processing (COSE461)


## Page 42

`[ 283 · paragraph]`

> Sequence-to-Sequence

`[ 284 · paragraph]`

> Attention Mechanism

`[ 285 · paragraph]`

> Attention

`[ 286 · paragraph]`

> < NEURAL MACHINE TRANSLATION BY JOINTLY LEARNING TO ALIGN AND TRANSLATE>, Bahdanau et al., ICLR25

`[ 287 · paragraph]`

> <Effective Approaches to Attention-based Neural Machine Translation> Luong et al., EMNLP15

`[ 288 · footer]`

> Natural Language Processing (COSE461)


## Page 43

`[ 289 · header]`

> Sequence-to-Sequence

`[ 290 · heading1]`

> Attention Mechanism

`[ 291 · heading1]`

> Definition: attention

`[ 292 · paragraph]`

> - Attention provides a solution to the bottleneck problem

`[ 293 · paragraph]`

> - Attention learns the notion of alignment
> “Which source words are more relevant to the current target word?”

`[ 294 · paragraph]`

> - Key idea: At each time step during decoding, focus on a particular part of source
> sentence
> (i.e. an idea of what you are
> This depends on the decoder’s current hidden state 𝐡𝑡 𝑑𝑒𝑐
> trying to decode)
> Usually implemented as a probability distribution over the hidden states of the encoder
> (𝐡𝑖 𝑒𝑛𝑐)

`[ 295 · footer]`

> Natural Language Processing (COSE461)


## Page 44

`[ 296 · header]`

> Sequence-to-Sequence

`[ 297 · paragraph]`

> Attention Mechanism

`[ 298 · heading1]`

> Seq2seq: encoder

`[ 299 · figure]` *(base64 115224 chars attached)*

> ![image](/image/placeholder)
> 𝐡𝑖 𝑒𝑛𝑐

`[ 300 · footer]`

> Natural Language Processing (COSE461)


## Page 45

`[ 301 · header]`

> Sequence-to-Sequence

`[ 302 · paragraph]`

> Attention Mechanism

`[ 303 · heading1]`

> Seq2seq: decoder

`[ 304 · figure]` *(base64 176564 chars attached)*

> ![image](/image/placeholder)
> 𝐡𝑡 𝑑𝑒𝑐

`[ 305 · footer]`

> Natural Language Processing (COSE461)


## Page 46

`[ 306 · paragraph]`

> Sequence-to-Sequence

`[ 307 · paragraph]`

> Attention Mechanism
> Seq2seq with attention

`[ 308 · figure]` *(base64 94764 chars attached)*

> ![image](/image/placeholder)

`[ 309 · footer]`

> Natural Language Processing (COSE461)


## Page 47

`[ 310 · header]`

> Sequence-to-Sequence

`[ 311 · paragraph]`

> Attention Mechanism

`[ 312 · heading1]`

> Seq2seq with attention

`[ 313 · figure]` *(base64 188992 chars attached)*

> ![image](/image/placeholder)

`[ 314 · footer]`

> Natural Language Processing (COSE461)


## Page 48

`[ 315 · paragraph]`

> Sequence-to-Sequence

`[ 316 · paragraph]`

> Attention Mechanism

`[ 317 · heading1]`

> Seq2seq with attention

`[ 318 · figure]` *(base64 162952 chars attached)*

> ![image](/image/placeholder)

`[ 319 · footer]`

> Natural Language Processing (COSE461)


## Page 49

`[ 320 · paragraph]`

> Sequence-to-Sequence

`[ 321 · paragraph]`

> Attention Mechanism

`[ 322 · heading1]`

> Seq2seq with attention

`[ 323 · figure]` *(base64 170276 chars attached)*

> ![image](/image/placeholder)

`[ 324 · footer]`

> Natural Language Processing (COSE461)


## Page 50

`[ 325 · heading1]`

> Sequence-to-Sequence

`[ 326 · paragraph]`

> Attention Mechanism

`[ 327 · heading1]`

> Seq2seq with attention

`[ 328 · figure]` *(base64 125624 chars attached)*

> ![image](/image/placeholder)

`[ 329 · list]`

> - Encoder hidden states: 𝐡1 𝑒𝑛𝑐, ⋯ , 𝐡𝑛 𝑒𝑛𝑐
> - Decoder hidden state at time 𝑡: 𝐡𝑡 𝑑𝑒𝑐
> - First, get attention scores for this time step of decoder

`[ 330 · paragraph]`

> 𝐞𝑡 = 𝑔 𝐡1 𝑒𝑛𝑐, 𝐡𝑡 𝑑𝑒𝑐 , ⋯ , 𝑔 𝐡𝑛 𝑒𝑛𝑐, 𝐡𝑡 𝑑𝑒𝑐

`[ 331 · paragraph]`

> - Obtain the attention distribution using softmax:

`[ 332 · paragraph]`

> 𝐚𝑡 = 𝑠𝑜𝑓𝑡𝑚𝑎𝑥 𝐞𝑡 ∈ ℝ𝑛

`[ 333 · paragraph]`

> - Compute weighted sum of encoder hidden states:

`[ 334 · figure]` *(base64 13796 chars attached)*

> ![image](/image/placeholder)
> 𝑛
> 𝐚𝑡 = ෍ 𝑎𝑖 𝑡𝐡𝑖 𝑒𝑛𝑐 ∈ ℝℎ
> 𝑖=1

`[ 335 · equation]` *(base64 11612 chars attached)*

`[ 336 · paragraph]`

> - Finally, concatenate with decoder state and pass on to
> output layer:

`[ 337 · paragraph]`

> ሚ = tanh 𝐖𝑐 𝐚𝑡; 𝐡𝑡 𝑑𝑒𝑐 ∈ ℝℎ 𝐖𝑐 ∈ ℝ2ℎ×h
> 𝐡𝑡

`[ 338 · footer]`

> Natural Language Processing (COSE461)


## Page 51

`[ 339 · paragraph]`

> Sequence-to-Sequence

`[ 340 · heading1]`

> Attention Mechanism

`[ 341 · heading1]`

> Animation of attention

`[ 342 · figure]` *(base64 116404 chars attached)*

> ![image](/image/placeholder)

`[ 343 · paragraph]`

> https://jalammar.github.io/visualizing-neural-machine-translation-mechanics-of-seq2seq-models-with-attention/

`[ 344 · paragraph]`

> https://jalammar.github.io/visualizing-neural-machine-translation-
> mechanics-of-seq2seq-models-with-attention/

`[ 345 · footer]`

> Natural Language Processing (COSE461)


## Page 52

`[ 346 · heading1]`

> Sequence-to-Sequence

`[ 347 · paragraph]`

> Attention Mechanism

`[ 348 · heading1]`

> Types of attention

`[ 349 · paragraph]`

> and a decoder hidden state 𝐡𝑡 𝑑𝑒𝑐
> - Assume encoder hidden states 𝐡1 𝑒𝑛𝑐, 𝐡2 𝑒𝑛𝑐, ⋯ , 𝐡𝑛 𝑒𝑛𝑐
> ):
> Dot-product attention (assumes equal dimensions for 𝐡𝑒𝑛𝑐 and 𝐡𝑡 𝑑𝑒𝑐

`[ 350 · paragraph]`

> 𝑇
> 𝑔 𝐡𝑖 𝑒𝑛𝑐, 𝐡𝑡 𝑑𝑒𝑐 = 𝐡𝑡 𝑑𝑒𝑐 𝐡𝑖 𝑒𝑛𝑐 ∈ ℝ

`[ 351 · paragraph]`

> Multiplicative attention:

`[ 352 · paragraph]`

> 𝑇
> 𝑔 𝐡𝑖 𝑒𝑛𝑐, 𝐡𝑡 𝑑𝑒𝑐 = 𝐡𝑡 𝑑𝑒𝑐 𝐖𝐡𝑖 𝑒𝑛𝑐 ∈ ℝ
> where 𝐖 is a weight matrix (learned)

`[ 353 · paragraph]`

> Additive attention:

`[ 354 · paragraph]`

> 𝑔 𝐡𝑖 𝑒𝑛𝑐, 𝐡𝑡 𝑑𝑒𝑐 = 𝐯𝑇 tanh 𝐖1𝐡𝑖 𝑒𝑛𝑐 + 𝐖2𝐡𝑡 𝑑𝑒𝑐 ∈ ℝ
> where 𝐖1, 𝐖2 are weight matrices (learned) and 𝐯 is a weight vector (learned)

`[ 355 · footer]`

> Natural Language Processing (COSE461)


## Page 53

`[ 356 · paragraph]`

> Sequence-to-Sequence

`[ 357 · heading1]`

> Attention Mechanism

`[ 358 · paragraph]`

> Example

`[ 359 · figure]` *(base64 111392 chars attached)*

> ![image](/image/placeholder)

`[ 360 · paragraph]`

> - Assume we use dot product attention, which input word will have the highest
> attention value at current time step?

`[ 361 · list]`

> (A) the
> (B) cat
> (C) sat

`[ 362 · paragraph]`

> - Dot-product attention:

`[ 363 · equation]` *(base64 10700 chars attached)*

> 𝑔 𝐡𝑖 𝑒𝑛𝑐, 𝐡𝑡 𝑑𝑒𝑐 = 𝐡𝑡 𝑑𝑒𝑐 ⋅ 𝐡𝑖 𝑒𝑛𝑐 ∈ ℝ

`[ 364 · footer]`

> Natural Language Processing (COSE461)


## Page 54

`[ 365 · header]`

> Sequence-to-Sequence

`[ 366 · paragraph]`

> Attention Mechanism

`[ 367 · paragraph]`

> Attention improves translation

`[ 368 · footer]`

> Natural Language Processing (COSE461)


## Page 55

`[ 369 · header]`

> Sequence-to-Sequence

`[ 370 · paragraph]`

> Attention Mechanism

`[ 371 · paragraph]`

> Attention improves translation

`[ 372 · footer]`

> Natural Language Processing (COSE461)


## Page 56

`[ 373 · heading1]`

> Sequence-to-Sequence

`[ 374 · paragraph]`

> Attention Mechanism

`[ 375 · heading1]`

> Visualizing attention

`[ 376 · chart]` *(base64 93576 chars attached)*

> ![image](/image/placeholder)
> - Chart Type: bar
> |  | L' | accord | sur | la | zone | €conomique | europaenne | a | ete | sign | en | aout | 1992 |  |
> | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
> | item_01 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |

`[ 377 · footer]`

> Natural Language Processing (COSE461)


## Page 57

`[ 378 · paragraph]`

> E.O.D
