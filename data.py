# -*- coding: utf-8 -*-
"""Knowledge base for TripMate AI — Tour & Travel chatbot."""

DESTINATIONS = {
    "goa": {
        "name": "Goa", "aliases": ["goa"],
        "duration": "4D/3N", "price": "₹12,999",
        "highlights": ["Beach parties", "Water sports", "Old Goa churches", "Nightlife"],
        "best_time": "November – February",
    },
    "manali": {
        "name": "Manali", "aliases": ["manali", "himachal"],
        "duration": "5D/4N", "price": "₹14,499",
        "highlights": ["Rohtang Pass", "Paragliding", "River rafting", "Solang Valley"],
        "best_time": "March – June, Dec – Jan (snow)",
    },
    "kerala": {
        "name": "Kerala", "aliases": ["kerala", "munnar", "alleppey"],
        "duration": "6D/5N", "price": "₹18,999",
        "highlights": ["Houseboat stay", "Tea gardens", "Ayurvedic spa", "Backwaters"],
        "best_time": "September – March",
    },
    "rajasthan": {
        "name": "Rajasthan", "aliases": ["rajasthan", "jaipur", "udaipur", "jodhpur"],
        "duration": "7D/6N", "price": "₹21,499",
        "highlights": ["Palaces & forts", "Desert safari", "Lake Pichola", "Local bazaars"],
        "best_time": "October – March",
    },
    "kashmir": {
        "name": "Kashmir", "aliases": ["kashmir", "srinagar", "gulmarg"],
        "duration": "6D/5N", "price": "₹23,999",
        "highlights": ["Dal Lake shikara", "Gulmarg gondola", "Trekking", "Houseboat"],
        "best_time": "April – October",
    },
    "dubai": {
        "name": "Dubai", "aliases": ["dubai", "uae"],
        "duration": "5D/4N", "price": "₹54,999",
        "highlights": ["Burj Khalifa", "Desert safari", "Dubai Mall", "Marina cruise"],
        "best_time": "November – March",
    },
    "bali": {
        "name": "Bali", "aliases": ["bali", "indonesia"],
        "duration": "6D/5N", "price": "₹58,999",
        "highlights": ["Ubud rice terraces", "Beach clubs", "Temples", "Water villas"],
        "best_time": "April – October",
    },
    "thailand": {
        "name": "Thailand", "aliases": ["thailand", "phuket", "bangkok", "pattaya"],
        "duration": "6D/5N", "price": "₹42,999",
        "highlights": ["Phi Phi islands", "Street markets", "Temples", "Nightlife"],
        "best_time": "November – February",
    },
    "singapore": {
        "name": "Singapore", "aliases": ["singapore"],
        "duration": "5D/4N", "price": "₹65,999",
        "highlights": ["Gardens by the Bay", "Sentosa Island", "Universal Studios", "Marina Bay"],
        "best_time": "February – April",
    },
    "maldives": {
        "name": "Maldives", "aliases": ["maldives"],
        "duration": "4D/3N", "price": "₹89,999",
        "highlights": ["Overwater villas", "Snorkeling", "Private beaches", "Sunset cruise"],
        "best_time": "November – April",
    },
    "europe": {
        "name": "Europe (Paris–Switzerland)", "aliases": ["europe", "paris", "switzerland"],
        "duration": "10D/9N", "price": "₹1,45,999",
        "highlights": ["Eiffel Tower", "Swiss Alps", "River Seine cruise", "Alpine trains"],
        "best_time": "May – September",
    },
}

