# TripMate AI — Tour & Travel Chatbot

Ek ready-to-run Flask chatbot jo tour & travel queries handle karta hai — destinations,
package pricing, visa, booking process, cancellation policy, FAQs, aur more.

## (Windows PowerShell)

1. Zip ko extract karein aur folder me jaayein:
   ```
   cd travel-chatbot
   ```
2. Dependencies install karein:
   ```
   pip install -r requirements.txt
   ```
3. App start karein:
   ```
   python app.py
   ```
4. Browser me kholein:
   ```
   http://127.0.0.1:5000
   ```

## Features
- Smart intent matching (TF-IDF + cosine similarity, scikit-learn) — 20 intents, 11 destinations
- Destination-aware replies (e.g. "Goa package", "price for Manali")
- "Destinations" tab — visual package cards
- "FAQs" tab — accordion-style, 12 common questions
- Match-confidence badge on every bot reply
- Typing indicator + quick-suggestion chips
- Clean, mobile-friendly UI, no external CDN dependency

## Customize
- Add/edit destinations, intents aur FAQs in `data.py`
- Colors/theme in `static/style.css` (CSS variables at the top)

## Project structure
```
travel-chatbot/
├── app.py
├── data.py
├── requirements.txt
├── templates/
│   └── index.html
└── static/
    ├── style.css
    └── script.js
```
