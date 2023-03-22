


import os


analyses = '/projects/klybarge/covid_diagnosis/analyses'



regression_table = '/projects/klybarge/covid_diagnosis/data/ChatGPT 1 30 23.xlsx'



gen_synthetic_prompts = os.path.join(analyses, 'step110_gen_synthetic_prompts')
synthetic_prompts = os.path.join(gen_synthetic_prompts, 'prompts.csv')

process_synthetic_prompts = os.path.join(analyses, 'step111_process_synthetic_prompts')
synthetic_responses = os.path.join(process_synthetic_prompts, 'responses.csv')


process_synthetic_prompts_async = os.path.join(analyses, 'step112_process_synthetic_prompts_async')
synthetic_prompts_async = os.path.join(process_synthetic_prompts_async, 'prompts.csv')
synthetic_responses_async = os.path.join(process_synthetic_prompts_async, 'output.jsonl')



aggregate_synthetic_ouputs = os.path.join(analyses, 'step113_aggregate_synthetic_ouputs')



