<template>
  <div class="welcome-container">
    <!-- Приветственное сообщение -->
    <div v-if="!started" class="welcome-text">
      <h1>Добро пожаловать!</h1>
      <p>
        <span class="highlight">{{ displayedText }}</span>
      </p>
    </div>

    <!-- Кнопка "Начать" -->
    <button v-if="!started" class="start-button" @click="start">Начать</button>

    <!-- Новый контент после нажатия на "Начать" -->
    <div v-if="started" class="chat-content">
      <h1 class="choose-photo-text">Выберите свою фотографию</h1>

      <!-- Кнопка для выбора файла -->
      <label for="file-input" class="file-input-label">
        <div class="file-input-box">
          <!-- Если фото выбрано, отображаем его в рамке -->
          <img v-if="selectedFile" :src="imageUrl" alt="Selected" class="selected-image" />
          <!-- Если фото не выбрано, показываем плюсик -->
          <span v-if="!selectedFile">+</span>
        </div>
      </label>
      <input
        type="file"
        id="file-input"
        accept="image/*"
        @change="onFileChange"
        style="display: none"
      />

      <!-- Кнопка "Подобрать лук" появляется только после выбора фотографии -->
      <button
        v-if="selectedFile"
        class="pick-look-button"
        @click="pickLook"
      >
        Подобрать лук
      </button>

      <!-- Маленькие квадраты с заглушками с картинками -->
      <div v-if="showImagePlaceholders" class="image-placeholders">
        <div v-for="(placeholder, index) in 5" :key="index" class="image-placeholder">
          <img src="https://via.placeholder.com/100" alt="Placeholder" class="placeholder-image" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      fullText: "Я LukaAI, ваш персональный AI стилист!!! ;)",
      displayedText: "",
      isErasing: false,
      started: false, // Состояние для отслеживания начала процесса
      selectedFile: null, // Для хранения выбранного файла
      imageUrl: '', // Для хранения URL изображения
      showImagePlaceholders: false, // Для отображения маленьких квадратов
    };
  },
  methods: {
    animateText() {
      const speed = 250; // Скорость печати/стирания в миллисекундах
      if (!this.isErasing && this.displayedText.length < this.fullText.length) {
        this.displayedText = this.fullText.slice(0, this.displayedText.length + 1);
      } else if (this.isErasing && this.displayedText.length > 0) {
        this.displayedText = this.fullText.slice(0, this.displayedText.length - 1);
      } else {
        this.isErasing = !this.isErasing;
      }
      setTimeout(this.animateText, speed);
    },
    start() {
      this.started = true; // Когда нажимают "Начать", показываем новый контент
    },
    onFileChange(event) {
      // Получаем файл и сохраняем его
      const file = event.target.files[0];
      if (file) {
        this.selectedFile = file;
        this.imageUrl = URL.createObjectURL(file); // Создаем URL для выбранного изображения
      }
    },
    pickLook() {
      // Логика для подбора лука
      alert("Лук подобран!");
      this.showImagePlaceholders = true; // Показать маленькие квадраты после нажатия на кнопку
    },
  },
  mounted() {
    this.animateText(); // Запускаем анимацию при монтировании компонента
  },
};
</script>

<style scoped>
.welcome-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100%; /* Занимает всю высоту родителя */
  text-align: center;
  background-color: var(--color-background); /* Фон */
}

.welcome-text h1 {
  font-size: 2.5rem;
  color: white;
  margin-bottom: 10px;
}

.welcome-text p {
  font-size: 1.5rem;
  color: white;
  margin: 0;
}

.welcome-text .highlight {
  color: var(--color-accent); /* Цвет выделения для "LukaAI" */
  font-weight: bold;
}

.start-button {
  margin-top: 20px;
  padding: 10px 20px;
  font-size: 1.2rem;
  color: white;
  background-color: var(--color-accent); /* Основной цвет кнопки */
  border: none;
  border-radius: var(--border-radius);
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.start-button:hover {
  background-color: var(--color-accent-hover); /* Цвет кнопки при наведении */
}

.chat-content {
  display: flex;
  flex-direction: column;
  margin-top: 72px;
  align-items: center;
  height: auto;
}

.choose-photo-text {
  font-size: 1.5rem;
  margin-top: 30px;
  color: white;
}

.file-input-label {
  display: inline-block;
  cursor: pointer;
  background-color: var(--color-background-light);
  padding: 20px;
  border-radius: var(--border-radius);
  border: 2px dashed var(--color-border);
  color: var(--color-text-muted);
  font-size: 1.2rem;
  margin-top: 20px;
}

.file-input-box {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 400px; /* Увеличили размер квадрата */
  height: 400px; /* Увеличили размер квадрата */
  background-color: var(--color-background-light);
  border: 2px dashed var(--color-border);
  border-radius: 10px;
  overflow: hidden;
  position: relative;
}

.selected-image {
  max-width: 100%;
  max-height: 100%;
  object-fit: cover;
}

.file-input-label span {
  font-size: 4rem; /* Сделали плюсик больше */
}

.pick-look-button {
  margin-top: 20px;
  padding: 10px 20px;
  font-size: 1rem;
  background-color: var(--color-accent);
  border: none;
  border-radius: var(--border-radius);
  cursor: pointer;
  display: block;
  margin-left: auto;
  margin-right: auto;
  color: white; /* Текст белый */
}

.image-placeholders {
  display: flex;
  justify-content: space-between; /* Располагаем квадраты по бокам кнопки */
  margin-top: 30px;
  margin-bottom: 30px;
  width: 100%; /* Занимаем всю ширину */
  padding: 0 20px; /* Отступы по бокам */
}

.image-placeholder {
  width: 120px; /* Увеличили размер маленького квадрата */
  height: 120px;
  background-color: var(--color-background-light);
  border: 2px dashed var(--color-border);
  margin: 0 10px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.placeholder-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
</style>
