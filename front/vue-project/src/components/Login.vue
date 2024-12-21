<template>
  <div class="auth-container">
    <button class="back-button" @click="goBack">← Назад</button>
    <div class="form-container">
      <h2>Вход</h2>
      <form @submit.prevent="submitForm">
        <div class="form-group">
          <label for="email">Электронная почта</label>
          <input type="email" id="email" v-model="email" required />
        </div>
        <div class="form-group">
          <label for="password">Пароль</label>
          <input type="password" id="password" v-model="password" required />
        </div>
        <button type="submit" class="submit-button">Войти</button>
      </form>
      <div class="if-not-container">
        <p>Если вы не зарегистированы - <a href="/register">Зарегистрироваться</a></p>
      </div>
    </div>
  </div>
</template>
  
<script>
import axios from "axios";

export default {
  name: "Login",
  data() {
    return {
      email: "",
      password: "",
      errorMessage: "",
      isSubmitting: false,
    };
  },
  methods: {
    goBack() {
      this.$router.push({ name: 'home' });
    },
    async submitForm() {
      this.isSubmitting = true; // Отображение индикатора загрузки
      this.errorMessage = ""; // Сброс ошибки

      try {
        const response = await axios.post("http://127.0.0.1:8000/api/auth/login", {
          email: this.email,
          password: this.password,
        });

        // Сохранение токена в localStorage
        const jwtToken = response.data.token;
        localStorage.setItem("jwt", jwtToken);

        // Редирект на страницу PersonalAccount
        this.$router.push({ name: 'PersonalAccount' });

      } catch (error) {
        this.errorMessage = "Ошибка входа: " + (error.response?.data?.detail || error.message);
      } finally {
        this.isSubmitting = false;
      }
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

input[type="email"],
input[type="password"] {
  width: 100%;
  padding: 0.8em;
  margin-top: 0.5em;
  border: 1px solid var(--color-border);
  border-radius: var(--border-radius);
  font-size: 1rem;
}

input[type="email"]:focus,
input[type="password"]:focus {
  border-color: var(--color-accent);
  outline: none;
}

.submit-button {
  width: 100%;
  padding: 0.8em;
  background-color: var(--color-accent);
  color: var(--color-text-muted);
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
  background-color: var(--color-accent);
}

.submit-button:focus {
  outline: none;
}

.if-not-container {
  color: var(--color-text-muted);
}

.if-not-container a {
  color: var(--color-accent);
}
</style>
  