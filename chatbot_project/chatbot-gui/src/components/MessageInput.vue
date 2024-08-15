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
    border-top: 1px solid #ddd;
    background: #f9f9f9;
  }
  
  input {
    flex: 1;
    padding: 10px;
    border: none;
    border-radius: 5px;
  }
  
  button {
    padding: 10px 15px;
    margin-left: 10px;
    border: none;
    background-color: #1890ff;
    color: white;
    border-radius: 5px;
    cursor: pointer;
  }
  
  button:hover {
    background-color: #40a9ff;
  }
  </style>
  