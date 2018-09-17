import re
import Stemmer

stemmer = Stemmer.Stemmer('english')
WORD = re.compile(r'\w+')

def word_tokenize(words):
    """Faster word tokenization than nltk.word_tokenize
    Input:
        words: a string to be tokenized
    Output:
        tokens: tokenized words
    """
    tokens = WORD.findall(words.lower())
    return(tokens)

def word_tokenize_stem(words):
    """Faster word tokenization than nltk.word_tokenize
    Input:
        words: a string to be tokenized
    Output:
        tokens: tokenized words
    """
    tokens = stemmer.stemWords(WORD.findall(words.lower()))
    return(tokens)
