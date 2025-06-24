import json
import os
import pandas as pd
import re
import emoji

# Paths
raw_path = "data/raw"
clean_path = "data/cleaned"
os.makedirs(clean_path, exist_ok=True)

def clean_amharic_text(text):
    # Remove emojis
    text = emoji.replace_emoji(text, replace='')

    # Remove punctuation and symbols, except @, #, and ብር
    text = re.sub(r"[^\u1200-\u137F0-9a-zA-Z@#፩-፱፻፼ብር/\s]", " ", text)

    # Normalize whitespace
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

    cleaned_rows = []
    for msg in data:
     cleaned_message = clean_amharic_text(msg["message"])
     #print("Original:", msg["message"])
     print("Cleaned:", cleaned_message)
