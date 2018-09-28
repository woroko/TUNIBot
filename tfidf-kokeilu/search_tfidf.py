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
import Levenshtein
import pickle
import pprint
from sklearn.metrics.pairwise import linear_kernel
import numpy as np
from tfidf_index import invertedIndex
from collections import deque
from operator import itemgetter
import time

questions_file = "data/q.txt"
answers_file = "data/a.txt"
def load_data(filename):
    with open(filename, 'r', encoding='ascii') as f:
        return f.readlines()

'''
def tokenize_nostem(text):
    tokens = nltk.word_tokenize(text)
    stems = []
    for item in tokens:
        stems.append(item.lower())
    return stems
'''

#context = sys.argv[1]
#topresults = []
#context = ''.join([x for x in q if ord(x) < 128]).encode("ascii")
#context_list = context.split("<s>")#[::-1] #reverse context
#context_list = [entry.strip() for entry in context_list]
#print("context len: " + str(len(context_list)))

with open( "tf_q.bin", "rb" ) as f:
    tf_q = pickle.load(f)
with open( "tf_matrix_q.bin", "rb" ) as f:
    matrix_q = pickle.load(f)

with open( "tf_a.bin", "rb" ) as f:
    tf_a = pickle.load(f)
with open( "tf_matrix_a.bin", "rb" ) as f:
    matrix_a = pickle.load(f)

questions = load_data(questions_file)
answers = load_data(answers_file)
idx_q = invertedIndex(file="idx_q.bin")
idx_a = invertedIndex(file="idx_a.bin")

print("loading finished")

def get_best_matches_idx(msg, is_q, idx_match_percentage, best_n_cosine, best_n_final):
    #t = time.process_time()
    if (is_q):
        msg_vec = tf_q.transform([msg]).toarray()
        potential_matches = idx_q.search_percentage(msg, idx_match_percentage)
        data = questions
        matrix = matrix_q
    else:
        msg_vec = tf_a.transform([msg]).toarray()
        potential_matches = idx_a.search_percentage(msg, idx_match_percentage)
        data = answers
        matrix = matrix_a

    if (len(potential_matches) < 1):
        return []

    #print("idx search done: " + "{:.2f}".format(time.process_time()-t))
    #t = time.process_time()
    cosine_similarities = linear_kernel(msg_vec, matrix[potential_matches]).flatten()
    #print("len potential matches: " + str(len(potential_matches)))
    if (len(potential_matches) < best_n_cosine):
        best_n_cosine = len(potential_matches)

    ind = np.argpartition(cosine_similarities, -best_n_cosine)[-best_n_cosine:]
    ind = ind[np.argsort(cosine_similarities[ind])][::-1]

    topresults = []
    msg_ascii = ''.join([x for x in msg if ord(x) < 128]).encode("ascii")

    for i in ind[:best_n_final]:
        current_data = data[potential_matches[i]]
        text = ''.join([x for x in current_data if ord(x) < 128]).encode("ascii")
        norm_distance = 1.0 - (Levenshtein.distance(text, msg_ascii)/float(max(len(text), len(msg_ascii))))
        topresults.append((potential_matches[i], (norm_distance * 0.5 + cosine_similarities[i] * 0.5)))

    #print("accurate matching: " + "{:.2f}".format(time.process_time()-t))
    return topresults

def idx_only(msg, p, bestn):
    matches = idx_a.search_percentage_bestn(msg, p, bestn)
    if (len(matches) < 1):
        return []
    return matches

def msg_compare(msg1_vec, msg2_vec, msg1_text, msg2_text):

    cosine_similarity = linear_kernel(msg1_vec, msg2_vec).flatten()
    #text = ''.join([x for x in current_data if ord(x) < 128]).encode("ascii")
    norm_distance = 1.0 - (Levenshtein.distance(msg1_text, msg2_text)/float(max(len(msg1_text), len(msg2_text))))
    return (norm_distance * 0.5 + cosine_similarity[0] * 0.5)


