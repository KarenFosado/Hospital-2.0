import { createRouter, createWebHistory } from "vue-router";
import Login from "../components/login.vue"
import RegisterUser from "../components/register.vue"
import Dashboard from "../components/Dashboard.vue"
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
            component: Dashboard
        }
    ]
});

export default router;  
