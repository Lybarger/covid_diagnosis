

import jsonlines
import json

from collections import Counter

MODEL = 'model'
CONTENT = 'content'
MESSAGES = 'messages'
MAX_TOKENS = 'max_tokens'
TEMPERATURE = 'temperature'

MAX_TOKENS_DEFAULT = 100

FINISH_REASON = "finish_reason"
FINISH_STOP = "stop"
FINISH_LENGTH = "length"
CHOICES = 'choices'

USAGE = 'usage'
PROMPT_TOKENS = 'prompt_tokens'
COMPLETION_TOKENS = 'completion_tokens'
TOTAL_TOKENS = 'total_tokens'
MESSAGE = "message"

path = '/projects/klybarge/covid_diagnosis/analyses/step112_process_synthetic_prompts_async/output.jsonl'

# with jsonlines.open(path, 'r') as f:

#     for line in f.iter(skip_empty=True):
#         if isinstance(line, list):
#             x = line[0]
#             print(x.keys())
#         else:
#             print('not a list')



total_tokens_all = 0
finish_reason_all = Counter()
messages_all = []
prompts_all = []

with open(path, 'r') as file:
    X = file.__iter__()
    for x in X:
        input, output = tuple(eval(x))

        message = input[CHOICES][MESSAGE][0][CONTENT]
        messages_all.append(message)

        prompt_tokens = output[USAGE][PROMPT_TOKENS]
        completion_tokens = output[USAGE][COMPLETION_TOKENS]
        total_tokens = output[USAGE][TOTAL_TOKENS]
        total_tokens_all += total_tokens

        finish_reason = output[CHOICES][0][FINISH_REASON]
        finish_reason_all[finish_reason] += 1

        message = output[CHOICES][0][MESSAGE][CONTENT]
        messages_all.append(message)
