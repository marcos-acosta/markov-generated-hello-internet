from util import *
import random
import re

text = get_corpus().split(' ')

def generate(text, count, trigram_threshold=0.5, verbose=1, start='.'):
    u_count = 0
    b_count = 0
    t_count = 0
    unigrams = get_ngrams(text, 1)
    bigrams = get_ngrams(text, 2)
    trigrams = get_ngrams(text, 3)
    # Initialize
    word1 = random.choice(unigrams[start])
    word2 = random.choice(unigrams[word1])
    u_count = 2
    bigram = word1 + ' ' + word2
    # Pick third word
    if bigram in bigrams:
        word3 = random.choice(bigrams[bigram])
        b_count += 1
    else:
        word3 = random.choice(unigrams[word1])
        u_count += 1
    message = word1 + ' ' + word2 + ' ' + word3
    # Generate following words
    next_ngram = ''
    while len(message.split(' ')) < count or next_ngram != '.':
        bigram = ' '.join(message.split(' ')[-2:])
        trigram = ' '.join(message.split(' ')[-3:])
        if trigram in trigrams and random.random() > trigram_threshold:
            t_count += 1
            next_ngram = random.choice(trigrams[trigram])
        else:
            b_count += 1
            next_ngram = random.choice(bigrams[bigram])
        message += ' ' + next_ngram
    if verbose == 1:
        total = u_count + b_count + t_count
        print('Unigrams:', u_count, '(', "{:.1%}".format((u_count/total)), ')')
        print('Bigrams:', b_count, '(', "{:.1%}".format((b_count/total)), ')')
        print('Trigrams:', t_count, '(', "{:.1%}".format((t_count/total)), ')')
    return message


message = generate(text, 1000, trigram_threshold=0.4)

# Capitalize after period
message = ' . '.join(map(lambda s: s.strip().capitalize(), message.split('.')))
# Capitalize 'I'
message = re.sub(r' i ', ' I ', message)
message = re.sub(r' i\'', ' I\'', message)
message = re.sub(r' \.', '.', message)
print(message)