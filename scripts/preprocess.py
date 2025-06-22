import json
import os
import pandas as pd
import re

# Paths
raw_path = "data/raw"
clean_path = "data/cleaned"
os.makedirs(clean_path, exist_ok=True)

def clean_amharic_text(text):
    # Basic cleanup: remove emojis, non-printable, extra whitespace
    text = re.sub(r"[^\u1200-\u137F\u1380-\u139F\u2D80-\u2DDF0-9a-zA-Z፩-፱፻፼ብርኛበ።፡፤፥፦፧፨,.!?@()«»\"'/-]+", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

# Loop over all JSON files in raw/
for filename in os.listdir(raw_path):
    if filename.endswith(".json"):
        with open(os.path.join(raw_path, filename), encoding="utf-8") as f:
            data = json.load(f)

        cleaned_rows = []
        for msg in data:
            cleaned_message = clean_amharic_text(msg["message"])
            cleaned_rows.append({
                "channel": msg["channel"],
                "date": msg["date"],
                "message": msg["message"],
                "cleaned_text": cleaned_message,
                "views": msg.get("views"),
                "image": msg.get("image", "")
            })

        # Save as CSV
        df = pd.DataFrame(cleaned_rows)
        output_file = os.path.join(clean_path, filename.replace(".json", "_cleaned.csv"))
        df.to_csv(output_file, index=False, encoding="utf-8-sig")
        print(f"✅ Cleaned and saved: {output_file}")






# Data preprocessing script placeholder
# import re
# import pandas as pd

# def preprocess_text(text):
#     # Remove emojis and weird symbols
#     text = re.sub(r'[^\w\s።፡ሀ-፼]+', '', text)
#     # Normalize spaces
#     text = re.sub(r'\s+', ' ', text)
#     return text.strip()

# # Load data
# with open('output/marakibrand.json', 'r', encoding='utf-8') as f:
#     data = json.load(f)

# for msg in data:
#     msg['cleaned_text'] = preprocess_text(msg['message'])

# # Save preprocessed data
# df = pd.DataFrame(data)
# df.to_csv("output/marakibrand_cleaned.csv", index=False)


# # {
# #   "vendor": "ShagerStore",
# #   "date": "2025-06-01",
# #   "message": "አዲስ ቤት እቃ በ 1500 ብር በ ቦሌ",
# #   "views": 1200,
# #   "media": "image_123.jpg"
# # }
