# -*- coding: utf-8 -*-
import re
import random
from flask import Flask, render_template, request, jsonify
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from data import INTENTS, DESTINATIONS, FAQS

app = Flask(__name__)

# ---------- Build the intent matcher ----------
def clean(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    return re.sub(r"\s+", " ", text).strip()

PATTERNS, TAGS = [], []
for intent in INTENTS:
    for p in intent["patterns"]:
        PATTERNS.append(clean(p))
        TAGS.append(intent["tag"])

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(PATTERNS)
INTENT_MAP = {i["tag"]: i for i in INTENTS}

DEST_LOOKUP = {}
for key, info in DESTINATIONS.items():
    for alias in info["aliases"]:
        DEST_LOOKUP[alias] = key


def find_destination(cleaned_text: str):
    for alias, key in DEST_LOOKUP.items():
        if re.search(rf"\b{re.escape(alias)}\b", cleaned_text):
            return key
    return None


def destination_reply(key: str) -> str:
    d = DESTINATIONS[key]
    highlights = ", ".join(d["highlights"])
    return (
        f"🌍 {d['name']} Package\n"
        f"🗓️ Duration: {d['duration']}\n"
        f"💰 Price: {d['price']} per person\n"
        f"⭐ Highlights: {highlights}\n"
        f"📅 Best Time: {d['best_time']}\n\n"
        f"Availability check ya full itinerary chahiye ho toh bataiye!"
    )


def get_response(user_text: str):
    cleaned = clean(user_text)

    dest = find_destination(cleaned)
    if dest:
        return destination_reply(dest), 0.97, "package_query"

    if not PATTERNS:
        return "Sorry, I couldn't understand that. Could you rephrase?", 0.0, "fallback"

    vec = vectorizer.transform([cleaned])
    sims = cosine_similarity(vec, X)[0]
    best_idx = int(sims.argmax())
    confidence = float(sims[best_idx])
    tag = TAGS[best_idx]

    if confidence < 0.25:
        return (
            "Hmm, main is baare mein sure nahi hoon 🤔. Try: 'list destinations', "
            "'Goa package', ya 'booking process'.",
            confidence,
            "fallback",
        )

    intent = INTENT_MAP[tag]
    response = random.choice(intent["responses"])
    if tag == "list_destinations":
        names = ", ".join(sorted(d["name"] for d in DESTINATIONS.values()))
        response = response.format(destinations=names)
    return response, confidence, tag


# ---------- Routes ----------
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/chat", methods=["POST"])
def chat():
    payload = request.get_json(force=True, silent=True) or {}
    message = (payload.get("message") or "").strip()
    if not message:
        return jsonify({"reply": "Kuch likhiye toh sahi! 😊", "confidence": 0, "tag": "empty"})
    reply, confidence, tag = get_response(message)
    return jsonify({"reply": reply, "confidence": round(confidence, 3), "tag": tag})


@app.route("/api/faqs")
def faqs():
    return jsonify(FAQS)


@app.route("/api/destinations")
def destinations():
    return jsonify([
        {"key": k, **{kk: vv for kk, vv in v.items() if kk != "aliases"}}
        for k, v in DESTINATIONS.items()
    ])


if __name__ == "__main__":
    app.run(debug=True)
