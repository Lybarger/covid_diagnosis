# #COVID Diagnosis Project README

## Project Overview

The "COVID Diagnosis" project focuses on analyzing Reddit posts where users describe their experiences with COVID-19. The goal is to extract relevant features, including demographics and symptoms, from these posts. The extracted features are used to gain insights into users' experiences with the virus.

## Project Structure

The project consists of several Python scripts that perform different tasks:

`reddit_scrape.py`

This script is responsible for scraping Reddit posts related to COVID-19. It interacts with the Pushshift API to retrieve posts based on specified parameters such as subreddit, date range, and flair. The retrieved data is processed, sampled, and saved to CSV files for further analysis.

`annotation_preparation.py`

This script prepares data for annotation by randomly selecting a subset of Reddit posts for annotation purposes. It creates a CSV file containing these posts and converts it to JSONL format, which can be used with annotation tools like Doccano.

`prompt_engineering.py`

This script sets up the OpenAI API for generating completions. It defines prompts and instructions for extracting features from Reddit posts. The script demonstrates how to use the API to extract relevant features based on provided guidelines.

## Project Data

The data collected and processed by this project includes sampled Reddit posts related to COVID-19. These posts are used for feature extraction and analysis. The output of the project may include lists of extracted features from the posts, as demonstrated in the provided scripts.
