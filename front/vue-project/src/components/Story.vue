<template>
    <div class="history-container">
        <h2>История</h2>
        <button class="new-chat-button" @click="createNewChat">Создать новый чат</button>

        <div class="history-list" :style="{ height: listHeight + 'px' }">
            <div v-for="(item, index) in history" :key="index" class="history-item">
                <img :src="item.image" alt="Фото" class="history-image" />
                <div class="history-text">
                    <h3>{{ item.title }}</h3>
                    <p>{{ item.description }}</p>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            history: [
                { image: "https://via.placeholder.com/100", title: "Событие 1", description: "Описание события 1." },
                { image: "https://via.placeholder.com/100", title: "Событие 2", description: "Описание события 2." },
                { image: "https://via.placeholder.com/100", title: "Событие 3", description: "Описание события 3." },
                { image: "https://via.placeholder.com/100", title: "Событие 1", description: "Описание события 1." },
                { image: "https://via.placeholder.com/100", title: "Событие 2", description: "Описание события 2." },
                { image: "https://via.placeholder.com/100", title: "Событие 3", description: "Описание события 3." },
                { image: "https://via.placeholder.com/100", title: "Событие 1", description: "Описание события 1." },
                { image: "https://via.placeholder.com/100", title: "Событие 2", description: "Описание события 2." },
                { image: "https://via.placeholder.com/100", title: "Событие 3", description: "Описание события 3." },
            ],
            listHeight: 0, // Переменная для высоты списка
        };
    },
    mounted() {
        this.setListHeight();
        window.addEventListener("resize", this.setListHeight);
    },
    beforeDestroy() {
        window.removeEventListener("resize", this.setListHeight);
    },
    methods: {
        setListHeight() {
            const navbarHeight = document.querySelector(".navbar").offsetHeight;
            const windowHeight = window.innerHeight;
            this.listHeight = windowHeight - navbarHeight - 40;
        },
        createNewChat() {
            console.log("Создание нового чата!");
            // Добавьте логику для создания нового чата
        },
    },
};
</script>

<style scoped>
h2 {
    text-align: center;
    margin-bottom: 10px;
    color: var(--color-heading);
}

.history-container {
    display: flex;
    flex-direction: column;
    height: 100%;
    overflow: hidden;
}

.history-list {
    flex: 1;
    overflow-y: auto;
    scrollbar-width: thin;
    padding-right: 10px;
}

.history-item {
    display: flex;
    align-items: center;
    margin-bottom: 20px;
    padding: 10px;
    border-bottom: 1px solid var(--color-border);
}

.history-item:last-child {
    border-bottom: none;
}

.history-image {
    width: 100px;
    height: 100px;
    border-radius: 20%;
    object-fit: cover;
    margin-right: 20px;
    border: 2px solid var(--color-border);
}

.history-text {
    flex: 1;
}

.history-text h3 {
    margin: 0;
    font-size: 1.2rem;
    color: var(--color-heading);
}

.history-text p {
    margin: 5px 0 0;
    color: var(--color-text-muted);
    line-height: 1.4;
}



.new-chat-button {
    padding: 10px 20px;
    margin-bottom: 10px;
    align-self: center;
    font-size: 1rem;
    color: white;
    background-color: var(--color-accent);
    border: none;
    border-radius: var(--border-radius);
    cursor: pointer;
    transition: background-color 0.3s ease;
}

.new-chat-button:hover {
    background-color: var(--color-accent-hover);
}
</style>
