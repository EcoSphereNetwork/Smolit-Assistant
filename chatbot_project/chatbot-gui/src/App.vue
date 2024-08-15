<template>
  <div id="app">
    <ChatWindow />
  </div>
</template>

<script>
import ChatWindow from './components/ChatWindow.vue';

export default {
  components: {
    ChatWindow,
  },
};
</script>

<style>
#app {
  font-family: 'Roboto', sans-serif;
  text-align: center;
  color: var(--text-color);
  margin-top: 60px;
}
</style>

<style>
:root {
  --primary-color: #9F0E8A;
  --secondary-color: #1890ff;
  --background-color: #C0EDED;
  --text-color: #333;
  --message-bg-user: #1890ff;
  --message-bg-bot: #40E41B;
  --input-bg: #96B7B7;
  --border-color: #AB0895F7;
}

body.dark-mode {
  --primary-color: #AB0895F7;
  --secondary-color: #1890ff;
  --background-color: #2c3e50;
  --text-color: #f5f5f5;
  --message-bg-user: #1a3d5e;
  --message-bg-bot: #40E41B;
  --input-bg: #364759;
  --border-color: #AB0895F7;
}
</style>