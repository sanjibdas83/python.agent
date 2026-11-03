const chatForm = document.getElementById('chatForm');
const messageInput = document.getElementById('messageInput');
const chatMessages = document.getElementById('chatMessages');
const sendBtn = document.getElementById('sendBtn');
const dbStatus = document.getElementById('dbStatus');

function appendMessage(role, text) {
  const wrapper = document.createElement('div');
  wrapper.className = `message ${role}`;

  const bubble = document.createElement('div');
  bubble.className = 'bubble';
  bubble.textContent = text;

  wrapper.appendChild(bubble);
  chatMessages.appendChild(wrapper);
  chatMessages.scrollTop = chatMessages.scrollHeight;
}

async function checkDbStatus() {
  try {
    const response = await fetch('/api/v1/health');
    if (!response.ok) {
      throw new Error('Health endpoint unavailable');
    }
    const data = await response.json();
    dbStatus.textContent = data.status === 'ok' ? 'Service healthy' : 'Database check pending';
    dbStatus.style.background = 'rgba(34, 197, 94, 0.14)';
    dbStatus.style.color = '#bbf7d0';
  } catch (error) {
    dbStatus.textContent = 'Service unavailable';
    dbStatus.style.background = 'rgba(245, 158, 11, 0.12)';
    dbStatus.style.color = '#fcd34d';
  }
}

chatForm.addEventListener('submit', async (event) => {
  event.preventDefault();

  const text = messageInput.value.trim();
  if (!text) return;

  appendMessage('user', text);
  messageInput.value = '';
  sendBtn.disabled = true;

  try {
    const response = await fetch('/api/v1/chat', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ message: text, session_id: 'browser-session' }),
    });

    if (!response.ok) {
      throw new Error('Request failed');
    }

    const data = await response.json();
    appendMessage('bot', data.response || 'No reply received.');
  } catch (error) {
    appendMessage('bot', 'The assistant could not respond right now. Please check the backend service.');
  } finally {
    sendBtn.disabled = false;
    messageInput.focus();
  }
});

checkDbStatus();
