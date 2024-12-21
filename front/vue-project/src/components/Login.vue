<template>
  <div class="auth-container">
    <button class="back-button" @click="goBack">← Назад</button>
    <div class="form-container">
      <h2>Вход</h2>
      <form @submit.prevent="submitForm">
        <div class="form-group">
          <label for="username">Имя пользователя</label>
          <input type="text" id="username" v-model="username" required />
        </div>
        <div class="form-group">
          <label for="password">Пароль</label>
          <input type="password" id="password" v-model="password" required />
        </div>
        <button type="submit" class="submit-button" :disabled="isSubmitting">
          Войти
        </button>
      </form>
      <div class="if-not-container">
        <p>
          Если вы не зарегистированы -
          <a href="/register">Зарегистрироваться</a>
        </p>
      </div>
      <div v-if="errorMessage" class="error-message">{{ errorMessage }}</div>
    </div>
  </div>
</template>

<script>
import axios from "axios"

export default {
  name: "Login",
  data() {
    return {
      username: "",
      password: "",
      errorMessage: "",
      isSubmitting: false,
    }
  },
  methods: {
    goBack() {
      this.$router.push({ name: "home" })
    },
    async submitForm() {
      this.isSubmitting = true // Отображение индикатора загрузки
      this.errorMessage = "" // Сброс ошибки

      try {
        const response = await axios.post(
          "http://127.0.0.1:8000/login",
          {
            username: this.username,
            password: this.password,
          },
          {
            headers: {
              "Content-Type": "application/json", // Убедитесь, что отправляется правильный тип контента
            },
          }
        )

        // Сохранение токена в localStorage
        const jwtToken = response.data.access_token
        localStorage.setItem("jwt", jwtToken)

        // Редирект на страницу PersonalAccount
        this.$router.push({ name: "PersonalAccount" })
      } catch (error) {
        this.errorMessage =
          "Ошибка входа: " + (error.response?.data?.detail || error.message)
      } finally {
        this.isSubmitting = false
      }
    },
  },
}
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
input[type="password"] {
  width: 100%;
  padding: 0.8em;
  margin-top: 0.5em;
  border: 1px solid var(--color-border);
  border-radius: var(--border-radius);
  font-size: 1rem;
}

input[type="text"]:focus,
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

.error-message {
  color: red;
  margin-top: 10px;
}

/* Адаптивность для мобильных устройств */
@media (max-width: 768px) {
  .form-container {
    padding: 1.5em;
    max-width: 90%;
  }
  h2 {
    font-size: 1.5rem;
  }
  .form-group label {
    font-size: 1rem;
  }
  input[type="email"],
  input[type="password"] {
    font-size: 0.9rem;
    padding: 0.75em;
  }
  .submit-button {
    font-size: 0.9rem;
    padding: 0.75em;
  }
  .back-button {
    font-size: 1.2em;
    top: 15px;
    left: 15px;
  }
}
@media (max-width: 480px) {
  .form-container {
    padding: 1em;
  }
  h2 {
    font-size: 1.3rem;
  }
  .form-group label {
    font-size: 0.9rem;
  }
  input[type="email"],
  input[type="password"] {
    font-size: 0.9rem;
    padding: 0.7em;
  }
  .submit-button {
    font-size: 0.8rem;
    padding: 0.7em;
  }
  .back-button {
    font-size: 1.2em;
    top: 10px;
    left: 10px;
  }
}
</style>
