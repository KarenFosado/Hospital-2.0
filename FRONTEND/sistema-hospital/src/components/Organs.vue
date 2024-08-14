<template>
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
                        <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">{{ organo.Nombre }}</th>
                        <td class="px-6 py-4">{{ organo.Aparato_Sistema }}</td>
                        <td class="px-6 py-4">{{ organo.Descripcion }}</td>
                        <td class="px-6 py-4">{{ organo.Disponibilidad }}</td>
                        <td class="px-6 py-4">{{ organo.Tipo }}</td>
                        <td class="px-6 py-4">{{ organo.Fecha_Actualizacion }}</td>
                        <td class="px-6 py-4">{{ organo.Fecha_Registro }}</td>
                        <td class="px-6 py-4">{{ organo.Estatus }}</td>
                        <td class="px-6 py-4">
                            
                            <a href="#" class="font-medium text-blue-600 dark:text-blue-500 hover:underline mr-2">
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
        <nav class="flex items-center flex-column flex-wrap md:flex-row justify-between pt-4" aria-label="Table navigation">
            <span class="text-sm font-normal text-gray-500 dark:text-gray-400 mb-4 md:mb-0 block w-full md:inline md:w-auto">Showing <span class="font-semibold text-gray-900 dark:text-white">1-10</span> of <span class="font-semibold text-gray-900 dark:text-white">1000</span></span>
            <ul class="inline-flex -space-x-px rtl:space-x-reverse text-sm h-8">
                <li>
                    <a href="#" class="flex items-center justify-center px-3 h-8 ms-0 leading-tight text-gray-500 bg-white border border-gray-300 rounded-s-lg hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white">Anterior</a>
                </li>
                <li>
                    <a href="#" class="flex items-center justify-center px-3 h-8 leading-tight text-gray-500 bg-white border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white">1</a>
                </li>
                <li>
                    <a href="#" class="flex items-center justify-center px-3 h-8 leading-tight text-gray-500 bg-white border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white">2</a>
                </li>
                <li>
                    <a href="#" aria-current="page" class="flex items-center justify-center px-3 h-8 text-blue-600 border border-gray-300 bg-blue-50 hover:bg-blue-100 hover:text-blue-700 dark:border-gray-700 dark:bg-gray-700 dark:text-white">3</a>
                </li>
                <li>
                    <a href="#" class="flex items-center justify-center px-3 h-8 leading-tight text-gray-500 bg-white border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white">4</a>
                </li>
                <li>
                    <a href="#" class="flex items-center justify-center px-3 h-8 leading-tight text-gray-500 bg-white border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white">5</a>
                </li>
                <li>
                    <a href="#" class="flex items-center justify-center px-3 h-8 leading-tight text-gray-500 bg-white border border-gray-300 rounded-e-lg hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white">Siguiente</a>
                </li>
            </ul>
        </nav>
    </form>
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
