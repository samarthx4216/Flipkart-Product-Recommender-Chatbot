const API_URL = 'http://localhost:8000';

function addMessage(content, isUser, sources = []) {
  const messages = document.getElementById('messages');
  const div = document.createElement('div');
  div.className = `message ${isUser ? 'user-message' : 'bot-message'}`;

  let sourcesHTML = '';
  if (sources.length > 0) {
    sourcesHTML = `<div class="sources">
      📦 Products found: ${sources.map(s => `<span>${s}</span>`).join('')}
    </div>`;
  }

  div.innerHTML = `
    <div class="avatar">${isUser ? '👤' : '🤖'}</div>
    <div class="bubble">
      ${content}
      ${sourcesHTML}
    </div>
  `;

  messages.appendChild(div);
  messages.scrollTop = messages.scrollHeight;
}

function addTyping() {
  const messages = document.getElementById('messages');
  const div = document.createElement('div');
  div.className = 'message bot-message';
  div.id = 'typing';
  div.innerHTML = `
    <div class="avatar">🤖</div>
    <div class="typing">
      <span></span><span></span><span></span>
    </div>
  `;
  messages.appendChild(div);
  messages.scrollTop = messages.scrollHeight;
}

function removeTyping() {
  const typing = document.getElementById('typing');
  if (typing) typing.remove();
}

async function sendMessage() {
  const input = document.getElementById('userInput');
  const btn = document.getElementById('sendBtn');
  const message = input.value.trim();

  if (!message) return;

  // Hide suggestions
  document.getElementById('suggestions').style.display = 'none';

  // Add user message
  addMessage(message, true);
  input.value = '';
  btn.disabled = true;

  // Show typing
  addTyping();

  try {
    const response = await fetch(`${API_URL}/chat`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message })
    });

    const data = await response.json();
    removeTyping();
    addMessage(data.answer, false, data.sources);
  } catch (err) {
    removeTyping();
    addMessage(
      'Sorry, I could not connect to the server. Please try again!',
      false
    );
  }

  btn.disabled = false;
  input.focus();
}

function sendSuggestion(text) {
  document.getElementById('userInput').value = text;
  sendMessage();
}

function handleKeyPress(event) {
  if (event.key === 'Enter') sendMessage();
}