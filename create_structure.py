import os

# Define folder and file structure
project_name = "."

folders = [
    f"{project_name}/data/raw",
    f"{project_name}/data/cleaned",
    f"{project_name}/images",
    f"{project_name}/scripts"
]

files = {
    #f"{project_name}/README.md": "# Ethio Telegram NER Pipeline\n",
    f"{project_name}/requirements.txt": "telethon\npandas\n",
    f"{project_name}/.gitignore": "images/\ndata/\nscripts/config.py\n",
    f"{project_name}/scripts/telegram_scraper.py": "# Telegram scraper script placeholder\n",
    f"{project_name}/scripts/preprocess.py": "# Data preprocessing script placeholder\n",
    f"{project_name}/scripts/config.py": "# Store your api_id and api_hash here\napi_id = ''\napi_hash = ''\n",
    f"{project_name}/data/raw/marakibrand.json": "[]",
    f"{project_name}/data/raw/classybrands.json": "[]",
    f"{project_name}/data/cleaned/marakibrand_cleaned.csv": "channel,date,message,cleaned_text,views,image\n"
}

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create files with content
for path, content in files.items():
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"📁 Project structure '{project_name}' created successfully.")
