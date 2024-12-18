<template>
  <div @click="hideMenu" class="app-container">
    <!-- Навбар -->
    <header class="navbar">
      <div class="logo">
        <span>Luka</span>
      </div>

      <div class="settings-container" @click.stop>
        <div class="settings" @click="toggleMenu">⚙️</div>

        <!-- Выпадающее меню -->
        <div v-show="isMenuVisible" class="dropdown-menu">
          <button @click="goToProfile">Мой профиль</button>
          <button @click="logout">Выйти</button>
        </div>
      </div>
    </header>

    <div class="main-container">
      <!-- Лента истории слева -->
      <aside class="history-sidebar">
        <Story />
      </aside>

      <!-- Основной контент -->
      <main class="content-area">
        <WelcomeContent />
      </main>
    </div>
  </div>
</template>

<script>
import Story from "./Story.vue";
import WelcomeContent from "./WelcomeContent.vue";

export default {
  components: {
    Story,
    WelcomeContent,
  },
  data() {
    return {
      isMenuVisible: false, // Видимость меню
    };
  },
  methods: {
    toggleMenu() {
      this.isMenuVisible = !this.isMenuVisible; // Переключение видимости меню
    },
    hideMenu() {
      this.isMenuVisible = false; // Скрыть меню при клике в любую область
    },
    goToProfile() {
      // Логика перехода в "Мой профиль"
      this.$router.push("/profile"); // Пример маршрута
    },
    logout() {
      // Логика выхода из аккаунта
      console.log("Выход из аккаунта");

      // Удаление JWT токена
      localStorage.removeItem("jwt");

      // Редирект на домашнюю страницу
      this.$router.push("/"); // Переход на главную страницу (или любую другую)
    },
  },
};
</script>

<style scoped>
/* Основной контейнер */
.app-container {
  min-height: 100vh;
  background-color: var(--color-background); /* Фоновый цвет */
  display: flex;
  flex-direction: column;
}

/* Навбар */
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px 20px;
  background-color: var(--color-background-light);
  border-bottom: 1px solid var(--color-border);
}

.logo {
  color: var(--color-text-muted);
  font-size: 2rem;
}

.settings-container {
  position: relative;
}

.settings {
  font-size: 2rem;
  cursor: pointer;
}

/* Выпадающее меню */
.dropdown-menu {
  position: absolute;
  top: 2.5rem;
  right: 0;
  background-color: var(--color-background-light);
  border: 1px solid var(--color-border);
  border-radius: var(--border-radius);
  box-shadow: 0 4px 8px var(--color-shadow);
  z-index: 10;
  display: flex;
  flex-direction: column;
  padding: 0.5rem 0;
  width: 150px;
}

.dropdown-menu button {
  background: none;
  border: none;
  text-align: left;
  padding: 0.5rem 1rem;
  cursor: pointer;
  width: 100%;
  font-size: 1rem;
  color: white; /* Белый цвет текста */
  transition: color 0.3s ease; /* Плавное изменение цвета */
}

.dropdown-menu button:hover {
  color: #ff99cc; /* Нежно-розовый цвет при наведении */
  background-color: transparent; /* Убираем фон при наведении */
}

/* Основная часть страницы */
.main-container {
  display: flex;
  flex: 1;
}

/* Лента истории слева */
.history-sidebar {
  width: 300px; /* Ширина боковой панели */
  background-color: var(--color-background-light);
  border-right: 1px solid var(--color-border);
  overflow-y: auto; /* Прокрутка, если контента много */
  padding: 10px;
  scrollbar-width: thin;
}

.history-sidebar::-webkit-scrollbar {
  width: 8px;
}

.history-sidebar::-webkit-scrollbar-track {
  background: var(--color-border);
}

.history-sidebar::-webkit-scrollbar-thumb {
  background: var(--color-accent);
  border-radius: 4px;
}

.history-sidebar::-webkit-scrollbar-thumb:hover {
  background: var(--color-accent-hover);
}

/* Основной контент */
.content-area {
  flex: 1;
  padding: 20px;
}

/* Основной контейнер */
.app-container {
  height: 100vh; /* Устанавливаем 100% высоты окна */
  overflow: hidden; /* Убираем прокрутку для всего приложения */
  display: flex;
  flex-direction: column;
}

/* Основная часть страницы */
.main-container {
  display: flex;
  flex: 1;
  overflow: hidden; /* Убираем возможную прокрутку */
}

/* Лента истории слева */
.history-sidebar {
  width: 300px; /* Фиксированная ширина */
  background-color: var(--color-background-light);
  border-right: 1px solid var(--color-border);
  overflow-y: auto; /* Только вертикальная прокрутка, если контент выходит за пределы */
  max-height: 100%; /* Ограничение высоты */
}

/* Основной контент */
.content-area {
  flex: 1;
  padding: 20px;
  overflow-y: auto; /* Прокрутка для основного контента при необходимости */
}

</style>
