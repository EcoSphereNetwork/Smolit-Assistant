<template>
  <div :class="['message', sender]">
    <p>{{ message.text }}</p>
  </div>
</template>

<script>
export default {
  props: {
    message: Object,
  },
};
</script>

<style scoped>
.message {
  margin: 10px 0;
  padding: 10px;
  border-radius: 10px;
  max-width: 80%;
}

.message.user {
  background-color: #e6f7ff;
  align-self: flex-end;
}

.message.bot {
  background-color: #f5f5f5;
  align-self: flex-start;
}
</style>
