# Parsed dump — job 6be4d924665e

- Source: `6be4d924665e_Lec05 - Sequence Models.pdf`
- Elements: 573


## Page 1

`[   0 · heading1]`

> Natural Language Processing (COSE461)

`[   1 · paragraph]`

> Sequence Models

`[   2 · paragraph]`

> Instructor:
> Buru Chang, Ph.D.
> Assistant Professor
> Dept. of Computer Science & Engineering
> Korea University, Seoul, South Korea

`[   3 · figure]` *(base64 38572 chars attached)*

> ![image](/image/placeholder)
> KOREA
> U NIVERS | TY
> 1905


## Page 2

`[   4 · paragraph]`

> Sequence Models

`[   5 · paragraph]`

> Class Objective

`[   6 · paragraph]`

> Understanding sequence models

`[   7 · list]`

> - Sequence tagging NLP tasks
> Part-of-Speech (POS) tagging, Named Entity Recognition (NER)

`[   8 · list]`

> - Hidden Markov Models (HMM)

`[   9 · list]`

> - Viterbi algorithm

`[  10 · list]`

> - Maximum Entropy Markov Model (MEMMs)

`[  11 · list]`

> - Conditional Random Fields (CRFs)

`[  12 · paragraph]`

> Recommended reading
> textbook 17.1-17.4
> Michael Collins's notes

`[  13 · footer]`

> Natural Language Processing (COSE461)


## Page 3

`[  14 · paragraph]`

> What is sequence model?


## Page 4

`[  15 · header]`

> Sequence Models

`[  16 · heading1]`

> What is Sequence Model

`[  17 · heading1]`

> Examples

`[  18 · heading1]`

> - Part-of-speech (POS) tagging

`[  19 · paragraph]`

> PRP: Personal pronoun, VBZ: Verb, 3rd person singular present, NN: Singular noun, NNS:
> plural noun, IN: preposition or subordinating conjunction, DT: determiner

`[  20 · figure]` *(base64 202604 chars attached)*

> ![image](/image/placeholder)
> PRP VBZ NNS IN DT NN
> She sells seashells on the seashore
> Part Of Speech Tagging

`[  21 · footer]`

> Natural Language Processing (COSE461)


## Page 5

`[  22 · paragraph]`

> Sequence Models

`[  23 · paragraph]`

> What is Sequence Model

`[  24 · paragraph]`

> Examples

`[  25 · paragraph]`

> - Named entity recognition (NER)

`[  26 · paragraph]`

> P: person, L: location, O: organization, E: event, D: date

`[  27 · figure]` *(base64 235160 chars attached)*

> ![image](/image/placeholder)
> Person p Loc I Org 0 Event e Date d Other Z
> Barack Hussein Obama II x (born August 4, 1961 x ) is an American x attorney and
> politician who served as the 44th President of the United States x from
> January 20, 2009 × to January 20, 2017 × A member of the Democratic Party × he
> was the first African American × to serve as president. He was previously a
> United States Senator × from Illinois × and a member of the Illinois State Senate ×

`[  28 · footer]`

> Natural Language Processing (COSE461)


## Page 6

`[  29 · heading1]`

> Sequence Models

`[  30 · paragraph]`

> What is Sequence Model

`[  31 · heading1]`

> NLP pipelines

`[  32 · paragraph]`

> - NLP pipelines

`[  33 · figure]` *(base64 34764 chars attached)*

> ![image](/image/placeholder)
> nlp
> Text → tokenizer tagger parser ner → Doc

`[  34 · table]` *(base64 115620 chars attached)*

> | NAME | COMPONENT | CREATES | DESCRIPTION |
> | --- | --- | --- | --- |
> | tokenizer | Tokenizer 手 | Doc | Segment text into tokens. |
> | PROCESSING PIPELINE | PROCESSING PIPELINE | PROCESSING PIPELINE | PROCESSING PIPELINE |
> | tagger | Tagger 手 | Token. tag | Assign part-of-speech tags. |
> | parser | DependencyParser 手 | Token , head , Token dep , Doc. sents , Doc.noun_chunks | Assign dependency labels. |
> | ner | EntityRecognizer 手 | Doc. ents , Token. ent_iob , Token . ent_type | Detect and label named entities. |
> | lemmatizer | Lemmatizer 手 | Token . lemma | Assign base forms. |
> | textcat | TextCategorizer 手 | Doc.cats | Assign document labels. |
> | custom | custom components | Doc · XXX , Token . _.xxx , Span._.xxx | Assign custom attributes, methods or properties. |

`[  35 · paragraph]`

> https://spacy.io/usage/processing-pipelines

`[  36 · figure]` *(base64 183276 chars attached)*

> ![image](/image/placeholder)
> Buru previously worked at Hyperconnect as a machine learning engineer in 2022.
> - Annotations -
> parts-of-speech x named entities X dependency parse X
> Part-of-Speech:
> NNP RB VBD IN NNP IN DT NN VBG NN IN CD
> 1 Buru previously worked at Hyperconnect as a machine learning engineer in 2022
> Named Entity Recognition:
> PAST REF DATE
> PERSON DATE LOCATION TITLE 2022
> 1 Buru previously worked at Hyperconnect as a machine learning engineer in 2022
> Basic Dependencies:
> punct
> obl
> nsubj obl case dep nmod
> advmod case det- amod- ★case
> NNP RB VBD IN NNP IN DT NN VBG NN IN CD
> 1 Buru previously worked at Hyperconnect as a machine learning engineer in 2022
> Enhanced++ Dependencies:
> punct
> obl:as
> nsubj obl:at case dep nmod:in
> advmod case det amod case
> NNP RB VBD IN NNP IN DT NN VBG NN IN CD
> 1 Buru previously worked at Hyperconnect as a machine learning engineer in 2022

`[  37 · paragraph]`

> https://stanfordnlp.github.io/CoreNLP/

`[  38 · footer]`

> Natural Language Processing (COSE461)


## Page 7

`[  39 · header]`

> Sequence Models

`[  40 · paragraph]`

> What is Sequence Model

`[  41 · heading1]`

> NLP pipelines

`[  42 · paragraph]`

> - NLP pipelines

`[  43 · figure]` *(base64 157616 chars attached)*

> ![image](/image/placeholder)
> (a) PropBank representation S
> S s
> PP NP
> VP
> QP
> VP
> VP
> VP VP
> NP NP
> PP
> VP
> PP NP
> NP
> IN DT NN JJR IN CD CD NNS VBP VBN VBN CC DT JJ JJ NN VBZ VBN VBN IN CD NN IN CD NN
> I | I
> In that time more than 1.2 million jobs have been created and the official jobless rate has been pushed below 17 from 21 %
> ARG-1 ARG-2 ARGM-DIR
> ARG-TMP ARG-1

`[  44 · paragraph]`

> (b) FrameNet representation (three frames)

`[  45 · figure]` *(base64 114944 chars attached)*

> ![image](/image/placeholder)
> CARDINAL_NUMBERS INTENTIONALY_CREATE CAUSE_CHANGE_POSITION_ON A_SCALE
> million.NUM create.V push.V
> In that time more than 1.2 million jobs have been created and the official jobless rate has been pushed below 17% from 21%.
> Precision M Number E
> Time Created _entity
> Time Item Value 2 Value_ 1

`[  46 · footer]`

> Natural Language Processing (COSE461)


## Page 8

`[  47 · paragraph]`

> Sequence Models

`[  48 · paragraph]`

> Part-of-Speech Tagging

`[  49 · heading1]`

> Part-of-speech tags

`[  50 · list]`

> - Word classes or syntactic categories
> - Reveal useful information about a word (and its neighbors!)
> 1. The /DT cat/NN sat /VBD on /IN the/DT mat /NN

`[  51 · paragraph]`

> 2. KU/NNP is/VBZ in/IN Seoul /NNP

`[  52 · figure]` *(base64 136108 chars attached)*

> ![image](/image/placeholder)
> PRP VBZ NNS IN DT NN
> She sells seashells on the seashore
> Part Of Speech Tagging

`[  53 · footer]`

> Natural Language Processing (COSE461)


## Page 9

`[  54 · heading1]`

> Sequence Models

`[  55 · paragraph]`

> Part-of-Speech Tagging

`[  56 · heading1]`

> Part-of-speech tags

`[  57 · paragraph]`

> - Different words have different functions

`[  58 · paragraph]`

> - Can be roughly divided into two classes

`[  59 · paragraph]`

> - Closed class: fixed membership, function words
> e.g. prepositions (in, on, of), determiners (the, a)

