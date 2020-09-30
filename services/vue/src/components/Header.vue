<template>
    <header>
        <h2>COVID-19 Relevant Articles Finder</h2>
    </header>
</template>

<script>
export default {
    name: "Header"
}
</script>

<style scoped>
    header {   
        display: flex;
        justify-content: center;
    }
    header h2{
        background: linear-gradient(-90deg, red, orange);
        color:white;
        text-align: center;
        padding: 10px; 
        border-radius: 15px;
    }
</style>