<template>
  <form @submit.prevent="addOrgano">
    <div class="mx-auto max-w-4xl px-4 sm:px-6 lg:px-8 rounded-lg shadow-lg overflow-hidden mt-5">
      <div class="flex justify-between flex-col items-center">
        <label class="block text-gray-700 text-3xl font-normal mb-2">Datos del órgano</label>
      </div>

      <!-- Nombre -->
      <div class="mt-4">
        <div class="flex justify-between">
          <label class="block text-gray-700 text-sm font-bold mb-2">Nombre</label>
        </div>
        <input
          v-model="selectedOrgano.Nombre"
          class="bg-gray-200 text-gray-700 focus:outline-none focus:shadow-outline border border-gray-300 rounded py-2 px-4 block w-full appearance-none"
          type="text"
          placeholder="Introduce el nombre"
          required
        />
      </div>

      <!-- Aparato y Sistema -->
      <div class="mt-4">
        <div class="flex justify-between">
          <label class="block text-gray-700 text-sm font-bold mb-2">Aparato y Sistema</label>
        </div>
        <select
          v-model="selectedOrgano.Aparato_Sistema"
          class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline text-center"
          required
        >
          <option value="">-- Selecciona una opción --</option>
          <option v-for="aparato in aparatosSistemas" :key="aparato" :value="aparato">
            {{ aparato }}
          </option>
        </select>
      </div>

      <!-- Descripción -->
      <div class="mt-4">
        <div class="flex justify-between">
          <label class="block text-gray-700 text-sm font-bold mb-2">Descripción</label>
        </div>
        <textarea
          v-model="selectedOrgano.Descripcion"
          class="bg-gray-200 text-gray-700 focus:outline-none focus:shadow-outline border border-gray-300 rounded py-2 px-4 block w-full appearance-none"
          rows="4"
          placeholder="Escribe una descripción"
          required
        ></textarea>
      </div>

      <!-- Disponibilidad -->
      <div class="mt-4">
        <div class="flex justify-between">
          <label class="block text-gray-700 text-sm font-bold mb-2">Disponibilidad</label>
        </div>
        <select
          v-model="selectedOrgano.Disponibilidad"
          class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline text-center"
          required
        >
          <option value="">-- Selecciona una opción --</option>
          <option v-for="disponibilidad in disponibilidades" :key="disponibilidad" :value="disponibilidad">
            {{ disponibilidad }}
          </option>
        </select>
      </div>

      <!-- Tipo -->
      <div class="mt-4">
        <div class="flex justify-between">
          <label class="block text-gray-700 text-sm font-bold mb-2">Tipo</label>
        </div>
        <select
          v-model="selectedOrgano.Tipo"
          class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline text-center"
          required
        >
          <option value="">-- Selecciona una opción --</option>
          <option v-for="tipo in tipos" :key="tipo" :value="tipo">
            {{ tipo }}
          </option>
        </select>
      </div>

      <!-- Estatus -->
      <div class="mt-4">
        <div class="flex justify-between">
          <label class="block text-gray-700 text-sm font-bold mb-2">Estatus</label>
        </div>
        <select
          v-model="selectedOrgano.Estatus"
          class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline text-center"
          required
        >
          <option :value="true">Activo</option>
          <option :value="false">Inactivo</option>
        </select>
      </div>

      <!-- Botón de Envío -->
      <div class="mt-8">
        <button
          type="submit"
          class="bg-blue-500 text-white font-bold py-2 px-4 w-full rounded hover:bg-blue-600 mb-5"
        >
          Agregar Órgano
        </button>
      </div>
    </div>
  </form>
</template>

<script>
import axios from "axios";

const apiClient = axios.create({
  baseURL: "http://127.0.0.1:8000/",
});

export default {
  data() {
    return {
      selectedOrgano: {
        Nombre: "",
        Aparato_Sistema: "",
        Descripcion: "",
        Disponibilidad: "",
        Tipo: "",
        Estatus: true,
      },
      aparatosSistemas: [
        "Circulatorio",
        "Digestivo",
        "Respiratorio",
        "Nervioso",
        "Muscular",
        "Esquelético",
        "Endocrino",
        "Linfático",
        "Inmunológico",
        "Reproductor",
        "Urinario",
        "Sensorial",
      ],
      disponibilidades: ["Disponible", "No Disponible"],
      tipos: ["Vital", "No Vital"],
    };
  },
  methods: {
    async addOrgano() {
      try {
        const token = localStorage.getItem("token");
        const config = {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        };

        // Capturar la fecha y hora actual del sistema para las fechas de registro y actualización
        const currentDate = new Date().toISOString();
        this.selectedOrgano.Fecha_Registro = currentDate;
        this.selectedOrgano.Fecha_Actualizacion = currentDate;

        // Validación adicional (opcional) de campos antes de enviar
        if (!this.selectedOrgano.Nombre || !this.selectedOrgano.Aparato_Sistema) {
          alert("Todos los campos son obligatorios.");
          return;
        }

        await apiClient.post("organo/", this.selectedOrgano, config);

        alert("Órgano agregado con éxito");
        this.resetForm();
      } catch (error) {
        console.error("Error al agregar el órgano", error);
      }
    },
    resetForm() {
      this.selectedOrgano = {
        Nombre: "",
        Aparato_Sistema: "",
        Descripcion: "",
        Disponibilidad: "",
        Tipo: "",
        Estatus: true,
      };
    },
  },
};
</script>

<style scoped>
/* Add your component-specific styles here */
</style>
