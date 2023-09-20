import pandas as pd
import csv
import json

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('sampled_posts.csv')

# Randomly sample 5 posts from each of the two flairs: "Tested Positive - Me" and "Presumed Positive" for annotation
df_tested_positive   = df[df["flair"] == "Tested Positive - Me"]
df_presumed_positive = df[df["flair"] == "Presumed Positive"]

df_tested_positive_sampled   = df_tested_positive.sample(5)
df_presumed_positive_sampled = df_presumed_positive.sample(5)

data = [df_tested_positive_sampled, df_presumed_positive_sampled]
df_sample = pd.concat(data)

df_sample.to_csv("round_one_annotation.csv", index=False)

# Convert it to JSONL to feed it to Doccano
# Read the CSV file
with open("/projects/klybarge/covid_diagnosis/covid_diagnosis/data/round_one_annotation.csv", "r", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    
    # Write the JSONL file
    with open("/projects/klybarge/covid_diagnosis/covid_diagnosis/data/round_one_annotation_jsonl.jsonl", "w") as jsonlfile:
        for row in reader:
            jsonlfile.write(json.dumps(row) + "\n")