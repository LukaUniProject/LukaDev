<template>
    <div class="auth-container">
      <button class="back-button" @click="goBack">← Назад</button>
      <div class="form-container">
        <h2>Регистрация</h2>
        <form @submit.prevent="submitForm">
          <div class="form-group">
            <label for="username">Имя пользователя</label>
            <input type="text" id="username" v-model="username" required />
          </div>
          <div class="form-group">
            <label for="email">Электронная почта</label>
            <input type="email" id="email" v-model="email" required />
          </div>
          <div class="form-group">
            <label for="password">Пароль</label>
            <input type="password" id="password" v-model="password" required />
          </div>
          <div class="form-group">
            <label for="confirm-password">Повторите пароль</label>
            <input
              type="password"
              id="confirm-password"
              v-model="confirmPassword"
              required
            />
          </div>
          <div v-if="errorMessage" class="error-message">{{ errorMessage }}</div>
          <button type="submit" class="submit-button">Зарегистрироваться</button>
        </form>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        username: '',
        email: '',
        password: '',
        confirmPassword: '',
        errorMessage: '',
      };
    },
    methods: {
      goBack() {
        this.$router.go(-1);
      },
      submitForm() {

      },
    },
  };
  </script>
  
  <style scoped>
  .auth-container {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    background-color: var(--color-background);
  }
  
  .back-button {
    position: absolute;
    top: 20px;
    left: 20px;
    color: var(--color-heading);
    background: none;
    border: none;
    font-size: 1.5em;
    cursor: pointer;
  }
  
  .form-container {
    width: 100%;
    max-width: 500px;
    padding: 2em;
    background-color: var(--color-background-light);
    box-shadow: 0 4px 8px var(--color-shadow);
    border-radius: var(--border-radius);
    text-align: center;
  }
  
  h2 {
    color: var(--color-heading);
    margin-bottom: 1em;
  }
  
  .form-group {
    margin-bottom: 1.5em;
    text-align: left;
  }
  
  label {
    display: block;
    margin-bottom: 0.5em;
    color: var(--color-text-muted);
    font-weight: bold;
  }
  
  input[type="text"],
  input[type="email"],
  input[type="password"] {
    width: 100%;
    padding: 0.8em;
    margin-top: 0.5em;
    border: 1px solid var(--color-border);
    border-radius: var(--border-radius);
    font-size: 1rem;
  }
  
  input[type="text"]:focus,
  input[type="email"]:focus,
  input[type="password"]:focus {
    border-color: var(--color-accent);
    outline: none;
  }
  
  .error-message {
    color: var(--color-error);
    margin-bottom: 1em;
    font-size: 0.9rem;
  }
  
  .submit-button {
    width: 100%;
    padding: 0.8em;
    background-color: var(--color-accent);
    color: var(--color-background-light);
    border: none;
    border-radius: var(--border-radius);
    cursor: pointer;
    font-weight: bold;
    font-size: 1rem;
    transition: background-color var(--transition-speed);
  }
  
  .submit-button:hover {
    background-color: var(--color-accent-hover);
  }
  
  .submit-button:active {
    background-color: var(--color-accent-active);
  }
  
  .submit-button:focus {
    outline: none;
  }
  </style>
  