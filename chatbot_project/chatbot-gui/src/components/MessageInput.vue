<template>
    <div class="message-input">
      <input
        v-model="text"
        @keyup.enter="handleSend"
        type="text"
        placeholder="Type a message..."
      />
      <button @click="handleSend">Send</button>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        text: '',
      };
    },
    methods: {
      handleSend() {
        if (this.text.trim()) {
          this.$emit('sendMessage', this.text);
          this.text = '';
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .message-input {
    display: flex;
    padding: 10px;
    border-top: 1px solid var(--border-color);
    background: var(--input-bg);
  }
  
  input {
    flex: 1;
    padding: 10px;
    border: none;
    border-radius: 5px;
    background: var(--input-bg);
    color: var(--text-color);
  }
  
  input:focus {
    outline: none;
    box-shadow: 0 0 5px var(--primary-color);
  }
  
  button {
    padding: 10px 15px;
    margin-left: 10px;
    border: none;
    background-color: var(--primary-color);
    color: white;
    border-radius: 5px;
    cursor: pointer;
  }
  
  button:hover {
    background-color: var(--secondary-color);
  }
  </style>
  