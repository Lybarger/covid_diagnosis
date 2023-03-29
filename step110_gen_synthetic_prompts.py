import os
import sys
import pandas as pd
import numpy as np
import random
import argparse
from tqdm import tqdm


import paths
import config

from config import REGRESSION_SYMPTOMS, REGRESSION_ONSET
from config import REGRESSION_TEST, REGRESSION_AGE
from config import TEST_POSITIVE, TEST_NEGATIVE


from utils import make_and_clear




# LENGTHS = [ \
#         'brief', 
#         'short',
#         'one sentence', 
#         'two sentence', 
#         'three sentence',
#         'four sentence',
#         'five sentence',
#         'one paragraph',
#         'two paragraph',
#         'three paragraph']

LENGTHS = [ \
        'brief']


# FORMATS = ['social media post']

def symptom_str(X, conj='and'):

    if len(X) == 0:
        return None
    elif len(X) == 1:
        return X[0]   
    elif len(X) == 2:
        return f"{X[0]} {conj} {X[1]}"            
    else:
        return f'''{", ".join(X[:-1])}, {conj} {X[-1]}'''
    


def template(length, symptoms_present, symptoms_absent, test=None):
    
  

    prompt = ''

    length_txt = length
    prompt += f'Create a {length_txt} social media post for a user who thinks they may have COVID.'

    if len(symptoms_present):
        random.shuffle(symptoms_present)
        prompt += f''' The user is experiencing {symptom_str(symptoms_present, conj='and')}.'''

    if len(symptoms_absent):
        random.shuffle(symptoms_absent)
        prompt += f''' The user is not experiencing {symptom_str(symptoms_absent, conj='or')}.'''

    if test is None:
        pass
    elif test == TEST_POSITIVE:
        prompt += ' The user recently had a positive at-home COVID test.'
    elif test == TEST_NEGATIVE:
        prompt += ' The user recently had a negative at-home COVID test.'

    prompt +=  ' Use conversational language and synonyms for symptoms.'

    return prompt


def create_prompts(path_regression_table, \
                    col_symptoms = REGRESSION_SYMPTOMS,
                    col_onset = REGRESSION_ONSET,
                    col_test = REGRESSION_TEST,
                    col_age = REGRESSION_AGE):


    df = pd.read_excel(path_regression_table)


    prompts = []
    pbar = tqdm(total=len(df))
    for index, row in df.iterrows():

        symptoms_binary = row[col_symptoms]
        symptoms_present = []
        symptoms_absent = []
        for c, s in zip(col_symptoms, symptoms_binary):
            c = c.lower()
            if s:
                symptoms_present.append(c)
            else:
                symptoms_absent.append(c)

        onset = row[col_onset]
        test = row[col_test]
        age = row[col_age]

        length = random.choice(LENGTHS)

        num_keep = random.randint(0, len(symptoms_absent))
        symptoms_absent = symptoms_absent[:num_keep]


        prompt = template( \
                length =  length,
                symptoms_present = symptoms_present,
                symptoms_absent = symptoms_absent,
                test = test)
        
        prompts.append(prompt)
        pbar.update()
    
    pbar.close()
    df[config.PROMPT] = prompts

    return df
    
def main(args):


    destination = args.destination
    make_and_clear(destination)


    df = create_prompts(path_regression_table = args.path_regression_table)
    df.to_csv(args.synthetic_prompts)


if __name__ == '__main__':


    destination = paths.gen_synthetic_prompts
    synthetic_prompts = paths.synthetic_prompts

    path_regression_table = paths.regression_table

    arg_parser = argparse.ArgumentParser(add_help=False)
    arg_parser.add_argument('--destination', type=str, default=destination, help="output directory")
    arg_parser.add_argument('--synthetic_prompts', type=str, default=synthetic_prompts, help="output directory")
    
    arg_parser.add_argument('--path_regression_table', type=str, default=path_regression_table, help="path to regression table")

    args, _ = arg_parser.parse_known_args()

    sys.exit(main(args)) 