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
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
