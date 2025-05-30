<template>
  <div class="max-w-md mx-auto p-4 sm:p-6 lg:p-8 bg-gray-50 min-h-screen">
    <form @submit.prevent="addTask" class="mb-4 flex gap-2 flex-col sm:flex-row">
      <input
        v-model="newTaskTitle"
        type="text"
        placeholder="Новая задача"
        class="flex-grow p-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
        required
      />
      <button
        type="submit"
        class="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700 transition"
      >
        Добавить
      </button>
    </form>

    <ul>
      <li
        v-for="task in tasks"
        :key="task.id"
        class="flex items-center justify-between p-2 mb-2 bg-white rounded shadow"
      >
        <div class="flex items-center gap-3">
          <input
            type="checkbox"
            v-model="task.completed"
            @change="updateTaskStatus(task)"
            class="w-5 h-5"
          />
          <span :class="{ 'line-through text-gray-400': task.completed }">
            {{ task.title }}
          </span>
        </div>
        <button
          class="text-red-600 hover:text-red-800"
          @click="deleteTask(task.id)"
          title="Удалить задачу"
        >
          &#10006;
        </button>
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const tasks = ref([])
const newTaskTitle = ref('')

const fetchTasks = async () => {
  try {
    const response = await axios.get('/api/tasks')
    tasks.value = response.data
  } catch (error) {
    console.error('Ошибка при загрузке задач:', error)
  }
}

const addTask = async () => {
  if (!newTaskTitle.value.trim()) return
  try {
    const newTask = {
      title: newTaskTitle.value.trim(),
      completed: false,
    }
    await axios.post('/api/tasks', newTask)
    newTaskTitle.value = ''
    await fetchTasks()
  } catch (error) {
    console.error('Ошибка при добавлении задачи:', error)
  }
}

const deleteTask = async (id) => {
  try {
    await axios.delete(`/api/tasks/${id}`)
    await fetchTasks()
  } catch (error) {
    console.error('Ошибка при удалении задачи:', error)
  }
}

const updateTaskStatus = async (task) => {
  try {
    await axios.patch(`/api/tasks/${task.id}`, { completed: task.completed })
  } catch (error) {
    console.error('Ошибка при обновлении статуса задачи:', error)
  }
}

onMounted(fetchTasks)
</script>

<style scoped>
</style>
