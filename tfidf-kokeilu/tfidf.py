#
# Chatbot using combined TF-IDF and Levenshtein distance ranking
# Copyright (C) 2018 John Mäkelä
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import sys
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
import tokenizer

#path = sys.argv[1]

def load_data(filename):
    with open(filename, 'r', encoding='ascii') as f:
        return f.readlines()

def tokenize_nostem(text):
    tokens = nltk.word_tokenize(text)
    stems = []
    for item in tokens:
        stems.append(item.lower())
    return stems

def main():
    questions_file = "data/q.txt"
    answers_file = "data/a.txt"
    tf = TfidfVectorizer(analyzer='word', tokenizer=tokenizer.word_tokenize, ngram_range=(1,3), min_df = 1, stop_words = None)

    matrix = tf.fit_transform(load_data(questions_file))
    with open( "tf_q.bin", "wb" ) as f:
        pickle.dump( tf,  f)
    with open( "tf_matrix_q.bin", "wb" ) as f:
        pickle.dump( matrix,  f)

    tf = TfidfVectorizer(analyzer='word', tokenizer=tokenizer.word_tokenize, ngram_range=(1,3), min_df = 1, stop_words = None)

    matrix = tf.fit_transform(load_data(answers_file))
    with open( "tf_a.bin", "wb" ) as f:
        pickle.dump( tf,  f)
    with open( "tf_matrix_a.bin", "wb" ) as f:
        pickle.dump( matrix,  f)

if __name__ == "__main__":
    main()
