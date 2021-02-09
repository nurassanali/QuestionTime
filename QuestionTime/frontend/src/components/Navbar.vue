<template>
    <nav class="navbar navbar-expand-lg navbar-light bg-light my-navbar">
        <div class="container">
            <router-link
                :to="{ name: 'home' }"
                class="navbar-brand"
            >QuestionTIme</router-link>
            <div class="collapse navbar-collapse" >
                <ul class="navbar-nav ml-auto">
                    <li class="nav-item">
                        <router-link
                            :to="{ name: 'home' }"
                            class="btn btn-sm btn-success"
                        >Home</router-link>
                    </li>
                    <li class="nav-item mx-1">
                        <router-link
                                :to="{ name: 'question-editor' }"
                                class="btn btn-sm btn-danger"
                            >Add question</router-link>
                    </li>
                    <li class="nav-item dropdown">
                        <a class="btn btn-sm btn-outline-secondary" href="/accounts/logout/">Logout</a>
                    <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                        <li><a class="dropdown-item" href="#">Action</a></li>
                        <li><a class="dropdown-item" href="#">Another action</a></li>
                        <li><hr class="dropdown-divider"></li>
                        <li><a class="dropdown-item" href="#">Something else here</a></li>
                    </ul>
                    </li>
                    <li class="nav-item">
                    <a class="nav-link disabled" href="#" tabindex="-1" aria-disabled="true">Disabled</a>
                    </li>
                </ul>
            
            </div>
        </div>
    </nav>
</template>

<script>
export default {
    name: "NavbarComponent"    
}
</script>

<style scoped>
    .my-navbar { 
        border-bottom: 1px solid #DDD;
    }

    .navbar-brand {
        font-weight: bold;
        font-size: 130%;
    }

    .navbar-brand:hover {
        color: #DC3545 !important;
    }
</style>