// node/hello-chat.js  (Demo – Platzhalter-Endpunkt)
// Voraussetzung: Node 18+ (fetch ist global verfügbar)

async function askFennecAI(message) {
  const res = await fetch("https://api.example.com/chat", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "Authorization": `Bearer ${process.env.FENNECAI_API_KEY}` // Niemals echte Keys committen!
    },
    body: JSON.stringify({ message, locale: "de" })
  });
  const data = await res.json();
  console.log("Antwort:", data.reply);
}

askFennecAI("Hallo FennecAI!");
