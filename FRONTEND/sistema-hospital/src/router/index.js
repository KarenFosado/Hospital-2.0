import { createRouter, createWebHistory } from "vue-router";
import Login from "../components/login.vue"
import RegisterUser from "../components/register.vue"
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
        }
    ]
});

export default router;  
