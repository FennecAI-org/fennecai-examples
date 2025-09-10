# python/quickstart.py  (Demo – Platzhalter-Endpunkt)
import os, json, urllib.request

API_URL = "https://api.example.com/chat"  # Platzhalter
API_KEY = os.getenv("FENNECAI_API_KEY")   # Niemals Keys committen!

req = urllib.request.Request(
    API_URL,
    data=json.dumps({"message": "Hallo FennecAI!", "locale": "de"}).encode("utf-8"),
    headers={"Content-Type": "application/json", "Authorization": f"Bearer {API_KEY}"}
)
with urllib.request.urlopen(req) as res:
    print("Antwort:", json.loads(res.read().decode("utf-8")).get("reply"))