INTENTS = [
    {"tag": "greeting", "patterns": [
        "hi", "hello", "hey", "namaste", "good morning", "good evening", "yo", "hii", "helo", "kaise ho"],
        "responses": [
            "👋 Namaste! Main TripMate hoon, aapka personal travel assistant. Kahan ghoomne ka plan hai?",
            "Hello! Ready to plan your next adventure? Ask me about destinations, packages, or booking!"]},

    {"tag": "list_destinations", "patterns": [
        "list destinations", "which places do you cover", "destinations available", "where can i travel",
        "show me destinations", "tour options", "places you offer", "kaha kaha ghuma sakte ho", "all destinations"],
        "responses": ["Hum in destinations ke liye packages offer karte hain: {destinations}.\n\nKisi bhi jagah ka naam batayein, main package details bhej dunga!"]},

    {"tag": "packages_general", "patterns": [
        "tell me about packages", "what packages do you have", "tour packages", "show packages", "packages available"],
        "responses": ["Hamare paas domestic aur international dono tarah ke packages hain — Goa, Manali, Kerala, Rajasthan, Kashmir se lekar Dubai, Bali, Thailand, Singapore, Maldives aur Europe tak! Kisi specific destination ka naam bataiye."]},

    {"tag": "pricing", "patterns": [
        "price", "cost", "how much does it cost", "budget", "fees", "charges kya hai", "total cost", "kitna paisa lagega"],
        "responses": ["Packages ₹9,999 se shuru hokar ₹1,50,000+ tak range karte hain, destination aur duration ke hisaab se. Kis jagah ka price chahiye?"]},

    {"tag": "best_time", "patterns": [
        "best time to visit", "when should i go", "weather", "season for travel", "best season", "kab jaana chahiye"],
        "responses": ["Best time destination pe depend karta hai — hills October-March mein best hain, beaches November-February mein. Kis jagah ke liye poochh rahe hain?"]},

    {"tag": "visa", "patterns": [
        "visa", "documents required", "passport", "international travel documents", "visa process", "visa lagta hai kya"],
        "responses": ["International trips ke liye valid passport (6+ months validity) aur destination-specific visa chahiye hota hai. Hum visa assistance bhi provide karte hain — application se lekar appointment tak!"]},

    {"tag": "booking_process", "patterns": [
        "how to book", "booking process", "how do i book a trip", "book a package", "reserve a tour", "booking kaise kare"],
        "responses": ["Booking simple hai: 1) Destination choose karein 2) Package customize karein 3) 20% advance payment karein 4) Confirmation milega instantly! Chahenge main aapke liye shuru karu?"]},

    {"tag": "payment", "patterns": [
        "payment methods", "how can i pay", "upi", "credit card accepted", "payment options", "emi available"],
        "responses": ["Hum UPI, credit/debit cards, net banking aur EMI options accept karte hain. Advance payment sirf 20% hai, baaki trip se pehle."]},

    {"tag": "cancellation", "patterns": [
        "cancellation policy", "refund", "can i cancel my trip", "cancel booking", "trip cancel karni hai"],
        "responses": ["Cancellation 15+ din pehle: 90% refund. 7-14 din: 50% refund. 7 din se kam: no refund. Travel insurance lene se aap fully protected rehte hain."]},

    {"tag": "group_discount", "patterns": [
        "group discount", "corporate tour", "discount for groups", "bulk booking", "group booking discount"],
        "responses": ["10+ logo ke group ke liye 15% discount, aur corporate tours ke liye customized packages bhi available hain!"]},

    {"tag": "honeymoon", "patterns": [
        "honeymoon package", "romantic trip", "couple package", "honeymoon destination"],
        "responses": ["Humare honeymoon specials: Maldives, Bali aur Kashmir mein candlelight dinner, couple spa aur private stays ke saath!"]},

    {"tag": "adventure", "patterns": [
        "adventure tour", "trekking", "paragliding", "adventure sports", "rafting"],
        "responses": ["Adventure lovers ke liye Manali (paragliding, river rafting) aur Kashmir (trekking) top picks hain!"]},

    {"tag": "family", "patterns": [
        "family package", "trip with kids", "family friendly tour", "kids friendly trip"],
        "responses": ["Family packages mein kid-friendly activities, spacious stays aur flexible itineraries included hain — Goa aur Kerala especially popular hain families ke beech."]},

    {"tag": "custom_itinerary", "patterns": [
        "custom itinerary", "plan my own trip", "customize my trip", "personalized tour", "apna khud ka trip banao"],
        "responses": ["Bilkul! Bataiye aapki dates, budget aur interests — hum aapke liye ek fully customized itinerary bana denge."]},

    {"tag": "baggage", "patterns": [
        "baggage allowance", "luggage limit", "how much luggage", "saman kitna le ja sakte hai"],
        "responses": ["Domestic flights: 15kg check-in + 7kg cabin. International: airline ke hisaab se 20-30kg. Exact limit booking ke time confirm kar dete hain."]},

    {"tag": "insurance", "patterns": [
        "travel insurance", "trip insurance", "insurance cover", "insurance chahiye"],
        "responses": ["Travel insurance optional hai lekin highly recommended — medical emergencies, trip cancellation aur lost baggage cover karta hai. Sirf ₹299 se shuru!"]},

    {"tag": "contact", "patterns": [
        "contact support", "talk to agent", "customer care", "phone number", "email", "agent se baat karni hai"],
        "responses": ["Aap humein support@tripmate.example par email kar sakte hain, ya bas type karein 'talk to agent' — humari team turant reply karegi."]},

    {"tag": "about", "patterns": [
        "who are you", "what is tripmate", "about your agency", "tell me about yourself", "tum kaun ho"],
        "responses": ["Main TripMate AI hoon 🌍 — ek smart travel assistant jo aapke liye best destinations, packages aur travel tips dhundta hai!"]},

    {"tag": "thanks", "patterns": [
        "thanks", "thank you", "shukriya", "great help", "helpful hai"],
        "responses": ["Aapka swagat hai! 😊 Aur kuch janna hai apni trip ke baare mein?"]},

    {"tag": "bye", "patterns": [
        "bye", "goodbye", "see you", "alvida", "chalta hu"],
        "responses": ["Bye! Happy travels 🧳✈️ — dobara zarurat pade toh main yahin hoon."]},
]

FAQS = [
    {"q": "What is the minimum advance payment?", "a": "20% of the total package cost confirms your booking; the rest is due before travel."},
    {"q": "Do you offer EMI options?", "a": "Yes, no-cost EMI is available on select bank credit cards."},
    {"q": "Can I customize my itinerary?", "a": "Absolutely — share your dates, budget and interests and we'll tailor a plan just for you."},
    {"q": "Is travel insurance included?", "a": "Not by default, but it can be added to any package starting at ₹299."},
    {"q": "What documents are needed for international trips?", "a": "A passport valid for 6+ months and a visa as required for the destination."},
    {"q": "What is your cancellation policy?", "a": "15+ days before travel: 90% refund. 7–14 days: 50% refund. Under 7 days: no refund."},
    {"q": "Do you provide airport pickup?", "a": "Yes, airport transfers are included in most of our packages."},
    {"q": "Can I get a group discount?", "a": "Yes! Groups of 10 or more get a flat 15% discount."},
    {"q": "What's the best time to visit hill stations?", "a": "October to March is ideal for most Indian hill destinations."},
    {"q": "How do I contact customer support?", "a": "Email support@tripmate.example or type 'talk to agent' in the chat anytime."},
    {"q": "Do you help with visas?", "a": "Yes, we offer end-to-end visa assistance including document checklists and appointments."},
    {"q": "Are flights included in the package price?", "a": "Domestic packages usually exclude flights; international packages often bundle them — this is confirmed per destination."},
]
