# Quotes API 📖

API simple pour récupérer des citations en arabe organisées par catégories.

## 📋 Catégories disponibles

- **Hikam** : حكم عن الحياة والناس
- **Love** : أقوال عن الحب
- **Women** : أقوال عن المرأة
- **Dunya** : حكم عن الدنيا

## 🔗 Endpoints

### Toutes les catégories et quotes
```
https://gamedrivne.github.io/qts/api/quotes.json
```

### Par catégorie

**Hikam :**
```
https://gamedrivne.github.io/qts/api/hikam.json
```

**Love :**
```
https://gamedrivne.github.io/qts/api/love.json
```

**Women :**
```
https://gamedrivne.github.io/qts/api/women.json
```

**Dunya :**
```
https://gamedrivne.github.io/qts/api/dunya.json
```

## 📖 Utilisation

### Exemple avec JavaScript
```javascript
// Récupérer toutes les catégories
fetch('https://gamedrivne.github.io/qts/api/quotes.json')
  .then(response => response.json())
  .then(data => console.log(data.categories));

// Récupérer les quotes d'une catégorie
fetch('https://gamedrivne.github.io/qts/api/hikam.json')
  .then(response => response.json())
  .then(data => console.log(data.quotes));
```

## 📝 Structure des données

### Liste complète (quotes.json)
```json
{
  "categories": [
    {
      "id": "hikam",
      "name": "Hikam",
      "description": "حكم عن الحياة والناس"
    }
  ],
  "quotes": {
    "hikam": ["quote1", "quote2", ...]
  }
}
```

### Par catégorie (hikam.json, love.json, etc.)
```json
{
  "category": {
    "id": "hikam",
    "name": "Hikam",
    "description": "حكم عن الحياة والناس"
  },
  "quotes": ["quote1", "quote2", ...]
}
```

## 🚀 Développement

Chaque catégorie contient 100 citations.

---

Made with ❤️ by gamedrivne
