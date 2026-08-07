// ---------- Tabs ----------
const tabBtns = document.querySelectorAll(".tab-btn");
const panels = {
  chat: document.getElementById("panel-chat"),
  destinations: document.getElementById("panel-destinations"),
  faq: document.getElementById("panel-faq"),
};

tabBtns.forEach(btn => {
  btn.addEventListener("click", () => {
    tabBtns.forEach(b => b.classList.remove("active"));
    btn.classList.add("active");
    Object.values(panels).forEach(p => p.classList.add("hidden"));
    panels[btn.dataset.tab].classList.remove("hidden");
    if (btn.dataset.tab === "destinations") loadDestinations();
    if (btn.dataset.tab === "faq") loadFaqs();
  });
});

// ---------- Chat ----------
const chatWindow = document.getElementById("chatWindow");
const chatForm = document.getElementById("chatForm");
const userInput = document.getElementById("userInput");
const quickChips = document.getElementById("quickChips");

function scrollToBottom() {
  chatWindow.scrollTop = chatWindow.scrollHeight;
}

function addMessage(text, sender, confidence) {
  const msg = document.createElement("div");
  msg.className = `msg ${sender}`;
  const bubble = document.createElement("div");
  bubble.className = "bubble";
  bubble.textContent = text;
  msg.appendChild(bubble);
  if (sender === "bot" && typeof confidence === "number") {
    const badge = document.createElement("div");
    badge.className = "confidence-badge";
    badge.textContent = `match confidence: ${confidence}`;
    msg.appendChild(badge);
  }
  chatWindow.appendChild(msg);
  scrollToBottom();
}

function showTyping() {
  const msg = document.createElement("div");
  msg.className = "msg bot";
  msg.id = "typingIndicator";
  msg.innerHTML = `<div class="bubble typing"><span></span><span></span><span></span></div>`;
  chatWindow.appendChild(msg);
  scrollToBottom();
}

function hideTyping() {
  const el = document.getElementById("typingIndicator");
  if (el) el.remove();
}

async function sendMessage(text) {
  if (!text.trim()) return;
  addMessage(text, "user");
  userInput.value = "";
  showTyping();
  try {
    const res = await fetch("/api/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: text }),
    });
    const data = await res.json();
    setTimeout(() => {
      hideTyping();
      addMessage(data.reply, "bot", data.confidence);
    }, 350);
  } catch (err) {
    hideTyping();
    addMessage("Oops, connection issue. Please try again.", "bot", 0);
  }
}

chatForm.addEventListener("submit", e => {
  e.preventDefault();
  sendMessage(userInput.value);
});

quickChips.addEventListener("click", e => {
  if (e.target.classList.contains("chip")) {
    sendMessage(e.target.textContent);
  }
});

// ---------- Destinations ----------
let destLoaded = false;
async function loadDestinations() {
  if (destLoaded) return;
  const grid = document.getElementById("destGrid");
  const res = await fetch("/api/destinations");
  const data = await res.json();
  grid.innerHTML = data.map(d => `
    <div class="dest-tile">
      <h3>${d.name}</h3>
      <div class="price">${d.price}</div>
      <div class="dur">${d.duration} · Best: ${d.best_time}</div>
      <ul>${d.highlights.map(h => `<li>${h}</li>`).join("")}</ul>
    </div>
  `).join("");
  destLoaded = true;
}

// ---------- FAQs ----------
let faqLoaded = false;
async function loadFaqs() {
  if (faqLoaded) return;
  const list = document.getElementById("faqList");
  const res = await fetch("/api/faqs");
  const data = await res.json();
  list.innerHTML = data.map((f, i) => `
    <div class="faq-item" data-idx="${i}">
      <button class="faq-q">${f.q} <span class="faq-icon">+</span></button>
      <div class="faq-a">${f.a}</div>
    </div>
  `).join("");
  list.querySelectorAll(".faq-item").forEach(item => {
    item.querySelector(".faq-q").addEventListener("click", () => {
      item.classList.toggle("open");
    });
  });
  faqLoaded = true;
}
