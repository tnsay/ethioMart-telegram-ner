# ethioMart-telegram-ner
# EthioMart Telegram NER Pipeline

This project collects and preprocesses Amharic e-commerce data from Ethiopian-based Telegram channels to support Named Entity Recognition (NER) model fine-tuning.

## Features
- Scrapes messages, metadata, and images from Telegram channels
- Cleans and normalizes Amharic text
- Structures data for downstream NLP tasks (like NER)
- Outputs CSV and JSON format

## Channels Covered
- @marakibrand
- @classybrands
- @meneshayeofficial
- @forfreemarket
- @ZemenExpress

## Folder Structure
- `data/raw/`: Raw JSON files of messages
- `data/cleaned/`: Cleaned and tokenized CSV data
- `images/`: Downloaded product images
- `scripts/`: Python scripts for scraping and preprocessing

## Setup

1. Clone the repo:
```bash
git clone https://github.com/tnsay/ethioMart-telegram-ner.git

## Model Comparison

This notebook compares three multilingual transformer models for Amharic Named Entity Recognition (NER):

| Model Name                                   | F1-Score | Size (MB) | Notes |
|---------------------------------------------|----------|-----------|-------|
| xlm-roberta-base                             | 0.00     | 3351.87   | Largest, but no improvement in accuracy |
| bert-base-multilingual-cased                 | 0.00     | 2131.35   | Lighter, same performance |
| Davlan/bert-base-multilingual-cased-ner-hrl  | 0.00     | 2131.35   | Pretrained on NER, but label mismatch |

> All models were fine-tuned on custom Amharic NER labels. However, due to data limitations, no F1 improvement was observed. Models are saved locally and can be provided upon request.

## Interpretability
We used SHAP and LIME to interpret token-level predictions made by the NER models.

SHAP: Highlights which words contribute positively or negatively to the model’s NER predictions.

LIME: Generates human-readable explanations to validate model confidence across tokens.

These tools support model debugging and increase transparency for stakeholders.

## FinTech Vendor Scorecard
A vendor engagement scorecard was created to support micro-lending evaluations based on Telegram activity:

Input Metrics: Post frequency, product variety, customer interaction, sentiment polarity, and image presence

Output: Composite score per vendor indicating e-commerce engagement and potential trustworthiness

This scorecard enables ranking vendors and assessing lending eligibility based on behavioral analytics.