<template>
  <div class="chat-window">
    <div class="messages">
      <ChatMessage
        v-for="(msg, index) in messages"
        :key="index"
        :message="msg"
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
    };
  },
  methods: {
    async sendMessage(text) {
      this.messages.push({ text, sender: 'user' });
      const response = await axios.post('/api/chat', { message: text });
      this.messages.push({ text: response.data.reply, sender: 'bot' });
    },
  },
};
</script>

<style scoped>
.chat-window {
  max-width: 600px;
  margin: 0 auto;
  background: #fff;
  border: 1px solid #ddd;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}
.messages {
  padding: 20px;
  height: 400px;
  overflow-y: scroll;
}
</style>
