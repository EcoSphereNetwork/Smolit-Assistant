<template>
  <div :class="['chat-window', currentTheme]">
    <div class="header">
      <h2>ChatBot</h2>
      <button @click="toggleTheme">{{ themeLabel }}</button>
    </div>
    <div class="messages">
      <ChatMessage
        v-for="(msg, index) in messages"
        :key="index"
        :message="msg"
        :sender="msg.sender"
      />
    </div>
    <MessageInput @sendMessage="sendMessage" />
  </div>
</template>

<script>
import ChatMessage from './ChatMessage.vue';
import MessageInput from './MessageInput.vue';
import axios from 'axios';

export default {
  components: { ChatMessage, MessageInput },
  data() {
    return {
      messages: [],
      currentTheme: 'light-mode',
    };
  },
  computed: {
    themeLabel() {
      return this.currentTheme === 'light-mode' ? 'Dark Mode' : 'Light Mode';
    },
  },
  methods: {
    async sendMessage(text) {
      this.messages.push({ text, sender: 'user' });
      const response = await axios.post('/api/chat', { message: text });
      this.messages.push({ text: response.data.reply, sender: 'bot' });
    },
    toggleTheme() {
      this.currentTheme =
        this.currentTheme === 'light-mode' ? 'dark-mode' : 'light-mode';
      document.body.className = this.currentTheme;
      localStorage.setItem('theme', this.currentTheme);
    },
  },
  created() {
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme) {
      this.currentTheme = savedTheme;
      document.body.className = this.currentTheme;
    }
  },
};
</script>

<style scoped>
.chat-window {
  max-width: 600px;
  margin: 0 auto;
  background: var(--background-color);
  color: var(--text-color);
  border: 1px solid var(--border-color);
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
  display: flex;
  flex-direction: column;
}

.header {
  display: flex;
  justify-content: space-between;
  padding: 10px 20px;
  background: var(--primary-color);
  color: #fff;
}

.header h2 {
  margin: 0;
  font-size: 1.5rem;
}

.header button {
  background: none;
  border: none;
  color: #fff;
  cursor: pointer;
  font-size: 1rem;
}

.header button:hover {
  text-decoration: underline;
}

.messages {
  padding: 20px;
  height: 400px;
  overflow-y: scroll;
}

.message-input {
  background: var(--input-bg);
}
</style>