`[  60 · paragraph]`

> - Open class: New words get added frequently
> e.g. nouns (Twitter, Facebook), verbs (google),
> adjectives, adverbs

`[  61 · figure]` *(base64 97740 chars attached)*

> ![image](/image/placeholder)
> Noun
> Interjection Pronoun
> Part of
> Conjunction Speech Verb
> (POS)
> Adverb
> Preposition
> Adjective

`[  62 · footer]`

> Natural Language Processing (COSE461)


## Page 10

`[  63 · heading1]`

> Sequence Models

`[  64 · paragraph]`

> Part-of-Speech Tagging

`[  65 · heading1]`

> Part-of-speech tags

`[  66 · paragraph]`

> - How many part of speech tags do you think
> English has?

`[  67 · list]`

> (A) < 10
> (B) 10 - 20
> (c) 20 - 40
> (D) > 40

`[  68 · figure]` *(base64 98932 chars attached)*

> ![image](/image/placeholder)
> Noun
> Interjection
> Pronoun
> Part of
> Conjunction Speech Verb
> (POS)
> Adverb
> Preposition
> Adjective

`[  69 · footer]`

> Natural Language Processing (COSE461)


## Page 11

`[  70 · header]`

> Sequence Models

`[  71 · paragraph]`

> Part-of-Speech Tagging

`[  72 · heading1]`

> Part-of-speech tags

`[  73 · paragraph]`

> - Penn treebank part-of-speech tag set

`[  74 · paragraph]`

> 45 tags (Marcus et al., 1993) based on Wall Street Journal (WSJ)

`[  75 · table]` *(base64 373620 chars attached)*

> | Tag | Description | Example | Tag | Description | Example | Tag | Description | Example |
> | --- | --- | --- | --- | --- | --- | --- | --- | --- |
> | CC | coordinating conjunction | and, but, or | PDT | predeterminer | all, both | VBP | verb non-3sg present | eat |
> | CD | cardinal number | one, two | POS | possessive ending | 's | VBZ | verb 3sg pres | eats |
> | DT | determiner | a, the | PRP | personal pronoun | I, you, he | WDT | wh-determ. | which, that |
> | EX | existential 'there' | there | PRP$ | possess. pronoun | your, one's | WP | wh-pronoun | what, who |
> | FW | foreign word | mea culpa | RB | adverb | quickly | WP$ | wh-possess. | whose |
> | IN | preposition/ subordin-conj | of, in, by | RBR | comparative adverb | faster | WRB | wh-adverb | how, where |
> | JJ | adjective | yellow | RBS | superlatv. adverb | fastest | $ | dollar sign |  |
> | JJR | comparative adj | bigger | RP | particle | up, off | # | pound sign | # |
> | JJS | superlative adj | wildest | SYM | symbol | +, %, & | " | left quote | or ' " |
> | LS | list item marker | 1, 2, One | TO | "to" | to | " | right quote | , " or |
> | MD | modal | can, should | UH | interjection | ah, oops |  | left paren | 666 < |
> | NN | sing or mass noun | llama | VB | verb base form | eat |  | right paren | ],),},> |
> | NNS | noun, plural | llamas | VBD | verb past tense | ate |  | comma | , |
> | NNP | proper noun, sing. | IBM | VBG | verb gerund | eating |  | sent-end punc | · ! ? |
> | NNPS | proper noun, plu. | Carolinas | VBN | verb past part. | eaten |  | sent-mid punc | : ; ··· |

`[  76 · footer]`

> Natural Language Processing (COSE461)


## Page 12

`[  77 · paragraph]`

> Sequence Models

`[  78 · heading1]`

> Part-of-Speech Tagging

`[  79 · heading1]`

> Part-of-speech ambiguous

`[  80 · paragraph]`

> - Tag each word in a sentence with its part of speech

`[  81 · paragraph]`

> - Disambiguation task: each word might have different functions in different contexts
> The/DT man/NN bought/VBD a/DT boat /NN
> same word but different tags
> The/DT old/NN man/VBP the/DT boat/NN

`[  82 · paragraph]`

> earnings growth took a back/JJ seat
> a small building in the back/NN
> a clear majority of senators back/VBP the bill
> Dave began to back/VB toward the door
> enable the country to buy back/RP about debt
> I was twenty-one back/RB then

`[  83 · paragraph]`

> some words have many functions

`[  84 · paragraph]`

> JJ: adjective, NN: single or mass noun, VBP: Verb, non-3rd person singular present VB: Verb,
> base form, RP: particle, RB: adverb

`[  85 · footer]`

> Natural Language Processing (COSE461)


## Page 13

`[  86 · paragraph]`

> Sequence Models

`[  87 · heading1]`

> Part-of-Speech Tagging

`[  88 · heading1]`

> Part-of-speech ambiguous

`[  89 · paragraph]`

> - Tag each word in a sentence with its part of speech

`[  90 · paragraph]`

> - Disambiguation task: each word might have different functions in different contexts

`[  91 · table]` *(base64 140456 chars attached)*

> | Types: | Types: | WSJ | Brown |
> | --- | --- | --- | --- |
> | Unambiguous | (1 tag) | 44,432 (86%) | 45,799 (85%) |
> | Ambiguous | (2+ tags) | 7,025 (14%) | 8,050 (15%) |
> | Tokens: | Tokens: | Tokens: | Tokens: |
> | Unambiguous | (1 tag) | 577,421 (45%) | 384,349 (33%) |
> | Ambiguous | (2+ tags) | 711,780 (55%) | 786,646 (67%) |

`[  92 · list]`

> - Types = distinct words in the corpus
> - Tokens = all words in the corpus (can be repeated)

`[  93 · paragraph]`

> Unambiguous types:
> Jane NNP
> hesitantly RB

`[  94 · footer]`

> Natural Language Processing (COSE461)


## Page 14

`[  95 · heading1]`

> Sequence Models

`[  96 · heading1]`

> Part-of-Speech Tagging

`[  97 · heading1]`

> Part-of-speech tagging performance

`[  98 · heading1]`

> - A simple baseline

`[  99 · paragraph]`

> motivation: many words might be easy to tag
> most frequent class: assign each word to the class it occurred most in the training set. (e.g.
> man/NN)

`[ 100 · paragraph]`

> - How accurate do you think this baseline would be at tagging words?

`[ 101 · paragraph]`

> (A) < 50%
> (B) 50-75%
> (c) 75-90%
> (D) > 90%

`[ 102 · list]`

`[ 103 · footer]`

> Natural Language Processing (COSE461)


## Page 15

`[ 104 · paragraph]`

> Sequence Models

`[ 105 · heading1]`

> Part-of-Speech Tagging

`[ 106 · paragraph]`

> Part-of-speech tagging performance

`[ 107 · heading1]`

> - A simple baseline

`[ 108 · paragraph]`

> motivation: many words might be easy to tag
> most frequent class: assign each word to the class it occurred most in the training set. (e.g.
> man/NN)

`[ 109 · paragraph]`

> - Accurately tags 92.34% of word tokens on Wall Street Journal (WSJ)!
> State-of-the-art performance ~ 97%
> Average English sentence ~ 14 words

`[ 110 · paragraph]`

> - Sentence level accuracies: 0.9214 = 31% VS 0.9714 = 65%
> POS tagging not solved yet!

`[ 111 · footer]`

> Natural Language Processing (COSE461)


## Page 16

`[ 112 · heading1]`

> Sequence Models

`[ 113 · paragraph]`

> Part-of-Speech Tagging

`[ 114 · paragraph]`

> How can we do better?

`[ 115 · paragraph]`

> - The function (or POS) of a word depends on its context
> The/ DT old /JJ man /NN bought/VBP the /DT boat/NN
> The/DT old/NN man /VBP the/DT boat/NN

`[ 116 · paragraph]`

> - Certain POS combinations are extremely unlikely
> <JJ, DT> ("good the") or <DT, IN> ("the in")

`[ 117 · paragraph]`

> - Better to make decisions on entire sentences instead of individual words

`[ 118 · footer]`

> Natural Language Processing (COSE461)


## Page 17

`[ 119 · paragraph]`

> Hidden Markov Model


## Page 18

`[ 120 · paragraph]`

> Transitive Verb Sentence (3형식 문장)

`[ 121 · paragraph]`

> Subject + Verb + Object

`[ 122 · paragraph]`

> ex) | like apples


## Page 19

`[ 123 · heading1]`

> Sequence Models

`[ 124 · paragraph]`

