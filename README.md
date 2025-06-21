# ethioMart-telegram-ner
# Ethio Telegram NER Pipeline

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
git clone https://github.com/your-username/ethio-telegram-ner.git
