<template>
  <div :class="['message', sender]">
    <p>{{ message.text }}</p>
  </div>
</template>

<script>
export default {
  props: {
    message: Object,
    sender: String,
  },
};
</script>

<style scoped>
.message {
  margin: 10px 0;
  padding: 10px;
  border-radius: 10px;
  max-width: 80%;
  background-color: var(--message-bg-bot);
  color: var(--text-color);
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.message.user {
  background-color: var(--message-bg-user);
  align-self: flex-end;
}

.message.bot {
  background-color: var(--message-bg-bot);
  align-self: flex-start;
}
</style>
