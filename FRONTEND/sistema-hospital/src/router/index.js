import { createRouter, createWebHistory } from "vue-router";
import Login from "../components/login.vue"
import RegisterUser from "../components/register.vue"
import Dashboard from "../components/Dashboard.vue"
import Person from '../components/personas.vue'
import User from '../components/usuarios.vue'
const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes:[
        {
            path: '/',
            name: 'Login',
            component: Login
        },
        {
            path: '/register',
            name: 'register',
            component: RegisterUser
        },
        {
            path: '/dashboard',
            name: 'dashboard',
            component: Dashboard,
            children:[{path: '/personas', name: 'personas', component: Person}]
        },
        {
            path: '/usarios',
            name: 'usarios',
            component: User
        }
    ]
});

export default router;  
