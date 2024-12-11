<template>
    <section class="slide">
      <header class="navbar">
        <div class="logo">
          <!-- <img src="/path/to/logo.png" alt="Логотип" class="logo-image" /> -->
          <span>Luka</span>
        </div>
        <div class="auth-links">
          <a href="#" @click="onLogin" class="auth-link">вход</a>
          <a href="#" @click="onRegister" class="auth-link">регистрация</a>
        </div>
      </header>
  
      <div class="content">
        <div class="text-block">
          <h1>Ваш персональный стилист</h1>
          <p>
            Равным образом рамки и место обучения кадров представляет собой
            интересный эксперимент проверки новых предложений. Повседневная
            практика показывает, что постоянный количественный рост и сфера
            нашей активности требуют определения и уточнения форм развития.
          </p>
          <button class="action-button">Начать</button>
        </div>
        <div class="image-block">
          <!-- <img src="/path/to/image.jpg" alt="Стилист" class="image" /> -->
        </div>
      </div>
  
      <div class="scroll-indicator">
        <span>⬇</span>
      </div>
    </section>
  </template>
  
  <script>
  import { useRouter } from 'vue-router';
  
  export default {
    name: "Main",
    setup() {
      const router = useRouter();
  
      const onLogin = () => {
        router.push({ name: 'login' });
      };
  
      const onRegister = () => {
        router.push({ name: 'register' });
      };
  
      return {
        onLogin,
        onRegister,
      };
    },
  };
  </script>
  
  
  <style scoped>
  .slide {
  display: flex;
  flex-direction: column;
  height: 100vh;
  background-color: var(--color-background);
}

.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px 20px;
  background-color: var(--color-background-light);
  border-bottom: 1px solid var(--color-border);
}

.logo {
  display: flex;
  align-items: center;
  font-size: 1.5rem;
  font-weight: bold;
}

.logo-image {
  width: 30px;
  height: 30px;
  margin-right: 10px;
}

.auth-links {
  display: flex;
  gap: 15px;
}

.auth-link {
  text-decoration: none;
  color: var(--color-heading);
  font-size: 1rem;
}

.auth-link:hover {
  text-decoration: underline;
}

.content {
  display: flex;
  flex-direction: column;
  justify-content: center; /* Центрирование по вертикали */
  align-items: center; /* Центрирование по горизонтали */
  height: 100vh;
  background-color: var(--color-background);
}

.text-block {
  max-width: 500px;
  background: var(--color-background-light);
  padding: 20px;
  border-radius: var(--border-radius);
  box-shadow: 0 2px 5px var(--color-shadow);
}

.text-block h1 {
  font-size: 2rem;
  margin-bottom: 15px;
  color: var(--color-heading);
}

.text-block p {
  font-size: 1rem;
  color: var(--color-text-muted);
  margin-bottom: 20px;
}

.action-button {
  padding: 10px 20px;
  background-color: var(--color-accent);
  color: var(--color-background-light);
  border: none;
  border-radius: 5px;
  font-size: 1rem;
  cursor: pointer;
  transition: background-color var(--transition-speed);
}

.action-button:hover {
  background-color: var(--color-accent-hover);
}

.image-block {
  position: relative;
  max-width: 400px;
}

.image {
  width: 100%;
  border-radius: var(--border-radius);
  box-shadow: 0 2px 5px var(--color-shadow);
}

.scroll-indicator {
  text-align: center;
  font-size: 2rem;
  color: var(--color-scroll-indicator);
  margin-bottom: 20px;
}

  </style>
  