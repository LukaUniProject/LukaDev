<template>
  <div class="profile-container">
    <button class="back-button" @click="goBack">← Назад</button>

    <div class="profile-content">
      <!-- Аватарка -->
      <div class="avatar">
        <img :src="avatarUrl" alt="Avatar" />
        <input type="file" @change="changeAvatar" />
      </div>

      <!-- Форма для изменения email и пароля -->
      <form @submit.prevent="saveChanges" class="form">
        <div class="form-group">
          <label for="email">Электронная почта</label>
          <input type="email" id="email" v-model="email" required />
        </div>
        <div class="form-group">
          <label for="password">Новый пароль</label>
          <input type="password" id="password" v-model="password" required />
        </div>
        <button type="submit" class="save-button">Сохранить изменения</button>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      avatarUrl: "https://via.placeholder.com/150", // Путь к аватару по умолчанию
      email: "user@example.com", // Пример email
      password: "", // Новый пароль
    }
  },
  methods: {
    goBack() {
      // Возврат на предыдущую страницу
      this.$router.go(-1)
    },
    changeAvatar(event) {
      const file = event.target.files[0]
      if (file) {
        // Логика загрузки аватарки (например, через FileReader)
        const reader = new FileReader()
        reader.onload = e => {
          this.avatarUrl = e.target.result // Отображение нового аватара
        }
        reader.readAsDataURL(file)
      }
    },
    saveChanges() {
      // Логика сохранения изменений (email и пароль)
      console.log("Изменения сохранены:", {
        email: this.email,
        password: this.password,
      })
      alert("Изменения успешно сохранены!")
    },
  },
}
</script>

<style scoped>
.profile-container {
  max-width: 500px;
  margin: 0 auto;
  padding: 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: var(--color-background-light);
  box-shadow: 0 4px 8px var(--color-shadow);
  border-radius: var(--border-radius);
}

.back-button {
  align-self: flex-start;
  margin-bottom: 20px;
  font-size: 1.2rem;
  background: none;
  border: none;
  color: var(--color-text-muted);
  cursor: pointer;
}

.avatar {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-bottom: 20px;
}

.avatar img {
  width: 150px;
  height: 150px;
  border-radius: 50%;
  object-fit: cover;
  margin-bottom: 10px;
  border: 2px solid var(--color-border);
}

.avatar input {
  margin-top: 10px;
  cursor: pointer;
}

.form {
  width: 100%;
  display: flex;
  flex-direction: column;
}

.form-group {
  margin-bottom: 20px;
  display: flex;
  flex-direction: column;
}

label {
  font-size: 1rem;
  color: var(--color-text-muted);
  margin-bottom: 5px;
}

input[type="email"],
input[type="password"] {
  width: 100%;
  padding: 10px;
  border: 1px solid var(--color-border);
  border-radius: var(--border-radius);
  font-size: 1rem;
}

input:focus {
  border-color: var(--color-accent);
  outline: none;
}

.save-button {
  padding: 10px;
  background-color: var(--color-accent);
  color: white;
  border: none;
  border-radius: var(--border-radius);
  font-size: 1rem;
  cursor: pointer;
  transition: background-color 0.3s;
}

.save-button:hover {
  background-color: var(--color-accent-hover);
}

.profile-container {
  max-width: 500px;
  width: 100%;
  margin: 0 auto;
  padding: 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center; /* Центрирование по вертикали */
  position: absolute; /* Для точного размещения */
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%); /* Смещение на половину размера */
  background-color: var(--color-background-light);
  box-shadow: 0 4px 8px var(--color-shadow);
  border-radius: var(--border-radius);
}
</style>
