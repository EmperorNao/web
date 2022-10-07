<template>

  <header>
    <nav class="navbar navbar-expand-lg navbar-dark bg-black">
      <div class="container">


        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav mb-2 mb-lg-0 header-buttons-list">

            <li class="nav-item description">
              <router-link class="nav-link" :to="{name: 'home'}">Лаборатория анализа данных Владислава Фахретдинова</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" :to="{name: 'demo'}">Демонстрация</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" :to="{name: 'reviews'}">Отзывы</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" :to="{name: 'contacts'}">Контакты</router-link>
            </li>

          </ul>
        </div>

      </div>
    </nav>
  </header>

</template>

<script>
export default {
  name: "Header"
}
</script>

<style>


  header .container {
    max-width: 1800px;
    display: flex;
    flex-direction: row;
    align-items: center;
    height: 100px;
  }


  .header-buttons-list {
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-content: center;
    width: 100%;
  }


  header nav .description {
    font-size: 25px;
    padding: 10px 200px 10px 10px;
  }


  header nav ul {
    display: flex;
    list-style: none;
    padding: 0;
    margin: 0;
    align-items: center;
  }

  header nav ul li {
    font-size: 18px;
    padding: 15px 15px;
  }


  header nav .nav-link {
    color: #fff;
  }


</style>