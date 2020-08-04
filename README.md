# markov-generated-hello-internet
An implementation of a Markov chain to produce sentences that approximate conversation in the podcast Hello Internet, featuring CGP Grey and Brady Haran.

## How to use ##

Just run `markov.py`. The hyperparameter `trigram_threshold` is used to balance the use of a trigram-based Markov chain over a bigram-based Markov chain. Higher thresholds (closer to 1) result in more novel (but often less sensesible) text, while lower thresholds (closer to 0) result in closer regurgitation of the corpus.