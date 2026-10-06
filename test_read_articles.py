import json
import re

with open('assets/js/articles-data.js', 'r', encoding='utf-8') as f:
    js_content = f.read()

# Extract json part
json_str = js_content.replace('const JAWARA_ARTICLES = ', '').strip().rstrip(';')
articles = json.load(json_str) if isinstance(json_str, dict) else json.loads(json_str)

print(f"Loaded {len(articles)} articles.")
