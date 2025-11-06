import json
import re

def extract_quotes_from_file(filename):
    with open(f'data/{filename}', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    quotes = []
    for line in lines:
        line = line.strip()
        # Ignorer les lignes vides, les titres (##, ###), et les séparateurs (---)
        if line and not line.startswith('#') and not line.startswith('---'):
            quotes.append(line)
    
    return quotes

# Lire les 4 fichiers
categories = ['hikam', 'love', 'women', 'dunya']
all_quotes = {}

for cat in categories:
    all_quotes[cat] = extract_quotes_from_file(f'{cat}.txt')
    print(f"✓ {cat}: {len(all_quotes[cat])} quotes")

# Créer la structure JSON
api_data = {
    "categories": [
        {"id": "hikam", "name": "Hikam", "description": "حكم عن الحياة والناس"},
        {"id": "love", "name": "Love", "description": "أقوال عن الحب"},
        {"id": "women", "name": "Women", "description": "أقوال عن المرأة"},
        {"id": "dunya", "name": "Dunya", "description": "حكم عن الدنيا"}
    ],
    "quotes": all_quotes
}

# Sauvegarder dans api/quotes.json
with open('api/quotes.json', 'w', encoding='utf-8') as f:
    json.dump(api_data, f, ensure_ascii=False, indent=2)

print("\n✓ Fichier api/quotes.json créé avec succès!")
