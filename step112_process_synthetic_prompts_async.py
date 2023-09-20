import os
import sys
import pandas as pd
import numpy as np
from tqdm import tqdm
import jsonlines
import logging
import asyncio  # for running API calls concurrently
import argparse

# from utils import make_and_clear

import utils.api_request_parallel_processor_new as api_request

import config.paths as P
from config.constants import CHAT_RPM_LIMIT, CHAT_TPM_LIMIT, CHAT_URL, PROMPT

    
def main(args):

    destination = args.destination
    # make_and_clear(destination)

    df = pd.read_csv(args.synthetic_prompts_input)

    print(df)

    if args.num_prompts == -1:
        idx = list(range(len(df)))
    else:
        idx = np.round(np.linspace(0, len(df) - 1, args.num_prompts)).astype(int)

    df_temp = df.iloc[idx]
    df_temp.to_csv(args.synthetic_prompts_output)


    print(df_temp)

    prompts = df_temp[PROMPT].tolist()


    messages = []

    pbar = tqdm(total=len(prompts))
    for i, p in enumerate(prompts):
        m = { \
            api_request.MODEL: args.model,
            api_request.MESSAGES: [{'role': 'user', 'content': p}],
            api_request.MAX_TOKENS: args.max_tokens,
            api_request.TEMPERATURE: args.temperature
        }
        messages.append(m)
        pbar.update(1)
    pbar.close()

    # Create input jsonl for input
    requests_filepath = os.path.join(destination, 'requests.jsonl')
    with jsonlines.open(requests_filepath, 'w') as f:
        f.write_all(messages)

    # Define output jsonl
    # save_filepath = os.path.join(destination, 'output.jsonl')

    answer = input(f'''Confirm transmission of {len(prompts)} prompts. Enter yes or no: ''') 

    if answer == 'yes':

        asyncio.run(
            api_request.process_api_requests_from_file(
                requests_filepath = requests_filepath,
                save_filepath = args.save_filepath,
                api_key = args.api_key,
                request_url = args.request_url,
                token_encoding_name = args.token_encoding_name,
                max_requests_per_minute = float(args.max_requests_per_minute),
                max_tokens_per_minute = float(args.max_tokens_per_minute),
                max_attempts = int(args.max_attempts),
                logging_level = int(args.logging_level),
            )
        )

        pass
    else:
        print('Did not transmit')


if __name__ == '__main__':


    destination = P.process_synthetic_prompts_async
    synthetic_prompts_input = P.synthetic_prompts
    synthetic_prompts_output = P.synthetic_prompts_async
    save_filepath = P.synthetic_responses_async

    with open(P.api_key_file, 'r') as f:
        api_key = f.read()

    arg_parser = argparse.ArgumentParser(add_help=False)
    arg_parser.add_argument('--destination', type=str, default=destination, help="output directory")
    arg_parser.add_argument('--synthetic_prompts_input', type=str, default=synthetic_prompts_input, help="output directory")
    arg_parser.add_argument('--synthetic_prompts_output', type=str, default=synthetic_prompts_output, help="output directory")
    arg_parser.add_argument('--save_filepath', type=str, default=save_filepath, help="output directory")    
    arg_parser.add_argument('--num_prompts', type=int, default=5, help="max number of prompts")

    arg_parser.add_argument('--request_url', type=str, default=CHAT_URL, help="openai model url")       
    arg_parser.add_argument('--api_key', type=str, default=api_key, help="openai model url")    
    arg_parser.add_argument("--max_requests_per_minute", type=int, default=CHAT_RPM_LIMIT * 0.5)
    arg_parser.add_argument("--max_tokens_per_minute", type=int, default=CHAT_TPM_LIMIT * 0.5)
    arg_parser.add_argument('--model', type=str, default="gpt-3.5-turbo-0301", help="openai lm")
    arg_parser.add_argument('--token_encoding_name', type=str, default="cl100k_base", help="openai lm")    
    arg_parser.add_argument('--temperature', type=float, default=1.0, help="model temperature")
    arg_parser.add_argument('--max_tokens', type=int, default=300, help="max number of generated tokens")
    arg_parser.add_argument("--max_attempts", type=int, default=5)
    arg_parser.add_argument("--logging_level", default=logging.INFO)



    args, _ = arg_parser.parse_known_args()


    sys.exit(main(args)) 
