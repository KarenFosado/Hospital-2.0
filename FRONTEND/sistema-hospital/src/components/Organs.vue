<template>
    <div>
        <!-- Tabla de Órganos -->
        <form>
            <div class="relative overflow-x-auto shadow-md sm:rounded-lg">
                <div class="flex flex-column sm:flex-row flex-wrap space-y-4 sm:space-y-0 items-center justify-between pb-4">
                    <div class="relative">
                        <div class="absolute inset-y-0 left-0 rtl:inset-r-0 rtl:right-0 flex items-center ps-3 pointer-events-none">
                            <svg class="w-5 h-5 text-gray-500 dark:text-gray-400" aria-hidden="true" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                                <path fill-rule="evenodd" d="M8 4a4 4 0 100 8 4 4 0 000-8zM2 8a6 6 0 1110.89 3.476l4.817 4.817a1 1 0 01-1.414 1.414l-4.816-4.816A6 6 0 012 8z" clip-rule="evenodd"></path>
                            </svg>
                        </div>
                        <input type="text" id="table-search" class="block p-2 ps-10 text-sm text-gray-900 border border-gray-300 rounded-lg w-80 bg-gray-50 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Search for items">
                    </div>
                    <div>
                        <RouterLink to="/organform">
                            <button id="dropdownRadioButton" data-dropdown-toggle="dropdownRadio" class="inline-flex items-center text-white bg-blue-500 border border-blue-300 focus:outline-none hover:bg-blue-400 focus:ring-4 focus:ring-blue-100 font-medium rounded-lg text-sm px-3 py-1.5 dark:bg-blue-800 dark:text-white dark:border-blue-600 dark:hover:bg-blue-700 dark:hover:border-blue-600 dark:focus:ring-blue-700" type="button">
                                Agregar Órgano
                            </button>
                        </RouterLink>
                    </div>
                    <label for="table-search" class="sr-only">Search</label>
                </div>
                <table class="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400">
                    <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
                        <tr>
                            <th scope="col" class="p-4"></th>
                            <th scope="col" class="px-6 py-3">NOMBRE</th>
                            <th scope="col" class="px-6 py-3">APARATOS Y SISTEMAS</th>
                            <th scope="col" class="px-6 py-3">DESCRIPCIÓN</th>
                            <th scope="col" class="px-6 py-3">DISPONIBILIDAD</th>
                            <th scope="col" class="px-6 py-3">TIPO</th>
                            <th scope="col" class="px-6 py-3">FECHA DE ACTUALIZACIÓN</th>
                            <th scope="col" class="px-6 py-3">FECHA DE REGISTRO</th>
                            <th scope="col" class="px-6 py-3">ESTATUS</th>
                            <th scope="col" class="px-6 py-3">Acciones</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="organo in organos" :key="organo.ID" class="bg-white border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600">
                            <td class="w-4 p-4"></td>
                            <td class="px-6 py-4">{{ organo.Nombre }}</td>
                            <td class="px-6 py-4">{{ organo.Aparato_Sistema }}</td>
                            <td class="px-6 py-4">{{ organo.Descripcion }}</td>
                            <td class="px-6 py-4">{{ organo.Disponibilidad }}</td>
                            <td class="px-6 py-4">{{ organo.Tipo }}</td>
                            <td class="px-6 py-4">{{ organo.Fecha_Actualizacion }}</td>
                            <td class="px-6 py-4">{{ organo.Fecha_Registro }}</td>
                            <td class="px-6 py-4">{{ organo.Estatus }}</td>
                            <td class="px-6 py-4">
                                <a href="#" @click.prevent="editOrgano(organo)" class="font-medium text-blue-600 dark:text-blue-500 hover:underline mr-2">
                                    <span class="material-symbols-outlined">edit</span>
                                </a>
                                <a href="#" class="font-medium text-red-600 dark:text-red-500 hover:underline">
                                    <span class="material-symbols-outlined">delete</span>
                                </a>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </form>

        <!-- Modal de Edición -->
        <div v-if="showModal" class="fixed inset-0 z-50 flex items-center justify-center bg-black bg-opacity-50">
            <div class="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-lg w-full max-w-md">
                <h3 class="text-lg font-semibold text-gray-900 dark:text-white mb-4">Editar Órgano</h3>
                <form @submit.prevent="updateOrgano">
                    <div class="mb-4">
                        <label for="nombre" class="block text-sm font-medium text-gray-700 dark:text-gray-300">Nombre</label>
                        <input v-model="selectedOrgano.Nombre" type="text" id="nombre" class="mt-1 block w-full p-2 border border-gray-300 rounded-lg dark:bg-gray-700 dark:border-gray-600 dark:text-white">
                    </div>
                    
                    <div class="col-span-2 sm:col-span-1">
                        <label for="category" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Aparato Sistema</label>
                        <select id="category" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500">
                            <option selected="">--------</option>
                           
                        </select>
                    </div>
                    <div class="mb-4">
                        <label for="descripcion" class="block text-sm font-medium text-gray-700 dark:text-gray-300">Descripción</label>
                        <textarea v-model="selectedOrgano.Descripcion" id="descripcion" rows="4" class="mt-1 block w-full p-2 border border-gray-300 rounded-lg dark:bg-gray-700 dark:border-gray-600 dark:text-white"></textarea>
                    </div>
                    <div class="col-span-2 sm:col-span-1">
                        <label for="category" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Disponibilidad</label>
                        <select id="category" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500">
                            <option selected="">--------</option>
                           
                        </select>
                    </div>
                    <div class="col-span-2 sm:col-span-1">
                        <label for="category" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Tipo</label>
                        <select id="category" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500">
                            <option selected="">--------</option>
                           
                        </select>
                    </div>

                    <div class="col-span-2 sm:col-span-1">
                        <label for="datatime-local" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Fecha Actualizacion </label>
                        <input type="datetime-local" >
                    </div>

                    <div class="col-span-2 sm:col-span-1">
                        <label for="datatime" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Fecha Registro </label>
                        <input type="datetime-local" >
                    </div>

                    <div class="col-span-2 sm:col-span-1">
                        <label for="category" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Estatus</label>
                        <select id="category" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500">
                            <option :value="true" > Activo</option>
                            <option :value="false"> Inactivo</option>
                           
                        </select>
                    </div>


                    <div class="flex justify-end">
                        <button @click="closeModal" type="button" class="mr-4 px-4 py-2 bg-gray-300 dark:bg-gray-600 text-gray-800 dark:text-white rounded-lg">Cancelar</button>
                        <button type="submit" class="px-4 py-2 bg-blue-500 dark:bg-blue-700 text-white rounded-lg">Guardar</button>
                    </div>
                    
                </form>
            </div>
        </div>
    </div>
</template>


<script>
import axios from "axios";

const apiClient = axios.create({
    baseURL: 'http://127.0.0.1:8000/',
});

export default {
    name: "CreacionDeTablaOrganos",
    data() {
        return {
            organos: [],
            selectedOrgano: null,
            showModal: false,
            api: "organos/",
        };
    },
    methods: {
        async fetchOrganos() {
            try {
                const response = await apiClient.get(this.api);
                this.organos = response.data;
            } catch (error) {
                console.error("Error fetching organos:", error.response ? error.response.data : error.message);
            }
        },
        editOrgano(organo) {
            this.selectedOrgano = { ...organo }; // Clona el órgano seleccionado
            this.showModal = true;
        },
        closeModal() {
            this.showModal = false;
            this.selectedOrgano = null;
        },
        async updateOrgano() {
            try {
                await apiClient.put(`${this.api}${this.selectedOrgano.ID}/`, this.selectedOrgano);
                this.fetchOrganos();
                this.closeModal();
            } catch (error) {
                console.error("Error updating organo:", error.response ? error.response.data : error.message);
            }
        }
    },
    created() {
        this.fetchOrganos();
    }
};
</script>


<style scoped>
/* Add your component-specific styles here */
</style>
