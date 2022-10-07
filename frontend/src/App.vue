<template>
  <div id="app">
    <div class="wrapper">
      <Header></Header>
      <main class="container content">
        <router-view/>
      </main>
    </div>

    <Footer></Footer>
  </div>
</template>


<script>
import Header from "@/components/Main/Header";
import Footer from "@/components/Main/Footer";
export default {
  components: {Footer, Header}
}
</script>


<style>

  html, body {
    padding: 0;
    margin: 0;
    font-family: 'Ubuntu', sans-serif;
  }


  .wrapper {
    min-height: 100vh;
    margin-bottom: 30px;
  }


  .container {
    max-width: 1800px;
    margin: 0 auto;
  }


  .content {
    margin-top: 30px;
  }

</style>
