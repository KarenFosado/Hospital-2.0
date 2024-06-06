<template>
    
        <!-- Author: FormBold Team -->
        <div class="min-h-screen bg-gray-100 text-gray-900 flex justify-center">
            
        <div class="max-w-screen-xl m-0 sm:m-10 bg-white shadow sm:rounded-lg flex justify-center flex-1">
            <div clas>

                <h1 class="text-2xl xl:text-3xl font-extrabold text-center">
                        Resgitra tu usario
            </h1>
            </div>

            <div class=" w-full p-8 " >
                <personas/>
            </div>
            <div class=" w-full p-8 " >
                <usuarios/>
            </div>
        </div>
</div>

       

</template>

<script>
import  personas from './personas.vue';
import usuarios from './usuarios.vue';

export default {
    components:{
        personas,
        usuarios
    }

}
</script>