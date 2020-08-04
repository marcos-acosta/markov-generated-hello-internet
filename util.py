def get_corpus():
    return get_text_file('corpus.txt')

def get_text_file(fname):
    fh = open(fname)
    text = fh.read()
    fh.close()
    return text

def get_ngrams(text, lookahead):
    chain = {}
    index = lookahead
    for word in text[index:]:
        key = ' '.join(text[index-lookahead:index])
        if key in chain:
            chain[key].append(word)
        else:
            chain[key] = [word]
        index += 1
    return chain