#list context and weights
def gen_context_and_score(context, weights=[1.0, 1.0, 1.0]):
    if (len(weights) != 3 or len(context) < 1 or len(context) > 3):
        return None
    #is q
    topresults_0 = get_best_matches_idx(context[0], True, 0.5, 300, 100)
    scores = []
    if (len(context) > 1):
        context_vec_q = [tf_q.transform([msg]).toarray() for msg in context[1:]]
        #context_vec_a = [tf_a.transform([msg]).toarray() for msg in context[1:]] # 1 less
    for idx0, score0 in topresults_0:
        print("idx0: " + str(idx0))
        #tf_q.transform([msg]).toarray()
        #candidate_answers.append(idxscore0) # last message similarity, also possible answer indices
        if (len(context) > 1):
            #topresults_1 = get_best_matches_idx(questions[idx0], False, 0.5, 35, 3) #returns idx1 in answers
            topresults_1 = idx_only(questions[idx0], 0.5, 10)
        if (len(context) > 1 and len(topresults_1) > 0):
            for idx1 in topresults_1:
                match_score_1 = msg_compare(matrix_q[idx1], context_vec_q[0], questions[idx1], context[1])
                if (len(context) > 2):
                    #topresults_2 = get_best_matches_idx(questions[idx1], False, 0.5, 35, 3)
                    topresults_2 = idx_only(questions[idx1], 0.5, 10)
                if (len(context) > 2 and len(topresults_2) > 0):
                    #could add if get best context from idx1 (answer) -> idx1 (question) instead
                    for idx2 in topresults_2:
                        match_score_2 = msg_compare(matrix_q[idx2], context_vec_q[1], questions[idx2], context[2])
                        scores.append(([idx0, idx1, idx2], (score0*weights[0] + \
                        match_score_1*weights[1] + match_score_2*weights[2]) / \
                        (weights[0] + weights[1] + weights[2])))

                else:
                    scores.append(([idx0, idx1], (score0*weights[0] +\
                     match_score_1*weights[1]) / (weights[0] + weights[1])))
        else:
            scores.append(([idx0], (score0*weights[0]) / weights[0]))

    return scores


'''res = gen_context_and_score(context_list, weights=[1.0, 1.0, 0.5])

#res.sort(key=lambda x: x[1])

maxes = dict()
for idxlist, score in res:
    if idxlist[0] not in maxes:
        maxes[idxlist[0]] = (idxlist, score)
    else:
        if maxes[idxlist[0]][1] < score:
            maxes[idxlist[0]] = (idxlist, score)

#maxes_list = [(k, d[k]) for k in sorted(d, key=d.get, reverse=True)]
for idx, idxscore in sorted(maxes.items(), key = lambda x: x[1][1], reverse = True):
    print(" <s> ".join([questions[i].strip() for i in idxscore[0]]))
    print(answers[idx].strip() + " *SCORE: " + "{:.2f}".format(idxscore[1]))'''

que = deque()
previous_response = -1

while(True):
    new_input = input("> ")
    que.append(new_input)
    if (len(que) > 3):
        que.popleft()

    if (len(que) == 1):
        topresults = get_best_matches_idx(que[0], True, 0.5, 300, 30)
    else:
        topresults = get_best_matches_idx(" ".join(list(que)), True, 0.5, 300, 30)
    topresults.sort(key=lambda x: x[1], reverse=True)
    if ((len(topresults) < 1 or topresults[0][1] < 0.3) and len(que) > 1):
        que.popleft()
        topresults1 = get_best_matches_idx(" ".join(list(que)), True, 0.5, 300, 30)
        topresults1.sort(key=lambda x: x[1], reverse=True)
        topresults = (topresults + topresults1).sort(key=lambda x: x[1], reverse=True)
        if (len(que) > 1 and (len(topresults1) < 1 or topresults1[0][1] < 0.3)):
            que.popleft()
            topresults2 = get_best_matches_idx(" ".join(list(que)), True, 0.5, 300, 30)
            topresults2.sort(key=lambda x: x[1], reverse=True)
            if len(topresults2) > 1:
                topresults = (topresults + topresults2).sort(key=lambda x: x[1], reverse=True)

    if (topresults is None or (len(topresults) > 0 and topresults[0] is None)):
        topresults = get_best_matches_idx(new_input, True, 0.5, 300, 30)
        topresults.sort(key=lambda x: x[1], reverse=True)

    if (len(topresults) > 0 and len(topresults[0]) > 0 and topresults[0][0] == previous_response):
        topresults = get_best_matches_idx(new_input, True, 0.5, 300, 30)
        topresults.sort(key=lambda x: x[1], reverse=True)
        que.clear()

    for idx, score in topresults[:1]:
        #print(questions[idx].strip())
        print(answers[idx].strip() + " *SCORE " + "{:.2f}".format(score))

    if (len(topresults) > 0 and len(topresults[0]) > 0):
        previous_response = topresults[0][0]

'''

for result in topresults[:20]:
    text, score = result
    print(text.strip() + " *SCORE: " + "{:.2f}".format(score))
'''


#print(topresults[:15])
'''print(result['question_original'] + " SCORE: " + "{:.2f}".format(result['score']))
if (i>5):
    break'''
