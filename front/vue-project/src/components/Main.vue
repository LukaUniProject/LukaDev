<template>
  <section class="slide">
    <header class="navbar">
      <div class="logo">
        <span>Luka</span>
      </div>
      <div class="auth-links">
        <a href="#" @click="onLogin" class="auth-link">вход</a>
        <a href="#" @click="onRegister" class="auth-link">регистрация</a>
      </div>
    </header>

    <!-- Контейнер для снежинок -->
    <div class="snowflakes" aria-hidden="true">
      <div v-for="i in snowflakesCount" :key="i" class="snowflake">❄️</div>
    </div>

    <div class="content">
      <div class="text-block">
        <h1>Ваш персональный стилист</h1>
        <p>
          Равным образом рамки и место обучения кадров представляет собой
          интересный эксперимент проверки новых предложений. Повседневная
          практика показывает, что постоянный количественный рост и сфера нашей
          активности требуют определения и уточнения форм развития.
        </p>
        <button class="action-button">Начать</button>
      </div>
      <div class="image-block">
        <!-- <img src="/path/to/image.jpg" alt="Стилист" class="image" /> -->
      </div>
    </div>
  </section>
</template>

<script>
import { useRouter } from "vue-router"

export default {
  name: "Main",
  data() {
    return {
      snowflakesCount: 50, // Количество снежинок
    }
  },
  setup() {
    const router = useRouter()

    const onLogin = () => {
      router.push({ name: "login" })
    }

    const onRegister = () => {
      router.push({ name: "register" })
    }

    return {
      onLogin,
      onRegister,
    }
  },
  mounted() {
    this.createSnowflakes()
  },
  methods: {
    createSnowflakes() {
      const snowflakes = document.querySelectorAll(".snowflake")
      snowflakes.forEach(snowflake => {
        const startPosX = Math.random() * window.innerWidth
        const animationDuration = Math.random() * 20 + 5 + "s" // случайное время падения
        const delay = Math.random() * 10 + "s" // случайная задержка
        snowflake.style.left = `${startPosX}px`
        snowflake.style.animationDuration = animationDuration
        snowflake.style.animationDelay = delay
      })
    },
  },
}
</script>

<style scoped>
.slide {
  display: flex;
  flex-direction: column;
  height: 100vh;
  background-color: var(--color-background);
  position: relative;
  overflow: hidden;
}

.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px 20px;
  background-color: var(--color-background-light);
  border-bottom: 1px solid var(--color-border);
  position: relative;
  z-index: 10;
}

.logo {
  display: flex;
  align-items: center;
  font-size: 2rem;
  font-weight: bold;
  color: var(--color-heading);
}

.auth-links {
  display: flex;
  gap: 1.5em;
}

.auth-link {
  text-decoration: none;
  color: var(--color-heading);
  font-size: 1.2rem;
  border-bottom: 1px solid transparent;
}

.auth-link:hover {
  border-bottom-color: #ffffff;
}

.content {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100vh;
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
  font-size: 1.1rem;
  color: var(--color-text-muted);
  margin-bottom: 20px;
}

.action-button {
  align-items: center;
  padding: 10px 20px;
  background-color: var(--color-accent);
  color: var(--color-heading);
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

.snowflakes {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  pointer-events: none; /* Чтобы снежинки не мешали кликам */
  z-index: 0;
}

.snowflake {
  position: absolute;
  top: -10px;
  font-size: 36px; /* Размер эмодзи снежинки */
  color: #8a2be2; /* Фиолетовый цвет снежинки */
  opacity: 0.8;
  text-shadow: 0 0 5px #fff; /* Белое свечение для контраста */
  animation: fall linear infinite;
}

@keyframes fall {
  to {
    transform: translateY(calc(100vh + 10px));
    opacity: 0;
  }
}

/* Адаптация под мобильные устройства */
@media (max-width: 768px) {
  .navbar {
    flex-direction: column;
    align-items: center; /* Центрируем элементы на мобильных */
    padding: 15px;
  }

  .logo {
    font-size: 1.5rem;
  }

  .auth-links {
    margin-top: 10px;
    gap: 1em;
    justify-content: center; /* Центрируем ссылки для входа/регистрации */
  }

  .auth-link {
    font-size: 1rem;
  }

  .content {
    height: auto; /* Для мобильных устройств */
    padding: 20px;
  }

  .text-block {
    max-width: 100%;
    padding: 15px;
  }

  .text-block h1 {
    font-size: 1.5rem;
  }

  .text-block p {
    font-size: 1rem;
  }

  .action-button {
    font-size: 0.9rem;
    padding: 8px 16px;
  }

  .snowflake {
    font-size: 28px; /* Уменьшаем размер снежинок на мобильных */
  }
}

@media (max-width: 480px) {
  .logo {
    font-size: 1.2rem;
  }

  .auth-links {
    gap: 1em;
    font-size: 0.9rem;
    justify-content: center; /* Центрируем на самых маленьких экранах */
  }

  .text-block h1 {
    font-size: 1.3rem;
  }

  .text-block p {
    font-size: 0.9rem;
  }

  .action-button {
    font-size: 0.8rem;
    padding: 7px 14px;
  }

  .snowflake {
    font-size: 24px; /* Еще больше уменьшаем размер снежинок */
  }
}
</style>