> Hidden Markov Chain

`[ 125 · heading1]`

> Markov chains

`[ 126 · list]`

> - Want to model the probability of difference sequences
> - Making an assumption that the next "state" only depends on current state

`[ 127 · paragraph]`

> Where have we seen this before?

`[ 128 · footer]`

> Natural Language Processing (COSE461)


## Page 20

`[ 129 · heading1]`

> Sequence Models

`[ 130 · paragraph]`

> Hidden Markov Chain

`[ 131 · heading1]`

> Markov chains

`[ 132 · paragraph]`

> - Each state can take one of K values (can assume
> {1,2, : K} for simplicity)

`[ 133 · paragraph]`

> - Markov assumption: P(st|S1,s2, ···,St-1) 2 P(st|st-1)

`[ 134 · paragraph]`

> - A Markov chain is specified by
> Initial probability distribution (), AS E {1,2, ..., K}
> Transition probability matrix (K × K)

`[ 135 · paragraph]`

> P(st|st-1): transition probability

`[ 136 · figure]` *(base64 93140 chars attached)*

> ![image](/image/placeholder)
> 0.01
> the
> 0.5 0.9
> 0.09 0.03
> 0.4
> runs dog
> 0.95
> 0.1 0.02

`[ 137 · footer]`

> Natural Language Processing (COSE461)


## Page 21

`[ 138 · heading1]`

> Sequence Models

`[ 139 · paragraph]`

> Hidden Markov Chain

`[ 140 · heading1]`

> Markov chains

`[ 141 · list]`

> - What is the probability of the sequence
> "the dog runs"? (Assume (the) = 0.8)

`[ 142 · list]`

> (A) 0.8 X 0.9 X 0.95
> (B) 0.8 X 0.99 X 0.98
> (c) 0.2x 0.9 X 0.95
> (D) 0.2x 0.01 X 0.02 X 0.1

`[ 143 · figure]` *(base64 109440 chars attached)*

> ![image](/image/placeholder)
> (the): initial distribution 0.01
> the
> 0.5 0.9
> 0.09 0.03
> 0.4
> runs dog
> 0.95
> 0.1 0.02

`[ 144 · footer]`

> Natural Language Processing (COSE461)


## Page 22

`[ 145 · heading1]`

> Sequence Models

`[ 146 · paragraph]`

> Hidden Markov Chain

`[ 147 · paragraph]`

> Markov chains for Part-of-speech

`[ 148 · paragraph]`

> - The/DT cat/NN sat /VBD on/IN the/DT mat /NN

`[ 149 · paragraph]`

> - We want the states to be the part of speech tags

`[ 150 · paragraph]`

> - Problem: We don't normally see sequences of POS
> tags appearing in text:

`[ 151 · paragraph]`

> The/?? cat/?? sat/?? on/?? the/?? mat/??

`[ 152 · figure]` *(base64 101064 chars attached)*

> ![image](/image/placeholder)
> 0.01
> DT
> 0.5 0.9
> 0.09 0.03
> 0.4
> VBD NN
> 0.95
> 0.1 0.02

`[ 153 · footer]`

> Natural Language Processing (COSE461)


## Page 23

`[ 154 · paragraph]`

> Sequence Models

`[ 155 · paragraph]`

> Hidden Markov Chain

`[ 156 · paragraph]`

> Hidden Markov Model (HMM)

`[ 157 · figure]` *(base64 101244 chars attached)*

> ![image](/image/placeholder)
> Tags ···
> (hidden events) S1 S2 S3 S4
> Words
> the cat sat on
> (observed events)

`[ 158 · list]`

> - We don't normally see sequences of POS tags in text
> - However, we do observe the words!
> - The HMM allows us to jointly reason over both hidden and observed events.
> - Assume that each position has a tag that generates a word

`[ 159 · footer]`

> Natural Language Processing (COSE461)


## Page 24

`[ 160 · paragraph]`

> Sequence Models

`[ 161 · paragraph]`

> Hidden Markov Chain

`[ 162 · paragraph]`

> Component of an HMM

`[ 163 · figure]` *(base64 100512 chars attached)*

> ![image](/image/placeholder)
> Tags ···
> (hidden events) S1 S2 S3 S4
> Words
> the cat sat on
> (observed events)

`[ 164 · list]`

> - Set of states S = {1,2, : , K} and sequence of observations 0 = {01, 02, ··· , on}, Oi E V
> - Initial state probability distribution (si)
> - Transition probabilities P(st+1|st)
> - Emission probabilities P(ot|st)

`[ 165 · footer]`

> Natural Language Processing (COSE461)


## Page 25

`[ 166 · paragraph]`

> Sequence Models

`[ 167 · heading1]`

> Hidden Markov Chain

`[ 168 · heading1]`

> Assumptions

`[ 169 · figure]` *(base64 103144 chars attached)*

> ![image](/image/placeholder)
> Tags S4
> (hidden events) S1 S2 S3
> Words
> the cat sat on
> (observed events)

`[ 170 · paragraph]`

> - Markov assumption:

`[ 171 · paragraph]`

> P(st|S1, S2, ··· , St-1) 11 P(st|st-1)

`[ 172 · paragraph]`

> - Output independence:

`[ 173 · equation]` *(base64 10712 chars attached)*

> P(ot|S1, S2, ··· , st) 11 P(ot|st)

`[ 174 · footer]`

> Natural Language Processing (COSE461)


## Page 26

`[ 175 · paragraph]`

> Sequence Models

`[ 176 · paragraph]`

> Hidden Markov Chain

`[ 177 · heading1]`

> Sequence likelihood

`[ 178 · figure]` *(base64 99900 chars attached)*

> ![image](/image/placeholder)
> Tags ···
> (hidden events) S1 S2 S3 S4
> Words
> the cat sat on
> ···
> (observed events)

`[ 179 · heading1]`

> - Markov assumption:

`[ 180 · equation]` *(base64 38752 chars attached)*

> P(S,O) = P(S1,S2, ··· , Sn, 01, 02, ··· , On)
>  (s1)p(01|s1)n=2 P(silsi-1)P(oilsi)
>  transition emission
>  probability probability

`[ 181 · paragraph]`

> - If we add a dummy state SO =  at the beginning,

`[ 182 · footer]`

> P(S,O) = i=1P(si|si-1)P(oilsi) (si) = p(s1|⌀)


## Page 27

`[ 183 · paragraph]`

> Sequence Models

`[ 184 · heading1]`

> Hidden Markov Chain

`[ 185 · heading1]`

> Example: Sequence likelihood

`[ 186 · figure]` *(base64 269548 chars attached)*

> ![image](/image/placeholder)
> Tags ···
> (hidden events) S1 S2 S3 S4
> Words
> the cat sat on
> ···
> (observed events)
> - What is the joint probability
> Dummy St
> P(the cat, DT NN)?
> start state Ot
> DT NN
> the cat
> 0.8 0.2 (A) (0.8 * 0.8) * (0.9 * 0.5)
> St-1 St DT 0.9 0.1 (B) (0.2 * 0.8) * (0.9 * 0.5)
> DT 0.2 0.8
> NN 0.5 0.5 (c) (0.3 * 0.7) * (0.5 * 0.5)
> NN 0.3 0.7 (D) (0.8 * 0.2) * (0.5 * 0.1)

`[ 187 · footer]`

> Natural Language Processing (COSE461)


## Page 28

`[ 188 · heading1]`

> Sequence Models

`[ 189 · paragraph]`

> Hidden Markov Chain

`[ 190 · heading1]`

> Learning

`[ 191 · paragraph]`

> Training set:

`[ 192 · paragraph]`

> 1 Pierre / NNP Vinken /NNP 1/1 61 /CD years / NNS old /JJ ,/, will /MD
> join /VB the /DT board / NN as /IN a/DT nonexecutive / JJ director /NN
> Nov. NNP 29 /CD /
> 2 Mr. /NNP Vinken / NNP is /VBZ chairman /NN of /IN Elsevier /NNP
> N.V. /NNP ,/, the /DT Dutch /NNP publishing /VBG group / NN /
> 3 Rudolph /NNP Agnew /NNP 1, 55 /CD years / NNS old / JJ and/CC
> chairman /NN of /IN Consolidated / NNP Gold / NNP Fields / NNP PLC /NNP
> / was /VBD named /VBN a /DT nonexecutive / JJ director /NN of /IN
> this/DT British / JJ industrial / JJ conglomerate / NN ./.

`[ 193 · equation]` *(base64 18180 chars attached)*

