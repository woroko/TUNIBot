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

from collections import defaultdict, Counter
import itertools, sys
import pickle
import math
import tokenizer

questions_file = "data/q.txt"
answers_file = "data/a.txt"


def load_data(filename):
    with open(filename, 'r', encoding='ascii') as f:
        return f.readlines()


class invertedIndex(object):

    def __init__(self,docs=None, file=None):
        self.docSets = defaultdict(set)
        if (docs is not None):
            for index, doc in enumerate(docs):
                for term in doc.lower().split():
                    self.docSets[term].add(index)
        elif (file is not None):
            with open(file, 'rb') as f:
                self.docSets = pickle.load(f)

    def save_to_file(self,filename):
        with open(filename, 'wb') as f:
            pickle.dump(self.docSets, f)

    def search(self,term):
        return self.docSets[term]


    def search_percentage(self, query, p):
        c = Counter()
        query_words = tokenizer.word_tokenize_stem(query)
        for term in query_words:
            result = self.search(term)
            c.update(result)

        word_count = len(query_words)
        if (word_count == 1):
            n = 1
        else:
            n = int(math.floor(word_count * p))

        return [x for x, y in c.items() if y >= n]

    def search_percentage_bestn(self, query, p, bestn):
        c = Counter()
        query_words = tokenizer.word_tokenize_stem(query)
        for term in query_words:
            result = self.search(term)
            c.update(result)

        word_count = len(query_words)
        if (word_count == 1):
            n = 1
        else:
            n = int(math.floor(word_count * p))

        to_sort = [(x,y) for x, y in c.items() if y >= n]
        sorted_items = [x for x,y in sorted(to_sort, key=lambda x: x[1], reverse=True)[:bestn]]

        return sorted_items

    def search_n(self, query, n):
        c = Counter()
        for term in tokenizer.word_tokenize_stem(query):
            result = self.search(term)
            c.update(result)

        return [x for x, y in c.items() if y >= n]

    def search_n_score(self, query, n):
        c = Counter()
        for term in tokenizer.word_tokenize_stem(query):
            result = self.search(term)
            c.update(result)

        return [(x, y) for x, y in c.items() if y >= n]

def main():
    if (len(sys.argv) > 1):
        q = sys.argv[1]
        questions = load_data(questions_file)
        i_q = invertedIndex(file="idx_q.bin")
        print("file load finished")
        matches = i_q.search_n_score(q, 2)
        matches.sort(key=lambda x: x[1], reverse=True)
        for idx, count in matches[:10]:
            print(questions[idx] + " *" + str(count))
    else:
        i=invertedIndex(docs=load_data(questions_file))
        i.save_to_file("idx_q.bin")
        i=invertedIndex(docs=load_data(answers_file))
        i.save_to_file("idx_a.bin")

    #i_a=invertedIndex(load_data(answers_file))
     # outputs: set([0, 1, 2, 3])

if __name__ == "__main__":
    main()
