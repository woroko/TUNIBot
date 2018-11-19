import random
import sys

INTENT_MULTIPLIER = 30

with open(sys.argv[1], 'r') as intents, open("out_" + sys.argv[1], 'w') as out, open(sys.argv[2], 'r') as lookup:
    codes = lookup.readlines()
    intent_list = intents.readlines()
    for i in range(0, INTENT_MULTIPLIER):
        for row in intent_list:
            out.write(row.replace("*", random.choice(codes).strip()))