> Count(o, s)
>  P(o|s)
>  Count(s)

`[ 194 · paragraph]`

> 38,219 It/PRP is /VBZ also /RB pulling /VBG 20 /CD people/ NNS out /IN
> of/IN Puerto /NNP Rico / NNP / who /WP were /VBD helping /VBG
> Huricane / NNP Hugo / NNP victims /NNS / and /CC sending /VBG
> Q:
> them  PRP to /TO San 1 NNP Francisco /NNP instead /RB /

`[ 195 · paragraph]`

> - Maximum likelihood estimates:

`[ 196 · equation]` *(base64 20936 chars attached)*

> Count(sj, si)
>  P(silsj)
>  Count (sj

`[ 197 · paragraph]`

> How many probabilities to estimate?
> A: transition probabilities (K + 1) × (K)
> emission probabilities 121 × K

`[ 198 · footer]`

> Natural Language Processing (COSE461)


## Page 29

`[ 199 · heading1]`

> Sequence Models

`[ 200 · paragraph]`

> Hidden Markov Chain

`[ 201 · heading1]`

> Learning example

`[ 202 · paragraph]`

> - In our corpus:

`[ 203 · list]`

> 1. The/DT cat/NN sat /VBD on/IN the/DT mat /NN
> 2. KU/ NNP is/VBZ in/IN Seoul/NNP
> 3. The/DT old/NN man/VBP the/DT boat/NN

`[ 204 · paragraph]`

> - Estimates

`[ 205 · paragraph]`

> (DT) = P(DT|) = 2/3

`[ 206 · paragraph]`

> P(NN|DT) = 4/4 P(DT|IN) = 1/2

`[ 207 · paragraph]`

> assuming we differentiate
> P(cat|NN) = 1/4 P(the|DT) = 2/4
> cased VS uncased words

`[ 208 · footer]`

> Natural Language Processing (COSE461)


## Page 30

`[ 209 · paragraph]`

> Decoding with HMMs


## Page 31

`[ 210 · paragraph]`

> Sequence Models

`[ 211 · heading1]`

> Decoding with HMMs

`[ 212 · heading1]`

> Problem

`[ 213 · figure]` *(base64 99364 chars attached)*

> ![image](/image/placeholder)
> Tags ···
> (hidden events) S1 S2 S3 S4
> Words
> the cat sat on
> (observed events)

`[ 214 · paragraph]`

> - Task: find the most probable sequence of states S = S1, S2, ·· · Sn given the
> ,
> observations 0 = 01, 02, : · On
> ,

`[ 215 · paragraph]`

> P(O|S)P(S)

`[ 216 · heading1]`

> S = ar gmaxsP(S|O) = ar gmaxs

`[ 217 · paragraph]`

> [Bayes' Rule]

`[ 218 · paragraph]`

> P(O)

`[ 219 · paragraph]`

> - ar gmaxs1,...,sn i=1P(silsi-1)P(oilsi)

`[ 220 · paragraph]`

> = ar gmaxsP(O|S)P(S) [Drop P(O), it doesn't depend on s]

`[ 221 · paragraph]`

> How can we maximize this?
> Search over all state sequences?

`[ 222 · footer]`

> Natural Language Processing (COSE461)


## Page 32

`[ 223 · paragraph]`

> Sequence Models

`[ 224 · paragraph]`

> Decoding with HMMs

`[ 225 · paragraph]`

> Greedy search

`[ 226 · figure]` *(base64 93508 chars attached)*

> ![image](/image/placeholder)
> Decode tag ? ? ? ?
> Words
> the cat sat on
> (observed events)

`[ 227 · paragraph]`

> - Idea: decode one state at time

`[ 228 · paragraph]`

> ar gmaxs(s1 = s)P(The|s) = DT

`[ 229 · footer]`

> Natural Language Processing (COSE461)


## Page 33

`[ 230 · paragraph]`

> Sequence Models

`[ 231 · paragraph]`

> Decoding with HMMs

`[ 232 · paragraph]`

> Greedy search

`[ 233 · figure]` *(base64 95960 chars attached)*

> ![image](/image/placeholder)
> Decode tag DT ? ? ?
> Words
> the cat sat on
> (observed events)

`[ 234 · paragraph]`

> - Idea: decode one state at time

`[ 235 · paragraph]`

> ar gmaxsP(s|DT)P(cat|s) = NN

`[ 236 · footer]`

> Natural Language Processing (COSE461)


## Page 34

`[ 237 · paragraph]`

> Sequence Models

`[ 238 · paragraph]`

> Decoding with HMMs

`[ 239 · paragraph]`

> Greedy search

`[ 240 · figure]` *(base64 97704 chars attached)*

> ![image](/image/placeholder)
> Decode tag DT NN ? ?
> Words
> the cat sat on
> (observed events)

`[ 241 · paragraph]`

> - Idea: decode one state at time

`[ 242 · equation]` *(base64 13936 chars attached)*

> ^S t = ar gmaxsP(s|t-1)P(ot|s)

`[ 243 · paragraph]`

> - Very efficient but not guaranteed to be optimum!

`[ 244 · footer]`

> Natural Language Processing (COSE461)


## Page 35

`[ 245 · paragraph]`

> Sequence Models

`[ 246 · paragraph]`

> Decoding with HMMs

`[ 247 · paragraph]`

> Viterbi decoding

`[ 248 · paragraph]`

> - Use dynamic programming

`[ 249 · paragraph]`

> - Maintain some extra data structures

`[ 250 · paragraph]`

> - Probability lattice, M[T,K] and backtracking matrix, B[T,K]

`[ 251 · paragraph]`

> T: number of time steps
> K: number of states
> M[i,j] stores joint probability of most probable sequence of states ending with state j at
> time i
> B[i,j] is the tag at time i - 1 in the most probable sequence ending with tag j at time i

`[ 252 · footer]`

> Natural Language Processing (COSE461)


## Page 36

`[ 253 · heading1]`

> Sequence Models

`[ 254 · paragraph]`

> Decoding with HMMs

`[ 255 · paragraph]`

> Motivation: Viterbi decoding

`[ 256 · paragraph]`

> - Recall: we want to compute S = ar gmaxs1,...,sn i=1P(oi|si)P(silsi-1)

`[ 257 · paragraph]`

> - Let's first see how we can compute the maximum probability

`[ 258 · equation]` *(base64 30256 chars attached)*

> i=1P(oilsi)P(silsi-1)
>  maxs1,...,sn
>  P(on|sn) · P(On-1|sn-1) · · · · P(02|s2)
>  maxs1,...,sn

`[ 259 · paragraph]`

> P(S2|S1) · P(01|s1) · P(s1)

`[ 260 · paragraph]`

> These are the only terms
> that depend on S1!

`[ 261 · footer]`

> Natural Language Processing (COSE461)


## Page 37

`[ 262 · heading1]`

> Sequence Models

`[ 263 · paragraph]`

> Decoding with HMMs
> Motivation: Viterbi decoding

`[ 264 · table]` *(base64 83408 chars attached)*

> | maxs1,...,sn | i=1P(oilsi)P(silsi-1) |
> | --- | --- |
> | maxs1,...,sn | P(on|sn) · P(On-1|sn-1) · · · · P(02|s2) · P(S2|S1) · P(01|s1) · P(S1) |
> | maxs2,...,sn | P(on|sn) · P(On-1|sn-1) · · · · P(02|s2) · maxs1 P(S2|S1) · P(01|S1) · P(s1) |

`[ 265 · footer]`

> Natural Language Processing (COSE461)


## Page 38

`[ 266 · heading1]`

> Sequence Models

`[ 267 · paragraph]`

> Decoding with HMMs

`[ 268 · heading1]`

> Motivation: Viterbi decoding

`[ 269 · table]` *(base64 153796 chars attached)*

> | maxs1,...,sn i=1P(oi|si)P(silsi-1) | Define |
> | --- | --- |
> | = maxs1,...,sn P(on|sn) · P(On-1|sn-1) · · : P(02|s2) · P(S2|S1) · P(01|s1) · P(S1) score1 (s) = P(01|s) · P(s) | = maxs1,...,sn P(on|sn) · P(On-1|sn-1) · · : P(02|s2) · P(S2|S1) · P(01|s1) · P(S1) score1 (s) = P(01|s) · P(s) |
> | max P(on|sn) · P(On-1|sn-1) · ··· P(02|s2) · maxs1 P(S2|S1) S2,...,Sn | P(01|s1) · P(s1) |
> | = max P(on|sn) · P(On-1|sn-1) · : · P(02|s2) · maxs1 P(S2|S1) · score1 (S1) S2,...,Sn | = max P(on|sn) · P(On-1|sn-1) · : · P(02|s2) · maxs1 P(S2|S1) · score1 (S1) S2,...,Sn |

`[ 270 · footer]`

> Natural Language Processing (COSE461)


## Page 39

`[ 271 · paragraph]`

> Sequence Models

`[ 272 · heading1]`

> Decoding with HMMs

`[ 273 · heading1]`

> Motivation: Viterbi decoding

`[ 274 · table]` *(base64 178024 chars attached)*

> | max S1,...,Sn i=1P(oilsi)P(silsi-1) maxs2,...,sn P(on|sn) · P(On-1|sn-1) · ··· P(02|s2) · maxs1 P(S2|S1) · P(01|s1) · P(s1) | max S1,...,Sn i=1P(oilsi)P(silsi-1) maxs2,...,sn P(on|sn) · P(On-1|sn-1) · ··· P(02|s2) · maxs1 P(S2|S1) · P(01|s1) · P(s1) | max S1,...,Sn i=1P(oilsi)P(silsi-1) maxs2,...,sn P(on|sn) · P(On-1|sn-1) · ··· P(02|s2) · maxs1 P(S2|S1) · P(01|s1) · P(s1) |
> | --- | --- | --- |
> | = maxs1,...,sn P(on|sn) · P(On-1|sn-1) · · : P(02|s2) · P(S2|S1) · P(01|s1) · P(S1) | = maxs1,...,sn P(on|sn) · P(On-1|sn-1) · · : P(02|s2) · P(S2|S1) · P(01|s1) · P(S1) | = maxs1,...,sn P(on|sn) · P(On-1|sn-1) · · : P(02|s2) · P(S2|S1) · P(01|s1) · P(S1) |
> |  |  |  |
> | □ maxs2,...,sn P(on|sn) · P(On-1|sn-1) · ··· P(02|s2) · maxs1 P(S2|S1) · score1 (S1) | □ maxs2,...,sn P(on|sn) · P(On-1|sn-1) · ··· P(02|s2) · maxs1 P(S2|S1) · score1 (S1) | □ maxs2,...,sn P(on|sn) · P(On-1|sn-1) · ··· P(02|s2) · maxs1 P(S2|S1) · score1 (S1) |
> | max P(on|sn) · P(On-1|sn-1) · : · P(03|s3) S3,...,Sn | maxs2 P(S3|S2) · P(02|s2) · maxs1 P(S2|S1) | score1 (S1) |

`[ 275 · paragraph]`

> Only terms that depend on S2

`[ 276 · footer]`

> Natural Language Processing (COSE461)


## Page 40

`[ 277 · paragraph]`

> Sequence Models

`[ 278 · heading1]`

> Decoding with HMMs

`[ 279 · paragraph]`

> Motivation: Viterbi decoding

`[ 280 · list]`

> max S1,...,Sn i=1P(oilsi)P(silsi-1)
> P(on|sn) · P(On-1|sn-1) · · : P(02|s2) · P(S2|S1) · P(01|s1) · P(S1)
> = maxs1,...,sn
> P(on|sn) · P(On-1|sn-1) · ··· P(02|s2) · maxs1 P(S2|S1) · P(01|s1) · P(s1)
> maxs2,...,sn
> P(on|sn) · P(On-1|sn-1) · ··· P(02|s2) · maxs1 P(S2|S1) · score1 (S1)
> = maxs2,...,sn
> max P(on|sn) · P(On-1|sn-1) · ··· P(03|S3) · maxs2 P(s3|s2) P(02|s2) · maxs1 P(S2|S1) · score1 (S1)
> S3,...,Sn

`[ 281 · paragraph]`

> Define
> scorei(s) = maxsi-1 P(s|si-1) · P(oi|s) · scorei-1 (Si-1)

`[ 282 · footer]`

> Natural Language Processing (COSE461)


## Page 41

`[ 283 · paragraph]`

> Sequence Models

`[ 284 · paragraph]`

> Decoding with HMMs

`[ 285 · heading1]`

> Motivation: Viterbi decoding

`[ 286 · heading1]`

> max S1,...,Sn i=1P(oilsi)P(silsi-1)

`[ 287 · list]`

> P(on|sn) · P(On-1|sn-1) · · : P(02|s2) · P(S2|S1) · P(01|s1) · P(s1)
> = maxs1,...,sn
> P(on|sn) · P(On-1|sn-1) · : · P(02|s2) · maxs1 P(S2|S1) · P(01|s1) · P(s1)
> maxs2,...,sn
> P(on|sn) · P(On-1|sn-1) · : · P(02|s2) · maxs1 P(S2|S1) · score1 (S1)
> = maxs2,...,sn
> max P(on|sn) · P(On-1|sn-1) · : · P(03|S3) · maxs2 P(s3|s2) · P(02|s2) · maxs1 P(S2|S1) · score1 (S1)
> S3,...,Sn
> max P(on|sn) · P(On-1|sn-1) · ··· P(03|s3) · maxs2 P(s3|s2) · score2 (S2)
> S3,...,Sn

`[ 288 · footer]`

> Natural Language Processing (COSE461)


## Page 42

`[ 289 · heading1]`

> Sequence Models

`[ 290 · heading1]`

> Decoding with HMMs

`[ 291 · heading1]`

> Viterbi decoding

`[ 292 · table]` *(base64 175172 chars attached)*

> | 4 possible POS tags | DT | M[1, DT] = (DT)P(the|DT) |
> | --- | --- | --- |
> | 4 possible POS tags | NN | M[1, NN] = (NN)P(the INN) |
> | 4 possible POS tags | VBD | M[1, VBD] = (VBD)P(the|VBD) |
> | 4 possible POS tags | IN | M[1, IN] = (IN)P(the|IN) |
> | 4 possible POS tags | the | Initialize the table: score1 (s1) = P(01|s1) · P(S1) in M[1, : ] |

`[ 293 · footer]`

> Natural Language Processing (COSE461)


## Page 43

`[ 294 · heading1]`

> Sequence Models

`[ 295 · heading1]`

> Decoding with HMMs

`[ 296 · heading1]`

> Viterbi decoding

`[ 297 · table]` *(base64 294796 chars attached)*

> | 4 possible POS tags |  | Consider all possible previous tags |
> | --- | --- | --- |
> | 4 possible POS tags | DT DT | M[2, DT] = max M[1, k]P(DT|k) P(cat|DT) k |
> | 4 possible POS tags | NN NN | M[2, NN] = max M[1, k]P(NN|k) P(cat|NN) k |
> | 4 possible POS tags | VBD VBD | M[2, VBD] = max M[1,k]P(VBD|k) P(cat|VBD) k |
> | 4 possible POS tags | IN IN | M[2, IN] = max M[1, k] P(IN|k)P(cat|IN) k |
> | 4 possible POS tags | the cat | Next: we store score2 (s) = max P(s|s1) · P(o2|s) · M[1,s1] in M[2,:] S1 |

`[ 298 · figure]` *(base64 294796 chars attached)*

> ![image](/image/placeholder)

`[ 299 · footer]`

> Natural Language Processing (COSE461)


## Page 44

`[ 300 · heading1]`

> Sequence Models

`[ 301 · paragraph]`

> Decoding with HMMs

`[ 302 · heading1]`

> Viterbi decoding

`[ 303 · paragraph]`

> ···

`[ 304 · figure]` *(base64 194828 chars attached)*

> ![image](/image/placeholder)
> DT DT DT DT
> NN NN NN NN
> VBD VBD VBD VBD
> IN IN IN IN
> the cat sat on

`[ 305 · heading1]`

> ···

`[ 306 · paragraph]`

> - What is the time complexity
> of this algorithm?

`[ 307 · list]`

> (A) 0(n)

`[ 308 · paragraph]`

> (B) O(nK)

`[ 309 · paragraph]`

> The answer is (c)

`[ 310 · paragraph]`

> (c) O(nK2)

`[ 311 · list]`

> (D) O(n2K)

`[ 312 · paragraph]`

> n = number of timesteps

`[ 313 · paragraph]`

> K = number of states

`[ 314 · heading1]`

> k

`[ 315 · paragraph]`

> M[i,j] = max M[i - 1,k]P(sj|sk)P(oi|sj) 1≤k≤K 1 ≤ i ≤ n

`[ 316 · footer]`

> Natural Language Processing (COSE461)


## Page 45

`[ 317 · heading1]`

> Sequence Models

`[ 318 · paragraph]`

> Decoding with HMMs

`[ 319 · heading1]`

> Viterbi decoding

`[ 320 · heading1]`

> - Backward:

`[ 321 · paragraph]`

> Pick max M [n, k] and backtrack using B
> k

`[ 322 · paragraph]`

> - In practice, we maximize sum of log
> probabilities (or minimize the sum of
> negative log probabilities) instead of
> maximize the product of probabilities

`[ 323 · paragraph]`

> M[2, NN] = max{M[1, k] P(NN|k) P(cat|NN)}
> k
> M[2,NN] =
> max{M[1, k] + log P(NN|k) + log P(cat|NN)}
> k

`[ 324 · figure]` *(base64 199000 chars attached)*

> ![image](/image/placeholder)
> DT DT DT DT ···
> NN NN NN NN
> VBD VBD VBD VBD
> IN IN IN IN
> the cat sat on ···

`[ 325 · footer]`

> Natural Language Processing (COSE461)


## Page 46

`[ 326 · paragraph]`

> Sequence Models

`[ 327 · paragraph]`

> Decoding with HMMs

`[ 328 · heading1]`

> Example: Viterbi decoding

`[ 329 · paragraph]`

> - Suppose we want to compute tags for the phrase "the cat runs"

`[ 330 · table]` *(base64 150504 chars attached)*

> | - We need to compute the M and B matrices |  |
> | --- | --- |
> | DT | <table><thead><tr><td></td><td>DT</td><td>NN</td><td>VB</td></tr></thead><tbody><tr><td></td><td>0.5</td><td>0.3</td><td>0.2</td></tr><tr><td>DT</td><td>0.1</td><td>0.5</td><td>0.4</td></tr><tr><td>NN</td><td>0.2</td><td>0.3</td><td>0.5</td></tr><tr><td>VB</td><td>0.4</td><td>0.3</td><td>0.3</td></tr></tbody></table> |
> | NN |  |
> | VB | <table><thead><tr><td></td><td>the</td><td>cat</td><td>runs</td></tr></thead><tbody><tr><td>DT</td><td>0.4</td><td>0.5</td><td>0.1</td></tr><tr><td>NN</td><td>0.5</td><td>0.4</td><td>0.1</td></tr><tr><td>VB</td><td>0.2</td><td>0.3</td><td>0.5</td></tr></tbody></table> |
> | the |  |

`[ 331 · footer]`

> Natural Language Processing (COSE461)


## Page 47

`[ 332 · paragraph]`

> Sequence Models

`[ 333 · paragraph]`

> Decoding with HMMs

`[ 334 · heading1]`

> Motivation: Beam search

`[ 335 · list]`

> - If K (number of possible hidden states) is too large, Viterbi is too expensive
> - Observation: many paths have very low likelihood

`[ 336 · paragraph]`

> ···

`[ 337 · paragraph]`

> ···

`[ 338 · figure]` *(base64 183284 chars attached)*

> ![image](/image/placeholder)
> 0.0001 0.0001 0.0001
> DT DT DT DT
> 0.001
> NN NN NN NN
> 0.3 0.1
> VBD VBD 0.01 0.01 VBD
> VBD
> 0.00001
> IN IN IN IN
> the cat sat on

`[ 339 · chart]` *(base64 183284 chars attached)*

> ![image](/image/placeholder)
> - Chart Type: bar
> |  | DT | NN | VBD | IN | cat | sat | on |
> | --- | --- | --- | --- | --- | --- | --- | --- |
> | item_01 | 0.0001 | 0.001 | 0.3 | 0.001 | 0.01 | 0.0001 | 0.0001 |

`[ 340 · paragraph]`

> O(nK2)

`[ 341 · footer]`

> Natural Language Processing (COSE461)


## Page 48

`[ 342 · heading1]`

> Sequence Models

`[ 343 · paragraph]`

> Decoding with HMMs

`[ 344 · paragraph]`

> Beam search

`[ 345 · list]`

> - Keep a fixed number of hypotheses at each point
> - Beam width,

`[ 346 · paragraph]`

> DT

`[ 347 · paragraph]`

> score = -0.1

`[ 348 · paragraph]`

> NN

`[ 349 · paragraph]`

> score = -9.8

`[ 350 · paragraph]`

> = 2

`[ 351 · paragraph]`

> VBD

`[ 352 · paragraph]`

> score = -0.7

`[ 353 · paragraph]`

> IN

`[ 354 · paragraph]`

> score □ -10.1

`[ 355 · paragraph]`

> the

`[ 356 · paragraph]`

> log probabilities

`[ 357 · footer]`

> Natural Language Processing (COSE461)


## Page 49

`[ 358 · paragraph]`

> Sequence Models

`[ 359 · paragraph]`

> Decoding with HMMs

`[ 360 · paragraph]`

> Beam search

`[ 361 · list]`

> - Keep a fixed number of hypotheses at each point

`[ 362 · list]`

> - Beam width,

`[ 363 · paragraph]`

> = 2

`[ 364 · paragraph]`

> Step 1: Expand all partial sequences in current beam

`[ 365 · figure]` *(base64 122988 chars attached)*

> ![image](/image/placeholder)
> score = -16.5
> DT DT
> score = -6.5
> score = -3.0
> NN NN
> score = -22.1
> score = -0.5
> VBD VBD
> score = -13.5
> score = -32.0
> IN IN
> score = -20.3
> the cat

`[ 366 · paragraph]`

> Accumulated scores

`[ 367 · footer]`

> Natural Language Processing (COSE461)


## Page 50

`[ 368 · paragraph]`

> Sequence Models

`[ 369 · paragraph]`

> Decoding with HMMs

`[ 370 · paragraph]`

> Beam search

`[ 371 · list]`

> - Keep a fixed number of hypotheses at each point

`[ 372 · list]`

> - Beam width,

`[ 373 · paragraph]`

> = 2

`[ 374 · paragraph]`

> Step 2: Prune back to top  scores (sort and select) · · repeat!

`[ 375 · figure]` *(base64 100160 chars attached)*

> ![image](/image/placeholder)
> score = -16.5
> DT DT
> score = -6.5
> score = -3.0
> NN NN
> score = -22.1
> score = -0.5
> V VBD
> score = -13.5
> score = -32.0
> IN IN
> score = -20.3
> the cat

`[ 376 · paragraph]`

> Accumulated scores

`[ 377 · footer]`

> Natural Language Processing (COSE461)


## Page 51

`[ 378 · paragraph]`

> Sequence Models

`[ 379 · heading1]`

> Decoding with HMMs

`[ 380 · heading1]`

> Beam search

`[ 381 · list]`

> - Keep a fixed number of hypotheses at each point
> - Beam width,

`[ 382 · paragraph]`

> = 2

`[ 383 · table]` *(base64 245336 chars attached)*

> |  | - What is the time complexity of this algorithm? |
> | --- | --- |
> |  |  |
> |  | n = number of timesteps K states |
> | ![image](/image/placeholder)
> DT DT DT DT
> NN NN NN
> VBD VBD VBD
> IN IN IN IN
> the cat sat on | = number of  = beam width |
> |  | A: O(nK) |
> |  |  |
> |  |  |
> |  | Pick max M[n, k] |
> |  | from within beam and backtrack k (COSE461) |

`[ 384 · footer]`

> Natural Language Processing


## Page 52

`[ 385 · heading1]`

> Sequence Models

`[ 386 · heading1]`

> Decoding with HMMs

`[ 387 · heading1]`

> Beam search

`[ 388 · paragraph]`

> - If K (number of states) is too large, Viterbi is too expensive

`[ 389 · paragraph]`

> - Keep a fixed number of hypotheses at each point
> Beam width,

`[ 390 · list]`

`[ 391 · paragraph]`

> - Trade-off (some) accuracy for computational savings

`[ 392 · paragraph]`

> - Final remark: beam search is a common decoding method for any language
> generation tasks (e.g., n-gram LMs, GPT-3)

`[ 393 · footer]`

> Natural Language Processing (COSE461)


## Page 53

`[ 394 · heading1]`

> Sequence Models

`[ 395 · paragraph]`

> Decoding with HMMs

`[ 396 · paragraph]`

> Trigram hidden Markov models

`[ 397 · paragraph]`

> - What we have seen SO far is also bigram HMM

`[ 398 · paragraph]`

> - Can be extended to trigram, 4-gram etc..
> P(S,O) = n=1P(silsi-1, Si-2)P(oi|si)

`[ 399 · paragraph]`

> Count(si,si-1,si-2)
> - MLE estimate: P(Silsi-1,si-2)
> Count(si-1,si-2)

`[ 400 · paragraph]`

> - Viterbi: M[i,j,k] = max M[i - 1,k,r]P(sj|sk, sr)P(oi|sj) 1 ≤j,k,r ≤ K 1 ≤ i ≤ n
> r

`[ 401 · paragraph]`

> most probable sequence of states ending
> with state j at time i, and state k at i - 1

`[ 402 · paragraph]`

> Time complexity: O(nK3)

`[ 403 · footer]`

> Natural Language Processing (COSE461)


## Page 54

`[ 404 · paragraph]`

> Maximum Entropy Markov Models (MEMMs)
> ICML 2000


## Page 55

`[ 405 · header]`

> Sequence Models

`[ 406 · paragraph]`

> Maximum Entropy Markov Models

`[ 407 · heading1]`

> Motivation: MEMMs

`[ 408 · paragraph]`

> - Can we model P(S1, · · · , sn|01, · · · On) directly?
> ,

`[ 409 · figure]` *(base64 72180 chars attached)*

> ![image](/image/placeholder)
> DT NN VB IN
> the cat sat on
> ···

`[ 410 · paragraph]`

> HMM

`[ 411 · figure]` *(base64 83920 chars attached)*

> ![image](/image/placeholder)
> DT NN VB IN
> the cat sat on
> ···
> MEMM

`[ 412 · footer]`

> Natural Language Processing (COSE461)


## Page 56

`[ 413 · header]`

> Sequence Models

`[ 414 · paragraph]`

> Maximum Entropy Markov Models

`[ 415 · paragraph]`

> Definition of MEMM

`[ 416 · paragraph]`

> - Can we model P(S1, · · · ,sn|01, · · · On) directly?
> ,

`[ 417 · figure]` *(base64 81364 chars attached)*

> ![image](/image/placeholder)
> DT NN VB IN ···
> ···
> the cat sat on

`[ 418 · paragraph]`

> P(S|O) = i=1P(silsi-1, Si-2, ··· , S1, 0) 0 = < 01, 02, : · , On >
> = i=1P(silsi-1, 0) Markov assumption: Bigram MEMM
> P(si = S |Si-1, 0)  exp (w · f(si = S,Si-1, 0,i) ) Important: you can define features
> over entire word sequence O
> weight features

`[ 419 · footer]`

> Natural Language Processing (COSE461)


## Page 57

`[ 420 · paragraph]`

> Sequence Models

`[ 421 · heading1]`

> Maximum Entropy Markov Models

`[ 422 · heading1]`

> Definition of MEMM

`[ 423 · paragraph]`

> - Use features and weights: P(Si = S |Si-1, 0)  exp(w · f(si = S,Si-1, 0,i))

`[ 424 · paragraph]`

> - Which of the following is the correct way to calculate this probability?

`[ 425 · list]`

`[ 426 · list]`

> exp(w-f(si=s,si-1,0,i))
> (A) P(si = S |Si-1, 0)
> s'=1 exp(w·f(si=s,si-1=s',0,i)

`[ 427 · paragraph]`

> exp(w・f(si=s,si-1,0,i))
> (B) P(Si = S |Si-1, 0)
> s/=1 exp(w·f(si=s',si-1,0,i))

`[ 428 · paragraph]`

> exp(w·f(si=s,si-1,0,i))
> (c) P(Si = S |Si-1, 0)
> s/=1 exp(w·f(si=s,si-1,0',i))

`[ 429 · list]`

`[ 430 · footer]`

> Natural Language Processing (COSE461)


## Page 58

`[ 431 · header]`

> Sequence Models

`[ 432 · paragraph]`

> Maximum Entropy Markov Models

`[ 433 · paragraph]`

> Trigram MEMM

`[ 434 · paragraph]`

> - Bigram MEMM:

`[ 435 · equation]` *(base64 36392 chars attached)*

> exp(w · f(si = S,Si-1, 0,i))
>  P(Si = S|Si-1, 0) =
>  K'=1 exp ( w · f(si = S',Si-1' 0,i))

`[ 436 · paragraph]`

> - Can be easily extended to trigram MEMM, 4-gram MEMM...

`[ 437 · equation]` *(base64 40176 chars attached)*

> exp(w · f(si = S,Si-1,Si-2, 0,i))
>  P(Si = S|Si-1,Si-2, 0) =
>  K'=1 exp ( w · f(si = S',Si-1,Si-2, 0,i))

`[ 438 · footer]`

> Natural Language Processing (COSE461)


## Page 59

`[ 439 · heading1]`

> Sequence Models

`[ 440 · heading1]`

> Maximum Entropy Markov Models

`[ 441 · heading1]`

> How to define features?

`[ 442 · paragraph]`

> - Feature templates f(si = S',Si-1,Si-2, 0,i)

`[ 443 · equation]` *(base64 11460 chars attached)*

> < Si, Oi-2 >,< Si, 0i-1 >,<Si,0i >,<Si, 0i+1 >,< Si, 0i+2 >,< Si, Si-1 >,< Si,Si-1,Si-2 >

`[ 444 · paragraph]`

> - Features (binary)

`[ 445 · table]` *(base64 31620 chars attached)*

> | Si | = VB and Oi-2 = Janet |
> | --- | --- |
> | Si | = VB and Oi-1 = will |
> | Si | = VB and Si-1 = MD |

`[ 446 · figure]` *(base64 91980 chars attached)*

> ![image](/image/placeholder)
> Si-2 Si-1
> NNP MD VB
> Janet will back the
> Oi-2 0i-1 Oi 0i+1

`[ 447 · paragraph]`

> ···

`[ 448 · paragraph]`

> - Example

`[ 449 · paragraph]`

> 1, Oi = 'back' and Si-1 = MD
> f :=
> 0, otherwise

`[ 450 · footer]`

> Natural Language Processing (COSE461)


## Page 60

`[ 451 · header]`

> Sequence Models

`[ 452 · heading1]`

> Maximum Entropy Markov Models

`[ 453 · paragraph]`

> Decoding

`[ 454 · paragraph]`

> - Bigram MEMM:

`[ 455 · heading1]`

> S = ar gmaxsP(S|O) = ar gmaxsiP(si|si-1, 0)

`[ 456 · paragraph]`

> - Greedy decoding:

`[ 457 · figure]` *(base64 88996 chars attached)*

> ![image](/image/placeholder)
> DT ? ? ?
> the cat sat on

`[ 458 · paragraph]`

> S1 = ar gmaxsP(si = s⌀, 0) = ar gmaxs W · f(si = S, Si-1 = ,0) = DT

`[ 459 · footer]`

> Natural Language Processing (COSE461)


## Page 61

`[ 460 · header]`

> Sequence Models

`[ 461 · heading1]`

> Maximum Entropy Markov Models

`[ 462 · paragraph]`

> Decoding

`[ 463 · paragraph]`

> - Bigram MEMM:

`[ 464 · paragraph]`

> S ar gmaxsP(S|O) = ar gmaxsiP(si|si-1, 0)

`[ 465 · paragraph]`

> - Greedy decoding:

`[ 466 · figure]` *(base64 88460 chars attached)*

> ![image](/image/placeholder)
> DT NN ? ?
> the cat sat on

`[ 467 · paragraph]`

> S2 = ar gmaxsP(si = s|DT, 0) = NN

`[ 468 · footer]`

> Natural Language Processing (COSE461)


## Page 62

`[ 469 · header]`

> Sequence Models

`[ 470 · heading1]`

> Maximum Entropy Markov Models

`[ 471 · paragraph]`

> Decoding

`[ 472 · paragraph]`

> - Bigram MEMM:

`[ 473 · paragraph]`

> S ar gmaxsP(S|O) = ar gmaxsiP(si|si-1, 0)

`[ 474 · paragraph]`

> - Greedy decoding:

`[ 475 · figure]` *(base64 88932 chars attached)*

> ![image](/image/placeholder)
> DT NN ?
> the cat sat on

`[ 476 · paragraph]`

> Si ar gmaxsP(si = s|i-1, 0)

`[ 477 · footer]`

> Natural Language Processing (COSE461)


## Page 63

`[ 478 · header]`

> Sequence Models

`[ 479 · paragraph]`

> Maximum Entropy Markov Models

`[ 480 · paragraph]`

> Decoding

`[ 481 · paragraph]`

> - Viterbi decoding for MEMMs

`[ 482 · figure]` *(base64 111932 chars attached)*

> ![image](/image/placeholder)
> DT DT DT DT
> NN NN NN NN
> VBD VBD VBD VBD
> IN IN IN IN
> the cat sat on

`[ 483 · paragraph]`

> M[i,j] = max M[i - 1,k] P(si = j|si-1 = k, 0) 1 ≤ k ≤ K 1 ≤ i ≤ n
> k
> Backward: pick max M[n, k] and backtrack using B
> k

`[ 484 · footer]`

> Natural Language Processing (COSE461)


## Page 64

`[ 485 · paragraph]`

> Sequence Models

`[ 486 · heading1]`

> Maximum Entropy Markov Models

`[ 487 · paragraph]`

> Decoding

`[ 488 · paragraph]`

> - How would you compare the computational complexity of Viterbi decoding for
> MEMMs compared to decoding for bigram HMMs?

`[ 489 · list]`

> (A) More operations in HEMM
> (B) More operations in HMM
> (c) Equal
> (D) Depends on number of features in MEMM

`[ 490 · paragraph]`

> MEMM: M[i,j] = max M[i - 1,k]P(si = j|si-1 = k,0) 1 ≤ k ≤ K 1 ≤ i ≤ n
> k
> HMM: M[i,j] = max M[i - 1,k] P(sjsk)P(oisj) 1 ≤ k ≤ K 1 ≤ i ≤ n
> k

`[ 491 · footer]`

> Natural Language Processing (COSE461)


## Page 65

`[ 492 · paragraph]`

> Sequence Models

`[ 493 · heading1]`

> Maximum Entropy Markov Models

`[ 494 · paragraph]`

> Learning

`[ 495 · paragraph]`

> - Gradient descent: similar to logistic regression

`[ 496 · equation]` *(base64 35152 chars attached)*

> exp(w · f(si = S,Si-1, 0, i))
>  P(Si = S|Si-1, 0) =
>  Es' exp(w · f(si = S',Si-1' 0,i))

`[ 497 · paragraph]`

> - Given: annotated pairs of (S,O) where each S =< S1, S2, ...,Sn >
> Loss for one sequence, L = - Ei=1 logP(si|si-1, 0)

`[ 498 · paragraph]`

> - Compute gradients with respect to weights W and update

`[ 499 · footer]`

> Natural Language Processing (COSE461)


## Page 66

`[ 500 · paragraph]`

> Sequence Models

`[ 501 · paragraph]`

> Maximum Entropy Markov Models

`[ 502 · paragraph]`

> Learning

`[ 503 · paragraph]`

> - HMM models the joint P(S, 0) while MEMM models the required prediction P(S|O)

`[ 504 · paragraph]`

> - MEMM has more expressivity

`[ 505 · paragraph]`

> Accounts for dependencies between neighboring states and entire observation
> sequence
> Allows for more flexible features

`[ 506 · paragraph]`

> - HMM may hold an advantage if the dataset is small

`[ 507 · footer]`

> Natural Language Processing (COSE461)


## Page 67

`[ 508 · paragraph]`

> Conditional Random Fields (CRFs)
> ICML 2001


## Page 68

`[ 509 · heading1]`

> Sequence Models

`[ 510 · paragraph]`

> Conditional Random Field

`[ 511 · heading1]`

> Introduction

`[ 512 · paragraph]`

> - Model P(S1, ... , sn|01, · ·· On) directly
> ,

`[ 513 · paragraph]`

> - No Markov assumption

`[ 514 · equation]` *(base64 34660 chars attached)*

> exp ( W · f(S,O)) exp( W · f(S, 0))
>  P(S|O)
>  Es' exp ( W · f(S', 0)) Z(O)

`[ 515 · figure]` *(base64 87016 chars attached)*

> ![image](/image/placeholder)
> DT NN IN ···
> the cat sat on

`[ 516 · paragraph]`

> Map entire sequence of states S and observations 0 to a global feature vector

`[ 517 · paragraph]`

> - Normalize over entire sequences

`[ 518 · footer]`

> Natural Language Processing (COSE461)


## Page 69

`[ 519 · heading1]`

> Sequence Models

`[ 520 · paragraph]`

> Conditional Random Field

`[ 521 · paragraph]`

> Features

`[ 522 · paragraph]`

> - Each Fk in f is a global feature function

`[ 523 · paragraph]`

> m Fk(S,O) )
> exp ○ k=1 Wk ·
> P(S|O)
> m Fk(S', 0))
> Es' exp ( k=1 Wk ·

`[ 524 · paragraph]`

> - Can be computed as a combination of
> local features: Fk = Ei=1fk(si-1,si, 0,i)

`[ 525 · figure]` *(base64 85844 chars attached)*

> ![image](/image/placeholder)
> DT NN IN
> the cat sat on

`[ 526 · paragraph]`

> - Each local feature only depends on
> previous and current states

`[ 527 · footer]`

> Natural Language Processing (COSE461)


## Page 70

`[ 528 · heading1]`

> Sequence Models

`[ 529 · paragraph]`

> Conditional Random Field
> Decoding

`[ 530 · paragraph]`

> - S = ar gmaxsP(S|O)

`[ 531 · paragraph]`

> exp(w·f(S,O))

`[ 532 · paragraph]`

> ar gmaxs

`[ 533 · paragraph]`

> Z(O)

`[ 534 · list]`

> = ar gmaxs exp(w · f(S, 0))
> = ar gmaxs Ek=1 Ei=1 Wkfk (Si-1, Si, 0,i)

`[ 535 · paragraph]`

> - Use Viterbi similar to HMM and MEMM

`[ 536 · footer]`

> Natural Language Processing (COSE461)


## Page 71

`[ 537 · heading1]`

> Sequence Models

`[ 538 · paragraph]`

> Conditional Random Field

`[ 539 · paragraph]`

> Decoding

`[ 540 · paragraph]`

> - P(S|O)

`[ 541 · paragraph]`

> exp(Ek=1 Ei=1 wkfk(si-1,si,0,i))
> Z(O)

`[ 542 · equation]` *(base64 29496 chars attached)*

> exp(Ek=1 Li=1 Wkfk(Si-1,si,0,i))
>  n
>  Es1,...,s'n exp (k=1 Ei=1 wkfk(si-1,si,0,i))

`[ 543 · paragraph]`

> - log P(S|O) = - Ek=1 Ei=1 Wkfk (Si-1, Si, 0,i) + log Es'1...,s'n exp (Ek=1 Ei=1 Wkfk(si-1,si,0,i) )

`[ 544 · paragraph]`

> a log p(S|O)
> can be done efficiently using dynamic programming
> awk

`[ 545 · footer]`

> Natural Language Processing (COSE461)


## Page 72

`[ 546 · heading1]`

> Sequence Models

`[ 547 · paragraph]`

> Conditional Random Field

`[ 548 · paragraph]`

> Compared with MEMM

`[ 549 · paragraph]`

> - MEMM models the required prediction P(S|O) using the Markov assumption, while
> the CRF does not

`[ 550 · paragraph]`

> - CRF uses global features while MEMM features are localized

`[ 551 · paragraph]`

> - Feature design is flexible in both models

`[ 552 · list]`

`[ 553 · paragraph]`

> - CRF is computationally more complex

`[ 554 · footer]`

> Natural Language Processing (COSE461)


## Page 73

`[ 555 · paragraph]`

> Sequence Models

`[ 556 · paragraph]`

> Conditional Random Field

`[ 557 · paragraph]`

> History of CRFs

`[ 558 · paragraph]`

> - Very popular in the 2000s

`[ 559 · paragraph]`

> - Wide variety of applications:
> Information extraction

`[ 560 · paragraph]`

> Summarization

`[ 561 · paragraph]`

> Image labeling/segmentation

`[ 562 · footer]`

> Natural Language Processing (COSE461)


## Page 74

`[ 563 · heading1]`

> Sequence Models

`[ 564 · paragraph]`

> Conditional Random Field

`[ 565 · paragraph]`

> - Use CRFs on top of neural representations (instead of features and weights)

`[ 566 · heading1]`

> CRFs in deep learning era

`[ 567 · list]`

`[ 568 · paragraph]`

> - Joint sequence prediction without the need for defining features

`[ 569 · list]`

`[ 570 · paragraph]`

> - Recent architectures such as seq2seq w/ attention or Transformer may implicitly
> do the job

`[ 571 · footer]`

> Natural Language Processing (COSE461)


## Page 75

`[ 572 · paragraph]`

> E.O.D
