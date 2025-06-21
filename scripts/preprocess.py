# Data preprocessing script placeholder
import re
import pandas as pd

def preprocess_text(text):
    # Remove emojis and weird symbols
    text = re.sub(r'[^\w\s።፡ሀ-፼]+', '', text)
    # Normalize spaces
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

# Load data
with open('output/marakibrand.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for msg in data:
    msg['cleaned_text'] = preprocess_text(msg['message'])

# Save preprocessed data
df = pd.DataFrame(data)
df.to_csv("output/marakibrand_cleaned.csv", index=False)


# {
#   "vendor": "ShagerStore",
#   "date": "2025-06-01",
#   "message": "አዲስ ቤት እቃ በ 1500 ብር በ ቦሌ",
#   "views": 1200,
#   "media": "image_123.jpg"
# }
